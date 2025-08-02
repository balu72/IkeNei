from flask import jsonify
from datetime import datetime
from database import SubjectRepository
from utils.logger import get_logger, log_function_call

class SubjectsController:
    """
    Controller for subjects management
    """
    
    @staticmethod
    @log_function_call
    def get_all_subjects():
        """
        Get all subjects
        """
        logger = get_logger(__name__)
        logger.info("Retrieving all subjects")
        
        try:
            # Get pagination parameters (could be from request args)
            page = 1
            per_page = 20
            
            # Get subjects from database
            result = SubjectRepository.get_all_subjects(
                page=page,
                per_page=per_page
            )
            
            return jsonify({
                "success": True,
                "data": result['subjects'],
                "pagination": result['pagination']
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve subjects: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve subjects: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def create_subject(data):
        """
        Create a new subject
        """
        logger = get_logger(__name__)
        logger.info(f"Creating new subject with data: {data}")
        
        try:
            # Validate required fields
            required_fields = ['name', 'account_id']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        "success": False,
                        "error": {"message": f"Missing required field: {field}"}
                    }), 400
            
            # Create subject using repository
            subject = SubjectRepository.create_subject(
                account_id=data.get('account_id'),
                name=data.get('name'),
                email=data.get('email'),
                position=data.get('position'),
                department=data.get('department')
            )
            
            return jsonify({
                "success": True,
                "data": subject.to_public_dict(),
                "message": "Subject created successfully"
            }), 201
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create subject: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_subject_by_id(subject_id):
        """
        Get subject by ID
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving subject by ID: {subject_id}")
        
        try:
            subject = SubjectRepository.get_subject_by_id(subject_id)
            
            if not subject:
                return jsonify({
                    "success": False,
                    "error": {"message": "Subject not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": subject.to_public_dict()
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve subject {subject_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve subject: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_subject(subject_id, data):
        """
        Update subject
        """
        logger = get_logger(__name__)
        logger.info(f"Updating subject {subject_id} with data: {data}")
        
        try:
            subject = SubjectRepository.update_subject(subject_id, data)
            
            if not subject:
                return jsonify({
                    "success": False,
                    "error": {"message": "Subject not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": subject.to_public_dict(),
                "message": "Subject updated successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to update subject {subject_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update subject: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def delete_subject(subject_id):
        """
        Delete subject
        """
        logger = get_logger(__name__)
        logger.info(f"Deleting subject: {subject_id}")
        
        try:
            success = SubjectRepository.delete_subject(subject_id)
            
            if not success:
                return jsonify({
                    "success": False,
                    "error": {"message": "Subject not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "message": f"Subject {subject_id} deleted successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to delete subject {subject_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete subject: {str(e)}"}
            }), 500
