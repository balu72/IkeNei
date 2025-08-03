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
    @log_function_call
    def get_respondent_by_id(respondent_id):
        """
        Get respondent by ID
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving respondent by ID: {respondent_id}")
        
        try:
            # TODO: Implement actual respondent retrieval from database
            # This should:
            # - Query respondents collection for specific respondent
            # - Include subject information if needed
            # - Check user permissions for accessing this respondent
            # - Include response status and timestamps
            
            respondent = RespondentRepository.get_respondent_by_id(respondent_id)
            
            if not respondent:
                return jsonify({
                    "success": False,
                    "error": {"message": "Respondent not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": respondent.to_public_dict()
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve respondent {respondent_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve respondent: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_respondent(respondent_id, data):
        """
        Update respondent
        """
        logger = get_logger(__name__)
        logger.info(f"Updating respondent {respondent_id} with data: {data}")
        
        try:
            # TODO: Implement actual respondent update in database
            # This should:
            # - Validate respondent exists
            # - Check user permissions for updating this respondent
            # - Validate email format if provided
            # - Validate relationship type if provided
            # - Update respondent record in database
            
            respondent = RespondentRepository.update_respondent(respondent_id, data)
            
            if not respondent:
                return jsonify({
                    "success": False,
                    "error": {"message": "Respondent not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": respondent.to_public_dict(),
                "message": "Respondent updated successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to update respondent {respondent_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update respondent: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def delete_respondent(respondent_id):
        """
        Delete respondent
        """
        logger = get_logger(__name__)
        logger.info(f"Deleting respondent: {respondent_id}")
        
        try:
            # TODO: Implement actual respondent deletion from database
            # This should:
            # - Validate respondent exists
            # - Check user permissions for deleting this respondent
            # - Check if respondent has any survey responses (may need to handle cascading)
            # - Remove respondent record from database
            # - Log deletion activity
            
            success = RespondentRepository.delete_respondent(respondent_id)
            
            if not success:
                return jsonify({
                    "success": False,
                    "error": {"message": "Respondent not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "message": f"Respondent {respondent_id} deleted successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to delete respondent {respondent_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete respondent: {str(e)}"}
            }), 500
