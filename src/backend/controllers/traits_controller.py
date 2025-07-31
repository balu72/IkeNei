from flask import jsonify
from datetime import datetime

class TraitsController:
    """
    Controller for traits/competencies management
    """
    
    @staticmethod
    def get_all_traits(page=1, limit=20, filters=None):
        """
        Get all traits with pagination and filtering
        """
        try:
            mock_traits = [
                {
                    "id": "1",
                    "name": "Leadership",
                    "description": "Ability to guide and inspire others",
                    "category": "Leadership Skills",
                    "status": "active",
                    "usage_count": 25,
                    "created_at": "2024-01-01T00:00:00Z",
                    "updated_at": "2024-01-15T00:00:00Z"
                },
                {
                    "id": "2",
                    "name": "Communication",
                    "description": "Effective verbal and written communication",
                    "category": "Soft Skills",
                    "status": "active",
                    "usage_count": 30,
                    "created_at": "2024-01-01T00:00:00Z",
                    "updated_at": "2024-01-10T00:00:00Z"
                },
                {
                    "id": "3",
                    "name": "Technical Expertise",
                    "description": "Domain-specific technical knowledge",
                    "category": "Technical Skills",
                    "status": "active",
                    "usage_count": 18,
                    "created_at": "2024-01-05T00:00:00Z",
                    "updated_at": "2024-01-20T00:00:00Z"
                }
            ]
            
            # Apply filters
            if filters:
                if filters.get('category'):
                    mock_traits = [t for t in mock_traits if t['category'] == filters['category']]
                if filters.get('status'):
                    mock_traits = [t for t in mock_traits if t['status'] == filters['status']]
                if filters.get('search'):
                    search_term = filters['search'].lower()
                    mock_traits = [t for t in mock_traits if search_term in t['name'].lower() or search_term in t['description'].lower()]
            
            # Apply pagination
            start_idx = (page - 1) * limit
            end_idx = start_idx + limit
            paginated_traits = mock_traits[start_idx:end_idx]
            
            return jsonify({
                "success": True,
                "data": paginated_traits,
                "pagination": {
                    "page": page,
                    "limit": limit,
                    "total": len(mock_traits),
                    "pages": (len(mock_traits) + limit - 1) // limit
                }
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve traits: {str(e)}"}
            }), 500
    
    @staticmethod
    def create_trait(data):
        """
        Create a new trait
        """
        try:
            new_trait = {
                "id": "new_trait_id",
                "name": data.get('name'),
                "description": data.get('description', ''),
                "category": data.get('category', 'General'),
                "status": "active",
                "usage_count": 0,
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": new_trait,
                "message": "Trait created successfully"
            }), 201
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to create trait: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_trait_by_id(trait_id):
        """
        Get trait by ID
        """
        try:
            mock_trait = {
                "id": str(trait_id),
                "name": "Leadership",
                "description": "Ability to guide and inspire others",
                "category": "Leadership Skills",
                "status": "active",
                "usage_count": 25,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-15T00:00:00Z",
                "questions": [
                    "How effectively does this person communicate vision?",
                    "How well does this person motivate team members?",
                    "How does this person handle difficult decisions?"
                ]
            }
            
            return jsonify({
                "success": True,
                "data": mock_trait
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve trait: {str(e)}"}
            }), 500
    
    @staticmethod
    def update_trait(trait_id, data):
        """
        Update trait
        """
        try:
            updated_trait = {
                "id": str(trait_id),
                "name": data.get('name', 'Updated Trait'),
                "description": data.get('description', ''),
                "category": data.get('category', 'General'),
                "status": data.get('status', 'active'),
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": updated_trait,
                "message": "Trait updated successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update trait: {str(e)}"}
            }), 500
    
    @staticmethod
    def delete_trait(trait_id):
        """
        Delete trait
        """
        try:
            return jsonify({
                "success": True,
                "message": f"Trait {trait_id} deleted successfully"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to delete trait: {str(e)}"}
            }), 500
    
    @staticmethod
    def update_trait_status(trait_id, status):
        """
        Update trait status
        """
        try:
            updated_trait = {
                "id": str(trait_id),
                "status": status,
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            
            return jsonify({
                "success": True,
                "data": updated_trait,
                "message": f"Trait status updated to {status}"
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to update trait status: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_trait_categories():
        """
        Get trait categories
        """
        try:
            mock_categories = [
                {
                    "name": "Leadership Skills",
                    "count": 8,
                    "description": "Skills related to leading and managing teams"
                },
                {
                    "name": "Soft Skills",
                    "count": 12,
                    "description": "Interpersonal and communication skills"
                },
                {
                    "name": "Technical Skills",
                    "count": 15,
                    "description": "Domain-specific technical competencies"
                },
                {
                    "name": "Problem Solving",
                    "count": 6,
                    "description": "Analytical and critical thinking abilities"
                }
            ]
            
            return jsonify({
                "success": True,
                "data": mock_categories
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve trait categories: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_trait_usage():
        """
        Get trait usage statistics
        """
        try:
            mock_usage = {
                "total_traits": 41,
                "active_traits": 38,
                "most_used_traits": [
                    {"name": "Communication", "usage_count": 30},
                    {"name": "Leadership", "usage_count": 25},
                    {"name": "Teamwork", "usage_count": 22},
                    {"name": "Problem Solving", "usage_count": 20},
                    {"name": "Technical Expertise", "usage_count": 18}
                ],
                "usage_by_category": [
                    {"category": "Soft Skills", "count": 12, "percentage": 29.3},
                    {"category": "Technical Skills", "count": 15, "percentage": 36.6},
                    {"category": "Leadership Skills", "count": 8, "percentage": 19.5},
                    {"category": "Problem Solving", "count": 6, "percentage": 14.6}
                ]
            }
            
            return jsonify({
                "success": True,
                "data": mock_usage
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve trait usage: {str(e)}"}
            }), 500
