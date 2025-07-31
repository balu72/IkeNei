import logging
import logging.handlers
import os
from datetime import datetime
from flask import request, g
import functools

def setup_logging(app):
    """
    Set up comprehensive logging for the Flask application
    """
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    # Configure logging format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Set up file handlers
    # General application log
    app_log_file = os.path.join(logs_dir, 'app.log')
    app_handler = logging.handlers.RotatingFileHandler(
        app_log_file, maxBytes=10*1024*1024, backupCount=5
    )
    app_handler.setFormatter(formatter)
    app_handler.setLevel(logging.INFO)
    
    # Error log
    error_log_file = os.path.join(logs_dir, 'error.log')
    error_handler = logging.handlers.RotatingFileHandler(
        error_log_file, maxBytes=10*1024*1024, backupCount=5
    )
    error_handler.setFormatter(formatter)
    error_handler.setLevel(logging.ERROR)
    
    # API access log
    access_log_file = os.path.join(logs_dir, 'access.log')
    access_handler = logging.handlers.RotatingFileHandler(
        access_log_file, maxBytes=10*1024*1024, backupCount=5
    )
    access_formatter = logging.Formatter(
        '%(asctime)s - %(remote_addr)s - %(method)s %(url)s - %(status_code)s - %(response_time)sms'
    )
    access_handler.setFormatter(access_formatter)
    access_handler.setLevel(logging.INFO)
    
    # Configure Flask app logger
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(app_handler)
    app.logger.addHandler(error_handler)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(app_handler)
    root_logger.addHandler(error_handler)
    
    # Console handler for development
    if app.debug:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(console_handler)
        root_logger.addHandler(console_handler)
    
    # Set up request logging
    @app.before_request
    def log_request_info():
        g.start_time = datetime.now()
        app.logger.info(f"Request started: {request.method} {request.url} from {request.remote_addr}")
        if request.json:
            app.logger.debug(f"Request body: {request.json}")
    
    @app.after_request
    def log_request_result(response):
        if hasattr(g, 'start_time'):
            response_time = (datetime.now() - g.start_time).total_seconds() * 1000
            
            # Log to access log
            access_logger = logging.getLogger('access')
            access_logger.addHandler(access_handler)
            access_record = logging.LogRecord(
                name='access',
                level=logging.INFO,
                pathname='',
                lineno=0,
                msg='',
                args=(),
                exc_info=None
            )
            access_record.remote_addr = request.remote_addr
            access_record.method = request.method
            access_record.url = request.url
            access_record.status_code = response.status_code
            access_record.response_time = f"{response_time:.2f}"
            access_handler.emit(access_record)
            
            # Log to app log
            app.logger.info(
                f"Request completed: {request.method} {request.url} - "
                f"Status: {response.status_code} - Time: {response_time:.2f}ms"
            )
        
        return response
    
    # Error handler
    @app.errorhandler(Exception)
    def log_exception(error):
        app.logger.error(f"Unhandled exception: {str(error)}", exc_info=True)
        return {"error": "Internal server error"}, 500
    
    app.logger.info("Logging system initialized")
    return app

def log_function_call(func):
    """
    Decorator to log function calls in controllers
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
            raise
    
    return wrapper

def get_logger(name):
    """
    Get a logger instance for a specific module
    """
    return logging.getLogger(name)
