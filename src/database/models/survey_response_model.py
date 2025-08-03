"""
Survey Response Model for MongoDB
Handles individual survey responses from respondents
"""

from datetime import datetime
from bson import ObjectId
from database.base_model import BaseModel
from utils.logger import get_logger

logger = get_logger(__name__)

class SurveyResponse(BaseModel):
    """Survey Response model for managing individual survey responses"""
    
    collection_name = 'survey_responses'
    
    required_fields = ['survey_run_id', 'survey_id', 'respondent_id', 'response_token', 'responses']
    
    def __init__(self, **kwargs):
        """Initialize SurveyResponse with default values"""
        # Set default values
        if 'status' not in kwargs:
            kwargs['status'] = 'completed'
        
        if 'submitted_at' not in kwargs:
            kwargs['submitted_at'] = datetime.utcnow()
        
        super().__init__(**kwargs)
    
    @classmethod
    def create_response(cls, survey_run_id, survey_id, respondent_id, response_token, responses, **kwargs):
        """Create a new survey response"""
        # Validate IDs are ObjectId
        if isinstance(survey_run_id, str):
            try:
                survey_run_id = ObjectId(survey_run_id)
            except Exception:
                raise ValueError("Invalid survey_run_id format")
        
        if isinstance(survey_id, str):
            try:
                survey_id = ObjectId(survey_id)
            except Exception:
                raise ValueError("Invalid survey_id format")
        
        if isinstance(respondent_id, str):
            try:
                respondent_id = ObjectId(respondent_id)
            except Exception:
                raise ValueError("Invalid respondent_id format")
        
        # Validate response token
        if not response_token or not isinstance(response_token, str):
            raise ValueError("Valid response_token is required")
        
        # Validate responses data
        if not responses or not isinstance(responses, dict):
            raise ValueError("Responses must be a non-empty dictionary")
        
        # Validate response format (1-5 ratings)
        for question_id, rating in responses.items():
            if not isinstance(rating, int) or rating < 1 or rating > 5:
                raise ValueError(f"Invalid rating for question {question_id}: must be integer 1-5, got {rating}")
        
        # Create survey response data
        response_data = {
            'survey_run_id': survey_run_id,
            'survey_id': survey_id,
            'respondent_id': respondent_id,
            'response_token': response_token,
            'responses': responses,
            **kwargs
        }
        
        survey_response = cls(**response_data)
        survey_response.save()
        
        logger.info(f"Created new survey response: {survey_response._id} for survey run {survey_run_id}, respondent {respondent_id}")
        return survey_response
    
    @classmethod
    def find_by_token(cls, response_token):
        """Find survey response by response token"""
        if not response_token:
            raise ValueError("Response token is required")
        
        query = {'response_token': response_token}
        return cls.find_one(query)
    
    @classmethod
    def find_by_survey_run(cls, survey_run_id):
        """Find all responses for a survey run"""
        if isinstance(survey_run_id, str):
            try:
                survey_run_id = ObjectId(survey_run_id)
            except Exception:
                raise ValueError("Invalid survey_run_id format")
        
        query = {'survey_run_id': survey_run_id}
        return cls.find_many(query, sort=[('submitted_at', -1)])
    
    @classmethod
    def find_by_survey(cls, survey_id):
        """Find all responses for a survey"""
        if isinstance(survey_id, str):
            try:
                survey_id = ObjectId(survey_id)
            except Exception:
                raise ValueError("Invalid survey_id format")
        
        query = {'survey_id': survey_id}
        return cls.find_many(query, sort=[('submitted_at', -1)])
    
    @classmethod
    def find_by_respondent(cls, respondent_id):
        """Find all responses by a respondent"""
        if isinstance(respondent_id, str):
            try:
                respondent_id = ObjectId(respondent_id)
            except Exception:
                raise ValueError("Invalid respondent_id format")
        
        query = {'respondent_id': respondent_id}
        return cls.find_many(query, sort=[('submitted_at', -1)])
    
    @classmethod
    def get_response_statistics(cls, survey_run_id=None, survey_id=None):
        """Get response statistics"""
        try:
            collection = cls.get_collection()
            
            match_stage = {}
            if survey_run_id:
                if isinstance(survey_run_id, str):
                    try:
                        survey_run_id = ObjectId(survey_run_id)
                    except Exception:
                        raise ValueError("Invalid survey_run_id format")
                match_stage['survey_run_id'] = survey_run_id
            
            if survey_id:
                if isinstance(survey_id, str):
                    try:
                        survey_id = ObjectId(survey_id)
                    except Exception:
                        raise ValueError("Invalid survey_id format")
                match_stage['survey_id'] = survey_id
            
            pipeline = []
            if match_stage:
                pipeline.append({'$match': match_stage})
            
            # Calculate average ratings per question
            pipeline.extend([
                {'$unwind': {'path': '$responses', 'preserveNullAndEmptyArrays': True}},
                {
                    '$group': {
                        '_id': '$responses.k',  # Question ID
                        'avg_rating': {'$avg': '$responses.v'},
                        'total_responses': {'$sum': 1},
                        'ratings': {'$push': '$responses.v'}
                    }
                },
                {
                    '$project': {
                        'question_id': '$_id',
                        'average_rating': {'$round': ['$avg_rating', 2]},
                        'total_responses': 1,
                        'ratings_distribution': {
                            '1': {'$size': {'$filter': {'input': '$ratings', 'cond': {'$eq': ['$$this', 1]}}}},
                            '2': {'$size': {'$filter': {'input': '$ratings', 'cond': {'$eq': ['$$this', 2]}}}},
                            '3': {'$size': {'$filter': {'input': '$ratings', 'cond': {'$eq': ['$$this', 3]}}}},
                            '4': {'$size': {'$filter': {'input': '$ratings', 'cond': {'$eq': ['$$this', 4]}}}},
                            '5': {'$size': {'$filter': {'input': '$ratings', 'cond': {'$eq': ['$$this', 5]}}}}
                        }
                    }
                }
            ])
            
            stats = list(collection.aggregate(pipeline))
            
            return {
                'question_statistics': stats,
                'total_questions': len(stats),
                'overall_average': round(sum(s['average_rating'] for s in stats) / len(stats), 2) if stats else 0
            }
            
        except Exception as e:
            logger.error(f"Failed to get response statistics: {str(e)}")
            raise
    
    def get_response_summary(self):
        """Get summary of this response"""
        responses = self.get_field('responses', {})
        
        if not responses:
            return {
                'total_questions': 0,
                'average_rating': 0,
                'response_count': 0
            }
        
        ratings = list(responses.values())
        
        return {
            'total_questions': len(responses),
            'average_rating': round(sum(ratings) / len(ratings), 2) if ratings else 0,
            'response_count': len(ratings),
            'highest_rating': max(ratings) if ratings else 0,
            'lowest_rating': min(ratings) if ratings else 0
        }
    
    def validate_responses(self, question_ids):
        """Validate that all required questions are answered"""
        responses = self.get_field('responses', {})
        
        missing_questions = []
        invalid_ratings = []
        
        for question_id in question_ids:
            if question_id not in responses:
                missing_questions.append(question_id)
            else:
                rating = responses[question_id]
                if not isinstance(rating, int) or rating < 1 or rating > 5:
                    invalid_ratings.append(f"Question {question_id}: invalid rating {rating}")
        
        errors = []
        if missing_questions:
            errors.append(f"Missing responses for questions: {', '.join(missing_questions)}")
        if invalid_ratings:
            errors.extend(invalid_ratings)
        
        return errors
    
    def to_dict(self, include_id=True):
        """Convert to dictionary"""
        result = super().to_dict(include_id=include_id)
        
        # Convert ObjectId fields to strings
        for field in ['survey_run_id', 'survey_id', 'respondent_id']:
            if field in result and isinstance(result[field], ObjectId):
                result[field] = str(result[field])
        
        # Convert dates to ISO strings
        if 'submitted_at' in result and result['submitted_at']:
            if isinstance(result['submitted_at'], datetime):
                result['submitted_at'] = result['submitted_at'].isoformat() + 'Z'
        
        return result
    
    def to_public_dict(self):
        """Convert to public dictionary (safe for API responses)"""
        return {
            'id': str(self._id) if self._id else None,
            'survey_run_id': str(self.get_field('survey_run_id')) if self.get_field('survey_run_id') else None,
            'survey_id': str(self.get_field('survey_id')) if self.get_field('survey_id') else None,
            'respondent_id': str(self.get_field('respondent_id')) if self.get_field('respondent_id') else None,
            'responses': self.get_field('responses', {}),
            'submitted_at': self.get_field('submitted_at').isoformat() + 'Z' if self.get_field('submitted_at') else None,
            'status': self.get_field('status'),
            'response_summary': self.get_response_summary(),
            'created_at': self.get_field('created_at').isoformat() + 'Z' if self.get_field('created_at') else None,
            'updated_at': self.get_field('updated_at').isoformat() + 'Z' if self.get_field('updated_at') else None
        }
    
    def to_anonymous_dict(self):
        """Convert to anonymous dictionary (no respondent identification)"""
        return {
            'id': str(self._id) if self._id else None,
            'responses': self.get_field('responses', {}),
            'submitted_at': self.get_field('submitted_at').isoformat() + 'Z' if self.get_field('submitted_at') else None,
            'response_summary': self.get_response_summary()
        }
    
    def __str__(self):
        """String representation"""
        return f"SurveyResponse({self.get_field('survey_run_id')}, {self.get_field('respondent_id')})"
    
    def __repr__(self):
        """Detailed string representation"""
        return f"SurveyResponse(id={self._id}, survey_run_id={self.get_field('survey_run_id')}, respondent_id={self.get_field('respondent_id')}, status={self.get_field('status')})"
