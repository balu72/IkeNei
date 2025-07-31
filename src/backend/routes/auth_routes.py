from flask import Blueprint, request
from controllers.auth_controller import AuthController
from utils.response_helpers import validation_error_response, handle_exception
from utils.logger import get_logger

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """
    Account login with email/password
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/auth/login ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Request data received: {data}")
        
        # Basic validation
        if not data:
            logger.warning("Login request failed: No request body provided")
            return validation_error_response({"request": "Request body is required"})
        
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            logger.warning(f"Login request failed: Missing required fields - email: {bool(email)}, password: {bool(password)}")
            return validation_error_response({
                "email": "Email is required" if not email else None,
                "password": "Password is required" if not password else None
            })
        
        logger.info(f"Processing login request for email: {email}")
        result = AuthController.login(email, password)
        logger.info("=== EXIT: POST /api/auth/login - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/auth/login - ERROR: {str(e)} ===")
        return handle_exception(e)

@auth_bp.route('/api/auth/logout', methods=['POST'])
def logout():
    """
    Account logout
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/auth/logout ===")
    
    try:
        result = AuthController.logout()
        logger.info("=== EXIT: POST /api/auth/logout - SUCCESS ===")
        return result
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/auth/logout - ERROR: {str(e)} ===")
        return handle_exception(e)

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    """
    Account registration
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/auth/register ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Registration data: {data}")
        
        # Basic validation
        if not data:
            logger.warning("Registration failed: No request body provided")
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['email', 'password', 'account_name']
        errors = {}
        
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        if errors:
            logger.warning(f"Registration validation failed: {errors}")
            return validation_error_response(errors)
        
        logger.info(f"Processing registration for email: {data.get('email')}")
        result = AuthController.register(data)
        logger.info("=== EXIT: POST /api/auth/register - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/auth/register - ERROR: {str(e)} ===")
        return handle_exception(e)

@auth_bp.route('/api/auth/me', methods=['GET'])
def get_current_account():
    """
    Get current account profile
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: GET /api/auth/me ===")
    
    try:
        result = AuthController.get_current_account()
        logger.info("=== EXIT: GET /api/auth/me - SUCCESS ===")
        return result
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/auth/me - ERROR: {str(e)} ===")
        return handle_exception(e)

@auth_bp.route('/api/auth/profile', methods=['PUT'])
def update_profile():
    """
    Update account profile
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: PUT /api/auth/profile ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Profile update data: {data}")
        
        if not data:
            logger.warning("Profile update failed: No request body provided")
            return validation_error_response({"request": "Request body is required"})
        
        result = AuthController.update_profile(data)
        logger.info("=== EXIT: PUT /api/auth/profile - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: PUT /api/auth/profile - ERROR: {str(e)} ===")
        return handle_exception(e)

@auth_bp.route('/api/auth/refresh', methods=['POST'])
def refresh_token():
    """
    Token refresh
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/auth/refresh ===")
    
    try:
        result = AuthController.refresh_token()
        logger.info("=== EXIT: POST /api/auth/refresh - SUCCESS ===")
        return result
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/auth/refresh - ERROR: {str(e)} ===")
        return handle_exception(e)

@auth_bp.route('/api/auth/forgot', methods=['POST'])
def forgot_password():
    """
    Password reset request
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/auth/forgot ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Forgot password request: {data}")
        
        if not data or not data.get('email'):
            logger.warning("Forgot password failed: Email is required")
            return validation_error_response({"email": "Email is required"})
        
        logger.info(f"Processing forgot password for email: {data.get('email')}")
        result = AuthController.forgot_password(data.get('email'))
        logger.info("=== EXIT: POST /api/auth/forgot - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/auth/forgot - ERROR: {str(e)} ===")
        return handle_exception(e)

@auth_bp.route('/api/auth/reset', methods=['POST'])
def reset_password():
    """
    Password reset confirmation
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/auth/reset ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Password reset data: {data}")
        
        if not data:
            logger.warning("Password reset failed: No request body provided")
            return validation_error_response({"request": "Request body is required"})
        
        token = data.get('token')
        new_password = data.get('new_password')
        
        if not token or not new_password:
            logger.warning(f"Password reset validation failed - token: {bool(token)}, password: {bool(new_password)}")
            return validation_error_response({
                "token": "Reset token is required" if not token else None,
                "new_password": "New password is required" if not new_password else None
            })
        
        logger.info("Processing password reset")
        result = AuthController.reset_password(token, new_password)
        logger.info("=== EXIT: POST /api/auth/reset - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/auth/reset - ERROR: {str(e)} ===")
        return handle_exception(e)
