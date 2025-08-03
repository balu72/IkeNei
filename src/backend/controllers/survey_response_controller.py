"""
Survey Response Controller
Handles public survey response submission (no authentication required)
"""

from flask import jsonify
from datetime import datetime
from database.repositories.survey_response_repository import SurveyResponseRepository
from database.repositories.survey_run_repository import SurveyRunRepository
from database.repositories.survey_repository import SurveyRepository
from database.repositories.subject_repository import SubjectRepository
from database.repositories.respondent_repository import RespondentRepository
from services.email_service import email_service
from utils.logger import get_logger, log_function_call

logger = get_logger(__name__)

class SurveyResponseController:
    """Controller for survey response management"""
    
    @staticmethod
    @log_function_call
    def get_survey_by_token(response_token):
        """Get survey form by response token (public endpoint)"""
        logger.info(f"Loading survey form for token: {response_token[:8]}...")
        
        try:
            # Check if response already exists for this token
            existing_response = SurveyResponseRepository.get_response_by_token(response_token)
            if existing_response:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey has already been completed with this link"}
                }), 400
            
            # Find survey run by token
            survey_run, respondent = SurveyRunRepository.get_respondent_by_token(response_token)
            
            if not survey_run or not respondent:
                return jsonify({
                    "success": False,
                    "error": {"message": "Invalid or expired survey link"}
                }), 404
            
            # Check if survey run is still active
            if survey_run.get_field('status') != 'active':
                return jsonify({
                    "success": False,
                    "error": {"message": "This survey is no longer active"}
                }), 400
            
            # Check if survey run is overdue
            if survey_run.is_overdue():
                return jsonify({
                    "success": False,
                    "error": {"message": "This survey has expired"}
                }), 400
            
            # Get survey details
            survey = SurveyRepository.get_survey_by_id(survey_run.get_field('survey_id'))
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            # Get subject details
            subject = SubjectRepository.get_subject_by_id(survey_run.get_field('subject_id'))
            if not subject:
                return jsonify({
                    "success": False,
                    "error": {"message": "Subject not found"}
                }), 404
            
            # Get respondent details
            respondent_details = RespondentRepository.get_respondent_by_id(respondent['respondent_id'])
            if not respondent_details:
                return jsonify({
                    "success": False,
                    "error": {"message": "Respondent not found"}
                }), 404
            
            # Return survey form data
            return jsonify({
                "success": True,
                "data": {
                    "survey_run_id": str(survey_run._id),
                    "survey": {
                        "id": str(survey._id),
                        "title": survey.get_field('title'),
                        "description": survey.get_field('description'),
                        "questions": survey.get_field('questions', [])
                    },
                    "subject": {
                        "id": str(subject._id),
                        "name": subject.get_field('name'),
                        "email": subject.get_field('email')
                    },
                    "respondent": {
                        "relationship": respondent.get('relationship'),
                        "weight": respondent.get('weight')
                    },
                    "due_date": survey_run.get_field('due_date').isoformat() + 'Z' if survey_run.get_field('due_date') else None,
                    "days_until_due": survey_run.days_until_due()
                }
            })
            
        except Exception as e:
            logger.error(f"Failed to load survey form for token {response_token[:8]}...: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to load survey: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def submit_survey_response(response_token, data):
        """Submit survey response (public endpoint)"""
        logger.info(f"Submitting survey response for token: {response_token[:8]}...")
        
        try:
            # Check if response already exists for this token
            existing_response = SurveyResponseRepository.get_response_by_token(response_token)
            if existing_response:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey has already been completed with this link"}
                }), 400
            
            # Find survey run by token
            survey_run, respondent = SurveyRunRepository.get_respondent_by_token(response_token)
            
            if not survey_run or not respondent:
                return jsonify({
                    "success": False,
                    "error": {"message": "Invalid or expired survey link"}
                }), 404
            
            # Check if survey run is still active
            if survey_run.get_field('status') != 'active':
                return jsonify({
                    "success": False,
                    "error": {"message": "This survey is no longer active"}
                }), 400
            
            # Check if survey run is overdue
            if survey_run.is_overdue():
                return jsonify({
                    "success": False,
                    "error": {"message": "This survey has expired"}
                }), 400
            
            # Validate request data
            if not data or not data.get('responses'):
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey responses are required"}
                }), 400
            
            responses = data.get('responses')
            
            # Get survey to validate questions
            survey = SurveyRepository.get_survey_by_id(survey_run.get_field('survey_id'))
            if not survey:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey not found"}
                }), 404
            
            # Get required question IDs
            questions = survey.get_field('questions', [])
            required_questions = [q['id'] for q in questions if q.get('required', True)]
            
            # Validate response data
            validation_errors = SurveyResponseRepository.validate_response_data(responses, required_questions)
            if validation_errors:
                return jsonify({
                    "success": False,
                    "error": {"message": "Validation failed", "details": validation_errors}
                }), 400
            
            # Create survey response
            survey_response = SurveyResponseRepository.create_response(
                survey_run_id=survey_run._id,
                survey_id=survey_run.get_field('survey_id'),
                respondent_id=respondent['respondent_id'],
                response_token=response_token,
                responses=responses
            )
            
            # Update survey run respondent status
            SurveyRunRepository.update_respondent_status(
                survey_run_id=survey_run._id,
                respondent_id=respondent['respondent_id'],
                status='completed'
            )
            
            # Send completion confirmation email
            try:
                # Get respondent and subject details for email
                respondent_details = RespondentRepository.get_respondent_by_id(respondent['respondent_id'])
                subject_details = SubjectRepository.get_subject_by_id(survey_run.get_field('subject_id'))
                
                if respondent_details and subject_details:
                    email_service.send_completion_confirmation(
                        respondent_email=respondent_details.get_field('email'),
                        respondent_name=respondent_details.get_field('name'),
                        subject_name=subject_details.get_field('name'),
                        survey_title=survey.get_field('title')
                    )
            except Exception as e:
                logger.warning(f"Failed to send completion confirmation email: {str(e)}")
                # Don't fail the response submission if email fails
            
            return jsonify({
                "success": True,
                "data": {
                    "response_id": str(survey_response._id),
                    "survey_run_id": str(survey_run._id),
                    "submitted_at": survey_response.get_field('submitted_at').isoformat() + 'Z',
                    "response_summary": survey_response.get_response_summary()
                },
                "message": "Survey response submitted successfully. Thank you for your feedback!"
            }), 201
            
        except ValueError as e:
            logger.error(f"Validation error submitting response for token {response_token[:8]}...: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": str(e)}
            }), 400
            
        except Exception as e:
            logger.error(f"Failed to submit survey response for token {response_token[:8]}...: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to submit survey response: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_survey_run_responses(survey_run_id):
        """Get all responses for a survey run (admin endpoint)"""
        logger.info(f"Retrieving responses for survey run: {survey_run_id}")
        
        try:
            # Get survey run
            survey_run = SurveyRunRepository.get_survey_run_by_id(survey_run_id)
            if not survey_run:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey run not found"}
                }), 404
            
            # Get all responses
            responses = SurveyResponseRepository.get_responses_by_survey_run(survey_run_id)
            
            # Get response statistics
            statistics = SurveyResponseRepository.get_response_statistics(survey_run_id=survey_run_id)
            
            # Get completion summary
            completion_summary = SurveyResponseRepository.get_completion_summary(survey_run_id)
            
            return jsonify({
                "success": True,
                "data": {
                    "survey_run": survey_run.to_public_dict(),
                    "responses": [response.to_public_dict() for response in responses],
                    "statistics": statistics,
                    "completion_summary": completion_summary
                }
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve responses for survey run {survey_run_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve responses: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_survey_run_analytics(survey_run_id):
        """Get analytics for a survey run (admin endpoint)"""
        logger.info(f"Retrieving analytics for survey run: {survey_run_id}")
        
        try:
            # Get survey run
            survey_run = SurveyRunRepository.get_survey_run_by_id(survey_run_id)
            if not survey_run:
                return jsonify({
                    "success": False,
                    "error": {"message": "Survey run not found"}
                }), 404
            
            # Get average ratings by question
            average_ratings = SurveyResponseRepository.get_average_ratings_by_survey_run(survey_run_id)
            
            # Get completion summary
            completion_summary = SurveyResponseRepository.get_completion_summary(survey_run_id)
            
            # Get survey details for question context
            survey = SurveyRepository.get_survey_by_id(survey_run.get_field('survey_id'))
            questions = survey.get_field('questions', []) if survey else []
            
            # Combine question text with ratings
            question_analytics = []
            for question in questions:
                question_id = question['id']
                if question_id in average_ratings:
                    question_analytics.append({
                        'question_id': question_id,
                        'question_text': question['text'],
                        'question_type': question['type'],
                        **average_ratings[question_id]
                    })
            
            return jsonify({
                "success": True,
                "data": {
                    "survey_run": survey_run.to_public_dict(),
                    "question_analytics": question_analytics,
                    "completion_summary": completion_summary,
                    "response_rate": {
                        "expected_responses": len(survey_run.get_field('respondents', [])),
                        "actual_responses": completion_summary['total_responses'],
                        "completion_percentage": round(
                            (completion_summary['total_responses'] / len(survey_run.get_field('respondents', [])) * 100)
                            if survey_run.get_field('respondents') else 0, 2
                        )
                    }
                }
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve analytics for survey run {survey_run_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve analytics: {str(e)}"}
            }), 500
