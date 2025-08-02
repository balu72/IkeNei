from flask import jsonify
from datetime import datetime
from database import RespondentRepository
from utils.logger import get_logger, log_function_call

class RespondentsController:
    """
    Controller for respondents management
    """
    
    @staticmethod
    @log_function_call
    def get_all_respondents(subject_id=None):
        """
        Get all respondents, optionally filtered by subject
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving all respondents, subject_id filter: {subject_id}")
        
        try:
            # Get pagination parameters (could be from request args)
            page = 1
            per_page = 20
            
            # Get respondents from database
            result = RespondentRepository.get_all_respondents(
                page=page,
                per_page=per_page,
                subject_id=subject_id
            )
            
            # Convert to public dict format
            respondents_data = [respondent.to_public_dict() for respondent in result['respondents']]
            
            return jsonify({
                "success": True,
                "data": respondents_data,
                "pagination": result['pagination']
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve respondents: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve respondents: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def create_respondent(data):
        """
        Create a new respondent
        """
        logger = get_logger(__name__)
        logger.info(f"Creating new respondent with data: {data}")
        
        try:
            # Validate required fields
            required_fields = ['name', 'email', 'subject_id', 'relationship']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        "success": False,
                        "error": {"message": f"Missing required field: {field}"}
                    }), 400
            
            # Create respondent using repository
            respondent = RespondentRepository.create_respondent(
                subject_id=data.get('subject_id'),
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                address=data.get('address'),
                relationship=data.get('relationship'),
                other_info=data.get('other_info')
            )
            
            return jsonify({
                "success": True,
                "data": respondent.to_public_dict(),
                "message": "Respondent created successfully"
            }), 201
            
        except Exception as e:
            logger.error(f"Failed to create respondent: {str(e)}")
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
