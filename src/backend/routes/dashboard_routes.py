from flask import Blueprint
from controllers.dashboard_controller import DashboardController
from middleware.auth_middleware import require_auth
from utils.response_helpers import handle_exception
from utils.route_logger import log_route

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/api/dashboard/stats', methods=['GET'])
@require_auth
@log_route
def get_dashboard_stats():
    """
    Get role-specific dashboard statistics
    """
    try:
        return DashboardController.get_dashboard_stats()
    
    except Exception as e:
        return handle_exception(e)

@dashboard_bp.route('/api/dashboard/activity', methods=['GET'])
@require_auth
@log_route
def get_dashboard_activity():
    """
    Get recent activity feed
    """
    try:
        return DashboardController.get_recent_activity()
    
    except Exception as e:
        return handle_exception(e)

@dashboard_bp.route('/api/dashboard/analytics', methods=['GET'])
@require_auth
@log_route
def get_dashboard_analytics():
    """
    Get analytics data for charts
    """
    try:
        return DashboardController.get_analytics_data()
    
    except Exception as e:
        return handle_exception(e)
