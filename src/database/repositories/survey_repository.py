"""
Survey Repository
Handles database operations for Survey model
"""

from database.models.survey_model import Survey
from utils.logger import get_logger

logger = get_logger(__name__)

class SurveyRepository:
    """Repository for Survey database operations"""
    
    @staticmethod
    def create_survey(account_id, title, survey_type, description=None, due_date=None, **kwargs):
        """Create a new survey"""
        try:
            return Survey.create_survey(
                account_id=account_id,
                title=title,
                survey_type=survey_type,
                description=description,
                due_date=due_date,
                **kwargs
            )
        except Exception as e:
            logger.error(f"Failed to create survey: {str(e)}")
            raise
    
    @staticmethod
    def get_survey_by_id(survey_id):
        """Get survey by ID"""
        try:
            return Survey.find_by_id(survey_id)
        except Exception as e:
            logger.error(f"Failed to get survey by ID {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_surveys_by_account(account_id, active_only=True):
        """Get surveys by account ID"""
        try:
            return Survey.find_by_account(account_id, active_only=active_only)
        except Exception as e:
            logger.error(f"Failed to get surveys for account {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_all_surveys(page=1, per_page=20, filters=None):
        """Get all surveys with pagination and filtering"""
        try:
            query = {}
            
            # Apply filters
            if filters:
                if filters.get('search'):
                    search_term = filters['search']
                    query['$or'] = [
                        {'title': {'$regex': search_term, '$options': 'i'}},
                        {'description': {'$regex': search_term, '$options': 'i'}},
                        {'survey_type': {'$regex': search_term, '$options': 'i'}}
                    ]
                
                if filters.get('account_id'):
                    query['account_id'] = filters['account_id']
                
                if filters.get('status'):
                    query['status'] = filters['status']
                
                if filters.get('survey_type'):
                    query['survey_type'] = filters['survey_type']
                
                if filters.get('is_active') is not None:
                    query['is_active'] = filters['is_active']
            
            # Get paginated results
            result = Survey.paginate(
                query=query,
                page=page,
                per_page=per_page,
                sort=[('created_at', -1)]
            )
            
            # Convert surveys to dictionaries
            surveys_data = [survey.to_public_dict() for survey in result['documents']]
            
            return {
                'surveys': surveys_data,
                'pagination': result['pagination']
            }
            
        except Exception as e:
            logger.error(f"Failed to get surveys: {str(e)}")
            raise
    
    @staticmethod
    def update_survey(survey_id, update_data):
        """Update survey information"""
        try:
            survey = Survey.find_by_id(survey_id)
            if not survey:
                raise ValueError(f"Survey not found: {survey_id}")
            
            # Update fields
            survey.update_fields(**update_data)
            survey.save()
            
            return survey
            
        except Exception as e:
            logger.error(f"Failed to update survey {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def update_survey_status(survey_id, status):
        """Update survey status"""
        try:
            survey = Survey.find_by_id(survey_id)
            if not survey:
                raise ValueError(f"Survey not found: {survey_id}")
            
            survey.update_status(status)
            
            return survey
            
        except Exception as e:
            logger.error(f"Failed to update survey status {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def delete_survey(survey_id):
        """Delete survey (soft delete)"""
        try:
            survey = Survey.find_by_id(survey_id)
            if not survey:
                raise ValueError(f"Survey not found: {survey_id}")
            
            # Soft delete
            survey.soft_delete()
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete survey {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def search_surveys(search_term, account_id=None, active_only=True):
        """Search surveys by title, description, or type"""
        try:
            return Survey.search_surveys(
                search_term=search_term,
                account_id=account_id,
                active_only=active_only
            )
        except Exception as e:
            logger.error(f"Failed to search surveys: {str(e)}")
            raise
    
    @staticmethod
    def get_surveys_by_status(status, account_id=None):
        """Get surveys by status"""
        try:
            return Survey.find_by_status(status=status, account_id=account_id)
        except Exception as e:
            logger.error(f"Failed to get surveys by status {status}: {str(e)}")
            raise
    
    @staticmethod
    def get_surveys_by_type(survey_type, account_id=None):
        """Get surveys by type"""
        try:
            return Survey.find_by_type(survey_type=survey_type, account_id=account_id)
        except Exception as e:
            logger.error(f"Failed to get surveys by type {survey_type}: {str(e)}")
            raise
    
    @staticmethod
    def get_survey_statistics(account_id=None):
        """Get survey statistics"""
        try:
            return Survey.get_survey_statistics(account_id=account_id)
        except Exception as e:
            logger.error(f"Failed to get survey statistics: {str(e)}")
            raise
    
    @staticmethod
    def get_due_surveys(account_id=None):
        """Get surveys that are due or overdue"""
        try:
            return Survey.get_due_surveys(account_id=account_id)
        except Exception as e:
            logger.error(f"Failed to get due surveys: {str(e)}")
            raise
    
    @staticmethod
    def activate_survey(survey_id):
        """Activate survey"""
        try:
            survey = Survey.find_by_id(survey_id)
            if not survey:
                raise ValueError(f"Survey not found: {survey_id}")
            
            survey.activate()
            return survey
            
        except Exception as e:
            logger.error(f"Failed to activate survey {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def pause_survey(survey_id):
        """Pause survey"""
        try:
            survey = Survey.find_by_id(survey_id)
            if not survey:
                raise ValueError(f"Survey not found: {survey_id}")
            
            survey.pause()
            return survey
            
        except Exception as e:
            logger.error(f"Failed to pause survey {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def complete_survey(survey_id):
        """Complete survey"""
        try:
            survey = Survey.find_by_id(survey_id)
            if not survey:
                raise ValueError(f"Survey not found: {survey_id}")
            
            survey.complete()
            return survey
            
        except Exception as e:
            logger.error(f"Failed to complete survey {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def archive_survey(survey_id):
        """Archive survey"""
        try:
            survey = Survey.find_by_id(survey_id)
            if not survey:
                raise ValueError(f"Survey not found: {survey_id}")
            
            survey.archive()
            return survey
            
        except Exception as e:
            logger.error(f"Failed to archive survey {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def increment_response_count(survey_id):
        """Increment survey's response count"""
        try:
            survey = Survey.find_by_id(survey_id)
            if not survey:
                raise ValueError(f"Survey not found: {survey_id}")
            
            survey.increment_response_count()
            return survey
            
        except Exception as e:
            logger.error(f"Failed to increment response count for survey {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def update_completion_rate(survey_id, rate):
        """Update survey's completion rate"""
        try:
            survey = Survey.find_by_id(survey_id)
            if not survey:
                raise ValueError(f"Survey not found: {survey_id}")
            
            survey.update_completion_rate(rate)
            return survey
            
        except Exception as e:
            logger.error(f"Failed to update completion rate for survey {survey_id}: {str(e)}")
            raise
