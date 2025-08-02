from flask import jsonify
from datetime import datetime
import traceback

def success_response(data=None, message="Operation completed successfully", status_code=200):
    """
    Create a standardized success response
    """
    response = {
        "success": True,
        "data": data,
        "message": message,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    return jsonify(response), status_code

def error_response(message="An error occurred", error_code="INTERNAL_ERROR", 
                  details=None, status_code=500):
    """
    Create a standardized error response
    """
    response = {
        "success": False,
        "error": {
            "code": error_code,
            "message": message,
            "details": details
        },
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    return jsonify(response), status_code

def validation_error_response(errors, message="Validation failed"):
    """
    Create a validation error response
    """
    return error_response(
        message=message,
        error_code="VALIDATION_ERROR",
        details=errors,
        status_code=400
    )

def not_found_response(resource="Resource"):
    """
    Create a not found error response
    """
    return error_response(
        message=f"{resource} not found",
        error_code="NOT_FOUND",
        status_code=404
    )

def unauthorized_response(message="Authentication required"):
    """
    Create an unauthorized error response
    """
    return error_response(
        message=message,
        error_code="UNAUTHORIZED",
        status_code=401
    )

def forbidden_response(message="Access denied"):
    """
    Create a forbidden error response
    """
    return error_response(
        message=message,
        error_code="FORBIDDEN",
        status_code=403
    )

def conflict_response(message="Resource already exists"):
    """
    Create a conflict error response
    """
    return error_response(
        message=message,
        error_code="CONFLICT",
        status_code=409
    )

def handle_exception(e):
    """
    Handle unexpected exceptions
    """
    # Log the full traceback for debugging
    print(f"Unexpected error: {str(e)}")
    print(traceback.format_exc())
    
    return error_response(
        message="An unexpected error occurred",
        error_code="INTERNAL_ERROR",
        details=str(e) if hasattr(e, '__str__') else None,
        status_code=500
    )
