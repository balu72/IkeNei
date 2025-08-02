"""
MongoDB Connection Manager for IkeNei Application
Handles database connections, connection pooling, and health checks
"""

import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from flask import current_app
from utils.logger import get_logger
import time
from functools import wraps

logger = get_logger(__name__)

class DatabaseConnection:
    """MongoDB connection manager with connection pooling and error handling"""
    
    _instance = None
    _client = None
    _db = None
    
    def __new__(cls):
        """Singleton pattern to ensure single database connection"""
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize database connection if not already initialized"""
        if self._client is None:
            self.connect()
    
    def connect(self):
        """Establish connection to MongoDB"""
        try:
            # Get connection parameters from config
            mongo_uri = current_app.config.get('MONGO_URI', 'mongodb://localhost:27017/ikenei')
            db_name = current_app.config.get('MONGODB_DB_NAME', 'ikenei')
            
            logger.info(f"Connecting to MongoDB: {mongo_uri}")
            
            # Create MongoDB client with connection pooling
            self._client = MongoClient(
                mongo_uri,
                maxPoolSize=50,  # Maximum number of connections in the pool
                minPoolSize=5,   # Minimum number of connections in the pool
                maxIdleTimeMS=30000,  # Close connections after 30 seconds of inactivity
                serverSelectionTimeoutMS=5000,  # Timeout for server selection
                connectTimeoutMS=10000,  # Timeout for initial connection
                socketTimeoutMS=20000,   # Timeout for socket operations
                retryWrites=True,        # Enable retryable writes
                w='majority'             # Write concern
            )
            
            # Get database instance
            self._db = self._client[db_name]
            
            # Test connection
            self.health_check()
            
            logger.info("Successfully connected to MongoDB")
            
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {str(e)}")
            raise ConnectionFailure(f"Database connection failed: {str(e)}")
    
    def get_database(self):
        """Get database instance"""
        if self._db is None:
            self.connect()
        return self._db
    
    def get_client(self):
        """Get MongoDB client instance"""
        if self._client is None:
            self.connect()
        return self._client
    
    def health_check(self):
        """Check database connection health"""
        try:
            # Ping the database
            self._client.admin.command('ping')
            return True
        except Exception as e:
            logger.error(f"Database health check failed: {str(e)}")
            return False
    
    def close_connection(self):
        """Close database connection"""
        if self._client:
            self._client.close()
            self._client = None
            self._db = None
            logger.info("Database connection closed")
    
    def get_collection(self, collection_name):
        """Get a specific collection"""
        db = self.get_database()
        return db[collection_name]
    
    def create_indexes(self):
        """Create database indexes for optimal performance"""
        try:
            db = self.get_database()
            
            # Account indexes
            accounts = db.accounts
            accounts.create_index([("email", 1)], unique=True)
            accounts.create_index([("account_type", 1), ("is_active", 1)])
            accounts.create_index([("created_at", -1)])
            
            # Subject indexes
            subjects = db.subjects
            subjects.create_index([("account_id", 1), ("is_active", 1)])
            subjects.create_index([("email", 1)])
            subjects.create_index([("account_id", 1), ("name", 1)])
            
            # Survey indexes
            surveys = db.surveys
            surveys.create_index([("account_id", 1), ("status", 1)])
            surveys.create_index([("created_at", -1)])
            surveys.create_index([("status", 1), ("due_date", 1)])
            
            logger.info("Database indexes created successfully")
            
        except Exception as e:
            logger.error(f"Failed to create indexes: {str(e)}")
            raise

# Global database connection instance (will be initialized later)
db_connection = None

def get_db():
    """Get database instance - convenience function"""
    return db_connection.get_database()

def get_collection(collection_name):
    """Get collection instance - convenience function"""
    return db_connection.get_collection(collection_name)

def with_db_error_handling(func):
    """Decorator for database error handling"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionFailure as e:
            logger.error(f"Database connection error in {func.__name__}: {str(e)}")
            raise
        except ServerSelectionTimeoutError as e:
            logger.error(f"Database timeout error in {func.__name__}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Database error in {func.__name__}: {str(e)}")
            raise
    return wrapper

def init_database(app):
    """Initialize database with Flask app"""
    global db_connection
    
    with app.app_context():
        try:
            # Initialize the global connection
            db_connection = DatabaseConnection()
            
            # Create indexes
            db_connection.create_indexes()
            
            logger.info("Database initialization completed")
            
        except Exception as e:
            logger.error(f"Database initialization failed: {str(e)}")
            raise

def close_database():
    """Close database connection"""
    db_connection.close_connection()

# Database health check endpoint data
def get_database_status():
    """Get database status for health check endpoint"""
    try:
        if db_connection is None:
            return {
                "status": "unhealthy",
                "error": "Database not initialized"
            }
            
        is_healthy = db_connection.health_check()
        
        if is_healthy:
            try:
                client = db_connection.get_client()
                server_info = client.server_info()
                return {
                    "status": "healthy",
                    "mongodb_version": server_info.get("version", "unknown"),
                    "connection_pool_size": 50,
                    "database_name": "ikenei"
                }
            except Exception as e:
                return {
                    "status": "unhealthy",
                    "error": f"Failed to get server info: {str(e)}"
                }
        else:
            return {
                "status": "unhealthy",
                "error": "Database health check failed"
            }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }
