// MongoDB initialization script for IkeNei application
// This script runs when the MongoDB container starts for the first time

print('Starting MongoDB initialization for IkeNei...');

// Switch to the ikenei database
db = db.getSiblingDB('ikenei');

// Create application user with read/write permissions
db.createUser({
  user: 'ikenei_user',
  pwd: 'ikenei_password',
  roles: [
    {
      role: 'readWrite',
      db: 'ikenei'
    }
  ]
});

// Create collections with validation schemas
print('Creating collections with validation...');

// Accounts collection
db.createCollection('accounts', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['email', 'password_hash', 'account_name', 'account_type'],
      properties: {
        email: {
          bsonType: 'string',
          pattern: '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
          description: 'must be a valid email address'
        },
        password_hash: {
          bsonType: 'string',
          minLength: 1,
          description: 'must be a non-empty string'
        },
        account_name: {
          bsonType: 'string',
          minLength: 1,
          description: 'must be a non-empty string'
        },
        account_type: {
          bsonType: 'string',
          enum: ['standard', 'premium', 'enterprise'],
          description: 'must be one of: standard, premium, enterprise'
        },
        is_active: {
          bsonType: 'bool',
          description: 'must be a boolean'
        },
        email_verified: {
          bsonType: 'bool',
          description: 'must be a boolean'
        },
        settings: {
          bsonType: 'object',
          description: 'must be an object'
        },
        created_at: {
          bsonType: 'date',
          description: 'must be a date'
        },
        updated_at: {
          bsonType: 'date',
          description: 'must be a date'
        },
        last_login_at: {
          bsonType: 'date',
          description: 'must be a date'
        }
      }
    }
  }
});

// Subjects collection
db.createCollection('subjects', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['account_id', 'name'],
      properties: {
        account_id: {
          bsonType: 'objectId',
          description: 'must be a valid ObjectId'
        },
        name: {
          bsonType: 'string',
          minLength: 1,
          description: 'must be a non-empty string'
        },
        email: {
          bsonType: 'string',
          pattern: '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
          description: 'must be a valid email address'
        },
        position: {
          bsonType: 'string',
          description: 'must be a string'
        },
        department: {
          bsonType: 'string',
          description: 'must be a string'
        },
        is_active: {
          bsonType: 'bool',
          description: 'must be a boolean'
        },
        metadata: {
          bsonType: 'object',
          description: 'must be an object'
        },
        created_at: {
          bsonType: 'date',
          description: 'must be a date'
        },
        updated_at: {
          bsonType: 'date',
          description: 'must be a date'
        }
      }
    }
  }
});

// Surveys collection
db.createCollection('surveys', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['account_id', 'title', 'survey_type', 'status'],
      properties: {
        account_id: {
          bsonType: 'objectId',
          description: 'must be a valid ObjectId'
        },
        title: {
          bsonType: 'string',
          minLength: 1,
          description: 'must be a non-empty string'
        },
        description: {
          bsonType: 'string',
          description: 'must be a string'
        },
        survey_type: {
          bsonType: 'string',
          enum: ['360_feedback', 'skills', 'performance', 'custom'],
          description: 'must be one of: 360_feedback, skills, performance, custom'
        },
        status: {
          bsonType: 'string',
          enum: ['draft', 'active', 'completed', 'archived'],
          description: 'must be one of: draft, active, completed, archived'
        },
        settings: {
          bsonType: 'object',
          description: 'must be an object'
        },
        questions: {
          bsonType: 'array',
          description: 'must be an array'
        },
        statistics: {
          bsonType: 'object',
          description: 'must be an object'
        },
        created_at: {
          bsonType: 'date',
          description: 'must be a date'
        },
        updated_at: {
          bsonType: 'date',
          description: 'must be a date'
        },
        due_date: {
          bsonType: 'date',
          description: 'must be a date'
        }
      }
    }
  }
});

// Create indexes for performance
print('Creating indexes...');

// Account indexes
db.accounts.createIndex({ 'email': 1 }, { unique: true });
db.accounts.createIndex({ 'account_type': 1, 'is_active': 1 });
db.accounts.createIndex({ 'created_at': -1 });

// Subject indexes
db.subjects.createIndex({ 'account_id': 1, 'is_active': 1 });
db.subjects.createIndex({ 'email': 1 });
db.subjects.createIndex({ 'account_id': 1, 'name': 1 });

// Survey indexes
db.surveys.createIndex({ 'account_id': 1, 'status': 1 });
db.surveys.createIndex({ 'created_at': -1 });
db.surveys.createIndex({ 'status': 1, 'due_date': 1 });

print('MongoDB initialization completed successfully!');
print('Database: ikenei');
print('User: ikenei_user');
print('Collections created: accounts, subjects, surveys');
print('Indexes created for optimal performance');
