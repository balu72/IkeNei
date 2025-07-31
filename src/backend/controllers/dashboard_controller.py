from flask import jsonify
from datetime import datetime, timedelta

class DashboardController:
    """
    Controller for dashboard statistics and analytics
    """
    
    @staticmethod
    def get_dashboard_stats():
        """
        Get dashboard statistics
        """
        try:
            mock_stats = {
                "overview": {
                    "total_accounts": 125,
                    "active_surveys": 45,
                    "completed_surveys": 230,
                    "total_subjects": 1250,
                    "total_respondents": 8500,
                    "monthly_revenue": 15750.50
                },
                "recent_activity": {
                    "new_accounts_this_month": 8,
                    "surveys_created_this_week": 12,
                    "responses_collected_today": 156,
                    "active_users_today": 89
                },
                "growth_metrics": {
                    "account_growth_rate": 12.5,
                    "survey_completion_rate": 87.3,
                    "user_engagement_rate": 76.8,
                    "revenue_growth_rate": 23.4
                },
                "system_health": {
                    "uptime": "99.9%",
                    "response_time": "120ms",
                    "error_rate": "0.1%",
                    "active_connections": 234
                }
            }
            
            return jsonify({
                "success": True,
                "data": mock_stats
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve dashboard stats: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_dashboard_activity():
        """
        Get recent dashboard activity
        """
        try:
            mock_activity = [
                {
                    "id": "1",
                    "type": "survey_created",
                    "title": "New Leadership Assessment Survey",
                    "account_name": "Tech Corp",
                    "user_name": "John Smith",
                    "timestamp": (datetime.utcnow() - timedelta(minutes=15)).isoformat() + "Z",
                    "details": {
                        "survey_id": "survey_123",
                        "subjects_count": 5
                    }
                },
                {
                    "id": "2",
                    "type": "account_created",
                    "title": "New Account Registration",
                    "account_name": "Global Industries",
                    "user_name": "Sarah Johnson",
                    "timestamp": (datetime.utcnow() - timedelta(hours=2)).isoformat() + "Z",
                    "details": {
                        "account_type": "premium"
                    }
                },
                {
                    "id": "3",
                    "type": "survey_completed",
                    "title": "360 Feedback Survey Completed",
                    "account_name": "Innovation Labs",
                    "user_name": "Mike Davis",
                    "timestamp": (datetime.utcnow() - timedelta(hours=4)).isoformat() + "Z",
                    "details": {
                        "survey_id": "survey_456",
                        "responses_count": 25
                    }
                },
                {
                    "id": "4",
                    "type": "payment_received",
                    "title": "Payment Processed",
                    "account_name": "Enterprise Solutions",
                    "user_name": "System",
                    "timestamp": (datetime.utcnow() - timedelta(hours=6)).isoformat() + "Z",
                    "details": {
                        "amount": 299.99,
                        "billing_period": "2024-01"
                    }
                },
                {
                    "id": "5",
                    "type": "user_login",
                    "title": "Domain Admin Login",
                    "account_name": "Consulting Group",
                    "user_name": "Lisa Wilson",
                    "timestamp": (datetime.utcnow() - timedelta(hours=8)).isoformat() + "Z",
                    "details": {
                        "ip_address": "192.168.1.100"
                    }
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_activity
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve dashboard activity: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_dashboard_analytics():
        """
        Get dashboard analytics data
        """
        try:
            mock_analytics = {
                "usage_trends": {
                    "daily_active_users": [
                        {"date": "2024-01-01", "count": 45},
                        {"date": "2024-01-02", "count": 52},
                        {"date": "2024-01-03", "count": 48},
                        {"date": "2024-01-04", "count": 61},
                        {"date": "2024-01-05", "count": 58},
                        {"date": "2024-01-06", "count": 67},
                        {"date": "2024-01-07", "count": 73}
                    ],
                    "survey_creation_trend": [
                        {"month": "2023-10", "count": 15},
                        {"month": "2023-11", "count": 18},
                        {"month": "2023-12", "count": 22},
                        {"month": "2024-01", "count": 28}
                    ]
                },
                "performance_metrics": {
                    "average_response_time": 145,
                    "survey_completion_rates": [
                        {"survey_type": "360_feedback", "completion_rate": 89.5},
                        {"survey_type": "leadership", "completion_rate": 76.3},
                        {"survey_type": "skills", "completion_rate": 82.1},
                        {"survey_type": "culture", "completion_rate": 91.2}
                    ],
                    "user_satisfaction": 4.6,
                    "system_reliability": 99.8
                },
                "geographic_distribution": [
                    {"region": "North America", "accounts": 45, "percentage": 36.0},
                    {"region": "Europe", "accounts": 38, "percentage": 30.4},
                    {"region": "Asia Pacific", "accounts": 28, "percentage": 22.4},
                    {"region": "Latin America", "accounts": 10, "percentage": 8.0},
                    {"region": "Other", "accounts": 4, "percentage": 3.2}
                ],
                "revenue_analytics": {
                    "monthly_recurring_revenue": 12500.00,
                    "average_revenue_per_account": 125.50,
                    "churn_rate": 2.3,
                    "growth_rate": 15.7
                }
            }
            
            return jsonify({
                "success": True,
                "data": mock_analytics
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve dashboard analytics: {str(e)}"}
            }), 500
