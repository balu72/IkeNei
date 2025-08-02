from flask import Blueprint
from controllers.categories_controller import CategoriesController
from middleware.auth_middleware import require_auth
from utils.response_helpers import handle_exception
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
