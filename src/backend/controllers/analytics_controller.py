from flask import jsonify
from datetime import datetime, timedelta

class AnalyticsController:
    """
    Controller for analytics and reporting
    """
    
    @staticmethod
    def get_analytics_overview():
        """
        Get analytics overview
        """
        try:
            mock_analytics = {
                "summary": {
                    "total_surveys": 156,
                    "active_surveys": 23,
                    "completed_surveys": 133,
                    "total_responses": 4250,
                    "average_completion_rate": 87.3,
                    "total_accounts": 45
                },
                "trends": {
                    "survey_creation_trend": [
                        {"month": "2023-09", "count": 12},
                        {"month": "2023-10", "count": 15},
                        {"month": "2023-11", "count": 18},
                        {"month": "2023-12", "count": 22},
                        {"month": "2024-01", "count": 28}
                    ],
                    "response_trend": [
                        {"month": "2023-09", "count": 320},
                        {"month": "2023-10", "count": 450},
                        {"month": "2023-11", "count": 520},
                        {"month": "2023-12", "count": 680},
                        {"month": "2024-01", "count": 750}
                    ]
                },
                "performance": {
                    "top_performing_surveys": [
                        {"title": "Leadership 360", "completion_rate": 95.2},
                        {"title": "Team Skills Assessment", "completion_rate": 92.8},
                        {"title": "Culture Survey", "completion_rate": 89.5}
                    ],
                    "account_engagement": [
                        {"account_name": "Tech Corp", "engagement_score": 94.5},
                        {"account_name": "Innovation Labs", "engagement_score": 88.2},
                        {"account_name": "Global Solutions", "engagement_score": 85.7}
                    ]
                }
            }
            
            return jsonify({
                "success": True,
                "data": mock_analytics
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve analytics overview: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_survey_analytics(survey_id=None):
        """
        Get survey-specific analytics
        """
        try:
            mock_survey_analytics = {
                "survey_id": str(survey_id) if survey_id else "all",
                "response_statistics": {
                    "total_invitations": 50,
                    "total_responses": 42,
                    "completion_rate": 84.0,
                    "average_response_time": "12 minutes",
                    "response_rate_by_day": [
                        {"date": "2024-01-15", "responses": 8},
                        {"date": "2024-01-16", "responses": 12},
                        {"date": "2024-01-17", "responses": 15},
                        {"date": "2024-01-18", "responses": 7}
                    ]
                },
                "demographic_breakdown": {
                    "by_relationship": [
                        {"relationship": "Direct Report", "count": 15, "percentage": 35.7},
                        {"relationship": "Peer", "count": 18, "percentage": 42.9},
                        {"relationship": "Manager", "count": 9, "percentage": 21.4}
                    ],
                    "by_department": [
                        {"department": "Engineering", "count": 20, "percentage": 47.6},
                        {"department": "Marketing", "count": 12, "percentage": 28.6},
                        {"department": "Sales", "count": 10, "percentage": 23.8}
                    ]
                },
                "question_analytics": [
                    {
                        "question_id": "q1",
                        "question_text": "Leadership effectiveness",
                        "average_score": 4.2,
                        "response_distribution": [
                            {"score": 1, "count": 1},
                            {"score": 2, "count": 2},
                            {"score": 3, "count": 8},
                            {"score": 4, "count": 18},
                            {"score": 5, "count": 13}
                        ]
                    }
                ]
            }
            
            return jsonify({
                "success": True,
                "data": mock_survey_analytics
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve survey analytics: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_account_analytics(account_id=None):
        """
        Get account-specific analytics
        """
        try:
            mock_account_analytics = {
                "account_id": str(account_id) if account_id else "all",
                "usage_statistics": {
                    "total_surveys_created": 25,
                    "active_surveys": 5,
                    "total_subjects": 45,
                    "total_respondents": 180,
                    "total_responses_collected": 1250,
                    "average_completion_rate": 89.2
                },
                "engagement_metrics": {
                    "monthly_active_users": 32,
                    "survey_creation_frequency": "weekly",
                    "response_collection_rate": 87.5,
                    "user_satisfaction_score": 4.6
                },
                "billing_analytics": {
                    "current_plan": "Premium",
                    "monthly_cost": 299.99,
                    "cost_per_response": 0.24,
                    "usage_vs_limit": {
                        "subjects_used": 45,
                        "subjects_limit": 100,
                        "respondents_used": 180,
                        "respondents_limit": 500
                    }
                },
                "growth_trends": {
                    "survey_growth": [
                        {"month": "2023-10", "count": 3},
                        {"month": "2023-11", "count": 5},
                        {"month": "2023-12", "count": 8},
                        {"month": "2024-01", "count": 9}
                    ],
                    "user_growth": [
                        {"month": "2023-10", "count": 15},
                        {"month": "2023-11", "count": 22},
                        {"month": "2023-12", "count": 28},
                        {"month": "2024-01", "count": 32}
                    ]
                }
            }
            
            return jsonify({
                "success": True,
                "data": mock_account_analytics
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve account analytics: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_system_analytics():
        """
        Get system-wide analytics (System Admin only)
        """
        try:
            mock_system_analytics = {
                "platform_statistics": {
                    "total_accounts": 125,
                    "active_accounts": 98,
                    "total_surveys": 1250,
                    "total_responses": 45000,
                    "total_revenue": 125000.00,
                    "average_revenue_per_account": 1000.00
                },
                "growth_metrics": {
                    "monthly_account_growth": 8.5,
                    "monthly_revenue_growth": 12.3,
                    "user_retention_rate": 94.2,
                    "churn_rate": 2.1
                },
                "usage_patterns": {
                    "peak_usage_hours": [9, 10, 11, 14, 15, 16],
                    "most_popular_survey_types": [
                        {"type": "360_feedback", "count": 450, "percentage": 36.0},
                        {"type": "skills_assessment", "count": 375, "percentage": 30.0},
                        {"type": "culture_survey", "count": 250, "percentage": 20.0},
                        {"type": "leadership", "count": 175, "percentage": 14.0}
                    ],
                    "average_survey_duration": "15 minutes",
                    "average_responses_per_survey": 36
                },
                "geographic_distribution": [
                    {"region": "North America", "accounts": 45, "percentage": 36.0},
                    {"region": "Europe", "accounts": 38, "percentage": 30.4},
                    {"region": "Asia Pacific", "accounts": 28, "percentage": 22.4},
                    {"region": "Other", "accounts": 14, "percentage": 11.2}
                ]
            }
            
            return jsonify({
                "success": True,
                "data": mock_system_analytics
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve system analytics: {str(e)}"}
            }), 500
