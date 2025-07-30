# Frontend Layer - IkeNei

This directory contains the React frontend application for the IkeNei 360-degree feedback and survey management platform.

## Directory Structure

```
frontend/
├── .env                           # Environment configuration
├── .gitignore                     # Git ignore rules
├── App.css                        # Global styles
├── App.jsx                        # Main application component
├── eslint.config.js               # ESLint configuration
├── index.css                      # Base styles
├── index.html                     # HTML template
├── main.jsx                       # Application entry point
├── package.json                   # Dependencies and scripts
├── package-lock.json              # Dependency lock file
├── README.md                      # Documentation
├── vite.config.js                 # Vite configuration
├── components/                    # Reusable UI components
│   ├── CreateRespondantModal.jsx  # Respondent creation modal
│   ├── CreateSubjectModal.jsx     # Subject creation modal
│   ├── CreateSurveyModal.jsx      # Survey creation modal
│   ├── Layout.jsx                 # Main layout wrapper
│   ├── Login.jsx                  # Authentication component
│   └── Sidebar.jsx                # Navigation sidebar
├── contexts/                      # React context providers
│   └── AuthContext.jsx            # Authentication context
├── pages/                         # Page components by role
│   ├── Home.jsx                   # Generic home page
│   ├── account_management_pages/  # Account role pages
│   │   ├── AccountHome.jsx        # Account dashboard
│   │   ├── ProfileUpdate.jsx      # Profile management
│   │   ├── RunSurvey.jsx          # Survey execution
│   │   └── Survey.jsx             # Survey participation
│   ├── domain_admin_pages/        # Domain admin pages
│   │   ├── CreateSurvey.jsx       # Survey creation
│   │   ├── CreateTrait.jsx        # Trait management
│   │   ├── DefineReport.jsx       # Report definition
│   │   ├── DomainAdminHome.jsx    # Domain admin dashboard
│   │   ├── DomainReports.jsx      # Report management
│   │   ├── DomainSurveys.jsx      # Survey management
│   │   └── DomainTraits.jsx       # Trait management
│   └── sys_admin_pages/           # System admin pages
│       ├── Accounts.jsx           # Account management
│       ├── CreateAccount.jsx      # Account creation
│       ├── Settings.jsx           # System settings
│       ├── Surveys.jsx            # System analytics
│       └── SysAdminHome.jsx       # System admin dashboard
└── services/                      # API service layer
    └── api.js                     # Complete API integration
```

## Key Features

### Account Management
- Account authentication and registration
- Role-based access control (Account, Domain Admin, System Admin)
- Profile management and settings
- Account dashboard with role-specific content

### 360-Degree Feedback System
- Survey creation and management interface
- Subject and respondent management
- Feedback collection and submission
- Real-time progress tracking
- Anonymous feedback handling

### Analytics & Reporting
- Interactive dashboards
- Data visualization and charts
- Report generation and export
- Performance metrics display

### Billing & Usage Tracking
- Survey usage monitoring
- Billing records and payment status
- Usage statistics and summaries

## Technology Stack

- **Framework**: React 18
- **Build Tool**: Vite
- **Routing**: React Router v6
- **State Management**: React Context API
- **Styling**: CSS3 with custom styles
- **Icons**: Heroicons
- **HTTP Client**: Fetch API
- **Authentication**: JWT tokens

## Application Architecture

### Page Structure

#### Account Management Pages
- **AccountHome.jsx** - Account dashboard and overview
- **ProfileUpdate.jsx** - Account profile management
- **RunSurvey.jsx** - Survey execution interface
- **Survey.jsx** - Survey participation interface

#### Domain Admin Pages
- **DomainAdminHome.jsx** - Domain admin dashboard
- **CreateSurvey.jsx** - Survey creation interface
- **CreateTrait.jsx** - Competency/trait management
- **CreateAccount.jsx** - Account creation for domain
- **DefineReport.jsx** - Report template creation
- **DomainSurveys.jsx** - Survey management interface
- **DomainTraits.jsx** - Trait/competency management
- **DomainReports.jsx** - Report management interface

#### System Admin Pages
- **SysAdminHome.jsx** - System admin dashboard
- **Accounts.jsx** - Account management interface
- **Settings.jsx** - System settings management
- **Surveys.jsx** - System-wide survey analytics

### Component Structure

#### Core Components
- **Layout.jsx** - Main application layout wrapper
- **Sidebar.jsx** - Role-based navigation sidebar
- **Login.jsx** - Authentication interface

#### Modal Components
- **CreateSubjectModal.jsx** - Subject creation interface
- **CreateRespondantModal.jsx** - Respondent creation interface
- **CreateSurveyModal.jsx** - Quick survey creation modal

### Context Providers

#### AuthContext
- Account authentication state management
- Role-based access control
- JWT token handling
- Account profile data

## User Roles & Access Control

### Account Role
- **Access**: Own subjects, respondents, surveys, and billing records
- **Capabilities**:
  - Manage personal subjects and respondents
  - Participate in surveys as subject or respondent
  - View own survey results and feedback
  - Access personal billing information
  - Update profile and account settings

### Domain Admin Role
- **Access**: Domain-specific surveys, traits, reports, and accounts
- **Capabilities**:
  - Create and manage surveys within domain
  - Define competencies and traits
  - Generate reports and analytics
  - Manage accounts within domain
  - Monitor survey progress and completion

### System Admin Role
- **Access**: System-wide administration and management
- **Capabilities**:
  - Manage all accounts across the platform
  - Configure system settings and parameters
  - Access comprehensive analytics and reports
  - Monitor system health and performance
  - Manage billing and usage tracking

## Routing Structure

### Public Routes
- `/login` - Account authentication

### Protected Routes (Account)
- `/` - Role-based home dashboard
- `/profile` - Account profile management
- `/run-survey` - Survey execution interface

### Protected Routes (Domain Admin)
- `/create-survey` - Survey creation
- `/create-trait` - Trait/competency management
- `/create-account` - Account creation
- `/reports` - Report definition
- `/domain-surveys` - Survey management
- `/domain-traits` - Trait management
- `/domain-reports` - Report management

### Protected Routes (System Admin)
- `/account-management` - Account administration
- `/system-settings` - System configuration
- `/analytics` - System analytics

## State Management

### Authentication State
- Account login status
- Account profile information
- Role-based permissions
- JWT token management

### Application State
- Current route and navigation
- Modal visibility and state
- Form data and validation
- Loading and error states

## API Integration

### ✅ Complete API Service Layer
- **`services/api.js`** - Complete API service layer with 89 endpoints across 12 modules
- **Real Backend Integration** - All API calls connect to Flask backend at `http://localhost:5000/api`
- **Authentication System** - JWT-based authentication with automatic token management
- **Error Handling** - Standardized error processing and user feedback

### API Modules (89 Total Endpoints)

#### Authentication & Account Management (14 endpoints)
- **authAPI**: login, logout, register, getCurrentUser, updateProfile, forgotPassword, resetPassword
- **accountsAPI**: getAll, create, getById, update, updateStatus, delete

#### Core Business Logic (32 endpoints)
- **surveysAPI**: getAll, create, getById, update, delete, updateStatus, getAvailable, getMySurveys, submitResponses, getResponses, runSurvey
- **traitsAPI**: getAll, create, getById, update, delete, updateStatus, getCategories, getUsage
- **reportsAPI**: getAll, create, getById, update, delete, generate, getInstances, updateStatus
- **subjectsAPI**: getAll, create, getById, update, delete

#### Advanced Features (43 endpoints)
- **respondentsAPI**: getAll, create, getById, update, delete
- **dashboardAPI**: getStats, getActivity, getAnalytics
- **settingsAPI**: getAll, update, toggle, reset, getCategories
- **billingAPI**: getAll, getById, getByAccount, getSummary, calculate
- **notificationsAPI**: getAll, markAsRead, create, delete
- **filesAPI**: upload, download, delete

### API Features
- **Automatic Authentication**: JWT token handling in all requests
- **Error Handling**: Standardized error processing with user-friendly messages
- **File Upload**: Multipart form data support for file operations
- **Pagination**: Built-in pagination support for list endpoints
- **Query Parameters**: URL parameter building for filtering and sorting

## Component Guidelines

### API Integration Pattern
```jsx
import React, { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { surveysAPI } from '../services/api';

const ComponentName = () => {
  const { user, isAccount, isDomainAdmin, isSystemAdmin } = useAuth();
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await surveysAPI.getAll();
        if (response.success) {
          setData(response.data);
        } else {
          setError(response.error?.message || 'Failed to fetch data');
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="component-container">
      {/* Component JSX with real data */}
    </div>
  );
};

export default ComponentName;
```

### Styling Conventions
- Use CSS classes with descriptive names
- Follow BEM methodology for complex components
- Maintain consistent spacing and typography
- Use CSS custom properties for theme values

### Error Handling
- Implement proper error boundaries
- Display user-friendly error messages
- Log errors for debugging purposes
- Provide fallback UI for failed states

## Development Guidelines

1. **Component Design**
   - Keep components focused and single-purpose
   - Use functional components with hooks
   - Implement proper prop validation
   - Follow React best practices

2. **State Management**
   - Use local state for component-specific data
   - Use context for shared application state
   - Minimize state complexity and nesting
   - Implement proper state updates

3. **Performance**
   - Use React.memo for expensive components
   - Implement proper dependency arrays in hooks
   - Optimize re-renders and API calls
   - Use code splitting for large components

4. **Accessibility**
   - Implement proper ARIA attributes
   - Ensure keyboard navigation support
   - Use semantic HTML elements
   - Test with screen readers

## Environment Configuration

### ✅ Current Configuration (`.env`)
```env
# API Configuration
VITE_API_BASE_URL=http://localhost:5000/api

# Application Configuration
VITE_APP_NAME=IkeNei
VITE_APP_VERSION=1.0.0

# Development Settings
VITE_NODE_ENV=development
```

### Backend Connection
- **API Base URL**: `http://localhost:5000/api`
- **Authentication**: JWT tokens stored in localStorage
- **CORS**: Backend configured to accept requests from `http://localhost:5173`
- **Error Handling**: Automatic token refresh and error recovery

## Build & Deployment

### Development
```bash
npm install          # Install dependencies
npm run dev         # Start development server
npm run lint        # Run ESLint
npm run test        # Run tests
```

### Production
```bash
npm run build       # Build for production
npm run preview     # Preview production build
npm run deploy      # Deploy to hosting platform
```

### Build Configuration
- **Vite**: Fast build tool with HMR
- **ESLint**: Code quality and consistency
- **PostCSS**: CSS processing and optimization
- **Environment Variables**: Configuration management

## Testing Strategy

### Unit Testing
- Component rendering tests
- Hook functionality tests
- Utility function tests
- API integration tests

### Integration Testing
- User workflow tests
- Authentication flow tests
- Role-based access tests
- Form submission tests

### E2E Testing
- Complete user journeys
- Cross-browser compatibility
- Performance testing
- Accessibility testing

## Security Considerations

### ✅ Implemented Security Features

#### Authentication & Authorization
- **JWT Token Management**: Automatic token storage and inclusion in API requests
- **Token Validation**: Real-time session validation with backend on app load
- **Role-Based Access**: Proper role checking (account, domain_admin, system_admin)
- **Secure Logout**: Complete token cleanup and session termination

#### API Security
- **HTTPS Ready**: Secure API communication in production
- **Error Handling**: No sensitive data exposure in error messages
- **Token Refresh**: Automatic token validation and refresh
- **Request Authentication**: Bearer token authentication on all protected endpoints

#### Data Protection
- **Input Validation**: Client-side validation before API calls
- **XSS Prevention**: Proper data sanitization and React's built-in protection
- **Secure Storage**: JWT tokens stored securely in localStorage
- **Session Management**: Automatic cleanup of invalid sessions

## Performance Optimization

### Code Splitting
- Route-based code splitting
- Component lazy loading
- Dynamic imports for large libraries
- Bundle size optimization

### Caching Strategy
- API response caching
- Static asset caching
- Browser storage optimization
- CDN integration

### Monitoring
- Performance metrics tracking
- Error logging and reporting
- User interaction analytics
- Load time optimization

## Getting Started

### Prerequisites
- **Node.js** (v18 or higher) - [Download here](https://nodejs.org/)
- **Python** (v3.8 or higher) - [Download here](https://python.org/)
- **MongoDB** (v5.0 or higher) - [Download here](https://mongodb.com/try/download/community)

### Complete Setup & Testing Guide

#### Step 1: Clone and Setup Project
```bash
# Clone the repository
git clone https://github.com/balu72/IkeNei.git
cd IkeNei
```

#### Step 2: Setup Backend (Flask API)
```bash
# Navigate to backend directory
cd src/backend

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Verify environment variables
cat .env
# Should show:
# FLASK_ENV=development
# FLASK_APP=app.py
# MONGODB_URI=mongodb://localhost:27017/ikenei
# JWT_SECRET_KEY=jwt-secret-string-change-in-production
```

#### Step 3: Setup MongoDB Database
```bash
# Start MongoDB service
# On macOS (with Homebrew):
brew services start mongodb-community

# On Linux:
sudo systemctl start mongod

# On Windows:
# Start MongoDB as a Windows service or run mongod.exe

# Verify MongoDB is running
mongosh
# Should connect to MongoDB shell
# Type 'exit' to quit
```

#### Step 4: Start Backend Server
```bash
# Make sure you're in src/backend directory
cd src/backend

# Activate virtual environment if not already active
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Start Flask development server
python app.py

# You should see:
# * Running on http://127.0.0.1:5000
# * Debug mode: on
```

#### Step 5: Setup Frontend (React App)
```bash
# Open a new terminal window/tab
# Navigate to frontend directory
cd src/frontend

# Install Node.js dependencies
npm install

# Verify environment configuration
cat .env
# Should show:
# VITE_API_BASE_URL=http://localhost:5000/api
# VITE_APP_NAME=IkeNei
# VITE_APP_VERSION=1.0.0
```

#### Step 6: Start Frontend Development Server
```bash
# Make sure you're in src/frontend directory
cd src/frontend

# Start Vite development server
npm run dev

# You should see:
# Local:   http://localhost:5173/
# Network: use --host to expose
```

#### Step 7: Access and Test Application

1. **Open Browser**
   - Navigate to: `http://localhost:5173`
   - You should see the IkeNei login page

2. **Test Authentication**
   ```
   Demo Login Credentials:
   
   Account Role:
   Email: account@example.com
   Password: password
   
   Domain Admin Role:
   Email: domainadmin@example.com  
   Password: password
   
   System Admin Role:
   Email: systemadmin@example.com
   Password: password
   ```

3. **Verify API Connection**
   - Open browser Developer Tools (F12)
   - Go to Network tab
   - Login with any demo credentials
   - You should see API calls to `http://localhost:5000/api/auth/login`

#### Step 8: Test Different User Roles

**Account Role Testing:**
1. Login with `account@example.com`
2. Should redirect to Account Dashboard
3. Test navigation: Profile, Run Survey
4. Verify sidebar shows account-specific options

**Domain Admin Role Testing:**
1. Login with `domainadmin@example.com`
2. Should redirect to Domain Admin Dashboard
3. Test navigation: Create Survey, Create Trait, Reports
4. Verify sidebar shows domain admin options

**System Admin Role Testing:**
1. Login with `systemadmin@example.com`
2. Should redirect to System Admin Dashboard
3. Test navigation: Account Management, Settings, Analytics
4. Verify sidebar shows system admin options

### Development Workflow

#### Daily Development Process
```bash
# Terminal 1: Start MongoDB (if not running as service)
mongod

# Terminal 2: Start Backend
cd src/backend
source venv/bin/activate  # Activate virtual environment
python app.py

# Terminal 3: Start Frontend
cd src/frontend
npm run dev

# Terminal 4: Development work
# Make your code changes here
```

#### Testing API Integration
1. **Check Backend Health**
   ```bash
   curl http://localhost:5000/api/auth/login
   # Should return method not allowed (needs POST)
   ```

2. **Test Authentication**
   ```bash
   curl -X POST http://localhost:5000/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email":"account@example.com","password":"password"}'
   ```

3. **Monitor Network Traffic**
   - Open browser DevTools → Network tab
   - Login and navigate through the app
   - Verify API calls are being made to backend

#### Troubleshooting Common Issues

**Backend Issues:**
```bash
# Port 5000 already in use
lsof -ti:5000 | xargs kill -9

# MongoDB connection issues
mongosh --eval "db.adminCommand('ping')"

# Python dependencies issues
pip install -r requirements.txt --force-reinstall
```

**Frontend Issues:**
```bash
# Port 5173 already in use
lsof -ti:5173 | xargs kill -9

# Node modules issues
rm -rf node_modules package-lock.json
npm install

# Clear Vite cache
rm -rf node_modules/.vite
```

**API Connection Issues:**
- Verify backend is running on port 5000
- Check CORS settings in backend
- Verify `.env` file has correct API URL
- Check browser console for CORS errors

### Production Deployment

#### Backend Deployment
```bash
# Set production environment variables
export FLASK_ENV=production
export MONGODB_URI=your-production-mongodb-uri
export JWT_SECRET_KEY=your-secure-jwt-secret

# Install production dependencies
pip install -r requirements.txt

# Run with production WSGI server
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Frontend Deployment
```bash
# Build for production
npm run build

# Preview production build locally
npm run preview

# Deploy dist/ folder to your hosting service
# (Netlify, Vercel, AWS S3, etc.)
```

### Testing Checklist

#### ✅ Backend Testing
- [ ] MongoDB connection successful
- [ ] Flask server starts without errors
- [ ] API endpoints respond correctly
- [ ] JWT authentication works
- [ ] CORS headers are set properly

#### ✅ Frontend Testing
- [ ] Vite dev server starts successfully
- [ ] Login page loads correctly
- [ ] Authentication flow works
- [ ] Role-based routing works
- [ ] API calls are successful
- [ ] Error handling displays properly

#### ✅ Integration Testing
- [ ] Login with all three user roles
- [ ] Navigation works for each role
- [ ] API calls show in Network tab
- [ ] JWT tokens are stored and sent
- [ ] Logout clears authentication
- [ ] Protected routes redirect properly

### Performance Monitoring
- **Backend**: Monitor Flask logs for API response times
- **Frontend**: Use React DevTools Profiler
- **Network**: Monitor API call performance in DevTools
- **Database**: Use MongoDB Compass for query performance
## Current Implementation Status

### ✅ Completed API Integration
- **Authentication System**: Fully integrated with backend JWT authentication
- **API Service Layer**: Complete service layer with 89 endpoints
- **Error Handling**: Standardized error processing and user feedback
- **Environment Configuration**: Proper API base URL configuration

### 🔄 Component Integration Status
- **Login Component**: ✅ Fully integrated (uses AuthContext with real API)
- **AuthContext**: ✅ Fully integrated with backend authentication
- **Dashboard Components**: 🔄 Ready for API integration (use `dashboardAPI`)
- **CreateSurvey**: 🔄 Ready for API integration (use `surveysAPI`, `traitsAPI`)
- **Account Management**: 🔄 Ready for API integration (use `accountsAPI`)
- **Settings**: 🔄 Ready for API integration (use `settingsAPI`)

### Next Steps for Full Integration
1. Update dashboard components to use `dashboardAPI.getStats()`
2. Update CreateSurvey to use `surveysAPI.create()` and `traitsAPI.getAll()`
3. Update account management pages to use `accountsAPI` methods
4. Update settings pages to use `settingsAPI` methods
5. Add proper loading states and error handling to all components

### Development Workflow
1. **Start Backend**: `cd src/backend && python app.py`
2. **Start Frontend**: `cd src/frontend && npm run dev`
3. **Test Integration**: Login with demo credentials and test API calls
4. **Monitor Network**: Use browser dev tools to verify API requests

## Troubleshooting

### Common Issues
- **Build Errors**: Check dependency versions and compatibility
- **API Errors**: Verify backend server is running and accessible
- **Authentication Issues**: Check JWT token validity and storage
- **Routing Problems**: Verify route configuration and protection

### Debug Tools
- React Developer Tools
- Browser Network tab
- Console logging
- Vite development server logs

## Contributing

1. Follow the established code style and conventions
2. Write comprehensive tests for new features
3. Update documentation for significant changes
4. Use descriptive commit messages
5. Submit pull requests for review
