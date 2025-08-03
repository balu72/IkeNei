# Database Layer - IkeNei

This directory contains all database-related files including models, repositories, configuration, and seeds for the IkeNei MongoDB application.

## Directory Structure

```
database/
├── __init__.py                    # Database package initialization
├── base_model.py                  # Base model class with common functionality
├── connection.py                  # MongoDB connection management
├── README.md                      # Database documentation
├── SETUP.md                       # Database setup instructions
├── config/                        # Database configuration
│   ├── docker-compose.yml         # MongoDB Docker setup
│   └── mongo-init.js              # MongoDB initialization script
├── models/                        # MongoDB document models
│   ├── account_model.py           # Account document model
│   ├── respondent_model.py        # Respondent document model
│   ├── subject_model.py           # Subject document model
│   ├── survey_model.py            # Survey document model
│   └── trait_model.py             # Trait/competency document model
├── repositories/                  # Data access layer
│   ├── account_repository.py      # Account data operations
│   ├── respondent_repository.py   # Respondent data operations
│   ├── subject_repository.py      # Subject data operations
│   ├── survey_repository.py       # Survey data operations
│   └── trait_repository.py        # Trait data operations
└── seeds/                         # Initial and test data
    └── development_seeds.py       # Development seed data
```

## Technology Stack

- **Database**: MongoDB
- **ODM**: PyMongo
- **Connection Management**: Custom connection pooling
- **Data Modeling**: Document-based with embedded and referenced relationships
- **Indexing**: MongoDB compound and single field indexes
- **Validation**: Schema validation at application level

## Database Architecture

### Models Layer (5 Models)
- `account_model.py` - Account document structure and validation
- `respondent_model.py` - Respondent document structure and validation
- `subject_model.py` - Subject document structure and validation
- `survey_model.py` - Survey document structure and validation
- `trait_model.py` - Trait/competency document structure and validation

### Repository Layer (5 Repositories)
- `account_repository.py` - Account data access operations
- `respondent_repository.py` - Respondent data access operations
- `subject_repository.py` - Subject data access operations
- `survey_repository.py` - Survey data access operations
- `trait_repository.py` - Trait data access operations

### Core Components
- `base_model.py` - Base model class with common functionality (timestamps, validation)
- `connection.py` - MongoDB connection management and configuration
- `development_seeds.py` - Sample data for development and testing

## MongoDB Collections

### Core Collections

#### Accounts Collection
```javascript
{
  "_id": ObjectId,
  "email": String,
  "password_hash": String,
  "account_name": String,
  "account_type": String, // "account", "domain_admin", "system_admin"
  "role": String,
  "is_active": Boolean,
  "email_verified": Boolean,
  "profile": {
    "first_name": String,
    "last_name": String,
    "organization": String,
    "department": String,
    "position": String
  },
  "last_login_at": Date,
  "created_at": Date,
  "updated_at": Date
}
```

#### Subjects Collection
```javascript
{
  "_id": ObjectId,
  "account_id": ObjectId, // Reference to accounts
  "name": String,
  "email": String,
  "position": String,
  "department": String,
  "is_active": Boolean,
  "created_at": Date,
  "updated_at": Date
}
```

#### Respondents Collection
```javascript
{
  "_id": ObjectId,
  "subject_id": ObjectId, // Reference to subjects
  "account_id": ObjectId, // Reference to accounts
  "name": String,
  "email": String,
  "relationship": String, // "supervisor", "peer", "direct_report", "self"
  "is_active": Boolean,
  "created_at": Date,
  "updated_at": Date
}
```

#### Surveys Collection
```javascript
{
  "_id": ObjectId,
  "account_id": ObjectId, // Reference to accounts
  "title": String,
  "description": String,
  "survey_type": String, // "360_feedback", "self_assessment", "peer_review"
  "status": String, // "draft", "active", "completed", "archived"
  "is_anonymous": Boolean,
  "traits": [ObjectId], // References to traits
  "questions": [{
    "trait_id": ObjectId,
    "question_text": String,
    "question_type": String, // "rating", "text", "multiple_choice"
    "scale": {
      "min": Number,
      "max": Number,
      "labels": [String]
    }
  }],
  "settings": {
    "allow_comments": Boolean,
    "require_all_questions": Boolean,
    "deadline": Date
  },
  "created_by": ObjectId, // Reference to accounts
  "created_at": Date,
  "updated_at": Date
}
```

#### Traits Collection
```javascript
{
  "_id": ObjectId,
  "account_id": ObjectId, // Reference to accounts (null for system traits)
  "name": String,
  "description": String,
  "category": String, // "leadership", "communication", "technical", "teamwork"
  "weight": Number, // 1.0 default
  "is_active": Boolean,
  "is_system_trait": Boolean, // true for default traits
  "created_at": Date,
  "updated_at": Date
}
```

## MongoDB Indexes

### Performance Optimization Indexes
```javascript
// Accounts collection
db.accounts.createIndex({ "email": 1 }, { unique: true })
db.accounts.createIndex({ "account_type": 1 })
db.accounts.createIndex({ "is_active": 1 })

// Subjects collection
db.subjects.createIndex({ "account_id": 1 })
db.subjects.createIndex({ "account_id": 1, "is_active": 1 })
db.subjects.createIndex({ "email": 1 })

// Respondents collection
db.respondents.createIndex({ "subject_id": 1 })
db.respondents.createIndex({ "account_id": 1 })
db.respondents.createIndex({ "account_id": 1, "is_active": 1 })

// Surveys collection
db.surveys.createIndex({ "account_id": 1 })
db.surveys.createIndex({ "account_id": 1, "status": 1 })
db.surveys.createIndex({ "created_by": 1 })
db.surveys.createIndex({ "status": 1 })

// Traits collection
db.traits.createIndex({ "account_id": 1 })
db.traits.createIndex({ "account_id": 1, "is_active": 1 })
db.traits.createIndex({ "category": 1 })
db.traits.createIndex({ "is_system_trait": 1 })
```

## Data Access Patterns

### Repository Pattern Implementation
```python
# Example: Account Repository
class AccountRepository:
    def __init__(self, db_connection):
        self.collection = db_connection.accounts
    
    def find_by_email(self, email):
        return self.collection.find_one({"email": email})
    
    def create(self, account_data):
        account_data["created_at"] = datetime.utcnow()
        account_data["updated_at"] = datetime.utcnow()
        result = self.collection.insert_one(account_data)
        return str(result.inserted_id)
    
    def update(self, account_id, update_data):
        update_data["updated_at"] = datetime.utcnow()
        return self.collection.update_one(
            {"_id": ObjectId(account_id)},
            {"$set": update_data}
        )
```

### Aggregation Queries
```javascript
// Get survey statistics for an account
db.surveys.aggregate([
  { $match: { "account_id": ObjectId("...") } },
  { $group: {
    "_id": "$status",
    "count": { $sum: 1 }
  }},
  { $sort: { "_id": 1 } }
])

// Get trait usage across surveys
db.surveys.aggregate([
  { $unwind: "$traits" },
  { $group: {
    "_id": "$traits",
    "usage_count": { $sum: 1 }
  }},
  { $lookup: {
    "from": "traits",
    "localField": "_id",
    "foreignField": "_id",
    "as": "trait_info"
  }},
  { $sort: { "usage_count": -1 } }
])
```

## Development Seeds

### Sample Data Structure
```python
# development_seeds.py structure
SAMPLE_ACCOUNTS = [
    {
        "email": "account@example.com",
        "role": "account",
        "account_name": "Sample Account User"
    },
    {
        "email": "domainadmin@example.com", 
        "role": "domain_admin",
        "account_name": "Domain Administrator"
    },
    {
        "email": "systemadmin@example.com",
        "role": "system_admin", 
        "account_name": "System Administrator"
    }
]

SAMPLE_TRAITS = [
    {
        "name": "Leadership",
        "category": "leadership",
        "is_system_trait": True
    },
    {
        "name": "Communication",
        "category": "communication", 
        "is_system_trait": True
    }
]
```

## Data Privacy & Security

### Sensitive Data Handling
- Password hashing with bcrypt
- PII encryption for sensitive fields
- Audit trails for data access
- Data retention policies

### GDPR Compliance
- Account data export functionality
- Right to be forgotten implementation
- Consent tracking
- Data processing logs

## Backup & Recovery

### Backup Strategy
- Daily automated backups using mongodump
- Point-in-time recovery with oplog
- Cross-region backup replication
- Backup integrity verification

### Recovery Procedures
- Database restoration using mongorestore
- Data consistency checks
- Rollback procedures using oplog
- Disaster recovery protocols

## Performance Monitoring

### Key Metrics
- Query execution times using MongoDB Profiler
- Index usage statistics
- Connection pool utilization
- Storage growth trends and collection stats

### Optimization Tools
- MongoDB Compass for query analysis
- explain() method for query optimization
- Performance baseline tracking
- Automated optimization alerts

## Development Guidelines

1. **Document Schema Design**
   - Design documents to minimize joins (use embedding when appropriate)
   - Use references for large or frequently changing data
   - Implement schema validation at application level
   - Document schema changes and versioning

2. **Query Performance**
   - Use MongoDB explain() for query analysis
   - Implement proper indexing strategy for common queries
   - Avoid N+1 query problems with aggregation pipelines
   - Use connection pooling and proper connection management

3. **Data Integrity**
   - Implement validation in models and repositories
   - Use MongoDB transactions for multi-document operations
   - Validate data at application level before database operations
   - Implement soft deletes with is_active flags

## Getting Started

1. **Setup MongoDB**
   ```bash
   # Using Docker (recommended)
   cd src/database/config
   docker-compose up -d
   
   # Or install MongoDB locally
   # macOS: brew install mongodb-community
   # Ubuntu: sudo apt install mongodb
   ```

2. **Initialize Database Connection**
   ```python
   from src.database.connection import get_database
   db = get_database()
   ```

3. **Run Development Seeds**
   ```python
   from src.database.seeds.development_seeds import seed_development_data
   seed_development_data()
   ```

4. **Verify Database Setup**
   ```python
   # Test connection and basic operations
   from src.database.repositories.account_repository import AccountRepository
   account_repo = AccountRepository(db)
   accounts = account_repo.find_all()
   ```

5. **Create Indexes**
   ```python
   # Run index creation script
   python -c "from src.database.connection import create_indexes; create_indexes()"
   ```

## Environment Configuration

```env
# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/ikenei
MONGODB_DB_NAME=ikenei
MONGODB_HOST=localhost
MONGODB_PORT=27017

# MongoDB Authentication (if enabled)
MONGODB_USERNAME=ikenei_user
MONGODB_PASSWORD=your_secure_password

# Connection Pool Settings
MONGODB_MAX_POOL_SIZE=100
MONGODB_MIN_POOL_SIZE=10
MONGODB_MAX_IDLE_TIME_MS=30000
MONGODB_CONNECT_TIMEOUT_MS=10000
MONGODB_SERVER_SELECTION_TIMEOUT_MS=5000

# SSL/TLS Configuration (for production)
MONGODB_SSL=false
MONGODB_SSL_CERT_PATH=/path/to/cert.pem
MONGODB_SSL_CA_CERTS=/path/to/ca.pem

# Backup Configuration
BACKUP_SCHEDULE=0 2 * * *
BACKUP_RETENTION_DAYS=30
BACKUP_S3_BUCKET=ikenei-backups
```

## Docker Setup

The `config/docker-compose.yml` provides a complete MongoDB setup:

```yaml
version: '3.8'
services:
  mongodb:
    image: mongo:7.0
    container_name: ikenei-mongodb
    restart: unless-stopped
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password
      MONGO_INITDB_DATABASE: ikenei
    volumes:
      - mongodb_data:/data/db
      - ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro
    networks:
      - ikenei-network

volumes:
  mongodb_data:

networks:
  ikenei-network:
    driver: bridge
