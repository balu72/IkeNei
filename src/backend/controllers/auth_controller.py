from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import bcrypt
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
            # Mock authentication - replace with actual database lookup
            # For demo purposes, accept any email/password combination
            mock_users = {
                "account@example.com": {
                    "id": "1",
                    "email": "account@example.com",
                    "name": "Account User",
                    "role": "account",
                    "account_name": "Demo Account",
                    "is_active": True
                },
                "domainadmin@example.com": {
                    "id": "2", 
                    "email": "domainadmin@example.com",
                    "name": "Domain Admin",
                    "role": "domain_admin",
                    "account_name": "Domain Admin Account",
                    "is_active": True
                },
                "systemadmin@example.com": {
                    "id": "3",
                    "email": "systemadmin@example.com", 
                    "name": "System Admin",
                    "role": "system_admin",
                    "account_name": "System Admin Account",
                    "is_active": True
                }
            }
            
            # Check if user exists in mock data
            user = mock_users.get(email)
            if not user:
                # For demo, create a default account user for any other email
                user = {
                    "id": "demo_user",
                    "email": email,
                    "name": "Demo User",
                    "role": "account",
                    "account_name": "Demo Account",
                    "is_active": True
                }
            
            # In real implementation, verify password hash
            # For demo, accept any password
            
            # Create JWT tokens
            access_token = create_access_token(
                identity=user["id"],
                additional_claims={
                    "email": user["email"],
                    "role": user["role"]
                }
            )
            refresh_token = create_refresh_token(identity=user["id"])
            
            return jsonify({
                "success": True,
                "data": {
                    "token": access_token,
                    "refresh_token": refresh_token,
                    "user": user
                },
                "message": "Login successful"
            })
            
        except Exception as e:
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
    def register(data):
        """
        Account registration
        """
        try:
            # Mock registration - replace with actual database operations
            new_user = {
                "id": "new_user_id",
                "email": data.get('email'),
                "name": data.get('name', data.get('account_name')),
                "role": "account",  # Default role for new registrations
                "account_name": data.get('account_name'),
                "is_active": True,
                "created_at": datetime.utcnow().isoformat() + "Z"
            }
            
            # In real implementation:
            # 1. Check if email already exists
            # 2. Hash the password
            # 3. Save to database
            # 4. Send verification email
            
            return jsonify({
                "success": True,
                "data": new_user,
                "message": "Registration successful"
            }), 201
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Registration failed: {str(e)}"}
            }), 500
    
    @staticmethod
    @jwt_required()
    def get_current_account():
        """
        Get current account profile
        """
        try:
            current_user_id = get_jwt_identity()
            
            # Mock user data - replace with actual database lookup
            mock_user = {
                "id": current_user_id,
                "email": "user@example.com",
                "name": "Current User",
                "role": "account",
                "account_name": "Demo Account",
                "is_active": True,
                "created_at": "2024-01-01T00:00:00Z",
                "last_login": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": mock_user
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to get current account: {str(e)}"}
            }), 500
    
    @staticmethod
    @jwt_required()
    def update_profile(data):
        """
        Update account profile
        """
        try:
            current_user_id = get_jwt_identity()
            
            # Mock profile update - replace with actual database update
            updated_user = {
                "id": current_user_id,
                "email": data.get('email', 'user@example.com'),
                "name": data.get('name', 'Updated User'),
                "role": "account",
                "account_name": data.get('account_name', 'Demo Account'),
                "is_active": True,
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": updated_user,
                "message": "Profile updated successfully"
            })
            
        except Exception as e:
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
    def forgot_password(email):
        """
        Password reset request
        """
        try:
            # Mock password reset - replace with actual implementation
            # In real implementation:
            # 1. Check if email exists
            # 2. Generate reset token
            # 3. Send reset email
            # 4. Store token with expiration
            
            return jsonify({
                "success": True,
                "message": "Password reset email sent (if account exists)"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Password reset request failed: {str(e)}"}
            }), 500
    
    @staticmethod
    def reset_password(token, new_password):
        """
        Password reset confirmation
        """
        try:
            # Mock password reset - replace with actual implementation
            # In real implementation:
            # 1. Validate reset token
            # 2. Check token expiration
            # 3. Hash new password
            # 4. Update password in database
            # 5. Invalidate reset token
            
            return jsonify({
                "success": True,
                "message": "Password reset successful"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Password reset failed: {str(e)}"}
            }), 500
