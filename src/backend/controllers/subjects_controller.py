from flask import jsonify
from datetime import datetime

class SubjectsController:
    """
    Controller for subjects management
    """
    
    @staticmethod
    def get_all_subjects():
        """
        Get all subjects
        """
        try:
            mock_subjects = [
                {
                    "id": "1",
                    "name": "John Smith",
                    "email": "john.smith@company.com",
                    "position": "Senior Manager",
                    "department": "Engineering",
                    "account_id": "1",
                    "status": "active",
                    "surveys_count": 3,
                    "created_at": "2024-01-01T00:00:00Z",
                    "updated_at": "2024-01-15T00:00:00Z"
                },
                {
                    "id": "2",
                    "name": "Sarah Johnson",
                    "email": "sarah.johnson@company.com",
                    "position": "Team Lead",
                    "department": "Marketing",
                    "account_id": "1",
                    "status": "active",
                    "surveys_count": 2,
                    "created_at": "2024-01-05T00:00:00Z",
                    "updated_at": "2024-01-20T00:00:00Z"
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_subjects
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve subjects: {str(e)}"}
            }), 500
    
    @staticmethod
    def create_subject(data):
        """
        Create a new subject
        """
        try:
            new_subject = {
                "id": "new_subject_id",
                "name": data.get('name'),
                "email": data.get('email'),
                "position": data.get('position', ''),
                "department": data.get('department', ''),
                "account_id": data.get('account_id'),
                "status": "active",
                "surveys_count": 0,
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": new_subject,
                "message": "Subject created successfully"
            }), 201
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create subject: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_subject_by_id(subject_id):
        """
        Get subject by ID
        """
        try:
            mock_subject = {
                "id": str(subject_id),
                "name": "John Smith",
                "email": "john.smith@company.com",
                "position": "Senior Manager",
                "department": "Engineering",
                "account_id": "1",
                "status": "active",
                "surveys_count": 3,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-15T00:00:00Z"
            }
            
            return jsonify({
                "success": True,
                "data": mock_subject
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve subject: {str(e)}"}
            }), 500
    
    @staticmethod
    def update_subject(subject_id, data):
        """
        Update subject
        """
        try:
            updated_subject = {
                "id": str(subject_id),
                "name": data.get('name', 'Updated Subject'),
                "email": data.get('email', 'updated@company.com'),
                "position": data.get('position', ''),
                "department": data.get('department', ''),
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": updated_subject,
                "message": "Subject updated successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update subject: {str(e)}"}
            }), 500
    
    @staticmethod
    def delete_subject(subject_id):
        """
        Delete subject
        """
        try:
            return jsonify({
                "success": True,
                "message": f"Subject {subject_id} deleted successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete subject: {str(e)}"}
            }), 500
