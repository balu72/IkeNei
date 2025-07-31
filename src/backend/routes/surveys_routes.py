from flask import Blueprint, request
from controllers.surveys_controller import SurveysController
from middleware.auth_middleware import require_domain_admin_role, require_admin_roles, require_auth
from utils.response_helpers import validation_error_response, handle_exception
from utils.pagination import get_pagination_params, get_filter_params
from utils.logger import get_logger
from utils.route_logger import log_route

surveys_bp = Blueprint('surveys', __name__)

@surveys_bp.route('/api/surveys', methods=['GET'])
@require_admin_roles
def get_surveys():
    """
    Get all surveys with filtering and pagination
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: GET /api/surveys ===")
    
    try:
        page, limit = get_pagination_params()
        filters = get_filter_params()
        logger.info(f"Request parameters - page: {page}, limit: {limit}, filters: {filters}")
        
        result = SurveysController.get_all_surveys(page, limit, filters)
        logger.info("=== EXIT: GET /api/surveys - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/surveys - ERROR: {str(e)} ===")
        return handle_exception(e)

@surveys_bp.route('/api/surveys', methods=['POST'])
@require_domain_admin_role
def create_survey():
    """
    Create new survey
    """
    logger = get_logger(__name__)
    logger.info("=== ENTRY: POST /api/surveys ===")
    
    try:
        data = request.get_json()
        logger.debug(f"Survey creation data: {data}")
        
        # Basic validation
        if not data:
            logger.warning("Create survey failed: No request body provided")
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['title', 'description']
        errors = {}
        
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        if errors:
            logger.warning(f"Create survey validation failed: {errors}")
            return validation_error_response(errors)
        
        logger.info(f"Creating survey: {data.get('title')}")
        result = SurveysController.create_survey(data)
        logger.info("=== EXIT: POST /api/surveys - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: POST /api/surveys - ERROR: {str(e)} ===")
        return handle_exception(e)

@surveys_bp.route('/api/surveys/<int:survey_id>', methods=['GET'])
@require_auth
def get_survey(survey_id):
    """
    Get specific survey details
    """
    logger = get_logger(__name__)
    logger.info(f"=== ENTRY: GET /api/surveys/{survey_id} ===")
    
    try:
        result = SurveysController.get_survey_by_id(survey_id)
        logger.info(f"=== EXIT: GET /api/surveys/{survey_id} - SUCCESS ===")
        return result
    
    except Exception as e:
        logger.error(f"=== EXIT: GET /api/surveys/{survey_id} - ERROR: {str(e)} ===")
        return handle_exception(e)

@surveys_bp.route('/api/surveys/<int:survey_id>', methods=['PUT'])
@require_domain_admin_role
@log_route
def update_survey(survey_id):
    """
    Update survey
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        return SurveysController.update_survey(survey_id, data)
    
    except Exception as e:
        return handle_exception(e)

@surveys_bp.route('/api/surveys/<int:survey_id>', methods=['DELETE'])
@require_domain_admin_role
@log_route
def delete_survey(survey_id):
    """
    Delete survey
    """
    try:
        return SurveysController.delete_survey(survey_id)
    
    except Exception as e:
        return handle_exception(e)

@surveys_bp.route('/api/surveys/<int:survey_id>/status', methods=['PATCH'])
@require_domain_admin_role
@log_route
def update_survey_status(survey_id):
    """
    Change survey status (Active/Draft/Completed)
    """
    try:
        data = request.get_json()
        
        if not data or not data.get('status'):
            return validation_error_response({"status": "Status is required"})
        
        status = data.get('status')
        valid_statuses = ['active', 'draft', 'completed']
        
        if status.lower() not in valid_statuses:
            return validation_error_response({
                "status": f"Status must be one of: {', '.join(valid_statuses)}"
            })
        
        return SurveysController.update_survey_status(survey_id, status)
    
    except Exception as e:
        return handle_exception(e)

@surveys_bp.route('/api/surveys/available', methods=['GET'])
@require_auth
@log_route
def get_available_surveys():
    """
    Get available surveys for current account
    """
    try:
        return SurveysController.get_available_surveys()
    
    except Exception as e:
        return handle_exception(e)

@surveys_bp.route('/api/surveys/<int:survey_id>/responses', methods=['POST'])
@require_auth
@log_route
def submit_survey_responses(survey_id):
    """
    Submit survey responses
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        if not data.get('responses'):
            return validation_error_response({"responses": "Responses are required"})
        
        return SurveysController.submit_survey_responses(survey_id, data)
    
    except Exception as e:
        return handle_exception(e)

@surveys_bp.route('/api/surveys/<int:survey_id>/responses', methods=['GET'])
@require_auth
@log_route
def get_survey_responses(survey_id):
    """
    Get survey responses
    """
    try:
        return SurveysController.get_survey_responses(survey_id)
    
    except Exception as e:
        return handle_exception(e)

@surveys_bp.route('/api/surveys/my-surveys', methods=['GET'])
@require_auth
@log_route
def get_my_surveys():
    """
    Get surveys where account is subject/respondent
    """
    try:
        return SurveysController.get_my_surveys()
    
    except Exception as e:
        return handle_exception(e)

@surveys_bp.route('/api/surveys/<int:survey_id>/run', methods=['POST'])
@require_auth
@log_route
def run_survey(survey_id):
    """
    Run/execute a survey
    """
    try:
        data = request.get_json()
        
        return SurveysController.run_survey(survey_id, data)
    
    except Exception as e:
        return handle_exception(e)
