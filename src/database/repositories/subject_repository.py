"""
Subject Repository
Handles database operations for Subject model
"""

from database.models.subject_model import Subject
from utils.logger import get_logger

logger = get_logger(__name__)

class SubjectRepository:
    """Repository for Subject database operations"""
    
    @staticmethod
    def create_subject(account_id, name, email=None, position=None, department=None, **kwargs):
        """Create a new subject"""
        try:
            return Subject.create_subject(
                account_id=account_id,
                name=name,
                email=email,
                position=position,
                department=department,
                **kwargs
            )
        except Exception as e:
            logger.error(f"Failed to create subject: {str(e)}")
            raise
    
    @staticmethod
    def get_subject_by_id(subject_id):
        """Get subject by ID"""
        try:
            return Subject.find_by_id(subject_id)
        except Exception as e:
            logger.error(f"Failed to get subject by ID {subject_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_subjects_by_account(account_id, active_only=True):
        """Get subjects by account ID"""
        try:
            return Subject.find_by_account(account_id, active_only=active_only)
        except Exception as e:
            logger.error(f"Failed to get subjects for account {account_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_all_subjects(page=1, per_page=20, filters=None):
        """Get all subjects with pagination and filtering"""
        try:
            query = {}
            
            # Apply filters
            if filters:
                if filters.get('search'):
                    search_term = filters['search']
                    query['$or'] = [
                        {'name': {'$regex': search_term, '$options': 'i'}},
                        {'email': {'$regex': search_term, '$options': 'i'}},
                        {'position': {'$regex': search_term, '$options': 'i'}},
                        {'department': {'$regex': search_term, '$options': 'i'}}
                    ]
                
                if filters.get('account_id'):
                    query['account_id'] = filters['account_id']
                
                if filters.get('department'):
                    query['department'] = filters['department']
                
                if filters.get('status'):
                    query['status'] = filters['status']
                
                if filters.get('is_active') is not None:
                    query['is_active'] = filters['is_active']
            
            # Get paginated results
            result = Subject.paginate(
                query=query,
                page=page,
                per_page=per_page,
                sort=[('created_at', -1)]
            )
            
            # Convert subjects to dictionaries
            subjects_data = [subject.to_public_dict() for subject in result['documents']]
            
            return {
                'subjects': subjects_data,
                'pagination': result['pagination']
            }
            
        except Exception as e:
            logger.error(f"Failed to get subjects: {str(e)}")
            raise
    
    @staticmethod
    def update_subject(subject_id, update_data):
        """Update subject information"""
        try:
            subject = Subject.find_by_id(subject_id)
            if not subject:
                raise ValueError(f"Subject not found: {subject_id}")
            
            # Update fields
            subject.update_fields(**update_data)
            subject.save()
            
            return subject
            
        except Exception as e:
            logger.error(f"Failed to update subject {subject_id}: {str(e)}")
            raise
    
    @staticmethod
    def update_subject_status(subject_id, status):
        """Update subject status"""
        try:
            subject = Subject.find_by_id(subject_id)
            if not subject:
                raise ValueError(f"Subject not found: {subject_id}")
            
            if status == 'active':
                subject.activate()
            else:
                subject.deactivate()
            
            return subject
            
        except Exception as e:
            logger.error(f"Failed to update subject status {subject_id}: {str(e)}")
            raise
    
    @staticmethod
    def delete_subject(subject_id):
        """Delete subject (soft delete)"""
        try:
            subject = Subject.find_by_id(subject_id)
            if not subject:
                raise ValueError(f"Subject not found: {subject_id}")
            
            # Soft delete
            subject.soft_delete()
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete subject {subject_id}: {str(e)}")
            raise
    
    @staticmethod
    def search_subjects(search_term, account_id=None, active_only=True):
        """Search subjects by name, email, position, or department"""
        try:
            return Subject.search_subjects(
                search_term=search_term,
                account_id=account_id,
                active_only=active_only
            )
        except Exception as e:
            logger.error(f"Failed to search subjects: {str(e)}")
            raise
    
    @staticmethod
    def get_subjects_by_department(department, account_id=None, active_only=True):
        """Get subjects by department"""
        try:
            return Subject.get_subjects_by_department(
                department=department,
                account_id=account_id,
                active_only=active_only
            )
        except Exception as e:
            logger.error(f"Failed to get subjects by department {department}: {str(e)}")
            raise
    
    @staticmethod
    def get_subject_statistics(account_id=None):
        """Get subject statistics"""
        try:
            return Subject.get_subject_statistics(account_id=account_id)
        except Exception as e:
            logger.error(f"Failed to get subject statistics: {str(e)}")
            raise
    
    @staticmethod
    def increment_surveys_count(subject_id):
        """Increment subject's surveys count"""
        try:
            subject = Subject.find_by_id(subject_id)
            if not subject:
                raise ValueError(f"Subject not found: {subject_id}")
            
            subject.increment_surveys_count()
            return subject
            
        except Exception as e:
            logger.error(f"Failed to increment surveys count for subject {subject_id}: {str(e)}")
            raise
    
    @staticmethod
    def decrement_surveys_count(subject_id):
        """Decrement subject's surveys count"""
        try:
            subject = Subject.find_by_id(subject_id)
            if not subject:
                raise ValueError(f"Subject not found: {subject_id}")
            
            subject.decrement_surveys_count()
            return subject
            
        except Exception as e:
            logger.error(f"Failed to decrement surveys count for subject {subject_id}: {str(e)}")
            raise
