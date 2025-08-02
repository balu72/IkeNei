from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from utils.logger import setup_logging, get_logger

# Import route blueprints
from routes.auth_routes import auth_bp
from routes.accounts_routes import accounts_bp
from routes.surveys_routes import surveys_bp
from routes.traits_routes import traits_bp
from routes.reports_routes import reports_bp
from routes.subjects_routes import subjects_bp
from routes.respondents_routes import respondents_bp
from routes.settings_routes import settings_bp
from routes.dashboard_routes import dashboard_bp
from routes.analytics_routes import analytics_bp
from routes.billing_routes import billing_bp
from routes.files_routes import files_bp
from routes.notifications_routes import notifications_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Set up logging first
    setup_logging(app)
    logger = get_logger(__name__)
    logger.info("Starting IkeNei Backend API application")
    
    # Initialize extensions with explicit CORS configuration
    CORS(app, 
         origins=['http://localhost:5173', 'http://localhost:5174', 'http://localhost:3000'],
         allow_headers=['Content-Type', 'Authorization'],
         methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
    jwt = JWTManager(app)
    logger.info("Flask extensions initialized")
    
    # Register blueprints
    blueprints = [
        (auth_bp, 'Authentication'),
        (accounts_bp, 'Accounts'),
        (surveys_bp, 'Surveys'),
        (traits_bp, 'Traits'),
        (reports_bp, 'Reports'),
        (subjects_bp, 'Subjects'),
        (respondents_bp, 'Respondents'),
        (settings_bp, 'Settings'),
        (dashboard_bp, 'Dashboard'),
        (analytics_bp, 'Analytics'),
        (billing_bp, 'Billing'),
        (files_bp, 'Files'),
        (notifications_bp, 'Notifications')
    ]
    
    for blueprint, name in blueprints:
        app.register_blueprint(blueprint)
        logger.info(f"Registered {name} blueprint")
    
    # Health check endpoint
    @app.route('/health')
    def health_check():
        logger.info("Health check endpoint accessed")
        return {"status": "healthy", "message": "IkeNei Backend API is running"}
    
    logger.info("IkeNei Backend API application setup completed")
    return app

if __name__ == '__main__':
    logger = get_logger(__name__)
    logger.info("Starting IkeNei Backend API server on 0.0.0.0:5000")
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
