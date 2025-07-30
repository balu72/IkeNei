from functools import wraps
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from utils.response_helpers import unauthorized_response, forbidden_response

def require_auth(f):
    """
    Decorator to require authentication for an endpoint
    """
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function

def require_roles(*allowed_roles):
    """
    Decorator to require specific roles for an endpoint
    Usage: @require_roles('system_admin', 'domain_admin')
    """
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def decorated_function(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get('role', 'account')
            
            if user_role not in allowed_roles:
                return forbidden_response(f"Access denied. Required roles: {', '.join(allowed_roles)}")
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def require_account_role(f):
    """
    Decorator to require account role
    """
    return require_roles('account')(f)

def require_domain_admin_role(f):
    """
    Decorator to require domain admin role
    """
    return require_roles('domain_admin')(f)

def require_system_admin_role(f):
    """
    Decorator to require system admin role
    """
    return require_roles('system_admin')(f)

def require_admin_roles(f):
    """
    Decorator to require either domain admin or system admin role
    """
    return require_roles('domain_admin', 'system_admin')(f)

def get_current_user_id():
    """
    Get the current authenticated user's ID
    """
    return get_jwt_identity()

def get_current_user_role():
    """
    Get the current authenticated user's role
    """
    claims = get_jwt()
    return claims.get('role', 'account')

def get_current_user_claims():
    """
    Get all claims for the current authenticated user
    """
    return get_jwt()

def check_resource_ownership(resource_user_id):
    """
    Check if the current user owns the resource or has admin privileges
    """
    current_user_id = get_current_user_id()
    current_user_role = get_current_user_role()
    
    # System admins can access any resource
    if current_user_role == 'system_admin':
        return True
    
    # Domain admins can access resources in their domain (simplified check)
    if current_user_role == 'domain_admin':
        return True
    
    # Regular accounts can only access their own resources
    return str(current_user_id) == str(resource_user_id)

def require_ownership_or_admin(get_resource_user_id):
    """
    Decorator to require resource ownership or admin privileges
    get_resource_user_id should be a function that returns the user_id of the resource
    """
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def decorated_function(*args, **kwargs):
            resource_user_id = get_resource_user_id(*args, **kwargs)
            
            if not check_resource_ownership(resource_user_id):
                return forbidden_response("Access denied. You can only access your own resources.")
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator
