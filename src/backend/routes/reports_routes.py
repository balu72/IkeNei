from flask import Blueprint, request
from controllers.reports_controller import ReportsController
from middleware.auth_middleware import require_domain_admin_role, require_admin_roles
from utils.response_helpers import validation_error_response, handle_exception
from utils.pagination import get_pagination_params, get_filter_params

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/api/reports', methods=['GET'])
@require_admin_roles
def get_reports():
    """
    Get all report templates
    """
    try:
        page, limit = get_pagination_params()
        filters = get_filter_params()
        
        return ReportsController.get_all_reports(page, limit, filters)
    
    except Exception as e:
        return handle_exception(e)

@reports_bp.route('/api/reports', methods=['POST'])
@require_domain_admin_role
def create_report():
    """
    Create new report template
    """
    try:
        data = request.get_json()
        
        # Basic validation
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['name', 'description', 'report_type']
        errors = {}
        
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        # Validate report type
        report_type = data.get('report_type')
        valid_types = ['feedback_summary', 'competency_analysis', 'survey_results', 'custom']
        
        if report_type and report_type not in valid_types:
            errors['report_type'] = f"Report type must be one of: {', '.join(valid_types)}"
        
        if errors:
            return validation_error_response(errors)
        
        return ReportsController.create_report(data)
    
    except Exception as e:
        return handle_exception(e)

@reports_bp.route('/api/reports/<int:report_id>', methods=['GET'])
@require_admin_roles
def get_report(report_id):
    """
    Get specific report template
    """
    try:
        return ReportsController.get_report_by_id(report_id)
    
    except Exception as e:
        return handle_exception(e)

@reports_bp.route('/api/reports/<int:report_id>', methods=['PUT'])
@require_domain_admin_role
def update_report(report_id):
    """
    Update report template
    """
    try:
        data = request.get_json()
        
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        # Validate report type if provided
        report_type = data.get('report_type')
        if report_type:
            valid_types = ['feedback_summary', 'competency_analysis', 'survey_results', 'custom']
            if report_type not in valid_types:
                return validation_error_response({
                    'report_type': f"Report type must be one of: {', '.join(valid_types)}"
                })
        
        return ReportsController.update_report(report_id, data)
    
    except Exception as e:
        return handle_exception(e)

@reports_bp.route('/api/reports/<int:report_id>', methods=['DELETE'])
@require_domain_admin_role
def delete_report(report_id):
    """
    Delete report template
    """
    try:
        return ReportsController.delete_report(report_id)
    
    except Exception as e:
        return handle_exception(e)

@reports_bp.route('/api/reports/<int:report_id>/generate', methods=['POST'])
@require_admin_roles
def generate_report(report_id):
    """
    Generate report instance
    """
    try:
        data = request.get_json() or {}
        
        return ReportsController.generate_report(report_id, data)
    
    except Exception as e:
        return handle_exception(e)

@reports_bp.route('/api/reports/<int:report_id>/instances', methods=['GET'])
@require_admin_roles
def get_report_instances(report_id):
    """
    Get generated report instances
    """
    try:
        page, limit = get_pagination_params()
        
        return ReportsController.get_report_instances(report_id, page, limit)
    
    except Exception as e:
        return handle_exception(e)

@reports_bp.route('/api/reports/<int:report_id>/status', methods=['PATCH'])
@require_domain_admin_role
def update_report_status(report_id):
    """
    Change report status
    """
    try:
        data = request.get_json()
        
        if not data or not data.get('status'):
            return validation_error_response({"status": "Status is required"})
        
        status = data.get('status')
        valid_statuses = ['active', 'draft', 'archived']
        
        if status.lower() not in valid_statuses:
            return validation_error_response({
                "status": f"Status must be one of: {', '.join(valid_statuses)}"
            })
        
        return ReportsController.update_report_status(report_id, status)
    
    except Exception as e:
        return handle_exception(e)
