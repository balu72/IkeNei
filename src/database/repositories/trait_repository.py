"""
Trait Repository
Handles database operations for Trait model
"""

from database.models.trait_model import Trait
from utils.logger import get_logger

logger = get_logger(__name__)

class TraitRepository:
    """Repository for Trait database operations"""
    
    @staticmethod
    def create_trait(name, category, description=None, items=None, **kwargs):
        """Create a new trait"""
        try:
            return Trait.create_trait(
                name=name,
                category=category,
                description=description,
                items=items,
                **kwargs
            )
        except Exception as e:
            logger.error(f"Failed to create trait: {str(e)}")
            raise
    
    @staticmethod
    def get_trait_by_id(trait_id):
        """Get trait by ID"""
        try:
            return Trait.find_by_id(trait_id)
        except Exception as e:
            logger.error(f"Failed to get trait by ID {trait_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_all_traits(page=1, per_page=20, filters=None):
        """Get all traits with pagination and filtering"""
        try:
            query = {}
            
            if filters:
                if filters.get('search'):
                    search_term = filters['search']
                    query['$or'] = [
                        {'name': {'$regex': search_term, '$options': 'i'}},
                        {'description': {'$regex': search_term, '$options': 'i'}},
                        {'category': {'$regex': search_term, '$options': 'i'}}
                    ]
                
                if filters.get('category'):
                    query['category'] = filters['category']
                
                if filters.get('is_active') is not None:
                    query['is_active'] = filters['is_active']
            
            result = Trait.paginate(
                query=query,
                page=page,
                per_page=per_page,
                sort=[('category', 1), ('name', 1)]
            )
            
            traits_data = [trait.to_public_dict() for trait in result['documents']]
            
            return {
                'traits': traits_data,
                'pagination': result['pagination']
            }
            
        except Exception as e:
            logger.error(f"Failed to get traits: {str(e)}")
            raise
    
    @staticmethod
    def get_traits_by_category(category, active_only=True):
        """Get traits by category"""
        try:
            return Trait.find_by_category(category=category, active_only=active_only)
        except Exception as e:
            logger.error(f"Failed to get traits by category {category}: {str(e)}")
            raise
    
    @staticmethod
    def update_trait(trait_id, update_data):
        """Update trait information"""
        try:
            trait = Trait.find_by_id(trait_id)
            if not trait:
                raise ValueError(f"Trait not found: {trait_id}")
            
            trait.update_fields(**update_data)
            trait.save()
            
            return trait
            
        except Exception as e:
            logger.error(f"Failed to update trait {trait_id}: {str(e)}")
            raise
    
    @staticmethod
    def delete_trait(trait_id):
        """Delete trait (soft delete)"""
        try:
            trait = Trait.find_by_id(trait_id)
            if not trait:
                raise ValueError(f"Trait not found: {trait_id}")
            
            trait.soft_delete()
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete trait {trait_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_trait_categories():
        """Get all trait categories"""
        try:
            collection = Trait.get_collection()
            categories = collection.distinct('category', {'is_active': True})
            return sorted(categories)
        except Exception as e:
            logger.error(f"Failed to get trait categories: {str(e)}")
            raise
