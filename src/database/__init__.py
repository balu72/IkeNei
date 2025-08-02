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
from database.models.subject_model import Subject
from database.models.survey_model import Survey
from database.models.trait_model import Trait
from database.models.respondent_model import RespondentModel
from database.repositories.account_repository import AccountRepository
from database.repositories.subject_repository import SubjectRepository
from database.repositories.survey_repository import SurveyRepository
from database.repositories.trait_repository import TraitRepository
from database.repositories.respondent_repository import RespondentRepository

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
    'Subject',
    'Survey',
    'Trait',
    'RespondentModel',
    
    # Repositories
    'AccountRepository',
    'SubjectRepository',
    'SurveyRepository',
    'TraitRepository',
    'RespondentRepository'
]
