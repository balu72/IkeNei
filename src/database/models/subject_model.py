"""
Subject Model for MongoDB
Handles individuals being assessed in 360-degree feedback
"""

from datetime import datetime
from bson import ObjectId
from database.base_model import BaseModel
from utils.logger import get_logger

logger = get_logger(__name__)

class Subject(BaseModel):
    """Subject model for individuals being assessed"""
    
    collection_name = 'subjects'
    
    required_fields = ['account_id', 'name']
    
    def __init__(self, **kwargs):
        """Initialize Subject with default values"""
        # Set default values
        if 'status' not in kwargs:
            kwargs['status'] = 'active'
        
        if 'surveys_count' not in kwargs:
            kwargs['surveys_count'] = 0
        
        super().__init__(**kwargs)
    
    @classmethod
    def create_subject(cls, account_id, name, email=None, position=None, department=None, **kwargs):
        """Create a new subject"""
        # Validate account_id is ObjectId
        if isinstance(account_id, str):
            try:
                account_id = ObjectId(account_id)
            except Exception:
                raise ValueError("Invalid account_id format")
        
        # Create subject data
        subject_data = {
            'account_id': account_id,
            'name': name.strip(),
            'email': email.strip() if email else None,
            'position': position.strip() if position else None,
            'department': department.strip() if department else None,
            **kwargs
        }
        
        subject = cls(**subject_data)
        subject.save()
        
        logger.info(f"Created new subject: {name} for account {account_id}")
        return subject
    
    @classmethod
    def find_by_account(cls, account_id, active_only=True):
        """Find subjects by account ID"""
        if isinstance(account_id, str):
            try:
                account_id = ObjectId(account_id)
            except Exception:
                raise ValueError("Invalid account_id format")
        
        query = {'account_id': account_id}
        if active_only:
            query['is_active'] = True
            query['status'] = 'active'
        
        return cls.find_many(query, sort=[('created_at', -1)])
    
    @classmethod
    def find_by_email(cls, email):
        """Find subject by email address"""
        return cls.find_one({'email': email.lower().strip()})
    
    @classmethod
    def search_subjects(cls, search_term, account_id=None, active_only=True):
        """Search subjects by name or email"""
        query = {
            '$or': [
                {'name': {'$regex': search_term, '$options': 'i'}},
                {'email': {'$regex': search_term, '$options': 'i'}},
                {'position': {'$regex': search_term, '$options': 'i'}},
                {'department': {'$regex': search_term, '$options': 'i'}}
            ]
        }
        
        if account_id:
            if isinstance(account_id, str):
                try:
                    account_id = ObjectId(account_id)
                except Exception:
                    raise ValueError("Invalid account_id format")
            query['account_id'] = account_id
        
        if active_only:
            query['is_active'] = True
            query['status'] = 'active'
        
        return cls.find_many(query, sort=[('name', 1)])
    
    def activate(self):
        """Activate subject"""
        self.set_field('status', 'active')
        self.set_field('is_active', True)
        return self.save()
    
    def deactivate(self):
        """Deactivate subject"""
        self.set_field('status', 'inactive')
        return self.save()
    
    def update_surveys_count(self, count):
        """Update surveys count"""
        self.set_field('surveys_count', count)
        return self.save()
    
    def increment_surveys_count(self):
        """Increment surveys count by 1"""
        current_count = self.get_field('surveys_count', 0)
        self.set_field('surveys_count', current_count + 1)
        return self.save()
    
    def decrement_surveys_count(self):
        """Decrement surveys count by 1"""
        current_count = self.get_field('surveys_count', 0)
        new_count = max(0, current_count - 1)
        self.set_field('surveys_count', new_count)
        return self.save()
    
    @classmethod
    def get_subjects_by_department(cls, department, account_id=None, active_only=True):
        """Get subjects by department"""
        query = {'department': department}
        
        if account_id:
            if isinstance(account_id, str):
                try:
                    account_id = ObjectId(account_id)
                except Exception:
                    raise ValueError("Invalid account_id format")
            query['account_id'] = account_id
        
        if active_only:
            query['is_active'] = True
            query['status'] = 'active'
        
        return cls.find_many(query, sort=[('name', 1)])
    
    @classmethod
    def get_subject_statistics(cls, account_id=None):
        """Get subject statistics"""
        collection = cls.get_collection()
        
        match_stage = {}
        if account_id:
            if isinstance(account_id, str):
                try:
                    account_id = ObjectId(account_id)
                except Exception:
                    raise ValueError("Invalid account_id format")
            match_stage['account_id'] = account_id
        
        pipeline = []
        if match_stage:
            pipeline.append({'$match': match_stage})
        
        pipeline.extend([
            {
                '$group': {
                    '_id': '$status',
                    'total': {'$sum': 1},
                    'departments': {'$addToSet': '$department'},
                    'avg_surveys': {'$avg': '$surveys_count'}
                }
            }
        ])
        
        stats = list(collection.aggregate(pipeline))
        
        # Calculate totals
        total_subjects = sum(stat['total'] for stat in stats)
        active_subjects = sum(stat['total'] for stat in stats if stat['_id'] == 'active')
        
        # Get unique departments
        all_departments = set()
        for stat in stats:
            if stat.get('departments'):
                all_departments.update(dept for dept in stat['departments'] if dept)
        
        return {
            'by_status': stats,
            'totals': {
                'total_subjects': total_subjects,
                'active_subjects': active_subjects,
                'inactive_subjects': total_subjects - active_subjects,
                'departments_count': len(all_departments),
                'departments': list(all_departments)
            }
        }
    
    def to_dict(self, include_id=True):
        """Convert to dictionary"""
        result = super().to_dict(include_id=include_id)
        
        # Convert ObjectId account_id to string
        if 'account_id' in result and isinstance(result['account_id'], ObjectId):
            result['account_id'] = str(result['account_id'])
        
        return result
    
    def to_public_dict(self):
        """Convert to public dictionary (safe for API responses)"""
        return {
            'id': str(self._id) if self._id else None,
            'account_id': str(self.get_field('account_id')) if self.get_field('account_id') else None,
            'name': self.get_field('name'),
            'email': self.get_field('email'),
            'position': self.get_field('position'),
            'department': self.get_field('department'),
            'status': self.get_field('status'),
            'surveys_count': self.get_field('surveys_count', 0),
            'is_active': self.get_field('is_active'),
            'created_at': self.get_field('created_at').isoformat() + 'Z' if self.get_field('created_at') else None,
            'updated_at': self.get_field('updated_at').isoformat() + 'Z' if self.get_field('updated_at') else None
        }
    
    def __str__(self):
        """String representation"""
        return f"Subject({self.get_field('name')})"
    
    def __repr__(self):
        """Detailed string representation"""
        return f"Subject(id={self._id}, name={self.get_field('name')}, account_id={self.get_field('account_id')})"
