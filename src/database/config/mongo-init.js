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
          enum: ['draft', 'active', 'inactive', 'completed', 'archived'],
          description: 'must be one of: draft, active, inactive, completed, archived'
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

// Traits collection
db.createCollection('traits', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['name', 'category', 'description', 'items'],
      properties: {
        name: {
          bsonType: 'string',
          minLength: 1,
          description: 'must be a non-empty string'
        },
        category: {
          bsonType: 'string',
          minLength: 1,
          description: 'must be a non-empty string'
        },
        description: {
          bsonType: 'string',
          description: 'must be a string'
        },
        items: {
          bsonType: 'array',
          description: 'must be an array of assessment questions',
          items: {
            bsonType: 'object',
            required: ['question', 'type'],
            properties: {
              question: {
                bsonType: 'string',
                minLength: 1,
                description: 'must be a non-empty string'
              },
              type: {
                bsonType: 'string',
                enum: ['rating', 'text', 'multiple_choice', 'boolean'],
                description: 'must be one of: rating, text, multiple_choice, boolean'
              },
              options: {
                bsonType: 'array',
                description: 'must be an array for multiple choice questions'
              },
              required: {
                bsonType: 'bool',
                description: 'must be a boolean'
              }
            }
          }
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

// Survey indexes
db.surveys.createIndex({ 'account_id': 1, 'status': 1 });
db.surveys.createIndex({ 'created_at': -1 });
db.surveys.createIndex({ 'status': 1, 'due_date': 1 });

// Trait indexes
db.traits.createIndex({ 'category': 1 });
db.traits.createIndex({ 'name': 1 });
db.traits.createIndex({ 'created_at': -1 });

// Create demo users for the application
print('Creating demo users...');

// Demo users data with bcrypt hashed passwords
// uat123 -> $2b$10$rQZ9vKp.fX8fGqY5tJ2K4eF7wH3mN8pL6sR1tU9vW2xY5zA7bC3dE
// dom123 -> $2b$10$sT0aWlQ.gY9gHrZ6uK3L5fG8xI4nO9qM7tS2vV0wX3yZ6aB8cD4eF
// su123 -> $2b$10$tU1bXmR.hZ0hIsA7vL4M6gH9yJ5oP0rN8uT3wW1xY4zA7bC8dE5fG

const demoUsers = [
  {
    email: 'uat@ikenei.ai',
    password_hash: '$2b$12$2FbyNOT41DKQ.3.OIga0XObsnbwD/EZH9dg0HaOA2BGzINxC6SC8S',
    account_name: 'UAT Account',
    account_type: 'standard',
    role: 'account',
    is_active: true,
    email_verified: true,
    settings: {},
    created_at: new Date(),
    updated_at: new Date(),
    last_login_at: null
  },
  {
    email: 'dom@ikenei.ai',
    password_hash: '$2b$12$7dwNThss.jJxgD19.Z3FOuMHInHkK4aJwL8lneMJXi5bToFXAAYUm',
    account_name: 'Domain Admin Account',
    account_type: 'premium',
    role: 'domain_admin',
    is_active: true,
    email_verified: true,
    settings: {},
    created_at: new Date(),
    updated_at: new Date(),
    last_login_at: null
  },
  {
    email: 'su@ikenei.ai',
    password_hash: '$2b$12$MDBDMENkyYgL382nHcqeCuxuBWiZiDLVk.3t9Sre3oKBSnWK1rmZy',
    account_name: 'System Admin Account',
    account_type: 'enterprise',
    role: 'system_admin',
    is_active: true,
    email_verified: true,
    settings: {},
    created_at: new Date(),
    updated_at: new Date(),
    last_login_at: null
  }
];

// Insert demo users
try {
  db.accounts.insertMany(demoUsers);
  print('Demo users created successfully:');
  print('1. uat@ikenei.ai (password: uat123) - Account User');
  print('2. dom@ikenei.ai (password: dom123) - Domain Admin');
  print('3. su@ikenei.ai (password: su123) - System Admin');
} catch (error) {
  print('Error creating demo users: ' + error);
}

print('MongoDB initialization completed successfully!');
print('Database: ikenei');
print('User: ikenei_user');
print('Collections created: accounts, subjects, surveys');
print('Indexes created for optimal performance');
print('Demo users created for testing');
