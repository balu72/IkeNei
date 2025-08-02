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
    @log_function_call
    def get_account_by_id(account_id):
        """
        Get account by ID
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving account by ID: {account_id}")
        
        try:
            account = AccountRepository.get_account_by_id(account_id)
            
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
            logger.error(f"Failed to retrieve account {account_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve account: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_account(account_id, data):
        """
        Update account information
        """
        logger = get_logger(__name__)
        logger.info(f"Updating account {account_id} with data: {data}")
        
        try:
            account = AccountRepository.update_account(account_id, data)
            
            if not account:
                return jsonify({
                    "success": False,
                    "error": {"message": "Account not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": account.to_public_dict(),
                "message": "Account updated successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to update account {account_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update account: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_account_status(account_id, is_active):
        """
        Update account active status
        """
        logger = get_logger(__name__)
        logger.info(f"Updating account {account_id} status to: {is_active}")
        
        try:
            account = AccountRepository.update_account_status(account_id, is_active)
            
            if not account:
                return jsonify({
                    "success": False,
                    "error": {"message": "Account not found"}
                }), 404
            
            status_text = "activated" if is_active else "deactivated"
            
            return jsonify({
                "success": True,
                "data": account.to_public_dict(),
                "message": f"Account {status_text} successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to update account status {account_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update account status: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def delete_account(account_id):
        """
        Delete account
        """
        logger = get_logger(__name__)
        logger.info(f"Deleting account: {account_id}")
        
        try:
            success = AccountRepository.delete_account(account_id)
            
            if not success:
                return jsonify({
                    "success": False,
                    "error": {"message": "Account not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "message": f"Account {account_id} deleted successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to delete account {account_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete account: {str(e)}"}
            }), 500
