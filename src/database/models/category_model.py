"""
Category Model for MongoDB
Handles respondent categories for 360-degree feedback
"""

from datetime import datetime
from bson import ObjectId
from database.base_model import BaseModel
from utils.logger import get_logger

logger = get_logger(__name__)

class Category(BaseModel):
    """Category model for respondent categories"""
    
    collection_name = 'categories'
    
    required_fields = ['name', 'type']
    
    # Category types
    CATEGORY_TYPES = ['respondent', 'survey', 'trait']
    
    def __init__(self, **kwargs):
        """Initialize Category with default values"""
        # Set default values
        if 'is_active' not in kwargs:
            kwargs['is_active'] = True
        
        if 'is_default' not in kwargs:
            kwargs['is_default'] = False
        
        super().__init__(**kwargs)
    
    @classmethod
    def create_category(cls, name, category_type='respondent', description=None, is_default=False, **kwargs):
        """Create a new category"""
        # Validate category type
        if category_type not in cls.CATEGORY_TYPES:
            raise ValueError(f"Invalid category type. Must be one of: {', '.join(cls.CATEGORY_TYPES)}")
        
        # Check if category already exists
        existing_category = cls.find_by_name_and_type(name, category_type)
        if existing_category:
            raise ValueError(f"Category '{name}' of type '{category_type}' already exists")
        
        # Create category data
        category_data = {
            'name': name.strip(),
            'type': category_type,
            'description': description.strip() if description else '',
            'is_default': is_default,
            **kwargs
        }
        
        category = cls(**category_data)
        category.save()
        
        logger.info(f"Created new category: {name} ({category_type})")
        return category
    
    @classmethod
    def find_by_name_and_type(cls, name, category_type):
        """Find category by name and type"""
        return cls.find_one({
            'name': name.strip(),
            'type': category_type,
            'is_active': True
        })
    
    @classmethod
    def get_categories_by_type(cls, category_type, active_only=True):
        """Get categories by type"""
        query = {'type': category_type}
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('is_default', -1), ('name', 1)])
    
    @classmethod
    def get_respondent_categories(cls, active_only=True):
        """Get respondent categories"""
        return cls.get_categories_by_type('respondent', active_only=active_only)
    
    @classmethod
    def get_default_categories(cls, category_type):
        """Get default categories for a type"""
        return cls.find_many({
            'type': category_type,
            'is_default': True,
            'is_active': True
        }, sort=[('name', 1)])
    
    @classmethod
    def create_default_respondent_categories(cls):
        """Create default respondent categories if they don't exist"""
        default_categories = [
            'Peer', 'Subordinate', 'Boss', 'Customer', 'Previous Employer',
            'Super Boss', 'Parent', 'Teacher', 'Counseller', 'Third Party', 'Others'
        ]
        
        created_categories = []
        for category_name in default_categories:
            try:
                existing = cls.find_by_name_and_type(category_name, 'respondent')
                if not existing:
                    category = cls.create_category(
                        name=category_name,
                        category_type='respondent',
                        description=f'Default {category_name} category',
                        is_default=True
                    )
                    created_categories.append(category)
                    logger.info(f"Created default category: {category_name}")
                else:
                    logger.info(f"Default category already exists: {category_name}")
            except Exception as e:
                logger.error(f"Failed to create default category {category_name}: {str(e)}")
        
        return created_categories
    
    def activate(self):
        """Activate category"""
        self.set_field('is_active', True)
        return self.save()
    
    def deactivate(self):
        """Deactivate category"""
        self.set_field('is_active', False)
        return self.save()
    
    def update_description(self, description):
        """Update category description"""
        self.set_field('description', description.strip() if description else '')
        return self.save()
    
    @classmethod
    def search_categories(cls, search_term, category_type=None, active_only=True):
        """Search categories by name or description"""
        query = {
            '$or': [
                {'name': {'$regex': search_term, '$options': 'i'}},
                {'description': {'$regex': search_term, '$options': 'i'}}
            ]
        }
        
        if category_type:
            query['type'] = category_type
        
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('name', 1)])
    
    @classmethod
    def get_category_statistics(cls):
        """Get category statistics"""
        collection = cls.get_collection()
        
        pipeline = [
            {
                '$group': {
                    '_id': '$type',
                    'total': {'$sum': 1},
                    'active': {
                        '$sum': {
                            '$cond': [{'$eq': ['$is_active', True]}, 1, 0]
                        }
                    },
                    'default': {
                        '$sum': {
                            '$cond': [{'$eq': ['$is_default', True]}, 1, 0]
                        }
                    }
                }
            }
        ]
        
        stats = list(collection.aggregate(pipeline))
        
        # Calculate totals
        total_categories = sum(stat['total'] for stat in stats)
        total_active = sum(stat['active'] for stat in stats)
        total_default = sum(stat['default'] for stat in stats)
        
        return {
            'by_type': stats,
            'totals': {
                'total_categories': total_categories,
                'active_categories': total_active,
                'default_categories': total_default,
                'inactive_categories': total_categories - total_active
            }
        }
    
    def to_dict(self, include_id=True):
        """Convert to dictionary"""
        return super().to_dict(include_id=include_id)
    
    def to_public_dict(self):
        """Convert to public dictionary (safe for API responses)"""
        return {
            'id': str(self._id) if self._id else None,
            'name': self.get_field('name'),
            'type': self.get_field('type'),
            'description': self.get_field('description'),
            'is_active': self.get_field('is_active'),
            'is_default': self.get_field('is_default'),
            'created_at': self.get_field('created_at').isoformat() + 'Z' if self.get_field('created_at') else None,
            'updated_at': self.get_field('updated_at').isoformat() + 'Z' if self.get_field('updated_at') else None
        }
    
    def __str__(self):
        """String representation"""
        return f"Category({self.get_field('name')} - {self.get_field('type')})"
    
    def __repr__(self):
        """Detailed string representation"""
        return f"Category(id={self._id}, name={self.get_field('name')}, type={self.get_field('type')})"
