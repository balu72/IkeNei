from flask import Blueprint, request
from controllers.notifications_controller import NotificationsController
from middleware.auth_middleware import require_auth
from utils.response_helpers import validation_error_response, handle_exception

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/api/notifications', methods=['GET'])
@require_auth
def get_notifications():
    """
    Get account notifications
    """
    try:
        return NotificationsController.get_account_notifications()
    
    except Exception as e:
        return handle_exception(e)

@notifications_bp.route('/api/notifications/<int:notification_id>/read', methods=['PATCH'])
@require_auth
def mark_notification_read(notification_id):
    """
    Mark notification as read
    """
    try:
        return NotificationsController.mark_notification_as_read(notification_id)
    
    except Exception as e:
        return handle_exception(e)

@notifications_bp.route('/api/notifications', methods=['POST'])
@require_auth
def create_notification():
    """
    Create notification
    """
    try:
        data = request.get_json()
        
        # Basic validation
        if not data:
            return validation_error_response({"request": "Request body is required"})
        
        required_fields = ['title', 'message', 'type']
        errors = {}
        
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_', ' ').title()} is required"
        
        # Validate notification type
        notification_type = data.get('type')
        valid_types = ['info', 'success', 'warning', 'error', 'survey_invitation', 'reminder']
        
        if notification_type and notification_type not in valid_types:
            errors['type'] = f"Notification type must be one of: {', '.join(valid_types)}"
        
        if errors:
            return validation_error_response(errors)
        
        return NotificationsController.create_notification(data)
    
    except Exception as e:
        return handle_exception(e)

@notifications_bp.route('/api/notifications/<int:notification_id>', methods=['DELETE'])
@require_auth
def delete_notification(notification_id):
    """
    Delete notification
    """
    try:
        return NotificationsController.delete_notification(notification_id)
    
    except Exception as e:
        return handle_exception(e)
