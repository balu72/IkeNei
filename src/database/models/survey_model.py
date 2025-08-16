"""
Survey Model for MongoDB
Handles 360-degree feedback surveys
"""

from datetime import datetime
from bson import ObjectId
from database.base_model import BaseModel
from utils.logger import get_logger

logger = get_logger(__name__)

class Survey(BaseModel):
    """Survey model for 360-degree feedback surveys"""
    
    collection_name = 'surveys'
    
    required_fields = ['account_id', 'title', 'survey_type']
    
    def __init__(self, **kwargs):
        """Initialize Survey with default values"""
        # Set default values
        if 'status' not in kwargs:
            kwargs['status'] = 'draft'
        
        if 'response_count' not in kwargs:
            kwargs['response_count'] = 0
        
        if 'completion_rate' not in kwargs:
            kwargs['completion_rate'] = 0.0
        
        super().__init__(**kwargs)
    
    @classmethod
    def create_survey(cls, account_id, title, survey_type, description=None, due_date=None, questions=None, **kwargs):
        """Create a new survey"""
        # Validate account_id is ObjectId
        if isinstance(account_id, str):
            try:
                account_id = ObjectId(account_id)
            except Exception:
                raise ValueError("Invalid account_id format")
        
        # Validate questions if provided
        if questions is not None:
            validated_questions = cls._validate_questions(questions)
        else:
            validated_questions = []
        
        # Create survey data
        survey_data = {
            'account_id': account_id,
            'title': title.strip(),
            'survey_type': survey_type,
            'description': description.strip() if description else None,
            'questions': validated_questions,
            **kwargs
        }
        
        # Only include due_date if it's provided
        if due_date is not None:
            survey_data['due_date'] = due_date
        
        survey = cls(**survey_data)
        survey.save()
        
        logger.info(f"Created new survey: {title} for account {account_id} with {len(validated_questions)} questions")
        return survey
    
    @staticmethod
    def _validate_questions(questions):
        """Validate survey questions format"""
        if not isinstance(questions, list):
            raise ValueError("Questions must be a list")
        
        validated_questions = []
        
        for i, question in enumerate(questions):
            if not isinstance(question, dict):
                raise ValueError(f"Question {i+1} must be a dictionary")
            
            # Required fields
            if 'text' not in question or not question['text'].strip():
                raise ValueError(f"Question {i+1} must have non-empty text")
            
            # Set default values
            question_data = {
                'id': question.get('id', f'q{i+1}'),
                'text': question['text'].strip(),
                'type': question.get('type', 'rating_1_5'),
                'required': question.get('required', True)
            }
            
            # Validate question type
            valid_types = ['rating_1_5', 'multiple_choice', 'text']
            if question_data['type'] not in valid_types:
                raise ValueError(f"Question {i+1} has invalid type. Must be one of: {valid_types}")
            
            validated_questions.append(question_data)
        
        return validated_questions
    
    @classmethod
    def find_by_account(cls, account_id, active_only=True):
        """Find surveys by account ID"""
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
    def find_by_status(cls, status, account_id=None):
        """Find surveys by status"""
        query = {'status': status}
        
        if account_id:
            if isinstance(account_id, str):
                try:
                    account_id = ObjectId(account_id)
                except Exception:
                    raise ValueError("Invalid account_id format")
            query['account_id'] = account_id
        
        return cls.find_many(query, sort=[('created_at', -1)])
    
    @classmethod
    def find_by_type(cls, survey_type, account_id=None):
        """Find surveys by type"""
        query = {'survey_type': survey_type}
        
        if account_id:
            if isinstance(account_id, str):
                try:
                    account_id = ObjectId(account_id)
                except Exception:
                    raise ValueError("Invalid account_id format")
            query['account_id'] = account_id
        
        return cls.find_many(query, sort=[('created_at', -1)])
    
    @classmethod
    def search_surveys(cls, search_term, account_id=None, active_only=True):
        """Search surveys by title or description"""
        query = {
            '$or': [
                {'title': {'$regex': search_term, '$options': 'i'}},
                {'description': {'$regex': search_term, '$options': 'i'}},
                {'survey_type': {'$regex': search_term, '$options': 'i'}}
            ]
        }
        
        if account_id:
            if isinstance(account_id, str):
                try:
                    account_id = ObjectId(account_id)
                except Exception:
                    raise ValueError("Invalid account_id format")
            query['account_id'] = account_id
        
        if active_only:
            query['is_active'] = True
        
        return cls.find_many(query, sort=[('title', 1)])
    
    def update_status(self, status):
        """Update survey status"""
        logger.info(f"Updating survey {self._id} status to: {status}")
        valid_statuses = ['draft', 'pending_approval', 'approved', 'rejected', 'active', 'paused', 'completed', 'archived', 'inactive']
        if status not in valid_statuses:
            logger.error(f"Invalid status '{status}' for survey {self._id}. Valid statuses: {valid_statuses}")
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        logger.info(f"Status '{status}' is valid, updating survey {self._id}")
        self.set_field('status', status)
        try:
            result = self.save()
            logger.info(f"Successfully updated survey {self._id} status to: {status}")
            return result
        except Exception as e:
            logger.error(f"Failed to save survey {self._id} with status {status}: {str(e)}")
            raise
    
    def activate(self):
        """Activate survey"""
        self.set_field('status', 'active')
        self.set_field('is_active', True)
        return self.save()
    
    def pause(self):
        """Pause survey"""
        self.set_field('status', 'paused')
        return self.save()
    
    def complete(self):
        """Complete survey"""
        self.set_field('status', 'completed')
        return self.save()
    
    def archive(self):
        """Archive survey"""
        self.set_field('status', 'archived')
        return self.save()
    
    def approve(self, approver_id):
        """Approve survey"""
        self.set_field('status', 'approved')
        self.set_field('approved_by', ObjectId(approver_id) if isinstance(approver_id, str) else approver_id)
        self.set_field('approved_at', datetime.utcnow())
        return self.save()
    
    def reject(self, approver_id, reason=None):
        """Reject survey"""
        self.set_field('status', 'rejected')
        self.set_field('approved_by', ObjectId(approver_id) if isinstance(approver_id, str) else approver_id)
        self.set_field('approved_at', datetime.utcnow())
        if reason:
            self.set_field('rejection_reason', reason)
        return self.save()
    
    def submit_for_approval(self, creator_role='domain_admin'):
        """Submit survey for approval"""
        self.set_field('status', 'pending_approval')
        self.set_field('created_by_role', creator_role)
        return self.save()
    
    def update_response_count(self, count):
        """Update response count"""
        self.set_field('response_count', count)
        return self.save()
    
    def increment_response_count(self):
        """Increment response count by 1"""
        current_count = self.get_field('response_count', 0)
        self.set_field('response_count', current_count + 1)
        return self.save()
    
    def update_completion_rate(self, rate):
        """Update completion rate"""
        if not 0 <= rate <= 100:
            raise ValueError("Completion rate must be between 0 and 100")
        
        self.set_field('completion_rate', rate)
        return self.save()
    
    @classmethod
    def get_survey_statistics(cls, account_id=None):
        """Get survey statistics"""
        collection = cls.get_collection()
        
        match_stage = {}
        if account_id:
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
                    'avg_responses': {'$avg': '$response_count'},
                    'avg_completion': {'$avg': '$completion_rate'},
                    'survey_types': {'$addToSet': '$survey_type'}
                }
            }
        ])
        
        stats = list(collection.aggregate(pipeline))
        
        # Calculate totals
        total_surveys = sum(stat['total'] for stat in stats)
        active_surveys = sum(stat['total'] for stat in stats if stat['_id'] == 'active')
        
        # Get unique survey types
        all_types = set()
        for stat in stats:
            if stat.get('survey_types'):
                all_types.update(survey_type for survey_type in stat['survey_types'] if survey_type)
        
        return {
            'by_status': stats,
            'totals': {
                'total_surveys': total_surveys,
                'active_surveys': active_surveys,
                'draft_surveys': sum(stat['total'] for stat in stats if stat['_id'] == 'draft'),
                'completed_surveys': sum(stat['total'] for stat in stats if stat['_id'] == 'completed'),
                'survey_types_count': len(all_types),
                'survey_types': list(all_types)
            }
        }
    
    @classmethod
    def get_due_surveys(cls, account_id=None):
        """Get surveys that are due or overdue"""
        query = {
            'due_date': {'$lte': datetime.utcnow()},
            'status': {'$in': ['active', 'draft']},
            'is_active': True
        }
        
        if account_id:
            if isinstance(account_id, str):
                try:
                    account_id = ObjectId(account_id)
                except Exception:
                    raise ValueError("Invalid account_id format")
            query['account_id'] = account_id
        
        return cls.find_many(query, sort=[('due_date', 1)])
    
    def to_dict(self, include_id=True):
        """Convert to dictionary"""
        result = super().to_dict(include_id=include_id)
        
        # Convert ObjectId account_id to string
        if 'account_id' in result and isinstance(result['account_id'], ObjectId):
            result['account_id'] = str(result['account_id'])
        
        # Convert due_date to ISO string if present
        if 'due_date' in result and result['due_date']:
            if isinstance(result['due_date'], datetime):
                result['due_date'] = result['due_date'].isoformat() + 'Z'
        
        return result
    
    def to_public_dict(self):
        """Convert to public dictionary (safe for API responses)"""
        return {
            'id': str(self._id) if self._id else None,
            'account_id': str(self.get_field('account_id')) if self.get_field('account_id') else None,
            'title': self.get_field('title'),
            'description': self.get_field('description'),
            'survey_type': self.get_field('survey_type'),
            'status': self.get_field('status'),
            'due_date': self.get_field('due_date').isoformat() + 'Z' if self.get_field('due_date') else None,
            'questions': self.get_field('questions', []),
            'traits': self.get_field('traits', []),
            'target_sector': self.get_field('target_sector'),
            'response_count': self.get_field('response_count', 0),
            'completion_rate': self.get_field('completion_rate', 0.0),
            'is_active': self.get_field('is_active'),
            'approved_by': str(self.get_field('approved_by')) if self.get_field('approved_by') else None,
            'approved_at': self.get_field('approved_at').isoformat() + 'Z' if self.get_field('approved_at') else None,
            'rejection_reason': self.get_field('rejection_reason'),
            'created_by_role': self.get_field('created_by_role'),
            'created_at': self.get_field('created_at').isoformat() + 'Z' if self.get_field('created_at') else None,
            'updated_at': self.get_field('updated_at').isoformat() + 'Z' if self.get_field('updated_at') else None
        }
    
    def __str__(self):
        """String representation"""
        return f"Survey({self.get_field('title')})"
    
    def __repr__(self):
        """Detailed string representation"""
        return f"Survey(id={self._id}, title={self.get_field('title')}, account_id={self.get_field('account_id')})"
