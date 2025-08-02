from bson import ObjectId
from database.connection import get_db
from database.models.respondent_model import RespondentModel
from utils.logger import get_logger

class RespondentRepository:
    """
    Repository for respondent data operations
    """
    
    @staticmethod
    def get_collection():
        """Get the respondents collection"""
        db = get_db()
        return db[RespondentModel.get_collection_name()]
    
    @staticmethod
    def create_respondent(subject_id, name, email, phone=None, address=None, 
                         relationship=None, other_info=None):
        """
        Create a new respondent
        """
        logger = get_logger(__name__)
        
        try:
            # Create respondent instance
            respondent = RespondentModel(
                subject_id=subject_id,
                name=name,
                email=email,
                phone=phone,
                address=address,
                relationship=relationship,
                other_info=other_info
            )
            
            # Validate the respondent
            validation_errors = respondent.validate()
            if validation_errors:
                raise ValueError(f"Validation failed: {', '.join(validation_errors)}")
            
            # Insert into database
            collection = RespondentRepository.get_collection()
            result = collection.insert_one(respondent.to_dict())
            
            # Retrieve the created respondent
            created_respondent = collection.find_one({'_id': result.inserted_id})
            
            logger.info(f"Created respondent: {created_respondent['name']} ({created_respondent['email']})")
            return RespondentModel.from_dict(created_respondent)
            
        except Exception as e:
            logger.error(f"Failed to create respondent: {str(e)}")
            raise
    
    @staticmethod
    def get_respondent_by_id(respondent_id):
        """
        Get respondent by ID
        """
        logger = get_logger(__name__)
        
        try:
            collection = RespondentRepository.get_collection()
            respondent_data = collection.find_one({'_id': ObjectId(respondent_id)})
            
            if respondent_data:
                logger.info(f"Retrieved respondent: {respondent_id}")
                return RespondentModel.from_dict(respondent_data)
            else:
                logger.warning(f"Respondent not found: {respondent_id}")
                return None
                
        except Exception as e:
            logger.error(f"Failed to retrieve respondent {respondent_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_all_respondents(page=1, per_page=20, subject_id=None):
        """
        Get all respondents with pagination
        """
        logger = get_logger(__name__)
        
        try:
            collection = RespondentRepository.get_collection()
            
            # Build query
            query = {}
            if subject_id:
                query['subject_id'] = ObjectId(subject_id)
            
            # Calculate pagination
            skip = (page - 1) * per_page
            
            # Get respondents
            cursor = collection.find(query).skip(skip).limit(per_page).sort('created_at', -1)
            respondents = [RespondentModel.from_dict(doc) for doc in cursor]
            
            # Get total count
            total_count = collection.count_documents(query)
            
            logger.info(f"Retrieved {len(respondents)} respondents (page {page}, total: {total_count})")
            
            return {
                'respondents': respondents,
                'pagination': {
                    'page': page,
                    'per_page': per_page,
                    'total': total_count,
                    'pages': (total_count + per_page - 1) // per_page
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to retrieve respondents: {str(e)}")
            raise
    
    @staticmethod
    def update_respondent(respondent_id, update_data):
        """
        Update respondent
        """
        logger = get_logger(__name__)
        
        try:
            collection = RespondentRepository.get_collection()
            
            # Add updated_at timestamp
            from datetime import datetime
            update_data['updated_at'] = datetime.utcnow()
            
            # Update the respondent
            result = collection.update_one(
                {'_id': ObjectId(respondent_id)},
                {'$set': update_data}
            )
            
            if result.matched_count == 0:
                logger.warning(f"Respondent not found for update: {respondent_id}")
                return None
            
            # Retrieve updated respondent
            updated_respondent = collection.find_one({'_id': ObjectId(respondent_id)})
            
            logger.info(f"Updated respondent: {respondent_id}")
            return RespondentModel.from_dict(updated_respondent)
            
        except Exception as e:
            logger.error(f"Failed to update respondent {respondent_id}: {str(e)}")
            raise
    
    @staticmethod
    def delete_respondent(respondent_id):
        """
        Delete respondent
        """
        logger = get_logger(__name__)
        
        try:
            collection = RespondentRepository.get_collection()
            result = collection.delete_one({'_id': ObjectId(respondent_id)})
            
            if result.deleted_count == 0:
                logger.warning(f"Respondent not found for deletion: {respondent_id}")
                return False
            
            logger.info(f"Deleted respondent: {respondent_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete respondent {respondent_id}: {str(e)}")
            raise
    
    @staticmethod
    def get_respondents_by_subject(subject_id):
        """
        Get all respondents for a specific subject
        """
        logger = get_logger(__name__)
        
        try:
            collection = RespondentRepository.get_collection()
            cursor = collection.find({'subject_id': ObjectId(subject_id)}).sort('created_at', -1)
            respondents = [RespondentModel.from_dict(doc) for doc in cursor]
            
            logger.info(f"Retrieved {len(respondents)} respondents for subject: {subject_id}")
            return respondents
            
        except Exception as e:
            logger.error(f"Failed to retrieve respondents for subject {subject_id}: {str(e)}")
            raise
