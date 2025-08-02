from flask import jsonify
from datetime import datetime, timedelta
from database import SurveyRepository
from utils.logger import get_logger, log_function_call

class SurveysController:
    """
    Controller for survey management
    """
    
    @staticmethod
    @log_function_call
    def get_all_surveys(page=1, limit=20, filters=None):
        """
        Get all surveys with pagination and filtering
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving surveys - page: {page}, limit: {limit}, filters: {filters}")
        
        try:
            result = SurveyRepository.get_all_surveys(
                page=page,
                per_page=limit,
                filters=filters
            )
            
            return jsonify({
                "success": True,
                "data": result['surveys'],
                "pagination": result['pagination']
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve surveys: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def create_survey(data):
        """
        Create a new survey
        """
        logger = get_logger(__name__)
        logger.info(f"Creating new survey with data: {data}")
        
        try:
            # Validate required fields
            required_fields = ['title', 'account_id', 'survey_type']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        "success": False,
                        "error": {"message": f"Missing required field: {field}"}
                    }), 400
            
            # Parse due_date if provided
            due_date = None
            if data.get('due_date'):
                try:
                    due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
                except ValueError:
                    return jsonify({
                        "success": False,
                        "error": {"message": "Invalid due_date format. Use ISO format."}
                    }), 400
            
            # Create survey using repository
            survey = SurveyRepository.create_survey(
                account_id=data.get('account_id'),
                title=data.get('title'),
                survey_type=data.get('survey_type'),
                description=data.get('description'),
                due_date=due_date
            )
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict(),
                "message": "Survey created successfully"
            }), 201
            
        except Exception as e:
            logger.error(f"Failed to create survey: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_survey_by_id(survey_id):
        """
        Get survey by ID
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving survey by ID: {survey_id}")
        
        try:
            survey = SurveyRepository.get_survey_by_id(survey_id)
            
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict()
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_survey(survey_id, data):
        """
        Update survey
        """
        logger = get_logger(__name__)
        logger.info(f"Updating survey {survey_id} with data: {data}")
        
        try:
            survey = SurveyRepository.update_survey(survey_id, data)
            
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict(),
                "message": "Survey updated successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to update survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def delete_survey(survey_id):
        """
        Delete survey
        """
        logger = get_logger(__name__)
        logger.info(f"Deleting survey: {survey_id}")
        
        try:
            success = SurveyRepository.delete_survey(survey_id)
            
            if not success:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "message": f"Survey {survey_id} deleted successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to delete survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_survey_status(survey_id, status):
        """
        Update survey status
        """
        logger = get_logger(__name__)
        logger.info(f"Updating survey {survey_id} status to: {status}")
        
        try:
            survey = SurveyRepository.update_survey_status(survey_id, status)
            
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict(),
                "message": f"Survey status updated to {status}"
            })
            
        except Exception as e:
            logger.error(f"Failed to update survey status {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update survey status: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_available_surveys():
        """
        Get surveys available to current user
        """
        try:
            mock_surveys = [
                {
                    "id": "1",
                    "title": "Leadership Assessment",
                    "description": "Please provide feedback on leadership skills",
                    "status": "active",
                    "due_date": "2024-02-15T00:00:00Z",
                    "estimated_time": "15 minutes"
                },
                {
                    "id": "2",
                    "title": "Team Collaboration Survey",
                    "description": "Evaluate team collaboration effectiveness",
                    "status": "active",
                    "due_date": "2024-02-20T00:00:00Z",
                    "estimated_time": "10 minutes"
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_surveys
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve available surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_my_surveys():
        """
        Get surveys created by current user
        """
        try:
            mock_surveys = [
                {
                    "id": "1",
                    "title": "My Leadership 360",
                    "status": "active",
                    "responses_count": 8,
                    "total_respondents": 12,
                    "completion_rate": 66.7,
                    "created_at": "2024-01-15T00:00:00Z"
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_surveys
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve my surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    def submit_survey_responses(survey_id, responses):
        """
        Submit survey responses
        """
        try:
            submission = {
                "survey_id": str(survey_id),
                "responses": responses,
                "submitted_at": datetime.utcnow().isoformat() + "Z",
                "submission_id": "submission_123"
            }
            
            return jsonify({
                "success": True,
                "data": submission,
                "message": "Survey responses submitted successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to submit survey responses: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_survey_responses(survey_id):
        """
        Get survey responses
        """
        try:
            mock_responses = [
                {
                    "id": "response_1",
                    "respondent_id": "resp_1",
                    "respondent_name": "Anonymous",
                    "submitted_at": "2024-01-20T10:30:00Z",
                    "responses": {
                        "q1": 4,
                        "q2": "Great communication skills"
                    }
                },
                {
                    "id": "response_2",
                    "respondent_id": "resp_2",
                    "respondent_name": "Anonymous",
                    "submitted_at": "2024-01-21T14:15:00Z",
                    "responses": {
                        "q1": 5,
                        "q2": "Excellent leadership qualities"
                    }
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_responses
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve survey responses: {str(e)}"}
            }), 500
    
    @staticmethod
    def run_survey(survey_id, data):
        """
        Run/launch survey
        """
        try:
            result = {
                "survey_id": str(survey_id),
                "status": "launched",
                "launched_at": datetime.utcnow().isoformat() + "Z",
                "notifications_sent": data.get('send_notifications', True),
                "recipients_count": 25
            }
            
            return jsonify({
                "success": True,
                "data": result,
                "message": "Survey launched successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to run survey: {str(e)}"}
            }), 500
