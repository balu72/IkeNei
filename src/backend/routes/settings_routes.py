from flask import Blueprint, request
from controllers.settings_controller import SettingsController
from middleware.auth_middleware import require_system_admin_role
from utils.response_helpers import validation_error_response, handle_exception
from utils.pagination import get_pagination_params, get_filter_params

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/api/settings', methods=['GET'])
@require_system_admin_role
def get_settings():
    """
    Get all system settings with filtering
    """
    try:
        page, limit = get_pagination_params()
        filters = get_filter_params()
        
        return SettingsController.get_all_settings(page, limit, filters)
    
    except Exception as e:
        return handle_exception(e)

@settings_bp.route('/api/settings/<string:setting_key>', methods=['PUT'])
@require_system_admin_role
def update_setting(setting_key):
    """
    Update specific setting
    """
    try:
        data = request.get_json()
        
        if not data or 'value' not in data:
            return validation_error_response({"value": "Setting value is required"})
        
        return SettingsController.update_setting(setting_key, data.get('value'))
    
    except Exception as e:
        return handle_exception(e)

@settings_bp.route('/api/settings/<string:setting_key>/toggle', methods=['PATCH'])
@require_system_admin_role
def toggle_setting(setting_key):
    """
    Toggle boolean settings
    """
    try:
        return SettingsController.toggle_boolean_setting(setting_key)
    
    except Exception as e:
        return handle_exception(e)

@settings_bp.route('/api/settings/reset/<string:setting_key>', methods=['POST'])
@require_system_admin_role
def reset_setting(setting_key):
    """
    Reset setting to default
    """
    try:
        return SettingsController.reset_setting_to_default(setting_key)
    
    except Exception as e:
        return handle_exception(e)

@settings_bp.route('/api/settings/categories', methods=['GET'])
@require_system_admin_role
def get_setting_categories():
    """
    Get setting categories
    """
    try:
        return SettingsController.get_setting_categories()
    
    except Exception as e:
        return handle_exception(e)
