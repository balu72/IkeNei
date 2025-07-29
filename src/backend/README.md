# Backend Layer - IkeNei

This directory contains the backend API server for the IkeNei, handling business logic, data processing, and survey management.

## Directory Structure

```
backend/
├── controllers/        # Request handlers and business logic
├── models/            # Data models and database schemas
├── routes/            # API route definitions
├── middleware/        # Custom middleware functions
├── services/          # Business logic and external service integrations
├── utils/             # Backend-specific utility functions
└── config/            # Configuration files and environment setup
```

## Key Features

### User Management
- User registration and authentication
- JWT token management
- Role-based access control (RBAC)
- Password reset and email verification

### 360-Degree Feedback System
- Feedback form creation and management
- Multi-source feedback collection
- Anonymous feedback handling
- Progress tracking and notifications
- Feedback cycle management

### Analytics & Reporting
- Data aggregation and analysis
- Report generation and export
- Performance metrics calculation
- Dashboard data preparation

## Technology Stack

- **Runtime**: Python
- **Framework**: Flask
- **Database**: MongoDB
- **ORM**: SQLAlchemy
- **Authentication**: JWT
- **Testing**: Pytest
- **Documentation**: OpenAPI

## API Architecture

### Controllers Directory
- `auth_controller.py` - Authentication and authorization
- `user_controller.py` - User management operations
- `feedback_controller.py` - 360-degree feedback operations
- `analytics_controller.py` - Analytics and reporting
- `admin_controller.py` - Administrative functions

### Models Directory
- `user.py` - User data model
- `feedback_form.py` - Feedback form structure
- `feedback_response.py` - Individual feedback responses
- `competency.py` - Skills and competency definitions
- `organization.py` - Organization/company data

### Services Directory
- `auth_service.py` - Authentication logic
- `feedback_service.py` - Feedback processing
- `email_service.py` - Email notifications
- `report_service.py` - Report generation
- `integration_service.py` - External API integrations

## API Endpoints

Based on the frontend requirements analysis, the following REST API endpoints are required to support the IkeNei application functionality:

### Authentication & Account Management

#### Authentication
```
POST   /api/auth/login              # User login with email/password
POST   /api/auth/logout             # User logout
POST   /api/auth/register           # User registration
GET    /api/auth/me                 # Get current user profile
PUT    /api/auth/profile            # Update user profile
POST   /api/auth/refresh            # Token refresh
POST   /api/auth/forgot             # Password reset request
POST   /api/auth/reset              # Password reset confirmation
```

#### Account Management (System Admin)
```
GET    /api/accounts                # Get all accounts with filtering (search, state, type)
POST   /api/accounts                # Create new account
GET    /api/accounts/{id}           # Get specific account details
PUT    /api/accounts/{id}           # Update account information
PATCH  /api/accounts/{id}/status    # Activate/deactivate account
DELETE /api/accounts/{id}           # Delete account
```

### Survey Management

#### Surveys (Domain Admin)
```
GET    /api/surveys                 # Get all surveys with filtering and pagination
POST   /api/surveys                 # Create new survey
GET    /api/surveys/{id}            # Get specific survey details
PUT    /api/surveys/{id}            # Update survey
DELETE /api/surveys/{id}            # Delete survey
PATCH  /api/surveys/{id}/status     # Change survey status (Active/Draft/Completed)
GET    /api/surveys/available       # Get available surveys for current user
```

#### Survey Execution (Accounts)
```
POST   /api/surveys/{id}/responses  # Submit survey responses
GET    /api/surveys/{id}/responses  # Get survey responses
GET    /api/surveys/my-surveys      # Get surveys where user is subject/respondent
POST   /api/surveys/{id}/run        # Run/execute a survey
```

### Traits & Competencies Management

#### Traits (Domain Admin)
```
GET    /api/traits                  # Get all traits with filtering
POST   /api/traits                  # Create new trait
GET    /api/traits/{id}             # Get specific trait details
PUT    /api/traits/{id}             # Update trait
DELETE /api/traits/{id}             # Delete trait
PATCH  /api/traits/{id}/status      # Change trait status (Active/Draft/Inactive)
GET    /api/traits/categories       # Get trait categories
GET    /api/traits/usage            # Get trait usage statistics
```

### Reports Management

#### Reports (Domain Admin)
```
GET    /api/reports                 # Get all report templates
POST   /api/reports                 # Create new report template
GET    /api/reports/{id}            # Get specific report template
PUT    /api/reports/{id}            # Update report template
DELETE /api/reports/{id}            # Delete report template
POST   /api/reports/{id}/generate   # Generate report instance
GET    /api/reports/{id}/instances  # Get generated report instances
PATCH  /api/reports/{id}/status     # Change report status
```

### Subject & Respondent Management

#### Subjects (Accounts)
```
GET    /api/subjects                # Get user's subjects
POST   /api/subjects                # Create new subject
GET    /api/subjects/{id}           # Get subject details
PUT    /api/subjects/{id}           # Update subject
DELETE /api/subjects/{id}           # Delete subject
```

#### Respondents (Accounts)
```
GET    /api/respondents             # Get user's respondents
POST   /api/respondents             # Create new respondent
GET    /api/respondents/{id}        # Get respondent details
PUT    /api/respondents/{id}        # Update respondent
DELETE /api/respondents/{id}        # Delete respondent
```

### System Settings

#### Settings (System Admin)
```
GET    /api/settings                # Get all system settings with filtering
PUT    /api/settings/{key}          # Update specific setting
PATCH  /api/settings/{key}/toggle   # Toggle boolean settings
POST   /api/settings/reset/{key}    # Reset setting to default
GET    /api/settings/categories     # Get setting categories
```

### Dashboard & Analytics

#### Dashboard Data
```
GET    /api/dashboard/stats         # Get role-specific dashboard statistics
GET    /api/dashboard/activity      # Get recent activity feed
GET    /api/dashboard/analytics     # Get analytics data for charts
```

#### System Analytics (System Admin)
```
GET    /api/analytics/surveys       # Get survey analytics
GET    /api/analytics/accounts      # Get account analytics
GET    /api/analytics/system-health # Get system health metrics
GET    /api/analytics/reports       # Generate analytics reports
POST   /api/analytics/export        # Export analytics data
```

### Additional Utility APIs

#### File Management
```
POST   /api/upload                  # Upload files (avatars, documents)
GET    /api/files/{id}              # Download/view files
DELETE /api/files/{id}              # Delete files
```

#### Notifications
```
GET    /api/notifications           # Get user notifications
PATCH  /api/notifications/{id}/read # Mark notification as read
POST   /api/notifications           # Create notification
DELETE /api/notifications/{id}      # Delete notification
```

### API Response Format

All API responses should follow this consistent format:

```json
{
  "success": true,
  "data": {
    // Response data here
  },
  "message": "Operation completed successfully",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

For errors:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      // Specific error details
    }
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Authentication Requirements

- **Public endpoints**: `/api/auth/login`, `/api/auth/register`, `/api/auth/forgot`, `/api/auth/reset`
- **Account role**: All `/api/subjects/*`, `/api/respondents/*`, `/api/surveys/my-surveys`, `/api/surveys/*/responses`
- **Domain Admin role**: All `/api/surveys/*`, `/api/traits/*`, `/api/reports/*` (except system-wide operations)
- **System Admin role**: All `/api/accounts/*`, `/api/settings/*`, `/api/analytics/*`

### Pagination & Filtering

List endpoints should support:
- `page` - Page number (default: 1)
- `limit` - Items per page (default: 20, max: 100)
- `search` - Search term for filtering
- `sort` - Sort field and direction (e.g., `name:asc`, `created_at:desc`)
- `filter` - Additional filters specific to each endpoint

Example: `GET /api/surveys?page=1&limit=20&search=leadership&sort=created_at:desc&filter=status:active`

## Development Guidelines

1. **API Design**
   - Follow RESTful principles
   - Use consistent naming conventions
   - Implement proper HTTP status codes
   - Version your APIs appropriately

2. **Security**
   - Implement proper authentication and authorization
   - Validate and sanitize all inputs
   - Use HTTPS in production
   - Implement rate limiting
   - Follow OWASP security guidelines

3. **Error Handling**
   - Use consistent error response format
   - Log errors appropriately
   - Don't expose sensitive information
   - Implement proper error recovery

4. **Performance**
   - Implement database query optimization
   - Use caching where appropriate
   - Implement pagination for large datasets
   - Monitor API performance metrics

## Environment Variables

```
FLASK_ENV=development
FLASK_APP=app.py
PORT=5000
MONGODB_URI=mongodb://localhost:27017/360planner
JWT_SECRET=your-jwt-secret
JWT_EXPIRES_IN=7d
EMAIL_SERVICE_API_KEY=your-email-api-key
REDIS_URL=redis://localhost:6379
```

## Database Schema

### Core Tables
- `users` - User accounts and profiles
- `organizations` - Company/organization data
- `feedback_forms` - Feedback form templates
- `feedback_responses` - Individual feedback submissions
- `competencies` - Skills and competency framework

## AI/ML Integration

### Feedback Analysis
- Natural language processing for text feedback
- Sentiment analysis and emotion detection
- Pattern recognition in feedback data
- Competency gap identification

## Testing Strategy

- Unit tests for all business logic
- Integration tests for API endpoints
- Database testing with test fixtures
- Performance and load testing

## Deployment

- Containerization with Docker
- Environment-specific configurations
- Database migration scripts
- Health check endpoints
- Monitoring and logging setup

## Getting Started

1. Create virtual environment: `python -m venv venv`
2. Activate virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Set up environment variables
5. Initialize database: `python manage.py init_db`
6. Seed initial data: `python manage.py seed_data`
7. Start development server: `python app.py` or `flask run`
8. Run tests: `pytest`
