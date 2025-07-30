from flask import Blueprint, request
from controllers.subjects_controller import SubjectsController
from middleware.auth_middleware import require_auth
from utils.response_helpers import validation_error_response, handle_exception

subjects_bp = Blueprint('subjects', __name__)

@subjects_bp.route('/api/subjects', methods=['GET'])
@require_auth
def get_subjects():
    """
    Get account's subjects
    """
    try:
        return SubjectsController.get_account_subjects()
    
    except Exception as e:
        return handle_exception(e)

@subjects_bp.route('/api/subjects', methods=['POST'])
@require_auth
def create_subject():
    """
    Create new subject
    """
    try:
        data = request.get_json()
        
        # Basic validation
        if not data:
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
            return validation_error_response(errors)
        
        return SubjectsController.create_subject(data)
    
    except Exception as e:
        return handle_exception(e)

@subjects_bp.route('/api/subjects/<int:subject_id>', methods=['GET'])
@require_auth
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
def delete_subject(subject_id):
    """
    Delete subject
    """
    try:
        return SubjectsController.delete_subject(subject_id)
    
    except Exception as e:
        return handle_exception(e)
