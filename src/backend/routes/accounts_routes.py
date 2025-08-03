from flask import Blueprint, request, jsonify
from controllers.accounts_controller import AccountsController
from middleware.auth_middleware import require_system_admin_role, require_admin_roles
from utils.response_helpers import validation_error_response, handle_exception
from utils.pagination import get_pagination_params, get_filter_params
from utils.logger import get_logger

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/api/accounts', methods=['GET'])
@require_admin_roles
def get_accounts():
    """
    Get all accounts with filtering (search, state, type)
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: GET /api/accounts ===")
    
    try:
        page, limit = get_pagination_params()
        filters = get_filter_params()
        logger.info(f"Request parameters - page: {page}, limit: {limit}, filters: {filters}")
        
        result = AccountsController.get_all_accounts(page, limit, filters)
        logger.info("=== EXIT: GET /api/accounts - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/accounts - ERROR: {str(e)} ===")
        return handle_exception(e)

@accounts_bp.route('/api/accounts', methods=['POST'])
@require_system_admin_role
def create_account():
    """
    Create new account
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/accounts ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Request data: {data}")
        
        # Basic validation
        if not data:
            logger.warning("Create account failed: No request body provided")
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
            logger.warning(f"Create account validation failed: {errors}")
            return validation_error_response(errors)
        
        logger.info(f"Creating account for email: {data.get('email')}")
        result = AccountsController.create_account(data)
        logger.info("=== EXIT: POST /api/accounts - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/accounts - ERROR: {str(e)} ===")
        return handle_exception(e)

@accounts_bp.route('/api/accounts/<int:account_id>', methods=['GET'])
@require_system_admin_role
def get_account(account_id):
    """
    Get specific account details
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: GET /api/accounts/{account_id} ===")
    
    try:
        result = AccountsController.get_account_by_id(account_id)
        logger.info(f"=== EXIT: GET /api/accounts/{account_id} - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/accounts/{account_id} - ERROR: {str(e)} ===")
        return handle_exception(e)

@accounts_bp.route('/api/accounts/<int:account_id>', methods=['PUT'])
@require_system_admin_role
def update_account(account_id):
    """
    Update account information
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: PUT /api/accounts/{account_id} ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Update data for account {account_id}: {data}")
        
        if not data:
            logger.warning(f"Update account {account_id} failed: No request body provided")
            return validation_error_response({"request": "Request body is required"})
        
        # Validate account type if provided
        account_type = data.get('account_type')
        if account_type:
            valid_types = ['standard', 'premium', 'enterprise']
            if account_type not in valid_types:
                logger.warning(f"Update account {account_id} failed: Invalid account type {account_type}")
                return validation_error_response({
                    'account_type': f"Account type must be one of: {', '.join(valid_types)}"
                })
        
        result = AccountsController.update_account(account_id, data)
        logger.info(f"=== EXIT: PUT /api/accounts/{account_id} - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: PUT /api/accounts/{account_id} - ERROR: {str(e)} ===")
        return handle_exception(e)

@accounts_bp.route('/api/accounts/<int:account_id>/status', methods=['PATCH'])
@require_system_admin_role
def update_account_status(account_id):
    """
    Activate/deactivate account
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: PATCH /api/accounts/{account_id}/status ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Status update data for account {account_id}: {data}")
        
        if not data or 'is_active' not in data:
            logger.warning(f"Update account {account_id} status failed: Missing is_active field")
            return validation_error_response({"is_active": "is_active field is required"})
        
        is_active = data.get('is_active')
        
        if not isinstance(is_active, bool):
            logger.warning(f"Update account {account_id} status failed: Invalid is_active value {is_active}")
            return validation_error_response({"is_active": "is_active must be a boolean value"})
        
        logger.info(f"Updating account {account_id} status to: {is_active}")
        result = AccountsController.update_account_status(account_id, is_active)
        logger.info(f"=== EXIT: PATCH /api/accounts/{account_id}/status - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: PATCH /api/accounts/{account_id}/status - ERROR: {str(e)} ===")
        return handle_exception(e)

@accounts_bp.route('/api/accounts/<int:account_id>', methods=['DELETE'])
@require_system_admin_role
def delete_account(account_id):
    """
    Delete account
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: DELETE /api/accounts/{account_id} ===")
    
    try:
        result = AccountsController.delete_account(account_id)
        logger.info(f"=== EXIT: DELETE /api/accounts/{account_id} - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: DELETE /api/accounts/{account_id} - ERROR: {str(e)} ===")
        return handle_exception(e)
