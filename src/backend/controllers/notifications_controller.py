from flask import jsonify
from datetime import datetime, timedelta

class NotificationsController:
    """
    Controller for notifications management
    """
    
    @staticmethod
    def get_all_notifications():
        """
        Get all notifications for current user
        """
        try:
            mock_notifications = [
                {
                    "id": "1",
                    "title": "Survey Response Received",
                    "message": "New response received for Leadership Assessment survey",
                    "type": "survey_response",
                    "priority": "normal",
                    "is_read": False,
                    "created_at": (datetime.utcnow() - timedelta(hours=2)).isoformat() + "Z",
                    "data": {
                        "survey_id": "survey_123",
                        "survey_title": "Leadership Assessment"
                    }
                },
                {
                    "id": "2",
                    "title": "Survey Reminder",
                    "message": "Please complete your pending survey responses",
                    "type": "survey_reminder",
                    "priority": "high",
                    "is_read": True,
                    "created_at": (datetime.utcnow() - timedelta(days=1)).isoformat() + "Z",
                    "read_at": (datetime.utcnow() - timedelta(hours=12)).isoformat() + "Z",
                    "data": {
                        "pending_count": 3
                    }
                },
                {
                    "id": "3",
                    "title": "Account Upgrade",
                    "message": "Your account has been upgraded to Premium",
                    "type": "account_update",
                    "priority": "normal",
                    "is_read": True,
                    "created_at": (datetime.utcnow() - timedelta(days=3)).isoformat() + "Z",
                    "read_at": (datetime.utcnow() - timedelta(days=2)).isoformat() + "Z",
                    "data": {
                        "account_type": "premium"
                    }
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_notifications
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve notifications: {str(e)}"}
            }), 500
    
    @staticmethod
    def mark_as_read(notification_id):
        """
        Mark notification as read
        """
        try:
            updated_notification = {
                "id": str(notification_id),
                "is_read": True,
                "read_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": updated_notification,
                "message": "Notification marked as read"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to mark notification as read: {str(e)}"}
            }), 500
    
    @staticmethod
    def create_notification(data):
        """
        Create a new notification
        """
        try:
            new_notification = {
                "id": "new_notification_id",
                "title": data.get('title'),
                "message": data.get('message'),
                "type": data.get('type', 'general'),
                "priority": data.get('priority', 'normal'),
                "is_read": False,
                "created_at": datetime.utcnow().isoformat() + "Z",
                "data": data.get('data', {})
            }
            
            return jsonify({
                "success": True,
                "data": new_notification,
                "message": "Notification created successfully"
            }), 201
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create notification: {str(e)}"}
            }), 500
    
    @staticmethod
    def delete_notification(notification_id):
        """
        Delete notification
        """
        try:
            return jsonify({
                "success": True,
                "message": f"Notification {notification_id} deleted successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete notification: {str(e)}"}
            }), 500
