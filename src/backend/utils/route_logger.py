import functools
from flask import request
from utils.logger import get_logger

def log_route(func):
    """
    Decorator to automatically log entry and exit for route functions
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger(func.__module__)
        
        # Extract route info
        method = request.method
        path = request.path
        
        # Log entry
        logger.info(f"=== ENTRY: {method} {path} ===")
        
        # Log request parameters if any
        if request.args:
            logger.debug(f"Query parameters: {dict(request.args)}")
        
        # Only try to access JSON for requests that might have a body
        if request.method in ['POST', 'PUT', 'PATCH'] and request.content_type == 'application/json':
            try:
                if request.json:
                    logger.debug(f"Request body: {request.json}")
            except Exception:
                # Ignore JSON parsing errors for logging
                pass
        
        # Log path parameters
        if kwargs:
            logger.debug(f"Path parameters: {kwargs}")
        
        try:
            # Execute the route function
            result = func(*args, **kwargs)
            
            # Log successful exit
            logger.info(f"=== EXIT: {method} {path} - SUCCESS ===")
            return result
            
        except Exception as e:
            # Log error exit
            logger.error(f"=== EXIT: {method} {path} - ERROR: {str(e)} ===")
            raise
    
    return wrapper
