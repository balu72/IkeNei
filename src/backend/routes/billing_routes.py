from flask import Blueprint, request
from controllers.billing_controller import BillingController
from middleware.auth_middleware import require_system_admin_role, require_auth
from utils.response_helpers import validation_error_response, handle_exception
from utils.pagination import get_pagination_params, get_filter_params

billing_bp = Blueprint('billing', __name__)

@billing_bp.route('/api/billing', methods=['GET'])
@require_system_admin_role
def get_billing_records():
    """
    Get billing records with filtering (account, date range, status)
    """
    try:
        page, limit = get_pagination_params()
        filters = get_filter_params()
        
        return BillingController.get_all_billing_records(page, limit, filters)
    
    except Exception as e:
        return handle_exception(e)

@billing_bp.route('/api/billing', methods=['POST'])
@require_system_admin_role
def create_billing_record():
    """
    Create new billing record (auto-generated on survey completion)
    """
    try:
        data = request.get_json()
        
        # Basic validation
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['account_id', 'survey_id', 'survey_title', 'subjects_count', 'respondents_count']
        errors = {}
        
        for field in required_fields:
            if data.get(field) is None:  # Allow 0 values
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        # Validate counts are non-negative integers
        for count_field in ['subjects_count', 'respondents_count']:
            count_value = data.get(count_field)
            if count_value is not None and (not isinstance(count_value, int) or count_value < 0):
                errors[count_field] = f"{count_field.replace('_', ' ').title()} must be a non-negative integer"
        
        if errors:
            return validation_error_response(errors)
        
        return BillingController.create_billing_record(data)
    
    except Exception as e:
        return handle_exception(e)

@billing_bp.route('/api/billing/<int:billing_id>', methods=['GET'])
@require_system_admin_role
def get_billing_record(billing_id):
    """
    Get specific billing record details
    """
    try:
        return BillingController.get_billing_record_by_id(billing_id)
    
    except Exception as e:
        return handle_exception(e)

@billing_bp.route('/api/billing/<int:billing_id>', methods=['PUT'])
@require_system_admin_role
def update_billing_record(billing_id):
    """
    Update billing record (amount, status)
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        # Validate billing amount if provided
        billing_amount = data.get('billing_amount')
        if billing_amount is not None:
            try:
                billing_amount = float(billing_amount)
                if billing_amount < 0:
                    return validation_error_response({"billing_amount": "Billing amount must be non-negative"})
            except (ValueError, TypeError):
                return validation_error_response({"billing_amount": "Billing amount must be a valid number"})
        
        # Validate billing status if provided
        billing_status = data.get('billing_status')
        if billing_status:
            valid_statuses = ['pending', 'paid', 'failed', 'cancelled', 'refunded']
            if billing_status not in valid_statuses:
                return validation_error_response({
                    'billing_status': f"Billing status must be one of: {', '.join(valid_statuses)}"
                })
        
        return BillingController.update_billing_record(billing_id, data)
    
    except Exception as e:
        return handle_exception(e)

@billing_bp.route('/api/billing/<int:billing_id>/status', methods=['PATCH'])
@require_system_admin_role
def update_billing_status(billing_id):
    """
    Update billing status (pending, paid, failed)
    """
    try:
        data = request.get_json()
        
        if not data or not data.get('status'):
            return validation_error_response({"status": "Status is required"})
        
        status = data.get('status')
        valid_statuses = ['pending', 'paid', 'failed', 'cancelled', 'refunded']
        
        if status not in valid_statuses:
            return validation_error_response({
                "status": f"Status must be one of: {', '.join(valid_statuses)}"
            })
        
        return BillingController.update_billing_status(billing_id, status)
    
    except Exception as e:
        return handle_exception(e)

@billing_bp.route('/api/billing/account/<int:account_id>', methods=['GET'])
@require_auth
def get_account_billing_records(account_id):
    """
    Get billing records for specific account
    """
    try:
        page, limit = get_pagination_params()
        return BillingController.get_account_billing_records(account_id, page, limit)
    
    except Exception as e:
        return handle_exception(e)

@billing_bp.route('/api/billing/summary', methods=['GET'])
@require_system_admin_role
def get_billing_summary():
    """
    Get billing summary and statistics
    """
    try:
        return BillingController.get_billing_summary()
    
    except Exception as e:
        return handle_exception(e)

@billing_bp.route('/api/billing/calculate', methods=['POST'])
@require_system_admin_role
def calculate_billing_amount():
    """
    Calculate billing amount for survey usage
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['subjects_count', 'respondents_count']
        errors = {}
        
        for field in required_fields:
            if data.get(field) is None:
                errors[field] = f"{field.replace('_', ' ').title()} is required"
            elif not isinstance(data.get(field), int) or data.get(field) < 0:
                errors[field] = f"{field.replace('_', ' ').title()} must be a non-negative integer"
        
        if errors:
            return validation_error_response(errors)
        
        return BillingController.calculate_billing_amount(data)
    
    except Exception as e:
        return handle_exception(e)
