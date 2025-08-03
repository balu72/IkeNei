"""
Survey Response Routes
Public routes for survey response submission (no authentication required)
"""

from flask import Blueprint, request
from controllers.survey_response_controller import SurveyResponseController
from middleware.auth_middleware import require_auth
from utils.response_helpers import validation_error_response, handle_exception
from utils.logger import get_logger
from utils.route_logger import log_route

survey_response_bp = Blueprint('survey_response', __name__)

@survey_response_bp.route('/api/survey/respond/<response_token>', methods=['GET'])
def get_survey_by_token(response_token):
    """
    Get survey form by response token (PUBLIC - no authentication required)
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: GET /api/survey/respond/{response_token[:8]}... ===")
    
    try:
        if not response_token:
            logger.warning("Get survey by token failed: No token provided")
            return validation_error_response({"token": "Response token is required"})
        
        result = SurveyResponseController.get_survey_by_token(response_token)
        logger.info(f"=== EXIT: GET /api/survey/respond/{response_token[:8]}... - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/survey/respond/{response_token[:8]}... - ERROR: {str(e)} ===")
        return handle_exception(e)

@survey_response_bp.route('/api/survey/respond/<response_token>', methods=['POST'])
def submit_survey_response(response_token):
    """
    Submit survey response (PUBLIC - no authentication required)
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: POST /api/survey/respond/{response_token[:8]}... ===")
    
    try:
        if not response_token:
            logger.warning("Submit survey response failed: No token provided")
            return validation_error_response({"token": "Response token is required"})
        
        data = request.get_json()
        logger.debug(f"Survey response data: {data}")
        
        # Basic validation
        if not data:
            logger.warning("Submit survey response failed: No request body provided")
            return validation_error_response({"request": "Request body is required"})
        
        if not data.get('responses'):
            logger.warning("Submit survey response failed: No responses provided")
            return validation_error_response({"responses": "Survey responses are required"})
        
        logger.info(f"Submitting survey response for token: {response_token[:8]}...")
        result = SurveyResponseController.submit_survey_response(response_token, data)
        logger.info(f"=== EXIT: POST /api/survey/respond/{response_token[:8]}... - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/survey/respond/{response_token[:8]}... - ERROR: {str(e)} ===")
        return handle_exception(e)

@survey_response_bp.route('/api/survey-runs/<survey_run_id>/responses', methods=['GET'])
@require_auth
@log_route
def get_survey_run_responses(survey_run_id):
    """
    Get all responses for a survey run (ADMIN - authentication required)
    """
    try:
        return SurveyResponseController.get_survey_run_responses(survey_run_id)
    
    except Exception as e:
        return handle_exception(e)

@survey_response_bp.route('/api/survey-runs/<survey_run_id>/analytics', methods=['GET'])
@require_auth
@log_route
def get_survey_run_analytics(survey_run_id):
    """
    Get analytics for a survey run (ADMIN - authentication required)
    """
    try:
        return SurveyResponseController.get_survey_run_analytics(survey_run_id)
    
    except Exception as e:
        return handle_exception(e)
