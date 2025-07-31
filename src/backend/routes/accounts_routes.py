from flask import Blueprint, request, jsonify
from controllers.accounts_controller import AccountsController
from middleware.auth_middleware import require_system_admin_role
from utils.response_helpers import validation_error_response, handle_exception
from utils.pagination import get_pagination_params, get_filter_params

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/api/accounts', methods=['GET'])
@require_system_admin_role
def get_accounts():
    """
    Get all accounts with filtering (search, state, type)
    """
    try:
        page, limit = get_pagination_params()
        filters = get_filter_params()
        
        return AccountsController.get_all_accounts(page, limit, filters)
    
    except Exception as e:
        return handle_exception(e)

@accounts_bp.route('/api/accounts', methods=['POST'])
@require_system_admin_role
def create_account():
    """
    Create new account
    """
    try:
        data = request.get_json()
        
        # Basic validation
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['email', 'account_name', 'account_type']
        errors = {}
        
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        # Validate account type
        account_type = data.get('account_type')
        valid_types = ['standard', 'premium', 'enterprise']
        
        if account_type and account_type not in valid_types:
            errors['account_type'] = f"Account type must be one of: {', '.join(valid_types)}"
        
        if errors:
            return validation_error_response(errors)
        
        return AccountsController.create_account(data)
    
    except Exception as e:
        return handle_exception(e)

@accounts_bp.route('/api/accounts/<int:account_id>', methods=['GET'])
@require_system_admin_role
def get_account(account_id):
    """
    Get specific account details
    """
    try:
        return AccountsController.get_account_by_id(account_id)
    
    except Exception as e:
        return handle_exception(e)

@accounts_bp.route('/api/accounts/<int:account_id>', methods=['PUT'])
@require_system_admin_role
def update_account(account_id):
    """
    Update account information
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        # Validate account type if provided
        account_type = data.get('account_type')
        if account_type:
            valid_types = ['standard', 'premium', 'enterprise']
            if account_type not in valid_types:
                return validation_error_response({
                    'account_type': f"Account type must be one of: {', '.join(valid_types)}"
                })
        
        return AccountsController.update_account(account_id, data)
    
    except Exception as e:
        return handle_exception(e)

@accounts_bp.route('/api/accounts/<int:account_id>/status', methods=['PATCH'])
@require_system_admin_role
def update_account_status(account_id):
    """
    Activate/deactivate account
    """
    try:
        data = request.get_json()
        
        if not data or 'is_active' not in data:
            return validation_error_response({"is_active": "is_active field is required"})
        
        is_active = data.get('is_active')
        
        if not isinstance(is_active, bool):
            return validation_error_response({"is_active": "is_active must be a boolean value"})
        
        return AccountsController.update_account_status(account_id, is_active)
    
    except Exception as e:
        return handle_exception(e)

@accounts_bp.route('/api/accounts/<int:account_id>', methods=['DELETE'])
@require_system_admin_role
def delete_account(account_id):
    """
    Delete account
    """
    try:
        return AccountsController.delete_account(account_id)
    
    except Exception as e:
        return handle_exception(e)
