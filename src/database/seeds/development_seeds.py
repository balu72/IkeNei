"""
Development Seed Data for IkeNei Application
Creates sample data for development and testing
"""

from database import AccountRepository
from utils.logger import get_logger

logger = get_logger(__name__)

def seed_accounts():
    """Create sample accounts for development"""
    accounts_data = [
        {
            'email': 'account1@example.com',
            'password': 'password123',
            'account_name': 'Demo Account 1',
            'account_type': 'account'
        },
        {
            'email': 'domainadmin@example.com',
            'password': 'password123',
            'account_name': 'Domain Admin',
            'account_type': 'domain_admin'
        },
        {
            'email': 'sysadmin@example.com',
            'password': 'password123',
            'account_name': 'System Admin',
            'account_type': 'system_admin'
        },
        {
            'email': 'test@example.com',
            'password': 'password',
            'account_name': 'Test Account',
            'account_type': 'account'
        }
    ]
    
    created_accounts = []
    
    for account_data in accounts_data:
        try:
            # Check if account already exists
            existing_account = AccountRepository.get_account_by_email(account_data['email'])
            if existing_account:
                logger.info(f"Account already exists: {account_data['email']}")
                created_accounts.append(existing_account)
                continue
            
            # Create new account
            account = AccountRepository.create_account(**account_data)
            created_accounts.append(account)
            logger.info(f"Created account: {account_data['email']}")
            
        except Exception as e:
            logger.error(f"Failed to create account {account_data['email']}: {str(e)}")
    
    return created_accounts

def run_development_seeds():
    """Run all development seeds"""
    logger.info("Starting development data seeding...")
    
    try:
        # Seed accounts
        accounts = seed_accounts()
        logger.info(f"Seeded {len(accounts)} accounts")
        
        logger.info("Development data seeding completed successfully!")
        
        return {
            'accounts': len(accounts),
            'success': True
        }
        
    except Exception as e:
        logger.error(f"Development seeding failed: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }

if __name__ == '__main__':
    # Run seeds directly
    result = run_development_seeds()
    if result['success']:
        print("✅ Development seeds completed successfully!")
        print(f"Created {result['accounts']} accounts")
    else:
        print(f"❌ Seeding failed: {result['error']}")
