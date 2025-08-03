# Backend Layer - IkeNei

This directory contains the backend API server for the IkeNei, handling business logic, data processing, and survey management.

## Directory Structure

```
backend/
├── .env                           # Environment configuration
├── app.py                         # Main Flask application entry point
├── config.py                      # Application configuration
├── requirements.txt               # Python dependencies
├── README.md                      # Backend documentation
├── IMPLEMENTATION_STATUS.md       # Implementation progress tracking
├── controllers/                   # Request handlers and business logic
│   ├── __init__.py               # Controllers package initialization
│   ├── accounts_controller.py    # Account management operations
│   ├── analytics_controller.py   # Analytics and reporting logic
│   ├── auth_controller.py        # Authentication and authorization
│   ├── billing_controller.py     # Billing and usage tracking
│   ├── categories_controller.py  # Category management
│   ├── dashboard_controller.py   # Dashboard data aggregation
│   ├── files_controller.py       # File upload and management
│   ├── notifications_controller.py # Notification handling
│   ├── reports_controller.py     # Report generation and management
│   ├── respondents_controller.py # Respondent management
│   ├── settings_controller.py    # System settings management
│   ├── subjects_controller.py    # Subject management
│   ├── surveys_controller.py     # Survey creation and management
│   └── traits_controller.py      # Trait/competency management
├── logs/                          # Application logs
│   ├── access.log                # HTTP access logs
│   ├── app.log                   # Application logs
│   └── error.log                 # Error logs
├── middleware/                    # Custom middleware functions
│   ├── __init__.py               # Middleware package initialization
│   └── auth_middleware.py        # JWT authentication middleware
└── routes/                        # API route definitions
    ├── __init__.py               # Routes package initialization
    ├── accounts_routes.py        # Account management routes
    ├── analytics_routes.py       # Analytics and reporting routes
    ├── auth_routes.py            # Authentication routes
    ├── billing_routes.py         # Billing and usage routes
    ├── categories_routes.py      # Category management routes
    ├── dashboard_routes.py       # Dashboard data routes
    ├── files_routes.py           # File management routes
    ├── notifications_routes.py   # Notification routes
    ├── reports_routes.py         # Report management routes
    ├── respondents_routes.py     # Respondent management routes
    ├── settings_routes.py        # Settings management routes
    ├── subjects_routes.py        # Subject management routes
    ├── surveys_routes.py         # Survey management routes
    └── traits_routes.py          # Trait/competency routes
```

## Key Features

### Account Management
- Account registration and authentication
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
- **ODM**: PyMongo
- **Authentication**: JWT
- **Testing**: Pytest
- **Documentation**: OpenAPI

## API Architecture

### Controllers Directory (14 Controllers)
- `accounts_controller.py` - Account management operations
- `analytics_controller.py` - Analytics and reporting logic
- `auth_controller.py` - Authentication and authorization
- `billing_controller.py` - Billing and usage tracking
- `categories_controller.py` - Category management
- `dashboard_controller.py` - Dashboard data aggregation
- `files_controller.py` - File upload and management
- `notifications_controller.py` - Notification handling
- `reports_controller.py` - Report generation and management
- `respondents_controller.py` - Respondent management
- `settings_controller.py` - System settings management
- `subjects_controller.py` - Subject management
- `surveys_controller.py` - Survey creation and management
- `traits_controller.py` - Trait/competency management

### Routes Directory (14 Route Files)
- `accounts_routes.py` - Account management API routes
- `analytics_routes.py` - Analytics and reporting API routes
- `auth_routes.py` - Authentication API routes
- `billing_routes.py` - Billing and usage API routes
- `categories_routes.py` - Category management API routes
- `dashboard_routes.py` - Dashboard data API routes
- `files_routes.py` - File management API routes
- `notifications_routes.py` - Notification API routes
- `reports_routes.py` - Report management API routes
- `respondents_routes.py` - Respondent management API routes
- `settings_routes.py` - Settings management API routes
- `subjects_routes.py` - Subject management API routes
- `surveys_routes.py` - Survey management API routes
- `traits_routes.py` - Trait/competency API routes

### Middleware Directory
- `auth_middleware.py` - JWT authentication and authorization middleware

### Application Structure
- `app.py` - Main Flask application with route registration and configuration
- `config.py` - Application configuration and environment settings
- `logs/` - Application logging (access, application, and error logs)

## API Endpoints

Based on the frontend requirements analysis, the following REST API endpoints are required to support the IkeNei application functionality:

### Authentication & Account Management

#### Authentication
```
POST   /api/auth/login              # Account login with email/password
POST   /api/auth/logout             # Account logout
POST   /api/auth/register           # Account registration
GET    /api/auth/me                 # Get current account profile
PUT    /api/auth/profile            # Update account profile
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
GET    /api/surveys/available       # Get available surveys for current account
```

#### Survey Execution (Accounts)
```
POST   /api/surveys/{id}/responses  # Submit survey responses
GET    /api/surveys/{id}/responses  # Get survey responses
GET    /api/surveys/my-surveys      # Get surveys where account is subject/respondent
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
GET    /api/subjects                # Get account's subjects
POST   /api/subjects                # Create new subject
GET    /api/subjects/{id}           # Get subject details
PUT    /api/subjects/{id}           # Update subject
DELETE /api/subjects/{id}           # Delete subject
```

#### Respondents (Accounts)
```
GET    /api/respondents             # Get account's respondents
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

### Billing & Usage Tracking

#### Billing Management (System Admin & Account)
```
GET    /api/billing                 # Get billing records with filtering (account, date range, status)
POST   /api/billing                 # Create new billing record (auto-generated on survey completion)
GET    /api/billing/{id}            # Get specific billing record details
PUT    /api/billing/{id}            # Update billing record (amount, status)
PATCH  /api/billing/{id}/status     # Update billing status (pending, paid, failed)
GET    /api/billing/account/{id}    # Get billing records for specific account
GET    /api/billing/summary         # Get billing summary and statistics
POST   /api/billing/calculate       # Calculate billing amount for survey usage
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
GET    /api/notifications           # Get account notifications
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
- **Account role**: All `/api/subjects/*`, `/api/respondents/*`, `/api/surveys/my-surveys`, `/api/surveys/*/responses`, `/api/billing/account/{own_id}`
- **Domain Admin role**: All `/api/surveys/*`, `/api/traits/*`, `/api/reports/*` (except system-wide operations)
- **System Admin role**: All `/api/accounts/*`, `/api/settings/*`, `/api/analytics/*`, `/api/billing/*`

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
MONGODB_URI=mongodb://localhost:27017/ikenei
MONGODB_DB_NAME=ikenei
JWT_SECRET_KEY=your-jwt-secret
EMAIL_SERVICE_API_KEY=your-email-api-key
```

## Database Schema

### Core Collections
- `accounts` - Account profiles and data
- `subjects` - Individuals being assessed
- `respondents` - Feedback providers
- `feedback_forms` - Feedback form templates
- `feedback_responses` - Individual feedback submissions
- `competencies` - Skills and competency framework
- `billing` - Survey usage tracking and billing records

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
4. Set up environment variables (copy `.env` and update values)
5. Start MongoDB server: `mongod`
6. Initialize database collections and indexes
7. Seed initial data with sample accounts and data
8. Start development server: `python app.py`
9. Run tests: `pytest`
