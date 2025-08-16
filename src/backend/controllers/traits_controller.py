from flask import jsonify
from datetime import datetime
from database import TraitRepository
from utils.logger import get_logger, log_function_call

class TraitsController:
    """
    Controller for traits management
    """
    
    @staticmethod
    @log_function_call
    def get_all_traits(page=1, limit=20, filters=None):
        """
        Get all traits with pagination and filtering
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving traits - page: {page}, limit: {limit}, filters: {filters}")
        
        try:
            result = TraitRepository.get_all_traits(
                page=page,
                per_page=limit,
                filters=filters
            )
            
            return jsonify({
                "success": True,
                "data": result['traits'],
                "pagination": result['pagination']
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve traits: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve traits: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def create_trait(data):
        """
        Create a new trait
        """
        logger = get_logger(__name__)
        logger.info(f"Creating new trait with data: {data}")
        
        try:
            # Validate required fields
            required_fields = ['name', 'category']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        "success": False,
                        "error": {"message": f"Missing required field: {field}"}
                    }), 400
            
            # Create trait using repository
            trait = TraitRepository.create_trait(
                name=data.get('name'),
                category=data.get('category'),
                description=data.get('description')
            )
            
            return jsonify({
                "success": True,
                "data": trait.to_public_dict(),
                "message": "Trait created successfully"
            }), 201
            
        except Exception as e:
            logger.error(f"Failed to create trait: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create trait: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_trait_by_id(trait_id):
        """
        Get trait by ID
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving trait by ID: {trait_id}")
        
        try:
            trait = TraitRepository.get_trait_by_id(trait_id)
            
            if not trait:
                return jsonify({
                    "success": False,
                    "error": {"message": "Trait not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": trait.to_public_dict()
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve trait {trait_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve trait: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_trait(trait_id, data):
        """
        Update trait
        """
        logger = get_logger(__name__)
        logger.info(f"Updating trait {trait_id} with data: {data}")
        
        try:
            trait = TraitRepository.update_trait(trait_id, data)
            
            if not trait:
                return jsonify({
                    "success": False,
                    "error": {"message": "Trait not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": trait.to_public_dict(),
                "message": "Trait updated successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to update trait {trait_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update trait: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def delete_trait(trait_id):
        """
        Delete trait
        """
        logger = get_logger(__name__)
        logger.info(f"Deleting trait: {trait_id}")
        
        try:
            success = TraitRepository.delete_trait(trait_id)
            
            if not success:
                return jsonify({
                    "success": False,
                    "error": {"message": "Trait not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "message": f"Trait {trait_id} deleted successfully"
            })
            
        except Exception as e:
            logger.error(f"Failed to delete trait {trait_id}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete trait: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_trait_categories():
        """
        Get all trait categories
        """
        logger = get_logger(__name__)
        logger.info("Retrieving trait categories")
        
        try:
            categories = TraitRepository.get_trait_categories()
            
            return jsonify({
                "success": True,
                "data": categories
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve trait categories: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve trait categories: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_traits_by_category(category):
        """
        Get traits by category
        """
        logger = get_logger(__name__)
        logger.info(f"Retrieving traits for category: {category}")
        
        try:
            traits = TraitRepository.get_traits_by_category(category)
            traits_data = [trait.to_public_dict() for trait in traits]
            
            return jsonify({
                "success": True,
                "data": traits_data
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve traits for category {category}: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve traits for category: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def update_trait_status(trait_id, status):
        """
        Update trait status
        """
        logger = get_logger(__name__)
        logger.info(f"Updating trait {trait_id} status to {status}")
        
        try:
            trait = TraitRepository.update_trait(trait_id, {"status": status})
            
            if not trait:
                return jsonify({
                    "success": False,
                    "error": {"message": "Trait not found"}
                }), 404
            
            return jsonify({
                "success": True,
                "data": trait.to_public_dict(),
                "message": f"Trait status updated to {status}"
            })
            
        except Exception as e:
            logger.error(f"Failed to update trait {trait_id} status: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update trait status: {str(e)}"}
            }), 500
    
    @staticmethod
    @log_function_call
    def get_trait_usage_statistics():
        """
        Get trait usage statistics
        """
        logger = get_logger(__name__)
        logger.info("Retrieving trait usage statistics")
        
        try:
            # TODO: Implement actual trait usage statistics calculation
            # This should use aggregation pipeline to calculate:
            # - Total traits count from traits collection
            # - Active traits count (status = 'active')
            # - Categories count (distinct categories)
            # - Most used traits (from survey responses or usage tracking)
            # - Category distribution (traits per category)
            
            stats = {
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": stats
            })
            
        except Exception as e:
            logger.error(f"Failed to retrieve trait usage statistics: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve trait usage statistics: {str(e)}"}
            }), 500
