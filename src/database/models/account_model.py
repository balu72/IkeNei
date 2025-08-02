"""
Account Model for MongoDB
Handles user accounts, authentication, and account management
"""

import bcrypt
from datetime import datetime
from bson import ObjectId
from database.base_model import BaseModel
from utils.logger import get_logger

logger = get_logger(__name__)

class Account(BaseModel):
    """Account model for user authentication and management"""
    
    collection_name = 'accounts'
    
    required_fields = ['email', 'password_hash', 'account_name', 'account_type']
    
    # Account types
    ACCOUNT_TYPES = ['standard', 'premium', 'enterprise']
    
    # Default settings
    DEFAULT_SETTINGS = {
        'notifications_enabled': True,
        'theme': 'light',
        'timezone': 'UTC',
        'language': 'en',
        'email_notifications': {
            'survey_invitations': True,
            'survey_reminders': True,
            'survey_completions': True,
            'system_updates': False
        }
    }
    
    def __init__(self, **kwargs):
        """Initialize Account with default settings"""
        # Set default settings if not provided
        if 'settings' not in kwargs:
            kwargs['settings'] = self.DEFAULT_SETTINGS.copy()
        
        # Set default values
        if 'email_verified' not in kwargs:
            kwargs['email_verified'] = False
        
        if 'account_type' not in kwargs:
            kwargs['account_type'] = 'standard'
        
        super().__init__(**kwargs)
    
    @classmethod
    def create_account(cls, email, password, account_name, account_type='standard', **kwargs):
        """Create a new account with hashed password"""
        # Validate account type
        if account_type not in cls.ACCOUNT_TYPES:
            raise ValueError(f"Invalid account type. Must be one of: {', '.join(cls.ACCOUNT_TYPES)}")
        
        # Check if email already exists
        existing_account = cls.find_by_email(email)
        if existing_account:
            raise ValueError("Account with this email already exists")
        
        # Hash password
        password_hash = cls._hash_password(password)
        
        # Create account
        account_data = {
            'email': email.lower().strip(),
            'password_hash': password_hash,
            'account_name': account_name.strip(),
            'account_type': account_type,
            **kwargs
        }
        
        account = cls(**account_data)
        account.save()
        
        logger.info(f"Created new account: {email}")
        return account
    
    @classmethod
    def find_by_email(cls, email):
        """Find account by email address"""
        return cls.find_one({'email': email.lower().strip()})
    
    @classmethod
    def authenticate(cls, email, password):
        """Authenticate user with email and password"""
        account = cls.find_by_email(email)
        
        if not account:
            logger.warning(f"Authentication failed - account not found: {email}")
            return None
        
        if not account.get_field('is_active', True):
            logger.warning(f"Authentication failed - account inactive: {email}")
            return None
        
        if cls._verify_password(password, account.get_field('password_hash')):
            # Update last login
            account.update_last_login()
            logger.info(f"Successful authentication: {email}")
            return account
        else:
            logger.warning(f"Authentication failed - invalid password: {email}")
            return None
    
    def update_password(self, new_password):
        """Update account password"""
        password_hash = self._hash_password(new_password)
        self.set_field('password_hash', password_hash)
        return self.save()
    
    def verify_password(self, password):
        """Verify password against stored hash"""
        return self._verify_password(password, self.get_field('password_hash'))
    
    def update_last_login(self):
        """Update last login timestamp"""
        self.set_field('last_login_at', datetime.utcnow())
        return self.save()
    
    def verify_email(self):
        """Mark email as verified"""
        self.set_field('email_verified', True)
        return self.save()
    
    def update_settings(self, settings_update):
        """Update account settings"""
        current_settings = self.get_field('settings', self.DEFAULT_SETTINGS.copy())
        
        # Deep merge settings
        for key, value in settings_update.items():
            if isinstance(value, dict) and key in current_settings and isinstance(current_settings[key], dict):
                current_settings[key].update(value)
            else:
                current_settings[key] = value
        
        self.set_field('settings', current_settings)
        return self.save()
    
    def get_setting(self, setting_key, default=None):
        """Get specific setting value"""
        settings = self.get_field('settings', {})
        return settings.get(setting_key, default)
    
    def activate(self):
        """Activate account"""
        self.set_field('is_active', True)
        return self.save()
    
    def deactivate(self):
        """Deactivate account"""
        self.set_field('is_active', False)
        return self.save()
    
    def upgrade_account_type(self, new_type):
        """Upgrade account type"""
        if new_type not in self.ACCOUNT_TYPES:
            raise ValueError(f"Invalid account type. Must be one of: {', '.join(self.ACCOUNT_TYPES)}")
        
        self.set_field('account_type', new_type)
        return self.save()
    
    @classmethod
    def get_accounts_by_type(cls, account_type, active_only=True):
        """Get all accounts of specific type"""
        query = {'account_type': account_type}
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('created_at', -1)])
    
    @classmethod
    def get_active_accounts(cls):
        """Get all active accounts"""
        return cls.find_active(sort=[('created_at', -1)])
    
    @classmethod
    def search_accounts(cls, search_term, account_type=None, active_only=True):
        """Search accounts by name or email"""
        query = {
            '$or': [
                {'account_name': {'$regex': search_term, '$options': 'i'}},
                {'email': {'$regex': search_term, '$options': 'i'}}
            ]
        }
        
        if account_type:
            query['account_type'] = account_type
        
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('account_name', 1)])
    
    @classmethod
    def get_account_statistics(cls):
        """Get account statistics"""
        collection = cls.get_collection()
        
        pipeline = [
            {
                '$group': {
                    '_id': '$account_type',
                    'total': {'$sum': 1},
                    'active': {
                        '$sum': {
                            '$cond': [{'$eq': ['$is_active', True]}, 1, 0]
                        }
                    },
                    'verified': {
                        '$sum': {
                            '$cond': [{'$eq': ['$email_verified', True]}, 1, 0]
                        }
                    }
                }
            }
        ]
        
        stats = list(collection.aggregate(pipeline))
        
        # Calculate totals
        total_accounts = sum(stat['total'] for stat in stats)
        total_active = sum(stat['active'] for stat in stats)
        total_verified = sum(stat['verified'] for stat in stats)
        
        return {
            'by_type': stats,
            'totals': {
                'total_accounts': total_accounts,
                'active_accounts': total_active,
                'verified_accounts': total_verified,
                'inactive_accounts': total_accounts - total_active
            }
        }
    
    def to_dict(self, include_sensitive=False, include_id=True):
        """Convert to dictionary, optionally excluding sensitive data"""
        result = super().to_dict(include_id=include_id)
        
        # Remove sensitive fields unless explicitly requested
        if not include_sensitive:
            result.pop('password_hash', None)
        
        return result
    
    def to_public_dict(self):
        """Convert to public dictionary (safe for API responses)"""
        return {
            'id': str(self._id) if self._id else None,
            'email': self.get_field('email'),
            'account_name': self.get_field('account_name'),
            'account_type': self.get_field('account_type'),
            'is_active': self.get_field('is_active'),
            'email_verified': self.get_field('email_verified'),
            'created_at': self.get_field('created_at').isoformat() + 'Z' if self.get_field('created_at') else None,
            'last_login_at': self.get_field('last_login_at').isoformat() + 'Z' if self.get_field('last_login_at') else None
        }
    
    @staticmethod
    def _hash_password(password):
        """Hash password using bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    @staticmethod
    def _verify_password(password, password_hash):
        """Verify password against hash"""
        try:
            return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
        except Exception as e:
            logger.error(f"Password verification error: {str(e)}")
            return False
    
    def __str__(self):
        """String representation"""
        return f"Account({self.get_field('email')})"
    
    def __repr__(self):
        """Detailed string representation"""
        return f"Account(id={self._id}, email={self.get_field('email')}, type={self.get_field('account_type')})"
