from flask import jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
from datetime import datetime
import bcrypt
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
            # Mock implementation - replace with actual database queries
            mock_accounts = [
                {
                    "id": "1",
                    "email": "account1@example.com",
                    "account_name": "Demo Account 1",
                    "account_type": "standard",
                    "is_active": True,
                    "created_at": "2024-01-01T00:00:00Z",
                    "updated_at": "2024-01-01T00:00:00Z"
                },
                {
                    "id": "2",
                    "email": "account2@example.com",
                    "account_name": "Demo Account 2", 
                    "account_type": "premium",
                    "is_active": True,
                    "created_at": "2024-01-02T00:00:00Z",
                    "updated_at": "2024-01-02T00:00:00Z"
                }
            ]
            
            # Apply filters if provided
            if filters:
                # Filter by search term
                if filters.get('search'):
                    search_term = filters['search'].lower()
                    mock_accounts = [
                        acc for acc in mock_accounts 
                        if search_term in acc['account_name'].lower() or 
                           search_term in acc['email'].lower()
                    ]
                
                # Filter by account type
                if filters.get('account_type'):
                    mock_accounts = [
                        acc for acc in mock_accounts 
                        if acc['account_type'] == filters['account_type']
                    ]
                
                # Filter by status
                if filters.get('is_active') is not None:
                    is_active = filters['is_active'].lower() == 'true'
                    mock_accounts = [
                        acc for acc in mock_accounts 
                        if acc['is_active'] == is_active
                    ]
            
            # Apply pagination
            start_idx = (page - 1) * limit
            end_idx = start_idx + limit
            paginated_accounts = mock_accounts[start_idx:end_idx]
            
            return jsonify({
                "success": True,
                "data": paginated_accounts,
                "pagination": {
                    "page": page,
                    "limit": limit,
                    "total": len(mock_accounts),
                    "pages": (len(mock_accounts) + limit - 1) // limit
                }
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
            # Mock implementation - replace with actual database operations
            new_account = {
                "id": "new_account_id",
                "email": data.get('email'),
                "account_name": data.get('account_name'),
                "account_type": data.get('account_type', 'standard'),
                "is_active": True,
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": new_account,
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
