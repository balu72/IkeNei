from flask import Blueprint, request
from controllers.analytics_controller import AnalyticsController
from middleware.auth_middleware import require_system_admin_role
from utils.response_helpers import handle_exception

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/api/analytics/surveys', methods=['GET'])
@require_system_admin_role
def get_survey_analytics():
    """
    Get survey analytics
    """
    try:
        return AnalyticsController.get_survey_analytics()
    
    except Exception as e:
        return handle_exception(e)

@analytics_bp.route('/api/analytics/accounts', methods=['GET'])
@require_system_admin_role
def get_account_analytics():
    """
    Get account analytics
    """
    try:
        return AnalyticsController.get_account_analytics()
    
    except Exception as e:
        return handle_exception(e)

@analytics_bp.route('/api/analytics/system-health', methods=['GET'])
@require_system_admin_role
def get_system_health():
    """
    Get system health metrics
    """
    try:
        return AnalyticsController.get_system_health_metrics()
    
    except Exception as e:
        return handle_exception(e)

@analytics_bp.route('/api/analytics/reports', methods=['GET'])
@require_system_admin_role
def generate_analytics_reports():
    """
    Generate analytics reports
    """
    try:
        return AnalyticsController.generate_analytics_reports()
    
    except Exception as e:
        return handle_exception(e)

@analytics_bp.route('/api/analytics/export', methods=['POST'])
@require_system_admin_role
def export_analytics_data():
    """
    Export analytics data
    """
    try:
        data = request.get_json() or {}
        return AnalyticsController.export_analytics_data(data)
    
    except Exception as e:
        return handle_exception(e)
