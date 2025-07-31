from flask import jsonify
from datetime import datetime, timedelta

class SurveysController:
    """
    Controller for survey management
    """
    
    @staticmethod
    def get_all_surveys(page=1, limit=20, filters=None):
        """
        Get all surveys with pagination and filtering
        """
        try:
            mock_surveys = [
                {
                    "id": "1",
                    "title": "Leadership 360 Assessment",
                    "description": "Comprehensive leadership evaluation survey",
                    "account_id": "1",
                    "account_name": "Tech Corp",
                    "status": "active",
                    "survey_type": "360_feedback",
                    "subjects_count": 5,
                    "respondents_count": 25,
                    "responses_count": 18,
                    "completion_rate": 72.0,
                    "created_at": "2024-01-15T00:00:00Z",
                    "updated_at": "2024-01-20T00:00:00Z",
                    "due_date": "2024-02-15T00:00:00Z"
                },
                {
                    "id": "2",
                    "title": "Team Skills Assessment",
                    "description": "Technical and soft skills evaluation",
                    "account_id": "2",
                    "account_name": "Innovation Labs",
                    "status": "completed",
                    "survey_type": "skills",
                    "subjects_count": 8,
                    "respondents_count": 40,
                    "responses_count": 40,
                    "completion_rate": 100.0,
                    "created_at": "2023-12-01T00:00:00Z",
                    "updated_at": "2024-01-10T00:00:00Z",
                    "completed_at": "2024-01-10T00:00:00Z"
                }
            ]
            
            # Apply filters
            if filters:
                if filters.get('status'):
                    mock_surveys = [s for s in mock_surveys if s['status'] == filters['status']]
                if filters.get('survey_type'):
                    mock_surveys = [s for s in mock_surveys if s['survey_type'] == filters['survey_type']]
                if filters.get('account_id'):
                    mock_surveys = [s for s in mock_surveys if s['account_id'] == filters['account_id']]
                if filters.get('search'):
                    search_term = filters['search'].lower()
                    mock_surveys = [s for s in mock_surveys if search_term in s['title'].lower() or search_term in s['description'].lower()]
            
            # Apply pagination
            start_idx = (page - 1) * limit
            end_idx = start_idx + limit
            paginated_surveys = mock_surveys[start_idx:end_idx]
            
            return jsonify({
                "success": True,
                "data": paginated_surveys,
                "pagination": {
                    "page": page,
                    "limit": limit,
                    "total": len(mock_surveys),
                    "pages": (len(mock_surveys) + limit - 1) // limit
                }
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    def create_survey(data):
        """
        Create a new survey
        """
        try:
            new_survey = {
                "id": "new_survey_id",
                "title": data.get('title'),
                "description": data.get('description', ''),
                "account_id": data.get('account_id'),
                "status": "draft",
                "survey_type": data.get('survey_type', '360_feedback'),
                "subjects_count": 0,
                "respondents_count": 0,
                "responses_count": 0,
                "completion_rate": 0.0,
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z",
                "settings": {
                    "anonymous_responses": data.get('anonymous_responses', True),
                    "allow_comments": data.get('allow_comments', True),
                    "reminder_frequency": data.get('reminder_frequency', 'weekly')
                }
            }
            
            return jsonify({
                "success": True,
                "data": new_survey,
                "message": "Survey created successfully"
            }), 201
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create survey: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_survey_by_id(survey_id):
        """
        Get survey by ID
        """
        try:
            mock_survey = {
                "id": str(survey_id),
                "title": "Leadership 360 Assessment",
                "description": "Comprehensive leadership evaluation survey",
                "account_id": "1",
                "account_name": "Tech Corp",
                "status": "active",
                "survey_type": "360_feedback",
                "subjects_count": 5,
                "respondents_count": 25,
                "responses_count": 18,
                "completion_rate": 72.0,
                "created_at": "2024-01-15T00:00:00Z",
                "updated_at": "2024-01-20T00:00:00Z",
                "due_date": "2024-02-15T00:00:00Z",
                "settings": {
                    "anonymous_responses": True,
                    "allow_comments": True,
                    "reminder_frequency": "weekly"
                },
                "questions": [
                    {
                        "id": "q1",
                        "text": "How would you rate this person's leadership skills?",
                        "type": "rating",
                        "scale": 5,
                        "required": True
                    },
                    {
                        "id": "q2",
                        "text": "What are their key strengths?",
                        "type": "text",
                        "required": False
                    }
                ]
            }
            
            return jsonify({
                "success": True,
                "data": mock_survey
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve survey: {str(e)}"}
            }), 500
    
    @staticmethod
    def update_survey(survey_id, data):
        """
        Update survey
        """
        try:
            updated_survey = {
                "id": str(survey_id),
                "title": data.get('title', 'Updated Survey'),
                "description": data.get('description', ''),
                "status": data.get('status', 'active'),
                "survey_type": data.get('survey_type', '360_feedback'),
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": updated_survey,
                "message": "Survey updated successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update survey: {str(e)}"}
            }), 500
    
    @staticmethod
    def delete_survey(survey_id):
        """
        Delete survey
        """
        try:
            return jsonify({
                "success": True,
                "message": f"Survey {survey_id} deleted successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete survey: {str(e)}"}
            }), 500
    
    @staticmethod
    def update_survey_status(survey_id, status):
        """
        Update survey status
        """
        try:
            updated_survey = {
                "id": str(survey_id),
                "status": status,
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": updated_survey,
                "message": f"Survey status updated to {status}"
            })
            
        except Exception as e:
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
            mock_surveys = [
                {
                    "id": "1",
                    "title": "Leadership Assessment",
                    "description": "Please provide feedback on leadership skills",
                    "status": "active",
                    "due_date": "2024-02-15T00:00:00Z",
                    "estimated_time": "15 minutes"
                },
                {
                    "id": "2",
                    "title": "Team Collaboration Survey",
                    "description": "Evaluate team collaboration effectiveness",
                    "status": "active",
                    "due_date": "2024-02-20T00:00:00Z",
                    "estimated_time": "10 minutes"
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_surveys
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve available surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_my_surveys():
        """
        Get surveys created by current user
        """
        try:
            mock_surveys = [
                {
                    "id": "1",
                    "title": "My Leadership 360",
                    "status": "active",
                    "responses_count": 8,
                    "total_respondents": 12,
                    "completion_rate": 66.7,
                    "created_at": "2024-01-15T00:00:00Z"
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_surveys
            })
            
        except Exception as e:
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
            submission = {
                "survey_id": str(survey_id),
                "responses": responses,
                "submitted_at": datetime.utcnow().isoformat() + "Z",
                "submission_id": "submission_123"
            }
            
            return jsonify({
                "success": True,
                "data": submission,
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
            mock_responses = [
                {
                    "id": "response_1",
                    "respondent_id": "resp_1",
                    "respondent_name": "Anonymous",
                    "submitted_at": "2024-01-20T10:30:00Z",
                    "responses": {
                        "q1": 4,
                        "q2": "Great communication skills"
                    }
                },
                {
                    "id": "response_2",
                    "respondent_id": "resp_2",
                    "respondent_name": "Anonymous",
                    "submitted_at": "2024-01-21T14:15:00Z",
                    "responses": {
                        "q1": 5,
                        "q2": "Excellent leadership qualities"
                    }
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_responses
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
            result = {
                "survey_id": str(survey_id),
                "status": "launched",
                "launched_at": datetime.utcnow().isoformat() + "Z",
                "notifications_sent": data.get('send_notifications', True),
                "recipients_count": 25
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
