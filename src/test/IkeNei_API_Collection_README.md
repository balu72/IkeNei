# IkeNei API Collection - Postman Collection

This Postman collection contains all REST API endpoints for the IkeNei Backend - a comprehensive survey and feedback management system.

## Overview

The collection includes **100+ API endpoints** organized into the following categories:

### 📁 Collection Structure

1. **Authentication** (8 endpoints)
   - Login, Register, Profile management, Password reset, Token refresh

2. **Accounts Management** (6 endpoints)
   - CRUD operations for user accounts (System Admin only)

3. **Surveys** (17 endpoints)
   - Complete survey lifecycle management
   - Survey creation, execution, approval workflow

4. **Survey Responses** (4 endpoints)
   - Public survey response submission
   - Response analytics and management

5. **Subjects** (5 endpoints)
   - Manage survey subjects (people being evaluated)

6. **Respondents** (5 endpoints)
   - Manage survey respondents (people providing feedback)

7. **Traits** (8 endpoints)
   - Manage competencies and traits for evaluation

8. **Reports** (12 endpoints)
   - Report templates and generation system

9. **Analytics** (9 endpoints)
   - System analytics and insights (System Admin only)

10. **Dashboard** (3 endpoints)
    - Role-specific dashboard data

11. **Billing** (8 endpoints)
    - Survey usage billing and cost management

12. **Files** (3 endpoints)
    - File upload, download, and management

13. **Notifications** (4 endpoints)
    - User notification system

14. **Settings** (5 endpoints)
    - System configuration management

15. **Categories** (1 endpoint)
    - System category management

16. **System Health** (2 endpoints)
    - Health monitoring endpoints

## 🚀 Getting Started

### 1. Import the Collection

1. Open Postman
2. Click "Import" button
3. Select the `IkeNei_API_Collection.postman_collection.json` file
4. The collection will be imported with all endpoints organized in folders

### 2. Configure Environment Variables

The collection uses two main variables:

- `{{base_url}}` - Set to `http://localhost:5000` (default)
- `{{jwt_token}}` - Will be populated after successful login

#### Setting up Environment:

1. Create a new Environment in Postman
2. Add these variables:
   ```
   base_url: http://localhost:5000
   jwt_token: (leave empty initially)
   ```

### 3. Authentication Flow

1. **Register a new account** or **Login** using the Authentication folder
2. Copy the JWT token from the login response
3. Set the `jwt_token` environment variable
4. The collection is configured to automatically use Bearer token authentication

## 🔐 Authentication & Authorization

### Authentication Types:
- **Bearer Token**: Most endpoints require JWT authentication
- **No Auth**: Public endpoints (health checks, survey response submission)

### User Roles:
- **System Admin**: Full system access
- **Domain Admin**: Account-level administration
- **Account User**: Basic user operations

### Protected Endpoints:
- System Admin only: Analytics, Account Management, Settings
- Domain Admin: Survey creation, Trait management, Reports
- Authenticated users: Subjects, Respondents, Notifications

## 📋 Key API Workflows

### 1. User Registration & Login
```
POST /api/auth/register → Register new account
POST /api/auth/login → Get JWT token
GET /api/auth/me → Verify authentication
```

### 2. Survey Creation & Execution
```
POST /api/surveys → Create survey
POST /api/subjects → Add survey subjects
POST /api/respondents → Add respondents
POST /api/surveys/{id}/run → Execute survey
GET /api/surveys/{id}/responses → View responses
```

### 3. Public Survey Response
```
GET /api/survey/respond/{token} → Get survey form (no auth)
POST /api/survey/respond/{token} → Submit response (no auth)
```

### 4. Analytics & Reporting
```
GET /api/analytics/overview → System overview
POST /api/reports/{id}/generate → Generate report
GET /api/dashboard/stats → Dashboard data
```

## 🛠️ Request Examples

### Login Request:
```json
POST /api/auth/login
{
  "email": "user@example.com",
  "password": "password123"
}
```

### Create Survey:
```json
POST /api/surveys
{
  "title": "Employee Feedback Survey",
  "description": "Annual employee feedback and performance review survey"
}
```

### Create Subject:
```json
POST /api/subjects
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Engineering",
  "position": "Senior Developer"
}
```

## 📊 Response Formats

All API responses follow a consistent format:

### Success Response:
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation completed successfully"
}
```

### Error Response:
```json
{
  "success": false,
  "error": "Error message",
  "details": { ... }
}
```

### Paginated Response:
```json
{
  "success": true,
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 50,
    "pages": 5
  }
}
```

## 🔧 Configuration

### Base URL Configuration:
- **Development**: `http://localhost:5000`
- **Production**: Update the `base_url` variable accordingly

### Common Query Parameters:
- `page`: Page number for pagination (default: 1)
- `limit`: Items per page (default: 10)
- `search`: Search term for filtering
- `status`: Filter by status
- `type`: Filter by type

## 📝 Testing Tips

1. **Start with Authentication**: Always login first to get JWT token
2. **Use Environment Variables**: Leverage `{{base_url}}` and `{{jwt_token}}`
3. **Check Response Status**: Verify HTTP status codes (200, 201, 400, 401, etc.)
4. **Test Different Roles**: Create accounts with different permission levels
5. **Validate Data**: Check response data structure and content

## 🚨 Important Notes

### Public Endpoints (No Authentication Required):
- `GET /health` - System health check
- `GET /health/database` - Database health check
- `GET /api/survey/respond/{token}` - Get survey form
- `POST /api/survey/respond/{token}` - Submit survey response

### File Upload Endpoints:
- Use `multipart/form-data` for file uploads
- Include `file` field and optional `type` field

### Rate Limiting:
- Be mindful of API rate limits in production
- Implement appropriate delays between requests if needed

## 🐛 Troubleshooting

### Common Issues:

1. **401 Unauthorized**: 
   - Check if JWT token is set correctly
   - Verify token hasn't expired

2. **403 Forbidden**:
   - User doesn't have required permissions
   - Check user role and endpoint requirements

3. **404 Not Found**:
   - Verify endpoint URL is correct
   - Check if resource exists

4. **422 Validation Error**:
   - Review request body format
   - Check required fields

## 📞 Support

For API documentation updates or issues:
1. Check the backend route files in `/src/backend/routes/`
2. Review controller implementations in `/src/backend/controllers/`
3. Verify middleware requirements in `/src/backend/middleware/`

---

**Total Endpoints**: 100+
**Last Updated**: January 2025
**API Version**: 1.0
**Backend Framework**: Flask (Python)
**Authentication**: JWT Bearer Token
