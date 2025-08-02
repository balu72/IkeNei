from flask import jsonify
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
            # These should eventually come from database
            categories = [
                'Peer',
                'Subordinate', 
                'Boss',
                'Customer',
                'Previous Employer',
                'Super Boss',
                'Parent',
                'Teacher',
                'Counseller',
                'Third Party',
                'Others'
            ]
            
            return jsonify({
                "success": True,
                "data": categories
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve categories: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve categories: {str(e)}"}
            }), 500
