"""
Email Service for sending survey invitations and notifications
Uses SendGrid for email delivery
"""

import os
from datetime import datetime
from utils.logger import get_logger

logger = get_logger(__name__)

class EmailService:
    """Email service for survey notifications"""
    
    def __init__(self):
        """Initialize email service with SendGrid configuration"""
        self.sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
        self.from_email = os.getenv('FROM_EMAIL', 'noreply@ikenei.com')
        self.from_name = os.getenv('FROM_NAME', 'IkeNei Survey System')
        self.base_url = os.getenv('BASE_URL', 'http://localhost:3000')
        
        # Check if SendGrid is configured
        if not self.sendgrid_api_key:
            logger.warning("SENDGRID_API_KEY not configured. Email sending will be simulated.")
            self.sendgrid_enabled = False
        else:
            self.sendgrid_enabled = True
            try:
                # Import SendGrid only if API key is available
                import sendgrid
                from sendgrid.helpers.mail import Mail, Email, To, Content
                self.sg = sendgrid.SendGridAPIClient(api_key=self.sendgrid_api_key)
                self.Mail = Mail
                self.Email = Email
                self.To = To
                self.Content = Content
                logger.info("SendGrid email service initialized successfully")
            except ImportError:
                logger.error("SendGrid library not installed. Run: pip install sendgrid")
                self.sendgrid_enabled = False
            except Exception as e:
                logger.error(f"Failed to initialize SendGrid: {str(e)}")
                self.sendgrid_enabled = False
    
    def send_survey_invitation(self, survey_run_id, respondent_email, respondent_name, subject_name, survey_title, response_token, due_date):
        """Send survey invitation email to respondent"""
        try:
            # Generate survey link
            survey_link = f"{self.base_url}/survey/respond/{response_token}"
            
            # Format due date
            if isinstance(due_date, str):
                due_date_formatted = due_date
            else:
                due_date_formatted = due_date.strftime("%B %d, %Y at %I:%M %p")
            
            # Create email content
            subject = f"Survey Invitation: Feedback for {subject_name}"
            
            html_content = self._create_invitation_html(
                respondent_name=respondent_name,
                subject_name=subject_name,
                survey_title=survey_title,
                survey_link=survey_link,
                due_date=due_date_formatted
            )
            
            text_content = self._create_invitation_text(
                respondent_name=respondent_name,
                subject_name=subject_name,
                survey_title=survey_title,
                survey_link=survey_link,
                due_date=due_date_formatted
            )
            
            # Send email
            result = self._send_email(
                to_email=respondent_email,
                to_name=respondent_name,
                subject=subject,
                html_content=html_content,
                text_content=text_content
            )
            
            logger.info(f"Survey invitation sent to {respondent_email} for survey run {survey_run_id}")
            return result
            
        except Exception as e:
            logger.error(f"Failed to send survey invitation to {respondent_email}: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'email': respondent_email
            }
    
    def send_completion_confirmation(self, respondent_email, respondent_name, subject_name, survey_title):
        """Send survey completion confirmation email"""
        try:
            subject = f"Thank you for your feedback on {subject_name}"
            
            html_content = self._create_completion_html(
                respondent_name=respondent_name,
                subject_name=subject_name,
                survey_title=survey_title
            )
            
            text_content = self._create_completion_text(
                respondent_name=respondent_name,
                subject_name=subject_name,
                survey_title=survey_title
            )
            
            result = self._send_email(
                to_email=respondent_email,
                to_name=respondent_name,
                subject=subject,
                html_content=html_content,
                text_content=text_content
            )
            
            logger.info(f"Completion confirmation sent to {respondent_email}")
            return result
            
        except Exception as e:
            logger.error(f"Failed to send completion confirmation to {respondent_email}: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'email': respondent_email
            }
    
    def _send_email(self, to_email, to_name, subject, html_content, text_content):
        """Send email using SendGrid or simulate if not configured"""
        try:
            if not self.sendgrid_enabled:
                # Simulate email sending for development
                logger.info(f"SIMULATED EMAIL SEND:")
                logger.info(f"  To: {to_name} <{to_email}>")
                logger.info(f"  Subject: {subject}")
                logger.info(f"  Content: {text_content[:100]}...")
                
                return {
                    'success': True,
                    'message': 'Email simulated (SendGrid not configured)',
                    'email': to_email,
                    'simulated': True
                }
            
            # Create SendGrid email
            from_email = self.Email(self.from_email, self.from_name)
            to_email_obj = self.To(to_email, to_name)
            
            mail = self.Mail(
                from_email=from_email,
                to_emails=to_email_obj,
                subject=subject,
                html_content=html_content,
                plain_text_content=text_content
            )
            
            # Send email
            response = self.sg.send(mail)
            
            if response.status_code in [200, 201, 202]:
                return {
                    'success': True,
                    'message': 'Email sent successfully',
                    'email': to_email,
                    'status_code': response.status_code
                }
            else:
                return {
                    'success': False,
                    'error': f'SendGrid returned status code: {response.status_code}',
                    'email': to_email,
                    'status_code': response.status_code
                }
                
        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'email': to_email
            }
    
    def _create_invitation_html(self, respondent_name, subject_name, survey_title, survey_link, due_date):
        """Create HTML content for survey invitation"""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Survey Invitation</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background-color: #007bff; color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 20px; background-color: #f9f9f9; }}
                .button {{ 
                    display: inline-block; 
                    background-color: #007bff; 
                    color: white; 
                    padding: 12px 24px; 
                    text-decoration: none; 
                    border-radius: 5px; 
                    margin: 20px 0;
                }}
                .footer {{ padding: 20px; text-align: center; font-size: 12px; color: #666; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>360-Degree Feedback Survey</h1>
                </div>
                <div class="content">
                    <p>Hello {respondent_name},</p>
                    
                    <p>You have been invited to provide feedback for <strong>{subject_name}</strong> as part of our 360-degree feedback process.</p>
                    
                    <p><strong>Survey:</strong> {survey_title}</p>
                    <p><strong>Due Date:</strong> {due_date}</p>
                    
                    <p>Your feedback is valuable and will help {subject_name} in their professional development. The survey should take approximately 5-10 minutes to complete.</p>
                    
                    <p>Please click the button below to complete the survey:</p>
                    
                    <p style="text-align: center;">
                        <a href="{survey_link}" class="button">Complete Survey</a>
                    </p>
                    
                    <p>If the button doesn't work, you can copy and paste this link into your browser:</p>
                    <p style="word-break: break-all; background-color: #eee; padding: 10px;">{survey_link}</p>
                    
                    <p>Thank you for your participation!</p>
                </div>
                <div class="footer">
                    <p>This is an automated message from the IkeNei Survey System.</p>
                    <p>Please do not reply to this email.</p>
                </div>
            </div>
        </body>
        </html>
        """
    
    def _create_invitation_text(self, respondent_name, subject_name, survey_title, survey_link, due_date):
        """Create plain text content for survey invitation"""
        return f"""
360-Degree Feedback Survey

Hello {respondent_name},

You have been invited to provide feedback for {subject_name} as part of our 360-degree feedback process.

Survey: {survey_title}
Due Date: {due_date}

Your feedback is valuable and will help {subject_name} in their professional development. The survey should take approximately 5-10 minutes to complete.

Please click the link below to complete the survey:
{survey_link}

Thank you for your participation!

---
This is an automated message from the IkeNei Survey System.
Please do not reply to this email.
        """
    
    def _create_completion_html(self, respondent_name, subject_name, survey_title):
        """Create HTML content for completion confirmation"""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Survey Completed</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background-color: #28a745; color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 20px; background-color: #f9f9f9; }}
                .footer {{ padding: 20px; text-align: center; font-size: 12px; color: #666; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Survey Completed Successfully</h1>
                </div>
                <div class="content">
                    <p>Hello {respondent_name},</p>
                    
                    <p>Thank you for completing the feedback survey for <strong>{subject_name}</strong>.</p>
                    
                    <p><strong>Survey:</strong> {survey_title}</p>
                    
                    <p>Your feedback has been successfully submitted and will contribute to {subject_name}'s professional development.</p>
                    
                    <p>We appreciate the time you took to provide thoughtful feedback.</p>
                </div>
                <div class="footer">
                    <p>This is an automated message from the IkeNei Survey System.</p>
                    <p>Please do not reply to this email.</p>
                </div>
            </div>
        </body>
        </html>
        """
    
    def _create_completion_text(self, respondent_name, subject_name, survey_title):
        """Create plain text content for completion confirmation"""
        return f"""
Survey Completed Successfully

Hello {respondent_name},

Thank you for completing the feedback survey for {subject_name}.

Survey: {survey_title}

Your feedback has been successfully submitted and will contribute to {subject_name}'s professional development.

We appreciate the time you took to provide thoughtful feedback.

---
This is an automated message from the IkeNei Survey System.
Please do not reply to this email.
        """
    
    def test_email_configuration(self):
        """Test email configuration"""
        try:
            if not self.sendgrid_enabled:
                return {
                    'success': False,
                    'message': 'SendGrid not configured. Set SENDGRID_API_KEY environment variable.',
                    'configured': False
                }
            
            # Test SendGrid connection
            response = self.sg.client.mail.send.post(request_body={
                'personalizations': [{'to': [{'email': 'test@example.com'}]}],
                'from': {'email': self.from_email},
                'subject': 'Test',
                'content': [{'type': 'text/plain', 'value': 'Test'}]
            })
            
            return {
                'success': True,
                'message': 'SendGrid configuration is valid',
                'configured': True,
                'from_email': self.from_email,
                'from_name': self.from_name
            }
            
        except Exception as e:
            return {
                'success': False,
                'message': f'SendGrid configuration error: {str(e)}',
                'configured': False
            }

# Global email service instance
email_service = EmailService()
