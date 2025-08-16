from flask import jsonify, request
from database import CategoryRepository
from utils.logger import get_logger, log_function_call

class CategoriesController:
    """
    Controller for categories management
    """
    
    @staticmethod
    @log_function_call
    def get_respondent_categories():
        """
        Get all available respondent categories
        """
        logger = get_logger(__name__)
        logger.info("Retrieving respondent categories")
        
        try:
            categories = CategoryRepository.get_respondent_categories()
            
            # Convert to list of category names for backward compatibility
            category_names = [category.get_field('name') for category in categories]
            
            return jsonify({
                "success": True,
                "data": category_names
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve categories: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve categories: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_all_categories():
        """
        Get all categories with details
        """
        logger = get_logger(__name__)
        logger.info("Retrieving all categories")
        
        try:
            # Get pagination parameters
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 20))
            
            # Get filter parameters
            filters = {}
            if request.args.get('search'):
                filters['search'] = request.args.get('search')
            if request.args.get('type'):
                filters['type'] = request.args.get('type')
            if request.args.get('is_active'):
                filters['is_active'] = request.args.get('is_active').lower() == 'true'
            if request.args.get('is_default'):
                filters['is_default'] = request.args.get('is_default').lower() == 'true'
            
            result = CategoryRepository.get_all_categories(
                page=page,
                per_page=per_page,
                filters=filters
            )
            
            return jsonify({
                "success": True,
                "data": result['categories'],
                "pagination": result['pagination']
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve categories: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve categories: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def create_category(data):
        """
        Create a new category
        """
        logger = get_logger(__name__)
        logger.info(f"Creating new category with data: {data}")
        
        try:
            # Validate required fields
            required_fields = ['name', 'type']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        "success": False,
                        "error": {"message": f"Missing required field: {field}"}
                    }), 400
            
            # Create category using repository
            category = CategoryRepository.create_category(
                name=data.get('name'),
                category_type=data.get('type'),
                description=data.get('description'),
                is_default=data.get('is_default', False)
            )
            
            return jsonify({
                "success": True,
                "data": category.to_public_dict(),
                "message": "Category created successfully"
            }), 201
            
        except Exception as e:
            logger.error(f"Failed to create category: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create category: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_category_by_id(category_id):
        """
        Get category by ID
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving category by ID: {category_id}")
        
        try:
            category = CategoryRepository.get_category_by_id(category_id)
            
            if not category:
                return jsonify({
                    "success": False,
                    "error": {"message": "Category not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": category.to_public_dict()
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve category {category_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve category: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_category(category_id, data):
        """
        Update category
        """
        logger = get_logger(__name__)
        logger.info(f"Updating category {category_id} with data: {data}")
        
        try:
            category = CategoryRepository.update_category(category_id, data)
            
            if not category:
                return jsonify({
                    "success": False,
                    "error": {"message": "Category not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": category.to_public_dict(),
                "message": "Category updated successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to update category {category_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update category: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def delete_category(category_id):
        """
        Delete category
        """
        logger = get_logger(__name__)
        logger.info(f"Deleting category: {category_id}")
        
        try:
            success = CategoryRepository.delete_category(category_id)
            
            if not success:
                return jsonify({
                    "success": False,
                    "error": {"message": "Category not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "message": f"Category {category_id} deleted successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to delete category {category_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete category: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def create_default_categories():
        """
        Create default respondent categories
        """
        logger = get_logger(__name__)
        logger.info("Creating default respondent categories")
        
        try:
            categories = CategoryRepository.create_default_respondent_categories()
            
            return jsonify({
                "success": True,
                "data": [category.to_public_dict() for category in categories],
                "message": f"Created {len(categories)} default categories"
            })
            
        except Exception as e:
            logger.error(f"Failed to create default categories: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create default categories: {str(e)}"}
            }), 500
