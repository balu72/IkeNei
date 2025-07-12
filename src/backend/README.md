# Backend Layer - 360+AI Planner

This directory contains the backend API server for the 360+AI Planner, handling business logic, data processing, and AI-powered learning plan generation.

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

### AI-Powered Learning Plans
- Feedback data analysis using AI/ML algorithms
- Personalized learning recommendation engine
- Progress tracking and adaptive learning paths
- Integration with external learning resources

### Analytics & Reporting
- Data aggregation and analysis
- Report generation and export
- Performance metrics calculation
- Dashboard data preparation

## Technology Stack

- **Runtime**: Node.js/Python/Java (to be determined)
- **Framework**: Express.js/FastAPI/Spring Boot
- **Database**: PostgreSQL/MongoDB
- **ORM**: Prisma/Sequelize/SQLAlchemy
- **Authentication**: JWT/OAuth 2.0
- **AI/ML**: TensorFlow/PyTorch/Scikit-learn
- **Testing**: Jest/Pytest/JUnit
- **Documentation**: Swagger/OpenAPI

## API Architecture

### Controllers Directory
- `authController.js` - Authentication and authorization
- `userController.js` - User management operations
- `feedbackController.js` - 360-degree feedback operations
- `learningController.js` - Learning plan management
- `analyticsController.js` - Analytics and reporting
- `adminController.js` - Administrative functions

### Models Directory
- `User.js` - User data model
- `FeedbackForm.js` - Feedback form structure
- `FeedbackResponse.js` - Individual feedback responses
- `LearningPlan.js` - AI-generated learning plans
- `Competency.js` - Skills and competency definitions
- `Organization.js` - Organization/company data

### Services Directory
- `authService.js` - Authentication logic
- `feedbackService.js` - Feedback processing
- `aiService.js` - AI/ML integration
- `emailService.js` - Email notifications
- `reportService.js` - Report generation
- `integrationService.js` - External API integrations

## API Endpoints

### Authentication
```
POST /api/auth/register     # User registration
POST /api/auth/login        # User login
POST /api/auth/logout       # User logout
POST /api/auth/refresh      # Token refresh
POST /api/auth/forgot       # Password reset request
POST /api/auth/reset        # Password reset confirmation
```

### User Management
```
GET    /api/users/profile   # Get user profile
PUT    /api/users/profile   # Update user profile
GET    /api/users/settings  # Get user settings
PUT    /api/users/settings  # Update user settings
```

### Feedback Management
```
POST   /api/feedback/forms          # Create feedback form
GET    /api/feedback/forms          # List feedback forms
GET    /api/feedback/forms/:id      # Get specific form
PUT    /api/feedback/forms/:id      # Update feedback form
DELETE /api/feedback/forms/:id      # Delete feedback form
POST   /api/feedback/responses      # Submit feedback response
GET    /api/feedback/responses      # Get feedback responses
```

### Learning Plans
```
GET    /api/learning/plans          # Get user's learning plans
POST   /api/learning/plans          # Generate new learning plan
PUT    /api/learning/plans/:id      # Update learning plan
GET    /api/learning/resources      # Get learning resources
POST   /api/learning/progress       # Update learning progress
```

### Analytics
```
GET    /api/analytics/dashboard     # Dashboard data
GET    /api/analytics/reports       # Generate reports
GET    /api/analytics/metrics       # Performance metrics
POST   /api/analytics/export        # Export data
```

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
NODE_ENV=development
PORT=3001
DATABASE_URL=postgresql://user:password@localhost:5432/360planner
JWT_SECRET=your-jwt-secret
JWT_EXPIRES_IN=7d
EMAIL_SERVICE_API_KEY=your-email-api-key
AI_SERVICE_API_KEY=your-ai-service-key
REDIS_URL=redis://localhost:6379
```

## Database Schema

### Core Tables
- `users` - User accounts and profiles
- `organizations` - Company/organization data
- `feedback_forms` - Feedback form templates
- `feedback_responses` - Individual feedback submissions
- `learning_plans` - AI-generated learning plans
- `competencies` - Skills and competency framework
- `learning_resources` - External learning materials

## AI/ML Integration

### Feedback Analysis
- Natural language processing for text feedback
- Sentiment analysis and emotion detection
- Pattern recognition in feedback data
- Competency gap identification

### Learning Plan Generation
- Personalized recommendation algorithms
- Adaptive learning path optimization
- Resource matching and ranking
- Progress prediction and adjustment

## Testing Strategy

- Unit tests for all business logic
- Integration tests for API endpoints
- Database testing with test fixtures
- AI/ML model testing and validation
- Performance and load testing

## Deployment

- Containerization with Docker
- Environment-specific configurations
- Database migration scripts
- Health check endpoints
- Monitoring and logging setup

## Getting Started

1. Install dependencies: `npm install`
2. Set up environment variables
3. Run database migrations: `npm run migrate`
4. Seed initial data: `npm run seed`
5. Start development server: `npm run dev`
6. Run tests: `npm test`
