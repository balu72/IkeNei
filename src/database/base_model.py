"""
Base Model for MongoDB Documents
Provides common functionality for all database models
"""

from datetime import datetime
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from utils.logger import get_logger
from database.connection import get_collection, with_db_error_handling

logger = get_logger(__name__)

class BaseModel:
    """Base class for all MongoDB document models"""
    
    # Collection name - must be overridden in subclasses
    collection_name = None
    
    # Required fields - must be overridden in subclasses
    required_fields = []
    
    # Default field values
    default_fields = {
        'created_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
        'is_active': True
    }
    
    def __init__(self, **kwargs):
        """Initialize model with data"""
        self.data = {}
        self._id = kwargs.get('_id')
        
        # Set default values
        for field, default_value in self.default_fields.items():
            if field not in kwargs:
                if callable(default_value):
                    self.data[field] = default_value()
                else:
                    self.data[field] = default_value
        
        # Set provided values
        for key, value in kwargs.items():
            if key != '_id':
                self.data[key] = value
    
    @classmethod
    def get_collection(cls):
        """Get MongoDB collection for this model"""
        if cls.collection_name is None:
            raise NotImplementedError("collection_name must be defined in subclass")
        return get_collection(cls.collection_name)
    
    @with_db_error_handling
    def save(self):
        """Save document to database"""
        collection = self.get_collection()
        
        # Validate required fields
        self._validate_required_fields()
        
        # Update timestamp
        self.data['updated_at'] = datetime.utcnow()
        
        try:
            if self._id:
                # Update existing document
                result = collection.update_one(
                    {'_id': ObjectId(self._id)},
                    {'$set': self.data}
                )
                if result.modified_count == 0:
                    logger.warning(f"No document updated for ID: {self._id}")
                else:
                    logger.info(f"Updated document in {self.collection_name}: {self._id}")
            else:
                # Insert new document
                result = collection.insert_one(self.data)
                self._id = result.inserted_id
                logger.info(f"Created new document in {self.collection_name}: {self._id}")
            
            return self
            
        except DuplicateKeyError as e:
            logger.error(f"Duplicate key error in {self.collection_name}: {str(e)}")
            raise ValueError("Document with this unique field already exists")
        except Exception as e:
            logger.error(f"Database error in {self.collection_name}: {str(e)}")
            raise ValueError(f"Database operation failed: {str(e)}")
    
    @classmethod
    @with_db_error_handling
    def find_by_id(cls, document_id):
        """Find document by ID"""
        collection = cls.get_collection()
        
        try:
            object_id = ObjectId(document_id)
        except Exception:
            logger.error(f"Invalid ObjectId format: {document_id}")
            return None
        
        document = collection.find_one({'_id': object_id})
        
        if document:
            return cls(**document)
        return None
    
    @classmethod
    @with_db_error_handling
    def find_one(cls, query=None):
        """Find single document by query"""
        collection = cls.get_collection()
        query = query or {}
        
        document = collection.find_one(query)
        
        if document:
            return cls(**document)
        return None
    
    @classmethod
    @with_db_error_handling
    def find_many(cls, query=None, sort=None, limit=None, skip=None):
        """Find multiple documents by query"""
        collection = cls.get_collection()
        query = query or {}
        
        cursor = collection.find(query)
        
        if sort:
            cursor = cursor.sort(sort)
        if skip:
            cursor = cursor.skip(skip)
        if limit:
            cursor = cursor.limit(limit)
        
        documents = []
        for doc in cursor:
            documents.append(cls(**doc))
        
        return documents
    
    @classmethod
    @with_db_error_handling
    def count_documents(cls, query=None):
        """Count documents matching query"""
        collection = cls.get_collection()
        query = query or {}
        
        return collection.count_documents(query)
    
    @with_db_error_handling
    def delete(self):
        """Delete this document"""
        if not self._id:
            raise ValueError("Cannot delete document without ID")
        
        collection = self.get_collection()
        result = collection.delete_one({'_id': ObjectId(self._id)})
        
        if result.deleted_count > 0:
            logger.info(f"Deleted document from {self.collection_name}: {self._id}")
            return True
        else:
            logger.warning(f"No document deleted for ID: {self._id}")
            return False
    
    @classmethod
    @with_db_error_handling
    def delete_many(cls, query):
        """Delete multiple documents by query"""
        collection = cls.get_collection()
        result = collection.delete_many(query)
        
        logger.info(f"Deleted {result.deleted_count} documents from {cls.collection_name}")
        return result.deleted_count
    
    @with_db_error_handling
    def soft_delete(self):
        """Soft delete by setting is_active to False"""
        self.data['is_active'] = False
        self.data['deleted_at'] = datetime.utcnow()
        return self.save()
    
    @classmethod
    @with_db_error_handling
    def find_active(cls, query=None, **kwargs):
        """Find only active documents"""
        query = query or {}
        query['is_active'] = True
        return cls.find_many(query, **kwargs)
    
    @classmethod
    @with_db_error_handling
    def paginate(cls, query=None, page=1, per_page=20, sort=None):
        """Paginate query results"""
        query = query or {}
        
        # Calculate skip value
        skip = (page - 1) * per_page
        
        # Get documents
        documents = cls.find_many(
            query=query,
            sort=sort,
            limit=per_page,
            skip=skip
        )
        
        # Get total count
        total = cls.count_documents(query)
        
        # Calculate pagination info
        total_pages = (total + per_page - 1) // per_page
        has_prev = page > 1
        has_next = page < total_pages
        
        return {
            'documents': documents,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'pages': total_pages,
                'has_prev': has_prev,
                'has_next': has_next
            }
        }
    
    def to_dict(self, include_id=True):
        """Convert model to dictionary"""
        result = self.data.copy()
        
        if include_id and self._id:
            result['id'] = str(self._id)
        
        # Convert datetime objects to ISO strings
        for key, value in result.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat() + 'Z'
            elif isinstance(value, ObjectId):
                result[key] = str(value)
        
        return result
    
    def _validate_required_fields(self):
        """Validate that all required fields are present"""
        missing_fields = []
        
        for field in self.required_fields:
            if field not in self.data or self.data[field] is None:
                missing_fields.append(field)
        
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
    
    def update_fields(self, **kwargs):
        """Update multiple fields"""
        for key, value in kwargs.items():
            if key != '_id':
                self.data[key] = value
        
        self.data['updated_at'] = datetime.utcnow()
        return self
    
    def get_field(self, field_name, default=None):
        """Get field value with default"""
        return self.data.get(field_name, default)
    
    def set_field(self, field_name, value):
        """Set field value"""
        self.data[field_name] = value
        return self
    
    def __str__(self):
        """String representation"""
        return f"{self.__class__.__name__}({self._id})"
    
    def __repr__(self):
        """Detailed string representation"""
        return f"{self.__class__.__name__}(id={self._id}, data={self.data})"
