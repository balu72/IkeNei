"""
Survey Run Model for MongoDB
Handles survey execution with subjects and respondents
"""

from datetime import datetime
from bson import ObjectId
from database.base_model import BaseModel
from utils.logger import get_logger

logger = get_logger(__name__)

class SurveyRun(BaseModel):
    """Survey Run model for managing survey executions"""
    
    collection_name = 'survey_runs'
    
    required_fields = ['survey_id', 'subject_id', 'respondents', 'due_date', 'launched_by', 'account_id']
    
    def __init__(self, **kwargs):
        """Initialize SurveyRun with default values"""
        # Set default values
        if 'status' not in kwargs:
            kwargs['status'] = 'active'
        
        if 'response_count' not in kwargs:
            kwargs['response_count'] = 0
        
        if 'completion_rate' not in kwargs:
            kwargs['completion_rate'] = 0.0
        
        if 'total_weight' not in kwargs:
            kwargs['total_weight'] = 100
        
        if 'launched_at' not in kwargs:
            kwargs['launched_at'] = datetime.utcnow()
        
        super().__init__(**kwargs)
    
    @classmethod
    def create_survey_run(cls, survey_id, subject_id, respondents, due_date, launched_by, account_id, **kwargs):
        """Create a new survey run"""
        # Validate IDs are ObjectId
        if isinstance(survey_id, str):
            try:
                survey_id = ObjectId(survey_id)
            except Exception:
                raise ValueError("Invalid survey_id format")
        
        if isinstance(subject_id, str):
            try:
                subject_id = ObjectId(subject_id)
            except Exception:
                raise ValueError("Invalid subject_id format")
        
        if isinstance(launched_by, str):
            try:
                launched_by = ObjectId(launched_by)
            except Exception:
                raise ValueError("Invalid launched_by format")
        
        if isinstance(account_id, str):
            try:
                account_id = ObjectId(account_id)
            except Exception:
                raise ValueError("Invalid account_id format")
        
        # Validate respondents data
        if not respondents or not isinstance(respondents, list):
            raise ValueError("Respondents must be a non-empty list")
        
        # Process respondents to ensure ObjectId format
        processed_respondents = []
        total_weight = 0
        
        for respondent in respondents:
            if not isinstance(respondent, dict):
                raise ValueError("Each respondent must be a dictionary")
            
            respondent_id = respondent.get('respondent_id')
            weight = respondent.get('weight', 0)
            relationship = respondent.get('relationship', '')
            
            if isinstance(respondent_id, str):
                try:
                    respondent_id = ObjectId(respondent_id)
                except Exception:
                    raise ValueError(f"Invalid respondent_id format: {respondent_id}")
            
            if not isinstance(weight, (int, float)) or weight <= 0:
                raise ValueError(f"Invalid weight for respondent {respondent_id}: {weight}")
            
            total_weight += weight
            
            processed_respondents.append({
                'respondent_id': respondent_id,
                'weight': weight,
                'relationship': relationship,
                'status': 'pending',
                'invited_at': datetime.utcnow(),
                'completed_at': None,
                'response_token': cls._generate_response_token()
            })
        
        # Validate total weight equals 100
        if total_weight != 100:
            raise ValueError(f"Total respondent weights must equal 100, got {total_weight}")
        
        # Validate due_date
        if isinstance(due_date, str):
            try:
                due_date = datetime.fromisoformat(due_date.replace('Z', '+00:00'))
            except ValueError:
                raise ValueError("Invalid due_date format. Use ISO format.")
        
        if due_date <= datetime.utcnow():
            raise ValueError("Due date must be in the future")
        
        # Create survey run data
        survey_run_data = {
            'survey_id': survey_id,
            'subject_id': subject_id,
            'respondents': processed_respondents,
            'due_date': due_date,
            'launched_by': launched_by,
            'account_id': account_id,
            'total_weight': total_weight,
            **kwargs
        }
        
        survey_run = cls(**survey_run_data)
        survey_run.save()
        
        logger.info(f"Created new survey run: {survey_run._id} for survey {survey_id}, subject {subject_id}")
        return survey_run
    
    @staticmethod
    def _generate_response_token():
        """Generate a unique response token for respondent"""
        import secrets
        return secrets.token_urlsafe(32)
    
    @classmethod
    def find_active_run(cls, survey_id, subject_id):
        """Find active survey run for survey+subject combination"""
        if isinstance(survey_id, str):
            try:
                survey_id = ObjectId(survey_id)
            except Exception:
                raise ValueError("Invalid survey_id format")
        
        if isinstance(subject_id, str):
            try:
                subject_id = ObjectId(subject_id)
            except Exception:
                raise ValueError("Invalid subject_id format")
        
        query = {
            'survey_id': survey_id,
            'subject_id': subject_id,
            'status': {'$in': ['active', 'pending']},
            'is_active': True
        }
        
        return cls.find_one(query)
    
    @classmethod
    def find_by_survey(cls, survey_id, active_only=True):
        """Find survey runs by survey ID"""
        if isinstance(survey_id, str):
            try:
                survey_id = ObjectId(survey_id)
            except Exception:
                raise ValueError("Invalid survey_id format")
        
        query = {'survey_id': survey_id}
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('created_at', -1)])
    
    @classmethod
    def find_by_subject(cls, subject_id, active_only=True):
        """Find survey runs by subject ID"""
        if isinstance(subject_id, str):
            try:
                subject_id = ObjectId(subject_id)
            except Exception:
                raise ValueError("Invalid subject_id format")
        
        query = {'subject_id': subject_id}
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('created_at', -1)])
    
    @classmethod
    def find_by_account(cls, account_id, active_only=True):
        """Find survey runs by account ID"""
        if isinstance(account_id, str):
            try:
                account_id = ObjectId(account_id)
            except Exception:
                raise ValueError("Invalid account_id format")
        
        query = {'account_id': account_id}
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('created_at', -1)])
    
    @classmethod
    def find_by_respondent(cls, respondent_id, active_only=True):
        """Find survey runs where user is a respondent"""
        if isinstance(respondent_id, str):
            try:
                respondent_id = ObjectId(respondent_id)
            except Exception:
                raise ValueError("Invalid respondent_id format")
        
        query = {'respondents.respondent_id': respondent_id}
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('created_at', -1)])
    
    @classmethod
    def find_due_soon(cls, days_ahead=3):
        """Find survey runs due within specified days"""
        from datetime import timedelta
        
        due_date_threshold = datetime.utcnow() + timedelta(days=days_ahead)
        
        query = {
            'status': 'active',
            'due_date': {'$lte': due_date_threshold},
            'is_active': True
        }
        
        return cls.find_many(query, sort=[('due_date', 1)])
    
    @classmethod
    def find_overdue(cls):
        """Find overdue survey runs"""
        query = {
            'status': 'active',
            'due_date': {'$lt': datetime.utcnow()},
            'is_active': True
        }
        
        return cls.find_many(query, sort=[('due_date', 1)])
    
    def update_status(self, status):
        """Update survey run status"""
        valid_statuses = ['active', 'completed', 'cancelled', 'expired']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        self.set_field('status', status)
        return self.save()
    
    def complete(self):
        """Mark survey run as completed"""
        self.set_field('status', 'completed')
        self.set_field('completed_at', datetime.utcnow())
        return self.save()
    
    def cancel(self):
        """Cancel survey run"""
        self.set_field('status', 'cancelled')
        return self.save()
    
    def expire(self):
        """Mark survey run as expired"""
        self.set_field('status', 'expired')
        return self.save()
    
    def update_respondent_status(self, respondent_id, status, completed_at=None):
        """Update individual respondent status"""
        if isinstance(respondent_id, str):
            try:
                respondent_id = ObjectId(respondent_id)
            except Exception:
                raise ValueError("Invalid respondent_id format")
        
        respondents = self.get_field('respondents', [])
        updated = False
        
        for respondent in respondents:
            if respondent['respondent_id'] == respondent_id:
                respondent['status'] = status
                if completed_at:
                    respondent['completed_at'] = completed_at
                elif status == 'completed':
                    respondent['completed_at'] = datetime.utcnow()
                updated = True
                break
        
        if not updated:
            raise ValueError(f"Respondent {respondent_id} not found in survey run")
        
        self.set_field('respondents', respondents)
        self._update_completion_stats()
        return self.save()
    
    def _update_completion_stats(self):
        """Update response count and completion rate"""
        respondents = self.get_field('respondents', [])
        completed_count = sum(1 for r in respondents if r['status'] == 'completed')
        total_count = len(respondents)
        
        completion_rate = (completed_count / total_count * 100) if total_count > 0 else 0
        
        self.set_field('response_count', completed_count)
        self.set_field('completion_rate', completion_rate)
        
        # Auto-complete if all responses received
        if completed_count == total_count and self.get_field('status') == 'active':
            self.set_field('status', 'completed')
            self.set_field('completed_at', datetime.utcnow())
    
    def get_respondent_by_token(self, response_token):
        """Get respondent data by response token"""
        respondents = self.get_field('respondents', [])
        
        for respondent in respondents:
            if respondent.get('response_token') == response_token:
                return respondent
        
        return None
    
    def get_pending_respondents(self):
        """Get list of respondents who haven't completed the survey"""
        respondents = self.get_field('respondents', [])
        return [r for r in respondents if r['status'] == 'pending']
    
    def get_completed_respondents(self):
        """Get list of respondents who have completed the survey"""
        respondents = self.get_field('respondents', [])
        return [r for r in respondents if r['status'] == 'completed']
    
    def is_overdue(self):
        """Check if survey run is overdue"""
        due_date = self.get_field('due_date')
        return due_date and due_date < datetime.utcnow()
    
    def days_until_due(self):
        """Get number of days until due date"""
        due_date = self.get_field('due_date')
        if not due_date:
            return None
        
        delta = due_date - datetime.utcnow()
        return delta.days
    
    def to_dict(self, include_id=True):
        """Convert to dictionary"""
        result = super().to_dict(include_id=include_id)
        
        # Convert ObjectId fields to strings
        for field in ['survey_id', 'subject_id', 'launched_by', 'account_id']:
            if field in result and isinstance(result[field], ObjectId):
                result[field] = str(result[field])
        
        # Convert respondent ObjectIds to strings
        if 'respondents' in result:
            for respondent in result['respondents']:
                if 'respondent_id' in respondent and isinstance(respondent['respondent_id'], ObjectId):
                    respondent['respondent_id'] = str(respondent['respondent_id'])
        
        # Convert dates to ISO strings
        for date_field in ['due_date', 'launched_at', 'completed_at']:
            if date_field in result and result[date_field]:
                if isinstance(result[date_field], datetime):
                    result[date_field] = result[date_field].isoformat() + 'Z'
        
        return result
    
    def to_public_dict(self):
        """Convert to public dictionary (safe for API responses)"""
        return {
            'id': str(self._id) if self._id else None,
            'survey_id': str(self.get_field('survey_id')) if self.get_field('survey_id') else None,
            'subject_id': str(self.get_field('subject_id')) if self.get_field('subject_id') else None,
            'account_id': str(self.get_field('account_id')) if self.get_field('account_id') else None,
            'status': self.get_field('status'),
            'due_date': self.get_field('due_date').isoformat() + 'Z' if self.get_field('due_date') else None,
            'launched_at': self.get_field('launched_at').isoformat() + 'Z' if self.get_field('launched_at') else None,
            'completed_at': self.get_field('completed_at').isoformat() + 'Z' if self.get_field('completed_at') else None,
            'launched_by': str(self.get_field('launched_by')) if self.get_field('launched_by') else None,
            'respondents': [
                {
                    'respondent_id': str(r['respondent_id']) if r.get('respondent_id') else None,
                    'weight': r.get('weight'),
                    'relationship': r.get('relationship'),
                    'status': r.get('status'),
                    'invited_at': r['invited_at'].isoformat() + 'Z' if r.get('invited_at') else None,
                    'completed_at': r['completed_at'].isoformat() + 'Z' if r.get('completed_at') else None
                    # Note: response_token excluded for security
                }
                for r in self.get_field('respondents', [])
            ],
            'total_weight': self.get_field('total_weight', 100),
            'response_count': self.get_field('response_count', 0),
            'completion_rate': self.get_field('completion_rate', 0.0),
            'is_overdue': self.is_overdue(),
            'days_until_due': self.days_until_due(),
            'created_at': self.get_field('created_at').isoformat() + 'Z' if self.get_field('created_at') else None,
            'updated_at': self.get_field('updated_at').isoformat() + 'Z' if self.get_field('updated_at') else None
        }
    
    def __str__(self):
        """String representation"""
        return f"SurveyRun({self.get_field('survey_id')}, {self.get_field('subject_id')})"
    
    def __repr__(self):
        """Detailed string representation"""
        return f"SurveyRun(id={self._id}, survey_id={self.get_field('survey_id')}, subject_id={self.get_field('subject_id')}, status={self.get_field('status')})"
