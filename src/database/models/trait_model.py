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
        super().__init__(**kwargs)
    
    @classmethod
    def create_trait(cls, name, category, description=None, items=None, **kwargs):
        """Create a new trait with questions/items"""
        # Validate items if provided
        if items is not None:
            validated_items = cls._validate_items(items)
        else:
            validated_items = []
        
        trait_data = {
            'name': name.strip(),
            'category': category.strip(),
            'description': description.strip() if description else None,
            'items': validated_items,
            **kwargs
        }
        
        trait = cls(**trait_data)
        trait.save()
        
        logger.info(f"Created new trait: {name} in category {category} with {len(validated_items)} items")
        return trait
    
    @staticmethod
    def _validate_items(items):
        """Validate trait items/questions format"""
        if not isinstance(items, list):
            raise ValueError("Items must be a list")
        
        validated_items = []
        
        for i, item in enumerate(items):
            if not isinstance(item, dict):
                raise ValueError(f"Item {i+1} must be a dictionary")
            
            # Required fields
            if 'question' not in item or not item['question'].strip():
                raise ValueError(f"Item {i+1} must have non-empty question")
            
            if 'level' not in item or not item['level'].strip():
                raise ValueError(f"Item {i+1} must have a level")
            
            # Validate level
            valid_levels = ['basic', 'medium', 'advanced']
            if item['level'] not in valid_levels:
                raise ValueError(f"Item {i+1} has invalid level. Must be one of: {valid_levels}")
            
            item_data = {
                'id': item.get('id', f'item_{i+1}'),
                'question': item['question'].strip(),
                'level': item['level'],
                'type': item.get('type', 'rating_1_5')  # Default question type
            }
            
            validated_items.append(item_data)
        
        return validated_items
    
    @classmethod
    def find_by_category(cls, category, active_only=True):
        """Find traits by category"""
        query = {'category': category}
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('name', 1)])
    
    def update_fields(self, **kwargs):
        """Update multiple fields with validation"""
        # If items are being updated, validate them
        if 'items' in kwargs and kwargs['items'] is not None:
            kwargs['items'] = self._validate_items(kwargs['items'])
        
        # Call parent update_fields method
        return super().update_fields(**kwargs)
    
    def to_public_dict(self):
        """Convert to public dictionary"""
        return {
            'id': str(self._id) if self._id else None,
            'name': self.get_field('name'),
            'description': self.get_field('description'),
            'category': self.get_field('category'),
            'items': self.get_field('items', []),  # Include questions/items
            'is_active': self.get_field('is_active'),
            'created_at': self.get_field('created_at').isoformat() + 'Z' if self.get_field('created_at') else None,
            'updated_at': self.get_field('updated_at').isoformat() + 'Z' if self.get_field('updated_at') else None
        }
