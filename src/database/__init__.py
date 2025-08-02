"""
Database Package Initialization
Provides easy imports and database setup
"""

from database.connection import (
    get_db,
    get_collection,
    init_database,
    close_database,
    get_database_status,
    with_db_error_handling
)

from database.models.account_model import Account
from database.repositories.account_repository import AccountRepository

__all__ = [
    # Connection utilities
    'get_db',
    'get_collection',
    'init_database',
    'close_database',
    'get_database_status',
    'with_db_error_handling',
    
    # Models
    'Account',
    
    # Repositories
    'AccountRepository'
]
