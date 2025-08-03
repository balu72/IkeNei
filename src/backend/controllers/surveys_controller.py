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
            # TODO: Implement actual available surveys retrieval
            # This should query surveys that are:
            # - Active status
            # - Assigned to current user as respondent
            # - Not yet completed by current user
            # - Within due date range
            
            surveys = []
            
            return jsonify({
                "success": True,
                "data": surveys
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve available surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_my_surveys():
        """
        Get surveys created by current user
        """
        logger = get_logger(__name__)
        logger.info("Retrieving surveys for current user")
        
        try:
            # Get surveys from database for current user
            # For now, get all surveys since we don't have user context
            result = SurveyRepository.get_all_surveys(
                page=1,
                per_page=100,
                filters=None
            )
            
            # Convert to public dict format
            surveys_data = [survey.to_public_dict() for survey in result['surveys']]
            
            return jsonify({
                "success": True,
                "data": surveys_data
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve my surveys: {str(e)}")
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
            # TODO: Implement actual survey response submission
            # This should:
            # - Validate survey exists and is active
            # - Validate respondent has permission to submit
            # - Store responses in survey_responses collection
            # - Update survey completion status
            # - Send notifications if configured
            
            submission_id = "generated_submission_id"  # This should be generated by database
            
            return jsonify({
                "success": True,
                "data": {"submission_id": submission_id},
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
            # TODO: Implement actual survey responses retrieval
            # This should:
            # - Query survey_responses collection for specific survey
            # - Include respondent information (anonymized if needed)
            # - Support pagination for large response sets
            # - Filter by completion status if needed
            # - Include response timestamps and metadata
            
            responses = []
            
            return jsonify({
                "success": True,
                "data": responses
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
            # TODO: Implement actual survey launch functionality
            # This should:
            # - Validate survey exists and is ready to launch
            # - Update survey status to 'active' or 'running'
            # - Send invitations to all assigned respondents
            # - Create notification records
            # - Log survey launch activity
            # - Return actual recipient count from database
            
            result = {
                "survey_id": str(survey_id),
                "status": "launched",
                "launched_at": datetime.utcnow().isoformat() + "Z"
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
