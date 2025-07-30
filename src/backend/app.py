from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

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
    
    # Initialize extensions
    CORS(app)
    jwt = JWTManager(app)
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(accounts_bp)
    app.register_blueprint(surveys_bp)
    app.register_blueprint(traits_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(subjects_bp)
    app.register_blueprint(respondents_bp)
    app.register_blueprint(settings_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(billing_bp)
    app.register_blueprint(files_bp)
    app.register_blueprint(notifications_bp)
    
    # Health check endpoint
    @app.route('/health')
    def health_check():
        return {"status": "healthy", "message": "IkeNei Backend API is running"}
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
