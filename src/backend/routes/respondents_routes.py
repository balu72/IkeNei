from flask import Blueprint, request
from controllers.respondents_controller import RespondentsController
from middleware.auth_middleware import require_auth
from utils.response_helpers import validation_error_response, handle_exception

respondents_bp = Blueprint('respondents', __name__)

@respondents_bp.route('/api/respondents', methods=['GET'])
@require_auth
def get_respondents():
    """
    Get account's respondents
    """
    try:
        # Optional subject_id filter
        subject_id = request.args.get('subject_id', type=int)
        return RespondentsController.get_all_respondents(subject_id)
    
    except Exception as e:
        return handle_exception(e)

@respondents_bp.route('/api/respondents', methods=['POST'])
@require_auth
def create_respondent():
    """
    Create new respondent
    """
    try:
        data = request.get_json()
        
        # Basic validation
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['subject_id', 'name', 'email', 'relationship']
        errors = {}
        
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        # Validate email format (basic check)
        email = data.get('email')
        if email and '@' not in email:
            errors['email'] = "Invalid email format"
        
        # Validate relationship
        relationship = data.get('relationship')
        valid_relationships = [
            'Peer', 'Subordinate', 'Boss', 'Customer', 'Previous Employer', 
            'Super Boss', 'Parent', 'Teacher', 'Counseller', 'Third Party', 'other'
        ]
        
        if relationship and relationship not in valid_relationships:
            errors['relationship'] = f"Relationship must be one of: {', '.join(valid_relationships)}"
        
        if errors:
            return validation_error_response(errors)
        
        return RespondentsController.create_respondent(data)
    
    except Exception as e:
        return handle_exception(e)

@respondents_bp.route('/api/respondents/<int:respondent_id>', methods=['GET'])
@require_auth
def get_respondent(respondent_id):
    """
    Get respondent details
    """
    try:
        return RespondentsController.get_respondent_by_id(respondent_id)
    
    except Exception as e:
        return handle_exception(e)

@respondents_bp.route('/api/respondents/<int:respondent_id>', methods=['PUT'])
@require_auth
def update_respondent(respondent_id):
    """
    Update respondent
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        # Validate email format if provided
        email = data.get('email')
        if email and '@' not in email:
            return validation_error_response({"email": "Invalid email format"})
        
        # Validate relationship if provided
        relationship = data.get('relationship')
        if relationship:
            valid_relationships = ['supervisor', 'peer', 'direct_report', 'customer', 'other']
            if relationship not in valid_relationships:
                return validation_error_response({
                    'relationship': f"Relationship must be one of: {', '.join(valid_relationships)}"
                })
        
        return RespondentsController.update_respondent(respondent_id, data)
    
    except Exception as e:
        return handle_exception(e)

@respondents_bp.route('/api/respondents/<int:respondent_id>', methods=['DELETE'])
@require_auth
def delete_respondent(respondent_id):
    """
    Delete respondent
    """
    try:
        return RespondentsController.delete_respondent(respondent_id)
    
    except Exception as e:
        return handle_exception(e)
