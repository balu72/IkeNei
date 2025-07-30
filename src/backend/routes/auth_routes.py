from flask import Blueprint, request
from controllers.auth_controller import AuthController
from utils.response_helpers import validation_error_response, handle_exception

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """
    Account login with email/password
    """
    try:
        data = request.get_json()
        
        # Basic validation
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return validation_error_response({
                "email": "Email is required" if not email else None,
                "password": "Password is required" if not password else None
            })
        
        return AuthController.login(email, password)
    
    except Exception as e:
        return handle_exception(e)

@auth_bp.route('/api/auth/logout', methods=['POST'])
def logout():
    """
    Account logout
    """
    try:
        return AuthController.logout()
    except Exception as e:
        return handle_exception(e)

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    """
    Account registration
    """
    try:
        data = request.get_json()
        
        # Basic validation
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['email', 'password', 'account_name']
        errors = {}
        
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        if errors:
            return validation_error_response(errors)
        
        return AuthController.register(data)
    
    except Exception as e:
        return handle_exception(e)

@auth_bp.route('/api/auth/me', methods=['GET'])
def get_current_account():
    """
    Get current account profile
    """
    try:
        return AuthController.get_current_account()
    except Exception as e:
        return handle_exception(e)

@auth_bp.route('/api/auth/profile', methods=['PUT'])
def update_profile():
    """
    Update account profile
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        return AuthController.update_profile(data)
    
    except Exception as e:
        return handle_exception(e)

@auth_bp.route('/api/auth/refresh', methods=['POST'])
def refresh_token():
    """
    Token refresh
    """
    try:
        return AuthController.refresh_token()
    except Exception as e:
        return handle_exception(e)

@auth_bp.route('/api/auth/forgot', methods=['POST'])
def forgot_password():
    """
    Password reset request
    """
    try:
        data = request.get_json()
        
        if not data or not data.get('email'):
            return validation_error_response({"email": "Email is required"})
        
        return AuthController.forgot_password(data.get('email'))
    
    except Exception as e:
        return handle_exception(e)

@auth_bp.route('/api/auth/reset', methods=['POST'])
def reset_password():
    """
    Password reset confirmation
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        token = data.get('token')
        new_password = data.get('new_password')
        
        if not token or not new_password:
            return validation_error_response({
                "token": "Reset token is required" if not token else None,
                "new_password": "New password is required" if not new_password else None
            })
        
        return AuthController.reset_password(token, new_password)
    
    except Exception as e:
        return handle_exception(e)
