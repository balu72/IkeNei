"""
Survey Run Repository
Handles database operations for Survey Run model
"""

from database.models.survey_run_model import SurveyRun
from utils.logger import get_logger

logger = get_logger(__name__)

class SurveyRunRepository:
    """Repository for Survey Run database operations"""
    
    @staticmethod
    def create_survey_run(survey_id, subject_id, respondents, due_date, launched_by, account_id, **kwargs):
        """Create a new survey run"""
        try:
            return SurveyRun.create_survey_run(
                survey_id=survey_id,
                subject_id=subject_id,
                respondents=respondents,
                due_date=due_date,
                launched_by=launched_by,
                account_id=account_id,
                **kwargs
            )
        except Exception as e:
            logger.error(f"Failed to create survey run: {str(e)}")
            raise
    
    @staticmethod
    def get_survey_run_by_id(survey_run_id):
        """Get survey run by ID"""
        try:
            return SurveyRun.find_by_id(survey_run_id)
        except Exception as e:
            logger.error(f"Failed to get survey run by ID {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def find_active_run(survey_id, subject_id):
        """Find active survey run for survey+subject combination"""
        try:
            return SurveyRun.find_active_run(survey_id, subject_id)
        except Exception as e:
            logger.error(f"Failed to find active run for survey {survey_id}, subject {subject_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_runs_by_survey(survey_id, active_only=True):
        """Get survey runs by survey ID"""
        try:
            return SurveyRun.find_by_survey(survey_id, active_only=active_only)
        except Exception as e:
            logger.error(f"Failed to get runs for survey {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_runs_by_subject(subject_id, active_only=True):
        """Get survey runs by subject ID"""
        try:
            return SurveyRun.find_by_subject(subject_id, active_only=active_only)
        except Exception as e:
            logger.error(f"Failed to get runs for subject {subject_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_runs_by_account(account_id, active_only=True):
        """Get survey runs by account ID"""
        try:
            return SurveyRun.find_by_account(account_id, active_only=active_only)
        except Exception as e:
            logger.error(f"Failed to get runs for account {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_runs_by_respondent(respondent_id, active_only=True):
        """Get survey runs where user is a respondent"""
        try:
            return SurveyRun.find_by_respondent(respondent_id, active_only=active_only)
        except Exception as e:
            logger.error(f"Failed to get runs for respondent {respondent_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_all_survey_runs(page=1, per_page=20, filters=None):
        """Get all survey runs with pagination and filtering"""
        try:
            query = {}
            
            # Apply filters
            if filters:
                if filters.get('survey_id'):
                    query['survey_id'] = filters['survey_id']
                
                if filters.get('subject_id'):
                    query['subject_id'] = filters['subject_id']
                
                if filters.get('account_id'):
                    query['account_id'] = filters['account_id']
                
                if filters.get('status'):
                    query['status'] = filters['status']
                
                if filters.get('launched_by'):
                    query['launched_by'] = filters['launched_by']
                
                if filters.get('is_active') is not None:
                    query['is_active'] = filters['is_active']
                
                # Date range filters
                if filters.get('due_date_from') or filters.get('due_date_to'):
                    date_query = {}
                    if filters.get('due_date_from'):
                        date_query['$gte'] = filters['due_date_from']
                    if filters.get('due_date_to'):
                        date_query['$lte'] = filters['due_date_to']
                    query['due_date'] = date_query
                
                if filters.get('launched_from') or filters.get('launched_to'):
                    date_query = {}
                    if filters.get('launched_from'):
                        date_query['$gte'] = filters['launched_from']
                    if filters.get('launched_to'):
                        date_query['$lte'] = filters['launched_to']
                    query['launched_at'] = date_query
            
            # Get paginated results
            result = SurveyRun.paginate(
                query=query,
                page=page,
                per_page=per_page,
                sort=[('created_at', -1)]
            )
            
            # Convert survey runs to dictionaries
            runs_data = [run.to_public_dict() for run in result['documents']]
            
            return {
                'survey_runs': runs_data,
                'pagination': result['pagination']
            }
            
        except Exception as e:
            logger.error(f"Failed to get survey runs: {str(e)}")
            raise
    
    @staticmethod
    def update_survey_run(survey_run_id, update_data):
        """Update survey run information"""
        try:
            survey_run = SurveyRun.find_by_id(survey_run_id)
            if not survey_run:
                raise ValueError(f"Survey run not found: {survey_run_id}")
            
            # Update fields
            survey_run.update_fields(**update_data)
            survey_run.save()
            
            return survey_run
            
        except Exception as e:
            logger.error(f"Failed to update survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def update_survey_run_status(survey_run_id, status):
        """Update survey run status"""
        try:
            survey_run = SurveyRun.find_by_id(survey_run_id)
            if not survey_run:
                raise ValueError(f"Survey run not found: {survey_run_id}")
            
            survey_run.update_status(status)
            
            return survey_run
            
        except Exception as e:
            logger.error(f"Failed to update survey run status {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def complete_survey_run(survey_run_id):
        """Mark survey run as completed"""
        try:
            survey_run = SurveyRun.find_by_id(survey_run_id)
            if not survey_run:
                raise ValueError(f"Survey run not found: {survey_run_id}")
            
            survey_run.complete()
            return survey_run
            
        except Exception as e:
            logger.error(f"Failed to complete survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def cancel_survey_run(survey_run_id):
        """Cancel survey run"""
        try:
            survey_run = SurveyRun.find_by_id(survey_run_id)
            if not survey_run:
                raise ValueError(f"Survey run not found: {survey_run_id}")
            
            survey_run.cancel()
            return survey_run
            
        except Exception as e:
            logger.error(f"Failed to cancel survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def expire_survey_run(survey_run_id):
        """Mark survey run as expired"""
        try:
            survey_run = SurveyRun.find_by_id(survey_run_id)
            if not survey_run:
                raise ValueError(f"Survey run not found: {survey_run_id}")
            
            survey_run.expire()
            return survey_run
            
        except Exception as e:
            logger.error(f"Failed to expire survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def update_respondent_status(survey_run_id, respondent_id, status, completed_at=None):
        """Update individual respondent status"""
        try:
            survey_run = SurveyRun.find_by_id(survey_run_id)
            if not survey_run:
                raise ValueError(f"Survey run not found: {survey_run_id}")
            
            survey_run.update_respondent_status(respondent_id, status, completed_at)
            return survey_run
            
        except Exception as e:
            logger.error(f"Failed to update respondent status in survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_respondent_by_token(response_token):
        """Get survey run and respondent data by response token"""
        try:
            # Find survey run containing this response token
            query = {'respondents.response_token': response_token}
            survey_run = SurveyRun.find_one(query)
            
            if not survey_run:
                return None, None
            
            # Get the specific respondent data
            respondent = survey_run.get_respondent_by_token(response_token)
            
            return survey_run, respondent
            
        except Exception as e:
            logger.error(f"Failed to get respondent by token: {str(e)}")
            raise
    
    @staticmethod
    def get_due_soon_runs(days_ahead=3):
        """Get survey runs due within specified days"""
        try:
            return SurveyRun.find_due_soon(days_ahead=days_ahead)
        except Exception as e:
            logger.error(f"Failed to get due soon runs: {str(e)}")
            raise
    
    @staticmethod
    def get_overdue_runs():
        """Get overdue survey runs"""
        try:
            return SurveyRun.find_overdue()
        except Exception as e:
            logger.error(f"Failed to get overdue runs: {str(e)}")
            raise
    
    @staticmethod
    def get_survey_run_statistics(account_id=None):
        """Get survey run statistics"""
        try:
            collection = SurveyRun.get_collection()
            
            match_stage = {}
            if account_id:
                from bson import ObjectId
                if isinstance(account_id, str):
                    try:
                        account_id = ObjectId(account_id)
                    except Exception:
                        raise ValueError("Invalid account_id format")
                match_stage['account_id'] = account_id
            
            pipeline = []
            if match_stage:
                pipeline.append({'$match': match_stage})
            
            pipeline.extend([
                {
                    '$group': {
                        '_id': '$status',
                        'total': {'$sum': 1},
                        'avg_completion_rate': {'$avg': '$completion_rate'},
                        'avg_response_count': {'$avg': '$response_count'},
                        'total_respondents': {'$sum': {'$size': '$respondents'}}
                    }
                }
            ])
            
            stats = list(collection.aggregate(pipeline))
            
            # Calculate totals
            total_runs = sum(stat['total'] for stat in stats)
            active_runs = sum(stat['total'] for stat in stats if stat['_id'] == 'active')
            completed_runs = sum(stat['total'] for stat in stats if stat['_id'] == 'completed')
            
            return {
                'by_status': stats,
                'totals': {
                    'total_runs': total_runs,
                    'active_runs': active_runs,
                    'completed_runs': completed_runs,
                    'cancelled_runs': sum(stat['total'] for stat in stats if stat['_id'] == 'cancelled'),
                    'expired_runs': sum(stat['total'] for stat in stats if stat['_id'] == 'expired')
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to get survey run statistics: {str(e)}")
            raise
    
    @staticmethod
    def delete_survey_run(survey_run_id):
        """Delete survey run (soft delete)"""
        try:
            survey_run = SurveyRun.find_by_id(survey_run_id)
            if not survey_run:
                raise ValueError(f"Survey run not found: {survey_run_id}")
            
            # Soft delete
            survey_run.soft_delete()
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_pending_respondents(survey_run_id):
        """Get list of respondents who haven't completed the survey"""
        try:
            survey_run = SurveyRun.find_by_id(survey_run_id)
            if not survey_run:
                raise ValueError(f"Survey run not found: {survey_run_id}")
            
            return survey_run.get_pending_respondents()
            
        except Exception as e:
            logger.error(f"Failed to get pending respondents for survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_completed_respondents(survey_run_id):
        """Get list of respondents who have completed the survey"""
        try:
            survey_run = SurveyRun.find_by_id(survey_run_id)
            if not survey_run:
                raise ValueError(f"Survey run not found: {survey_run_id}")
            
            return survey_run.get_completed_respondents()
            
        except Exception as e:
            logger.error(f"Failed to get completed respondents for survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def bulk_expire_overdue_runs():
        """Bulk expire all overdue survey runs"""
        try:
            from datetime import datetime
            
            # Find all overdue active runs
            overdue_runs = SurveyRun.find_overdue()
            
            expired_count = 0
            for run in overdue_runs:
                try:
                    run.expire()
                    expired_count += 1
                except Exception as e:
                    logger.error(f"Failed to expire survey run {run._id}: {str(e)}")
            
            logger.info(f"Bulk expired {expired_count} overdue survey runs")
            return expired_count
            
        except Exception as e:
            logger.error(f"Failed to bulk expire overdue runs: {str(e)}")
            raise
    
    @staticmethod
    def get_response_rate_by_account(account_id):
        """Get response rate statistics for an account"""
        try:
            from bson import ObjectId
            
            if isinstance(account_id, str):
                try:
                    account_id = ObjectId(account_id)
                except Exception:
                    raise ValueError("Invalid account_id format")
            
            collection = SurveyRun.get_collection()
            
            pipeline = [
                {'$match': {'account_id': account_id, 'is_active': True}},
                {
                    '$group': {
                        '_id': None,
                        'total_runs': {'$sum': 1},
                        'avg_completion_rate': {'$avg': '$completion_rate'},
                        'total_respondents': {'$sum': {'$size': '$respondents'}},
                        'total_responses': {'$sum': '$response_count'}
                    }
                }
            ]
            
            result = list(collection.aggregate(pipeline))
            
            if result:
                stats = result[0]
                return {
                    'total_runs': stats['total_runs'],
                    'average_completion_rate': round(stats['avg_completion_rate'], 2),
                    'total_respondents': stats['total_respondents'],
                    'total_responses': stats['total_responses'],
                    'overall_response_rate': round(
                        (stats['total_responses'] / stats['total_respondents'] * 100) 
                        if stats['total_respondents'] > 0 else 0, 2
                    )
                }
            else:
                return {
                    'total_runs': 0,
                    'average_completion_rate': 0,
                    'total_respondents': 0,
                    'total_responses': 0,
                    'overall_response_rate': 0
                }
            
        except Exception as e:
            logger.error(f"Failed to get response rate for account {account_id}: {str(e)}")
            raise
