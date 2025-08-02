from flask import jsonify
from datetime import datetime
from database import AccountRepository
from utils.logger import get_logger, log_function_call

class AccountsController:
    """
    Controller for managing accounts (System Admin functionality)
    """
    
    @staticmethod
    @log_function_call
    def get_all_accounts(page=1, limit=20, filters=None):
        """
        Get all accounts with pagination and filtering
        """
        logger = get_logger(__name__)
        logger.info(f"Fetching accounts - page: {page}, limit: {limit}, filters: {filters}")
        
        try:
            # Use AccountRepository to get accounts from database
            result = AccountRepository.get_all_accounts(
                page=page,
                per_page=limit,
                filters=filters
            )
            
            return jsonify({
                "success": True,
                "data": result['accounts'],
                "pagination": result['pagination']
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve accounts: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def create_account(data):
        """
        Create a new account
        """
        logger = get_logger(__name__)
        logger.info(f"Creating new account with data: {data}")
        
        try:
            # Validate required fields
            required_fields = ['email', 'password', 'account_name']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        "success": False,
                        "error": {"message": f"Missing required field: {field}"}
                    }), 400
            
            # Create account using repository
            account = AccountRepository.create_account(
                email=data.get('email'),
                password=data.get('password'),
                account_name=data.get('account_name'),
                account_type=data.get('account_type', 'standard')
            )
            
            return jsonify({
                "success": True,
                "data": account.to_public_dict(),
                "message": "Account created successfully"
            }), 201
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create account: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_account_by_id(account_id):
        """
        Get account by ID
        """
        try:
            # Mock implementation - replace with actual database query
            mock_account = {
                "id": str(account_id),
                "email": f"account{account_id}@example.com",
                "account_name": f"Demo Account {account_id}",
                "account_type": "standard",
                "is_active": True,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
                "settings": {
                    "notifications_enabled": True,
                    "theme": "light"
                }
            }
            
            return jsonify({
                "success": True,
                "data": mock_account
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve account: {str(e)}"}
            }), 500
    
    @staticmethod
    def update_account(account_id, data):
        """
        Update account information
        """
        try:
            # Mock implementation - replace with actual database update
            updated_account = {
                "id": str(account_id),
                "email": data.get('email', f"account{account_id}@example.com"),
                "account_name": data.get('account_name', f"Demo Account {account_id}"),
                "account_type": data.get('account_type', 'standard'),
                "is_active": data.get('is_active', True),
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": updated_account,
                "message": "Account updated successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update account: {str(e)}"}
            }), 500
    
    @staticmethod
    def update_account_status(account_id, is_active):
        """
        Update account active status
        """
        try:
            # Mock implementation - replace with actual database update
            updated_account = {
                "id": str(account_id),
                "email": f"account{account_id}@example.com",
                "account_name": f"Demo Account {account_id}",
                "account_type": "standard",
                "is_active": is_active,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            status_text = "activated" if is_active else "deactivated"
            
            return jsonify({
                "success": True,
                "data": updated_account,
                "message": f"Account {status_text} successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update account status: {str(e)}"}
            }), 500
    
    @staticmethod
    def delete_account(account_id):
        """
        Delete account
        """
        try:
            # Mock implementation - replace with actual database deletion
            # In a real implementation, you might want to soft delete or archive
            
            return jsonify({
                "success": True,
                "message": f"Account {account_id} deleted successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete account: {str(e)}"}
            }), 500
