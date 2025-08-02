from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import bcrypt
from database import AccountRepository
from utils.logger import get_logger, log_function_call

class AuthController:
    """
    Controller for authentication and account management
    """
    
    @staticmethod
    @log_function_call
    def login(email, password):
        """
        Account login with email/password
        """
        logger = get_logger(__name__)
        logger.info(f"Login attempt for email: {email}")
        
        try:
            # Find account by email
            account = AccountRepository.get_account_by_email(email)
            
            if not account:
                return jsonify({
                    "success": False,
                    "error": {"message": "Invalid email or password"}
                }), 401
            
            # Check if account is active
            if not account.get_field('is_active'):
                return jsonify({
                    "success": False,
                    "error": {"message": "Account is deactivated"}
                }), 401
            
            # Verify password
            if not account.verify_password(password):
                return jsonify({
                    "success": False,
                    "error": {"message": "Invalid email or password"}
                }), 401
            
            # Update last login
            account.update_last_login()
            
            # Create JWT tokens
            access_token = create_access_token(
                identity=str(account._id),
                additional_claims={
                    "email": account.get_field('email'),
                    "account_type": account.get_field('account_type')
                }
            )
            refresh_token = create_refresh_token(identity=str(account._id))
            
            return jsonify({
                "success": True,
                "data": {
                    "token": access_token,
                    "refresh_token": refresh_token,
                    "user": account.to_public_dict()
                },
                "message": "Login successful"
            })
            
        except Exception as e:
            logger.error(f"Login failed for {email}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Login failed: {str(e)}"}
            }), 500
    
    @staticmethod
    def logout():
        """
        Account logout
        """
        try:
            # In a real implementation, you might want to blacklist the token
            return jsonify({
                "success": True,
                "message": "Logout successful"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Logout failed: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def register(data):
        """
        Account registration
        """
        logger = get_logger(__name__)
        logger.info(f"Registration attempt for email: {data.get('email')}")
        
        try:
            # Validate required fields
            required_fields = ['email', 'password', 'account_name']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        "success": False,
                        "error": {"message": f"Missing required field: {field}"}
                    }), 400
            
            # Check if email already exists
            existing_account = AccountRepository.get_account_by_email(data.get('email'))
            if existing_account:
                return jsonify({
                    "success": False,
                    "error": {"message": "Email already registered"}
                }), 409
            
            # Create new account
            account = AccountRepository.create_account(
                email=data.get('email'),
                password=data.get('password'),
                account_name=data.get('account_name'),
                account_type=data.get('account_type', 'standard')
            )
            
            return jsonify({
                "success": True,
                "data": account.to_public_dict(),
                "message": "Registration successful"
            }), 201
            
        except Exception as e:
            logger.error(f"Registration failed for {data.get('email')}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Registration failed: {str(e)}"}
            }), 500
    
    @staticmethod
    @jwt_required()
    @log_function_call
    def get_current_account():
        """
        Get current account profile
        """
        logger = get_logger(__name__)
        
        try:
            current_user_id = get_jwt_identity()
            logger.info(f"Getting current account for user: {current_user_id}")
            
            account = AccountRepository.get_account_by_id(current_user_id)
            
            if not account:
                return jsonify({
                    "success": False,
                    "error": {"message": "Account not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": account.to_public_dict()
            })
            
        except Exception as e:
            logger.error(f"Failed to get current account: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to get current account: {str(e)}"}
            }), 500
    
    @staticmethod
    @jwt_required()
    @log_function_call
    def update_profile(data):
        """
        Update account profile
        """
        logger = get_logger(__name__)
        
        try:
            current_user_id = get_jwt_identity()
            logger.info(f"Updating profile for user: {current_user_id}")
            
            account = AccountRepository.update_account(current_user_id, data)
            
            if not account:
                return jsonify({
                    "success": False,
                    "error": {"message": "Account not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": account.to_public_dict(),
                "message": "Profile updated successfully"
            })
            
        except Exception as e:
            logger.error(f"Profile update failed: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Profile update failed: {str(e)}"}
            }), 500
    
    @staticmethod
    @jwt_required(refresh=True)
    def refresh_token():
        """
        Token refresh
        """
        try:
            current_user_id = get_jwt_identity()
            
            # Create new access token
            new_access_token = create_access_token(identity=current_user_id)
            
            return jsonify({
                "success": True,
                "data": {
                    "token": new_access_token
                },
                "message": "Token refreshed successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Token refresh failed: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def forgot_password(email):
        """
        Password reset request
        """
        logger = get_logger(__name__)
        logger.info(f"Password reset request for email: {email}")
        
        try:
            # Check if account exists
            account = AccountRepository.get_account_by_email(email)
            
            # Always return success message for security (don't reveal if email exists)
            # In real implementation:
            # 1. Generate reset token if account exists
            # 2. Send reset email
            # 3. Store token with expiration
            
            if account:
                # TODO: Generate reset token and send email
                logger.info(f"Password reset token would be generated for: {email}")
            
            return jsonify({
                "success": True,
                "message": "Password reset email sent (if account exists)"
            })
            
        except Exception as e:
            logger.error(f"Password reset request failed for {email}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Password reset request failed: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def reset_password(token, new_password):
        """
        Password reset confirmation
        """
        logger = get_logger(__name__)
        logger.info(f"Password reset attempt with token: {token[:10]}...")
        
        try:
            # In real implementation:
            # 1. Validate reset token from database
            # 2. Check token expiration
            # 3. Find associated account
            # 4. Hash new password
            # 5. Update password in database
            # 6. Invalidate reset token
            
            # For now, return error since token system not implemented
            return jsonify({
                "success": False,
                "error": {"message": "Password reset token system not yet implemented"}
            }), 501
            
        except Exception as e:
            logger.error(f"Password reset failed: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Password reset failed: {str(e)}"}
            }), 500
