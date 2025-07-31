from flask import jsonify
from datetime import datetime

class RespondentsController:
    """
    Controller for respondents management
    """
    
    @staticmethod
    def get_all_respondents(subject_id=None):
        """
        Get all respondents, optionally filtered by subject
        """
        try:
            mock_respondents = [
                {
                    "id": "1",
                    "name": "Alice Brown",
                    "email": "alice.brown@company.com",
                    "relationship": "Direct Report",
                    "subject_id": "1",
                    "subject_name": "John Smith",
                    "status": "invited",
                    "response_status": "pending",
                    "invited_at": "2024-01-15T00:00:00Z",
                    "created_at": "2024-01-15T00:00:00Z"
                },
                {
                    "id": "2",
                    "name": "Bob Wilson",
                    "email": "bob.wilson@company.com",
                    "relationship": "Peer",
                    "subject_id": "1",
                    "subject_name": "John Smith",
                    "status": "active",
                    "response_status": "completed",
                    "invited_at": "2024-01-15T00:00:00Z",
                    "responded_at": "2024-01-18T00:00:00Z",
                    "created_at": "2024-01-15T00:00:00Z"
                }
            ]
            
            # Filter by subject if provided
            if subject_id:
                mock_respondents = [r for r in mock_respondents if r['subject_id'] == str(subject_id)]
            
            return jsonify({
                "success": True,
                "data": mock_respondents
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve respondents: {str(e)}"}
            }), 500
    
    @staticmethod
    def create_respondent(data):
        """
        Create a new respondent
        """
        try:
            new_respondent = {
                "id": "new_respondent_id",
                "name": data.get('name'),
                "email": data.get('email'),
                "relationship": data.get('relationship', 'Peer'),
                "subject_id": data.get('subject_id'),
                "status": "invited",
                "response_status": "pending",
                "invited_at": datetime.utcnow().isoformat() + "Z",
                "created_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": new_respondent,
                "message": "Respondent created successfully"
            }), 201
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create respondent: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_respondent_by_id(respondent_id):
        """
        Get respondent by ID
        """
        try:
            mock_respondent = {
                "id": str(respondent_id),
                "name": "Alice Brown",
                "email": "alice.brown@company.com",
                "relationship": "Direct Report",
                "subject_id": "1",
                "subject_name": "John Smith",
                "status": "active",
                "response_status": "completed",
                "invited_at": "2024-01-15T00:00:00Z",
                "responded_at": "2024-01-18T00:00:00Z",
                "created_at": "2024-01-15T00:00:00Z"
            }
            
            return jsonify({
                "success": True,
                "data": mock_respondent
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve respondent: {str(e)}"}
            }), 500
    
    @staticmethod
    def update_respondent(respondent_id, data):
        """
        Update respondent
        """
        try:
            updated_respondent = {
                "id": str(respondent_id),
                "name": data.get('name', 'Updated Respondent'),
                "email": data.get('email', 'updated@company.com'),
                "relationship": data.get('relationship', 'Peer'),
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": updated_respondent,
                "message": "Respondent updated successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update respondent: {str(e)}"}
            }), 500
    
    @staticmethod
    def delete_respondent(respondent_id):
        """
        Delete respondent
        """
        try:
            return jsonify({
                "success": True,
                "message": f"Respondent {respondent_id} deleted successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete respondent: {str(e)}"}
            }), 500
