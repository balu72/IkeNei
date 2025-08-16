"""
Category Repository
Handles database operations for Category model
"""

from database.models.category_model import Category
from utils.logger import get_logger

logger = get_logger(__name__)

class CategoryRepository:
    """Repository for Category database operations"""
    
    @staticmethod
    def create_category(name, category_type='respondent', description=None, is_default=False, **kwargs):
        """Create a new category"""
        try:
            return Category.create_category(
                name=name,
                category_type=category_type,
                description=description,
                is_default=is_default,
                **kwargs
            )
        except Exception as e:
            logger.error(f"Failed to create category: {str(e)}")
            raise
    
    @staticmethod
    def get_category_by_id(category_id):
        """Get category by ID"""
        try:
            return Category.find_by_id(category_id)
        except Exception as e:
            logger.error(f"Failed to get category by ID {category_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_categories_by_type(category_type, active_only=True):
        """Get categories by type"""
        try:
            return Category.get_categories_by_type(category_type, active_only=active_only)
        except Exception as e:
            logger.error(f"Failed to get categories by type {category_type}: {str(e)}")
            raise
    
    @staticmethod
    def get_respondent_categories(active_only=True):
        """Get respondent categories"""
        try:
            categories = Category.get_respondent_categories(active_only=active_only)
            
            # If no categories exist, create default ones
            if not categories:
                logger.info("No respondent categories found, creating default categories")
                Category.create_default_respondent_categories()
                categories = Category.get_respondent_categories(active_only=active_only)
            
            return categories
        except Exception as e:
            logger.error(f"Failed to get respondent categories: {str(e)}")
            raise
    
    @staticmethod
    def get_all_categories(page=1, per_page=20, filters=None):
        """Get all categories with pagination and filtering"""
        try:
            query = {}
            
            # Apply filters
            if filters:
                if filters.get('search'):
                    search_term = filters['search']
                    query['$or'] = [
                        {'name': {'$regex': search_term, '$options': 'i'}},
                        {'description': {'$regex': search_term, '$options': 'i'}}
                    ]
                
                if filters.get('type'):
                    query['type'] = filters['type']
                
                if filters.get('is_active') is not None:
                    query['is_active'] = filters['is_active']
                
                if filters.get('is_default') is not None:
                    query['is_default'] = filters['is_default']
            
            # Get paginated results
            result = Category.paginate(
                query=query,
                page=page,
                per_page=per_page,
                sort=[('type', 1), ('is_default', -1), ('name', 1)]
            )
            
            # Convert categories to dictionaries
            categories_data = [category.to_public_dict() for category in result['documents']]
            
            return {
                'categories': categories_data,
                'pagination': result['pagination']
            }
            
        except Exception as e:
            logger.error(f"Failed to get categories: {str(e)}")
            raise
    
    @staticmethod
    def update_category(category_id, update_data):
        """Update category information"""
        try:
            category = Category.find_by_id(category_id)
            if not category:
                raise ValueError(f"Category not found: {category_id}")
            
            # Update fields
            category.update_fields(**update_data)
            category.save()
            
            return category
            
        except Exception as e:
            logger.error(f"Failed to update category {category_id}: {str(e)}")
            raise
    
    @staticmethod
    def update_category_status(category_id, is_active):
        """Update category status"""
        try:
            category = Category.find_by_id(category_id)
            if not category:
                raise ValueError(f"Category not found: {category_id}")
            
            if is_active:
                category.activate()
            else:
                category.deactivate()
            
            return category
            
        except Exception as e:
            logger.error(f"Failed to update category status {category_id}: {str(e)}")
            raise
    
    @staticmethod
    def delete_category(category_id):
        """Delete category (soft delete)"""
        try:
            category = Category.find_by_id(category_id)
            if not category:
                raise ValueError(f"Category not found: {category_id}")
            
            # Soft delete
            category.soft_delete()
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete category {category_id}: {str(e)}")
            raise
    
    @staticmethod
    def search_categories(search_term, category_type=None, active_only=True):
        """Search categories by name or description"""
        try:
            return Category.search_categories(
                search_term=search_term,
                category_type=category_type,
                active_only=active_only
            )
        except Exception as e:
            logger.error(f"Failed to search categories: {str(e)}")
            raise
    
    @staticmethod
    def get_category_statistics():
        """Get category statistics"""
        try:
            return Category.get_category_statistics()
        except Exception as e:
            logger.error(f"Failed to get category statistics: {str(e)}")
            raise
    
    @staticmethod
    def create_default_respondent_categories():
        """Create default respondent categories"""
        try:
            return Category.create_default_respondent_categories()
        except Exception as e:
            logger.error(f"Failed to create default respondent categories: {str(e)}")
            raise
    
    @staticmethod
    def find_by_name_and_type(name, category_type):
        """Find category by name and type"""
        try:
            return Category.find_by_name_and_type(name, category_type)
        except Exception as e:
            logger.error(f"Failed to find category by name and type: {str(e)}")
            raise
