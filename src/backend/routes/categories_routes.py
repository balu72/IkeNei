from flask import Blueprint, request
from controllers.categories_controller import CategoriesController
from middleware.auth_middleware import require_auth
from utils.response_helpers import handle_exception, validation_error_response
from utils.logger import get_logger

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/api/categories/respondent-categories', methods=['GET'])
@require_auth
def get_respondent_categories():
    """
    Get available respondent categories
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: GET /api/categories/respondent-categories ===")
    
    try:
        result = CategoriesController.get_respondent_categories()
        logger.info("=== EXIT: GET /api/categories/respondent-categories - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/categories/respondent-categories - ERROR: {str(e)} ===")
        return handle_exception(e)

@categories_bp.route('/api/categories', methods=['GET'])
@require_auth
def get_all_categories():
    """
    Get all categories with details
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: GET /api/categories ===")
    
    try:
        result = CategoriesController.get_all_categories()
        logger.info("=== EXIT: GET /api/categories - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/categories - ERROR: {str(e)} ===")
        return handle_exception(e)

@categories_bp.route('/api/categories', methods=['POST'])
@require_auth
def create_category():
    """
    Create new category
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/categories ===")
    
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        result = CategoriesController.create_category(data)
        logger.info("=== EXIT: POST /api/categories - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/categories - ERROR: {str(e)} ===")
        return handle_exception(e)

@categories_bp.route('/api/categories/<category_id>', methods=['GET'])
@require_auth
def get_category(category_id):
    """
    Get category by ID
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: GET /api/categories/{category_id} ===")
    
    try:
        result = CategoriesController.get_category_by_id(category_id)
        logger.info(f"=== EXIT: GET /api/categories/{category_id} - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/categories/{category_id} - ERROR: {str(e)} ===")
        return handle_exception(e)

@categories_bp.route('/api/categories/<category_id>', methods=['PUT'])
@require_auth
def update_category(category_id):
    """
    Update category
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: PUT /api/categories/{category_id} ===")
    
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        result = CategoriesController.update_category(category_id, data)
        logger.info(f"=== EXIT: PUT /api/categories/{category_id} - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: PUT /api/categories/{category_id} - ERROR: {str(e)} ===")
        return handle_exception(e)

@categories_bp.route('/api/categories/<category_id>', methods=['DELETE'])
@require_auth
def delete_category(category_id):
    """
    Delete category
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: DELETE /api/categories/{category_id} ===")
    
    try:
        result = CategoriesController.delete_category(category_id)
        logger.info(f"=== EXIT: DELETE /api/categories/{category_id} - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: DELETE /api/categories/{category_id} - ERROR: {str(e)} ===")
        return handle_exception(e)

@categories_bp.route('/api/categories/create-defaults', methods=['POST'])
@require_auth
def create_default_categories():
    """
    Create default respondent categories
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/categories/create-defaults ===")
    
    try:
        result = CategoriesController.create_default_categories()
        logger.info("=== EXIT: POST /api/categories/create-defaults - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/categories/create-defaults - ERROR: {str(e)} ===")
        return handle_exception(e)
