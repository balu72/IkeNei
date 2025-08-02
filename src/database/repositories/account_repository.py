"""
Account Repository
Handles database operations for Account model
"""

from database.models.account_model import Account
from utils.logger import get_logger

logger = get_logger(__name__)

class AccountRepository:
    """Repository for Account database operations"""
    
    @staticmethod
    def create_account(email, password, account_name, account_type='standard', **kwargs):
        """Create a new account"""
        try:
            return Account.create_account(
                email=email,
                password=password,
                account_name=account_name,
                account_type=account_type,
                **kwargs
            )
        except Exception as e:
            logger.error(f"Failed to create account: {str(e)}")
            raise
    
    @staticmethod
    def get_account_by_id(account_id):
        """Get account by ID"""
        try:
            return Account.find_by_id(account_id)
        except Exception as e:
            logger.error(f"Failed to get account by ID {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_account_by_email(email):
        """Get account by email"""
        try:
            return Account.find_by_email(email)
        except Exception as e:
            logger.error(f"Failed to get account by email {email}: {str(e)}")
            raise
    
    @staticmethod
    def authenticate_account(email, password):
        """Authenticate account with email and password"""
        try:
            return Account.authenticate(email, password)
        except Exception as e:
            logger.error(f"Authentication failed for {email}: {str(e)}")
            raise
    
    @staticmethod
    def get_all_accounts(page=1, per_page=20, filters=None):
        """Get all accounts with pagination and filtering"""
        try:
            query = {}
            
            # Apply filters
            if filters:
                if filters.get('search'):
                    search_term = filters['search']
                    query['$or'] = [
                        {'account_name': {'$regex': search_term, '$options': 'i'}},
                        {'email': {'$regex': search_term, '$options': 'i'}}
                    ]
                
                if filters.get('account_type'):
                    query['account_type'] = filters['account_type']
                
                if filters.get('is_active') is not None:
                    query['is_active'] = filters['is_active']
            
            # Get paginated results
            result = Account.paginate(
                query=query,
                page=page,
                per_page=per_page,
                sort=[('created_at', -1)]
            )
            
            # Convert accounts to dictionaries
            accounts_data = [account.to_public_dict() for account in result['documents']]
            
            return {
                'accounts': accounts_data,
                'pagination': result['pagination']
            }
            
        except Exception as e:
            logger.error(f"Failed to get accounts: {str(e)}")
            raise
    
    @staticmethod
    def update_account(account_id, update_data):
        """Update account information"""
        try:
            account = Account.find_by_id(account_id)
            if not account:
                raise ValueError(f"Account not found: {account_id}")
            
            # Update fields
            account.update_fields(**update_data)
            account.save()
            
            return account
            
        except Exception as e:
            logger.error(f"Failed to update account {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def update_account_status(account_id, is_active):
        """Update account active status"""
        try:
            account = Account.find_by_id(account_id)
            if not account:
                raise ValueError(f"Account not found: {account_id}")
            
            if is_active:
                account.activate()
            else:
                account.deactivate()
            
            return account
            
        except Exception as e:
            logger.error(f"Failed to update account status {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def delete_account(account_id):
        """Delete account (soft delete)"""
        try:
            account = Account.find_by_id(account_id)
            if not account:
                raise ValueError(f"Account not found: {account_id}")
            
            # Soft delete
            account.soft_delete()
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete account {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def search_accounts(search_term, account_type=None, active_only=True):
        """Search accounts by name or email"""
        try:
            return Account.search_accounts(
                search_term=search_term,
                account_type=account_type,
                active_only=active_only
            )
        except Exception as e:
            logger.error(f"Failed to search accounts: {str(e)}")
            raise
    
    @staticmethod
    def get_accounts_by_type(account_type, active_only=True):
        """Get accounts by type"""
        try:
            return Account.get_accounts_by_type(
                account_type=account_type,
                active_only=active_only
            )
        except Exception as e:
            logger.error(f"Failed to get accounts by type {account_type}: {str(e)}")
            raise
    
    @staticmethod
    def get_account_statistics():
        """Get account statistics"""
        try:
            return Account.get_account_statistics()
        except Exception as e:
            logger.error(f"Failed to get account statistics: {str(e)}")
            raise
    
    @staticmethod
    def update_password(account_id, new_password):
        """Update account password"""
        try:
            account = Account.find_by_id(account_id)
            if not account:
                raise ValueError(f"Account not found: {account_id}")
            
            account.update_password(new_password)
            return account
            
        except Exception as e:
            logger.error(f"Failed to update password for account {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def verify_email(account_id):
        """Verify account email"""
        try:
            account = Account.find_by_id(account_id)
            if not account:
                raise ValueError(f"Account not found: {account_id}")
            
            account.verify_email()
            return account
            
        except Exception as e:
            logger.error(f"Failed to verify email for account {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def update_settings(account_id, settings_update):
        """Update account settings"""
        try:
            account = Account.find_by_id(account_id)
            if not account:
                raise ValueError(f"Account not found: {account_id}")
            
            account.update_settings(settings_update)
            return account
            
        except Exception as e:
            logger.error(f"Failed to update settings for account {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def upgrade_account_type(account_id, new_type):
        """Upgrade account type"""
        try:
            account = Account.find_by_id(account_id)
            if not account:
                raise ValueError(f"Account not found: {account_id}")
            
            account.upgrade_account_type(new_type)
            return account
            
        except Exception as e:
            logger.error(f"Failed to upgrade account type for {account_id}: {str(e)}")
            raise
