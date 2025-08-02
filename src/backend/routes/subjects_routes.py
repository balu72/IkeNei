from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity
from controllers.subjects_controller import SubjectsController
from middleware.auth_middleware import require_auth
from utils.response_helpers import validation_error_response, handle_exception
from utils.logger import get_logger
from utils.route_logger import log_route

subjects_bp = Blueprint('subjects', __name__)

@subjects_bp.route('/api/subjects', methods=['GET'])
@require_auth
def get_subjects():
    """
    Get account's subjects
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: GET /api/subjects ===")
    
    try:
        logger.info("Fetching subjects for current account")
        result = SubjectsController.get_all_subjects()
        logger.info("=== EXIT: GET /api/subjects - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/subjects - ERROR: {str(e)} ===")
        return handle_exception(e)

@subjects_bp.route('/api/subjects', methods=['POST'])
@require_auth
def create_subject():
    """
    Create new subject
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/subjects ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Subject creation data: {data}")
        
        # Basic validation
        if not data:
            logger.warning("Create subject failed: No request body provided")
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['name', 'email']
        errors = {}
        
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        # Validate email format (basic check)
        email = data.get('email')
        if email and '@' not in email:
            errors['email'] = "Invalid email format"
        
        if errors:
            logger.warning(f"Create subject validation failed: {errors}")
            return validation_error_response(errors)
        
        # Get account_id from JWT token
        current_user_id = get_jwt_identity()
        data['account_id'] = current_user_id
        
        logger.info(f"Creating subject: {data.get('name')} ({data.get('email')}) for account: {current_user_id}")
        result = SubjectsController.create_subject(data)
        logger.info("=== EXIT: POST /api/subjects - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/subjects - ERROR: {str(e)} ===")
        return handle_exception(e)

@subjects_bp.route('/api/subjects/<int:subject_id>', methods=['GET'])
@require_auth
@log_route
def get_subject(subject_id):
    """
    Get subject details
    """
    try:
        return SubjectsController.get_subject_by_id(subject_id)
    
    except Exception as e:
        return handle_exception(e)

@subjects_bp.route('/api/subjects/<int:subject_id>', methods=['PUT'])
@require_auth
@log_route
def update_subject(subject_id):
    """
    Update subject
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        # Validate email format if provided
        email = data.get('email')
        if email and '@' not in email:
            return validation_error_response({"email": "Invalid email format"})
        
        return SubjectsController.update_subject(subject_id, data)
    
    except Exception as e:
        return handle_exception(e)

@subjects_bp.route('/api/subjects/<int:subject_id>', methods=['DELETE'])
@require_auth
@log_route
def delete_subject(subject_id):
    """
    Delete subject
    """
    try:
        return SubjectsController.delete_subject(subject_id)
    
    except Exception as e:
        return handle_exception(e)
