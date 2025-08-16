from flask import Blueprint, request
from controllers.traits_controller import TraitsController
from middleware.auth_middleware import require_domain_admin_role, require_admin_roles
from utils.response_helpers import validation_error_response, handle_exception
from utils.pagination import get_pagination_params, get_filter_params
from utils.route_logger import log_route

traits_bp = Blueprint('traits', __name__)

@traits_bp.route('/api/traits', methods=['GET'])
@require_admin_roles
@log_route
def get_traits():
    """
    Get all traits with filtering
    """
    try:
        page, limit = get_pagination_params()
        filters = get_filter_params()
        
        return TraitsController.get_all_traits(page, limit, filters)
    
    except Exception as e:
        return handle_exception(e)

@traits_bp.route('/api/traits', methods=['POST'])
@require_domain_admin_role
@log_route
def create_trait():
    """
    Create new trait
    """
    try:
        data = request.get_json()
        
        # Basic validation
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['name', 'description']
        errors = {}
        
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        if errors:
            return validation_error_response(errors)
        
        return TraitsController.create_trait(data)
    
    except Exception as e:
        return handle_exception(e)

@traits_bp.route('/api/traits/<trait_id>', methods=['GET'])
@require_admin_roles
@log_route
def get_trait(trait_id):
    """
    Get specific trait details
    """
    try:
        return TraitsController.get_trait_by_id(trait_id)
    
    except Exception as e:
        return handle_exception(e)

@traits_bp.route('/api/traits/<trait_id>', methods=['PUT'])
@require_domain_admin_role
@log_route
def update_trait(trait_id):
    """
    Update trait
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        return TraitsController.update_trait(trait_id, data)
    
    except Exception as e:
        return handle_exception(e)

@traits_bp.route('/api/traits/<trait_id>', methods=['DELETE'])
@require_domain_admin_role
@log_route
def delete_trait(trait_id):
    """
    Delete trait
    """
    try:
        return TraitsController.delete_trait(trait_id)
    
    except Exception as e:
        return handle_exception(e)

@traits_bp.route('/api/traits/<trait_id>/status', methods=['PATCH'])
@require_domain_admin_role
@log_route
def update_trait_status(trait_id):
    """
    Change trait status (Active/Draft/Inactive)
    """
    try:
        data = request.get_json()
        
        if not data or not data.get('status'):
            return validation_error_response({"status": "Status is required"})
        
        status = data.get('status')
        valid_statuses = ['active', 'draft', 'inactive']
        
        if status.lower() not in valid_statuses:
            return validation_error_response({
                "status": f"Status must be one of: {', '.join(valid_statuses)}"
            })
        
        return TraitsController.update_trait_status(trait_id, status)
    
    except Exception as e:
        return handle_exception(e)

@traits_bp.route('/api/traits/categories', methods=['GET'])
@require_admin_roles
@log_route
def get_trait_categories():
    """
    Get trait categories
    """
    try:
        return TraitsController.get_trait_categories()
    
    except Exception as e:
        return handle_exception(e)

@traits_bp.route('/api/traits/usage', methods=['GET'])
@require_admin_roles
@log_route
def get_trait_usage():
    """
    Get trait usage statistics
    """
    try:
        return TraitsController.get_trait_usage_statistics()
    
    except Exception as e:
        return handle_exception(e)
