from flask import jsonify
from datetime import datetime, timedelta
from database import SurveyRepository
from database.repositories.survey_run_repository import SurveyRunRepository
from database.repositories.subject_repository import SubjectRepository
from database.repositories.respondent_repository import RespondentRepository
from services.email_service import email_service
from utils.logger import get_logger, log_function_call

class SurveysController:
    """
    Controller for survey management
    """
    
    @staticmethod
    @log_function_call
    def get_all_surveys(page=1, limit=20, filters=None):
        """
        Get all surveys with pagination and filtering
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving surveys - page: {page}, limit: {limit}, filters: {filters}")
        
        try:
            result = SurveyRepository.get_all_surveys(
                page=page,
                per_page=limit,
                filters=filters
            )
            
            return jsonify({
                "success": True,
                "data": result['surveys'],
                "pagination": result['pagination']
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve surveys: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def create_survey(data, creator_role='domain_admin'):
        """
        Create a new survey
        """
        logger = get_logger(__name__)
        logger.info(f"Creating new survey with data: {data}, creator_role: {creator_role}")
        
        try:
            # Validate required fields
            required_fields = ['title', 'account_id', 'survey_type']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        "success": False,
                        "error": {"message": f"Missing required field: {field}"}
                    }), 400
            
            # Parse due_date if provided
            due_date = None
            if data.get('due_date'):
                try:
                    due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
                except ValueError:
                    return jsonify({
                        "success": False,
                        "error": {"message": "Invalid due_date format. Use ISO format."}
                    }), 400
            
            # Set initial status based on creator role
            initial_status = 'pending_approval' if creator_role == 'domain_admin' else 'draft'
            
            # Create survey using repository
            survey = SurveyRepository.create_survey(
                account_id=data.get('account_id'),
                title=data.get('title'),
                survey_type=data.get('survey_type'),
                description=data.get('description'),
                due_date=due_date,
                status=initial_status,
                created_by_role=creator_role
            )
            
            # If created by domain admin, submit for approval
            if creator_role == 'domain_admin':
                survey.submit_for_approval(creator_role)
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict(),
                "message": "Survey created successfully" + (" and submitted for approval" if creator_role == 'domain_admin' else "")
            }), 201
            
        except Exception as e:
            logger.error(f"Failed to create survey: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_survey_by_id(survey_id):
        """
        Get survey by ID
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving survey by ID: {survey_id}")
        
        try:
            survey = SurveyRepository.get_survey_by_id(survey_id)
            
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict()
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_survey(survey_id, data):
        """
        Update survey
        """
        logger = get_logger(__name__)
        logger.info(f"Updating survey {survey_id} with data: {data}")
        
        try:
            survey = SurveyRepository.update_survey(survey_id, data)
            
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict(),
                "message": "Survey updated successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to update survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def delete_survey(survey_id):
        """
        Delete survey
        """
        logger = get_logger(__name__)
        logger.info(f"Deleting survey: {survey_id}")
        
        try:
            success = SurveyRepository.delete_survey(survey_id)
            
            if not success:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "message": f"Survey {survey_id} deleted successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to delete survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_survey_status(survey_id, status):
        """
        Update survey status
        """
        logger = get_logger(__name__)
        logger.info(f"Updating survey {survey_id} status to: {status}")
        
        try:
            survey = SurveyRepository.update_survey_status(survey_id, status)
            
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict(),
                "message": f"Survey status updated to {status}"
            })
            
        except Exception as e:
            logger.error(f"Failed to update survey status {survey_id}: {str(e)}")
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
            # TODO: Implement actual available surveys retrieval
            # This should query surveys that are:
            # - Active status
            # - Assigned to current user as respondent
            # - Not yet completed by current user
            # - Within due date range
            
            surveys = []
            
            return jsonify({
                "success": True,
                "data": surveys
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve available surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_my_surveys():
        """
        Get surveys created by current user
        """
        logger = get_logger(__name__)
        logger.info("Retrieving surveys for current user")
        
        try:
            # Get surveys from database for current user
            # For now, get all surveys since we don't have user context
            result = SurveyRepository.get_all_surveys(
                page=1,
                per_page=100,
                filters=None
            )
            
            # Convert to public dict format
            surveys_data = [survey.to_public_dict() for survey in result['surveys']]
            
            return jsonify({
                "success": True,
                "data": surveys_data
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve my surveys: {str(e)}")
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
            # TODO: Implement actual survey response submission
            # This should:
            # - Validate survey exists and is active
            # - Validate respondent has permission to submit
            # - Store responses in survey_responses collection
            # - Update survey completion status
            # - Send notifications if configured
            
            submission_id = "generated_submission_id"  # This should be generated by database
            
            return jsonify({
                "success": True,
                "data": {"submission_id": submission_id},
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
            # TODO: Implement actual survey responses retrieval
            # This should:
            # - Query survey_responses collection for specific survey
            # - Include respondent information (anonymized if needed)
            # - Support pagination for large response sets
            # - Filter by completion status if needed
            # - Include response timestamps and metadata
            
            responses = []
            
            return jsonify({
                "success": True,
                "data": responses
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve survey responses: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def run_survey(survey_id, data, current_user_id=None, current_account_id=None):
        """
        Run/launch survey with subject and respondents
        """
        logger = get_logger(__name__)
        logger.info(f"Running survey {survey_id} with data: {data}")
        
        try:
            # 1. Validate input data
            errors = SurveysController._validate_run_survey_data(survey_id, data)
            if errors:
                return jsonify({
                    "success": False,
                    "error": {"message": "Validation failed", "details": errors}
                }), 400
            
            # 2. Verify survey exists and is approved
            survey = SurveyRepository.get_survey_by_id(survey_id)
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
                
            if survey.get_field('status') != 'approved':
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey must be approved to run"}
                }), 400
            
            # 3. Parse due date
            due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
            
            # 4. Create survey run record
            survey_run = SurveyRunRepository.create_survey_run(
                survey_id=survey_id,
                subject_id=data['subject_id'],
                respondents=data['respondents'],
                due_date=due_date,
                launched_by=current_user_id or "system",  # TODO: Get from JWT token
                account_id=current_account_id or survey.get_field('account_id')  # TODO: Get from JWT token
            )
            
            # 5. Send email invitations to respondents
            invitation_results = []
            
            # Get subject details for email
            subject = SubjectRepository.get_subject_by_id(data['subject_id'])
            if not subject:
                return jsonify({
                    "success": False,
                    "error": {"message": "Subject not found"}
                }), 404
            
            subject_name = subject.get_field('name')
            survey_title = survey.get_field('title')
            
            for respondent_data in data['respondents']:
                try:
                    # Get respondent details
                    respondent = RespondentRepository.get_respondent_by_id(respondent_data['respondent_id'])
                    if not respondent:
                        invitation_results.append({
                            'respondent_id': respondent_data['respondent_id'],
                            'success': False,
                            'message': 'Respondent not found'
                        })
                        continue
                    
                    # Find the response token for this respondent
                    response_token = None
                    for survey_respondent in survey_run.get_field('respondents', []):
                        if str(survey_respondent['respondent_id']) == str(respondent_data['respondent_id']):
                            response_token = survey_respondent['response_token']
                            break
                    
                    if not response_token:
                        invitation_results.append({
                            'respondent_id': respondent_data['respondent_id'],
                            'success': False,
                            'message': 'Response token not found'
                        })
                        continue
                    
                    # Send email invitation
                    email_result = email_service.send_survey_invitation(
                        survey_run_id=str(survey_run._id),
                        respondent_email=respondent.get_field('email'),
                        respondent_name=respondent.get_field('name'),
                        subject_name=subject_name,
                        survey_title=survey_title,
                        response_token=response_token,
                        due_date=due_date
                    )
                    
                    invitation_results.append({
                        'respondent_id': respondent_data['respondent_id'],
                        'success': email_result['success'],
                        'message': email_result.get('message', 'Email sent'),
                        'email': respondent.get_field('email'),
                        'simulated': email_result.get('simulated', False)
                    })
                    
                except Exception as e:
                    logger.error(f"Failed to send invitation to respondent {respondent_data['respondent_id']}: {str(e)}")
                    invitation_results.append({
                        'respondent_id': respondent_data['respondent_id'],
                        'success': False,
                        'message': f'Failed to send invitation: {str(e)}'
                    })
            
            # 6. Return success response
            return jsonify({
                "success": True,
                "data": {
                    "survey_run_id": str(survey_run._id),
                    "survey_id": str(survey_id),
                    "subject_id": str(data['subject_id']),
                    "respondent_count": len(data['respondents']),
                    "total_weight": 100,
                    "status": "active",
                    "launched_at": survey_run.get_field('launched_at').isoformat() + "Z",
                    "due_date": due_date.isoformat() + "Z",
                    "invitations_sent": len([r for r in invitation_results if r['success']]),
                    "expected_responses": len(data['respondents'])
                },
                "message": f"Survey launched successfully for subject with {len(data['respondents'])} respondents"
            }), 201
            
        except ValueError as e:
            logger.error(f"Validation error running survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": str(e)}
            }), 400
            
        except Exception as e:
            logger.error(f"Failed to run survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to run survey: {str(e)}"}
            }), 500
    
    @staticmethod
    def _validate_run_survey_data(survey_id, data):
        """Validate survey run data with business rules"""
        errors = []
        
        # 1. Required fields validation
        if not data.get('subject_id'):
            errors.append("Subject ID is required")
        
        if not data.get('due_date'):
            errors.append("Due date is required")
        
        respondents = data.get('respondents', [])
        if not respondents:
            errors.append("At least one respondent is required")
        
        # 2. Weight sum validation (must equal 100)
        total_weight = sum(r.get('weight', 0) for r in respondents)
        if total_weight != 100:
            errors.append(f"Respondent weights must sum to 100, got {total_weight}")
        
        # 3. Respondent data validation
        for i, respondent in enumerate(respondents):
            if not respondent.get('respondent_id'):
                errors.append(f"Respondent {i+1}: respondent_id is required")
            if not respondent.get('weight'):
                errors.append(f"Respondent {i+1}: weight is required")
            if respondent.get('weight', 0) <= 0:
                errors.append(f"Respondent {i+1}: weight must be greater than 0")
        
        # 4. Due date validation
        try:
            due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
            if due_date <= datetime.utcnow():
                errors.append("Due date must be in the future")
        except (ValueError, KeyError):
            errors.append("Invalid due date format. Use ISO format.")
        
        # 5. CRITICAL: Check for duplicate survey+subject combination
        try:
            existing_run = SurveyRunRepository.find_active_run(
                survey_id=survey_id,
                subject_id=data.get('subject_id')
            )
            if existing_run:
                errors.append(f"Survey is already running for this subject. Existing run ID: {existing_run._id}")
        except Exception as e:
            errors.append(f"Error checking for duplicate runs: {str(e)}")
        
        return errors
    
    @staticmethod
    @log_function_call
    def approve_survey(survey_id, approver_id):
        """
        Approve survey (System Admin only)
        """
        logger = get_logger(__name__)
        logger.info(f"Approving survey {survey_id} by approver {approver_id}")
        
        try:
            survey = SurveyRepository.get_survey_by_id(survey_id)
            
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            if survey.get_field('status') != 'pending_approval':
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey is not pending approval"}
                }), 400
            
            # Approve the survey
            survey.approve(approver_id)
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict(),
                "message": "Survey approved successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to approve survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to approve survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def reject_survey(survey_id, approver_id, reason=None):
        """
        Reject survey (System Admin only)
        """
        logger = get_logger(__name__)
        logger.info(f"Rejecting survey {survey_id} by approver {approver_id}, reason: {reason}")
        
        try:
            survey = SurveyRepository.get_survey_by_id(survey_id)
            
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            if survey.get_field('status') != 'pending_approval':
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey is not pending approval"}
                }), 400
            
            # Reject the survey
            survey.reject(approver_id, reason)
            
            return jsonify({
                "success": True,
                "data": survey.to_public_dict(),
                "message": "Survey rejected successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to reject survey {survey_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to reject survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_pending_surveys(page=1, limit=20):
        """
        Get surveys pending approval (System Admin only)
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving pending surveys - page: {page}, limit: {limit}")
        
        try:
            filters = {'status': 'pending_approval'}
            result = SurveyRepository.get_all_surveys(
                page=page,
                per_page=limit,
                filters=filters
            )
            
            return jsonify({
                "success": True,
                "data": result['surveys'],
                "pagination": result['pagination']
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve pending surveys: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve pending surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_approved_surveys(page=1, limit=20):
        """
        Get approved surveys (Account users)
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving approved surveys - page: {page}, limit: {limit}")
        
        try:
            filters = {'status': 'approved'}
            result = SurveyRepository.get_all_surveys(
                page=page,
                per_page=limit,
                filters=filters
            )
            
            return jsonify({
                "success": True,
                "data": result['surveys'],
                "pagination": result['pagination']
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve approved surveys: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve approved surveys: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_surveys_by_role(user_role, page=1, limit=20):
        """
        Get surveys filtered by user role
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving surveys for role: {user_role} - page: {page}, limit: {limit}")
        
        try:
            if user_role == 'account':
                # Only approved surveys
                filters = {'status': 'approved'}
            elif user_role in ['domain_admin', 'sys_admin']:
                # All surveys
                filters = None
            else:
                return jsonify({
                    "success": False,
                    "error": {"message": "Invalid user role"}
                }), 400
            
            result = SurveyRepository.get_all_surveys(
                page=page,
                per_page=limit,
                filters=filters
            )
            
            return jsonify({
                "success": True,
                "data": result['surveys'],
                "pagination": result['pagination']
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve surveys by role {user_role}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve surveys by role: {str(e)}"}
            }), 500
