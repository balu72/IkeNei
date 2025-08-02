from datetime import datetime
from bson import ObjectId
from database.base_model import BaseModel

class RespondentModel(BaseModel):
    """
    Respondent model for managing survey respondents
    """
    
    def __init__(self, subject_id=None, name=None, email=None, phone=None, 
                 address=None, relationship=None, other_info=None, 
                 status='invited', response_status='pending', **kwargs):
        super().__init__(**kwargs)
        self.subject_id = ObjectId(subject_id) if subject_id and not isinstance(subject_id, ObjectId) else subject_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.relationship = relationship
        self.other_info = other_info
        self.status = status  # invited, active, inactive
        self.response_status = response_status  # pending, completed, declined
        self.invited_at = kwargs.get('invited_at', datetime.utcnow())
        self.responded_at = kwargs.get('responded_at')
    
    @classmethod
    def get_collection_name(cls):
        return 'respondents'
    
    def to_dict(self):
        """Convert to dictionary for database storage"""
        data = super().to_dict()
        data.update({
            'subject_id': self.subject_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'relationship': self.relationship,
            'other_info': self.other_info,
            'status': self.status,
            'response_status': self.response_status,
            'invited_at': self.invited_at,
            'responded_at': self.responded_at
        })
        return data
    
    def to_public_dict(self):
        """Convert to dictionary for public API responses"""
        data = self.to_dict()
        # Convert ObjectId to string for JSON serialization
        if isinstance(data.get('_id'), ObjectId):
            data['id'] = str(data['_id'])
            del data['_id']
        if isinstance(data.get('subject_id'), ObjectId):
            data['subject_id'] = str(data['subject_id'])
        
        # Format dates
        if data.get('invited_at'):
            data['invited_at'] = data['invited_at'].isoformat() + 'Z' if isinstance(data['invited_at'], datetime) else data['invited_at']
        if data.get('responded_at'):
            data['responded_at'] = data['responded_at'].isoformat() + 'Z' if isinstance(data['responded_at'], datetime) else data['responded_at']
        if data.get('created_at'):
            data['created_at'] = data['created_at'].isoformat() + 'Z' if isinstance(data['created_at'], datetime) else data['created_at']
        if data.get('updated_at'):
            data['updated_at'] = data['updated_at'].isoformat() + 'Z' if isinstance(data['updated_at'], datetime) else data['updated_at']
        
        return data
    
    @classmethod
    def from_dict(cls, data):
        """Create instance from dictionary"""
        if not data:
            return None
        
        # Handle ObjectId conversion
        if '_id' in data:
            data['id'] = data['_id']
        
        return cls(**data)
    
    def validate(self):
        """Validate the respondent data"""
        errors = []
        
        if not self.name or not self.name.strip():
            errors.append("Name is required")
        
        if not self.email or not self.email.strip():
            errors.append("Email is required")
        elif '@' not in self.email:
            errors.append("Invalid email format")
        
        if not self.subject_id:
            errors.append("Subject ID is required")
        
        if not self.relationship or not self.relationship.strip():
            errors.append("Relationship is required")
        
        return errors
