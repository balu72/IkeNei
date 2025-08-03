"""
Survey Response Repository
Handles database operations for Survey Response model
"""

from database.models.survey_response_model import SurveyResponse
from utils.logger import get_logger

logger = get_logger(__name__)

class SurveyResponseRepository:
    """Repository for Survey Response database operations"""
    
    @staticmethod
    def create_response(survey_run_id, survey_id, respondent_id, response_token, responses, **kwargs):
        """Create a new survey response"""
        try:
            return SurveyResponse.create_response(
                survey_run_id=survey_run_id,
                survey_id=survey_id,
                respondent_id=respondent_id,
                response_token=response_token,
                responses=responses,
                **kwargs
            )
        except Exception as e:
            logger.error(f"Failed to create survey response: {str(e)}")
            raise
    
    @staticmethod
    def get_response_by_id(response_id):
        """Get survey response by ID"""
        try:
            return SurveyResponse.find_by_id(response_id)
        except Exception as e:
            logger.error(f"Failed to get survey response by ID {response_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_response_by_token(response_token):
        """Get survey response by response token"""
        try:
            return SurveyResponse.find_by_token(response_token)
        except Exception as e:
            logger.error(f"Failed to get survey response by token: {str(e)}")
            raise
    
    @staticmethod
    def get_responses_by_survey_run(survey_run_id):
        """Get all responses for a survey run"""
        try:
            return SurveyResponse.find_by_survey_run(survey_run_id)
        except Exception as e:
            logger.error(f"Failed to get responses for survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_responses_by_survey(survey_id):
        """Get all responses for a survey"""
        try:
            return SurveyResponse.find_by_survey(survey_id)
        except Exception as e:
            logger.error(f"Failed to get responses for survey {survey_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_responses_by_respondent(respondent_id):
        """Get all responses by a respondent"""
        try:
            return SurveyResponse.find_by_respondent(respondent_id)
        except Exception as e:
            logger.error(f"Failed to get responses for respondent {respondent_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_response_statistics(survey_run_id=None, survey_id=None):
        """Get response statistics"""
        try:
            return SurveyResponse.get_response_statistics(
                survey_run_id=survey_run_id,
                survey_id=survey_id
            )
        except Exception as e:
            logger.error(f"Failed to get response statistics: {str(e)}")
            raise
    
    @staticmethod
    def check_token_exists(response_token):
        """Check if a response with this token already exists"""
        try:
            response = SurveyResponse.find_by_token(response_token)
            return response is not None
        except Exception as e:
            logger.error(f"Failed to check token existence: {str(e)}")
            raise
    
    @staticmethod
    def get_all_responses(page=1, per_page=20, filters=None):
        """Get all survey responses with pagination and filtering"""
        try:
            query = {}
            
            # Apply filters
            if filters:
                if filters.get('survey_run_id'):
                    query['survey_run_id'] = filters['survey_run_id']
                
                if filters.get('survey_id'):
                    query['survey_id'] = filters['survey_id']
                
                if filters.get('respondent_id'):
                    query['respondent_id'] = filters['respondent_id']
                
                if filters.get('status'):
                    query['status'] = filters['status']
                
                # Date range filters
                if filters.get('submitted_from') or filters.get('submitted_to'):
                    date_query = {}
                    if filters.get('submitted_from'):
                        date_query['$gte'] = filters['submitted_from']
                    if filters.get('submitted_to'):
                        date_query['$lte'] = filters['submitted_to']
                    query['submitted_at'] = date_query
            
            # Get paginated results
            result = SurveyResponse.paginate(
                query=query,
                page=page,
                per_page=per_page,
                sort=[('submitted_at', -1)]
            )
            
            # Convert responses to dictionaries
            responses_data = [response.to_public_dict() for response in result['documents']]
            
            return {
                'responses': responses_data,
                'pagination': result['pagination']
            }
            
        except Exception as e:
            logger.error(f"Failed to get survey responses: {str(e)}")
            raise
    
    @staticmethod
    def update_response(response_id, update_data):
        """Update survey response information"""
        try:
            response = SurveyResponse.find_by_id(response_id)
            if not response:
                raise ValueError(f"Survey response not found: {response_id}")
            
            # Update fields
            response.update_fields(**update_data)
            response.save()
            
            return response
            
        except Exception as e:
            logger.error(f"Failed to update survey response {response_id}: {str(e)}")
            raise
    
    @staticmethod
    def delete_response(response_id):
        """Delete survey response (soft delete)"""
        try:
            response = SurveyResponse.find_by_id(response_id)
            if not response:
                raise ValueError(f"Survey response not found: {response_id}")
            
            # Soft delete
            response.soft_delete()
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete survey response {response_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_response_count_by_survey_run(survey_run_id):
        """Get count of responses for a survey run"""
        try:
            responses = SurveyResponse.find_by_survey_run(survey_run_id)
            return len(responses)
        except Exception as e:
            logger.error(f"Failed to get response count for survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_average_ratings_by_survey_run(survey_run_id):
        """Get average ratings for each question in a survey run"""
        try:
            responses = SurveyResponse.find_by_survey_run(survey_run_id)
            
            if not responses:
                return {}
            
            # Aggregate ratings by question
            question_ratings = {}
            
            for response in responses:
                response_data = response.get_field('responses', {})
                for question_id, rating in response_data.items():
                    if question_id not in question_ratings:
                        question_ratings[question_id] = []
                    question_ratings[question_id].append(rating)
            
            # Calculate averages
            averages = {}
            for question_id, ratings in question_ratings.items():
                averages[question_id] = {
                    'average_rating': round(sum(ratings) / len(ratings), 2),
                    'total_responses': len(ratings),
                    'ratings_distribution': {
                        '1': ratings.count(1),
                        '2': ratings.count(2),
                        '3': ratings.count(3),
                        '4': ratings.count(4),
                        '5': ratings.count(5)
                    }
                }
            
            return averages
            
        except Exception as e:
            logger.error(f"Failed to get average ratings for survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_completion_summary(survey_run_id):
        """Get completion summary for a survey run"""
        try:
            responses = SurveyResponse.find_by_survey_run(survey_run_id)
            
            if not responses:
                return {
                    'total_responses': 0,
                    'completion_rate': 0,
                    'average_rating': 0,
                    'response_distribution': {}
                }
            
            # Calculate summary statistics
            total_responses = len(responses)
            all_ratings = []
            
            for response in responses:
                response_data = response.get_field('responses', {})
                all_ratings.extend(response_data.values())
            
            average_rating = round(sum(all_ratings) / len(all_ratings), 2) if all_ratings else 0
            
            # Rating distribution
            rating_distribution = {
                '1': all_ratings.count(1),
                '2': all_ratings.count(2),
                '3': all_ratings.count(3),
                '4': all_ratings.count(4),
                '5': all_ratings.count(5)
            }
            
            return {
                'total_responses': total_responses,
                'total_ratings': len(all_ratings),
                'average_rating': average_rating,
                'rating_distribution': rating_distribution,
                'highest_rating': max(all_ratings) if all_ratings else 0,
                'lowest_rating': min(all_ratings) if all_ratings else 0
            }
            
        except Exception as e:
            logger.error(f"Failed to get completion summary for survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def export_responses(survey_run_id, format='json'):
        """Export responses for a survey run"""
        try:
            responses = SurveyResponse.find_by_survey_run(survey_run_id)
            
            if format == 'json':
                return [response.to_public_dict() for response in responses]
            elif format == 'anonymous':
                return [response.to_anonymous_dict() for response in responses]
            else:
                raise ValueError(f"Unsupported export format: {format}")
            
        except Exception as e:
            logger.error(f"Failed to export responses for survey run {survey_run_id}: {str(e)}")
            raise
    
    @staticmethod
    def validate_response_data(responses, required_questions):
        """Validate response data format and completeness"""
        errors = []
        
        # Check if responses is a dictionary
        if not isinstance(responses, dict):
            errors.append("Responses must be a dictionary")
            return errors
        
        # Check for missing required questions
        missing_questions = []
        for question_id in required_questions:
            if question_id not in responses:
                missing_questions.append(question_id)
        
        if missing_questions:
            errors.append(f"Missing responses for required questions: {', '.join(missing_questions)}")
        
        # Validate rating values
        for question_id, rating in responses.items():
            if not isinstance(rating, int):
                errors.append(f"Question {question_id}: rating must be an integer, got {type(rating).__name__}")
            elif rating < 1 or rating > 5:
                errors.append(f"Question {question_id}: rating must be between 1 and 5, got {rating}")
        
        return errors
