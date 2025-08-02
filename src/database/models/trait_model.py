"""
Trait Model for MongoDB
Handles assessment traits/competencies
"""

from datetime import datetime
from bson import ObjectId
from database.base_model import BaseModel
from utils.logger import get_logger

logger = get_logger(__name__)

class Trait(BaseModel):
    """Trait model for assessment competencies"""
    
    collection_name = 'traits'
    
    required_fields = ['name', 'category']
    
    def __init__(self, **kwargs):
        """Initialize Trait with default values"""
        if 'status' not in kwargs:
            kwargs['status'] = 'active'
        
        if 'usage_count' not in kwargs:
            kwargs['usage_count'] = 0
        
        super().__init__(**kwargs)
    
    @classmethod
    def create_trait(cls, name, category, description=None, **kwargs):
        """Create a new trait"""
        trait_data = {
            'name': name.strip(),
            'category': category.strip(),
            'description': description.strip() if description else None,
            **kwargs
        }
        
        trait = cls(**trait_data)
        trait.save()
        
        logger.info(f"Created new trait: {name} in category {category}")
        return trait
    
    @classmethod
    def find_by_category(cls, category, active_only=True):
        """Find traits by category"""
        query = {'category': category}
        if active_only:
            query['is_active'] = True
            query['status'] = 'active'
        
        return cls.find_many(query, sort=[('name', 1)])
    
    def to_public_dict(self):
        """Convert to public dictionary"""
        return {
            'id': str(self._id) if self._id else None,
            'name': self.get_field('name'),
            'description': self.get_field('description'),
            'category': self.get_field('category'),
            'status': self.get_field('status'),
            'usage_count': self.get_field('usage_count', 0),
            'is_active': self.get_field('is_active'),
            'created_at': self.get_field('created_at').isoformat() + 'Z' if self.get_field('created_at') else None,
            'updated_at': self.get_field('updated_at').isoformat() + 'Z' if self.get_field('updated_at') else None
        }
