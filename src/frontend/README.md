# Frontend Layer - IkeNei

This directory contains the React frontend application for the IkeNei 360-degree feedback and survey management platform.

## Directory Structure

```
frontend/
├── components/         # Reusable UI components
├── pages/             # Page components organized by user roles
├── contexts/          # React context providers
├── assets/            # Static assets (images, icons, etc.)
├── public/            # Public static files
├── src/               # Source code
└── config/            # Configuration files
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

### Authentication Endpoints
- `POST /api/auth/login` - Account login
- `POST /api/auth/register` - Account registration
- `GET /api/auth/me` - Get account profile
- `PUT /api/auth/profile` - Update account profile

### Account Management
- `GET /api/accounts` - List accounts (System Admin)
- `POST /api/accounts` - Create account
- `PUT /api/accounts/{id}` - Update account
- `DELETE /api/accounts/{id}` - Delete account

### Survey Management
- `GET /api/surveys` - List surveys
- `POST /api/surveys` - Create survey
- `GET /api/surveys/{id}` - Get survey details
- `POST /api/surveys/{id}/responses` - Submit responses

### Subject & Respondent Management
- `GET /api/subjects` - List account subjects
- `POST /api/subjects` - Create subject
- `GET /api/respondents` - List subject respondents
- `POST /api/respondents` - Create respondent

### Billing & Usage
- `GET /api/billing/account/{id}` - Get account billing records
- `GET /api/billing/summary` - Get billing summary

## Component Guidelines

### Component Structure
```jsx
import React, { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';

const ComponentName = () => {
  const { account, isAccount, isDomainAdmin, isSystemAdmin } = useAuth();
  const [state, setState] = useState(initialState);

  useEffect(() => {
    // Component initialization
  }, []);

  return (
    <div className="component-container">
      {/* Component JSX */}
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

```env
# API Configuration
VITE_API_BASE_URL=http://localhost:5000/api
VITE_APP_NAME=IkeNei
VITE_APP_VERSION=1.0.0

# Authentication
VITE_JWT_STORAGE_KEY=ikenei_token
VITE_TOKEN_REFRESH_INTERVAL=300000

# Feature Flags
VITE_ENABLE_ANALYTICS=true
VITE_ENABLE_BILLING=true
VITE_ENABLE_NOTIFICATIONS=true
```

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

### Authentication
- JWT token storage and management
- Automatic token refresh
- Secure logout functionality
- Session timeout handling

### Authorization
- Role-based route protection
- Component-level access control
- API endpoint authorization
- Data visibility restrictions

### Data Protection
- Input validation and sanitization
- XSS prevention measures
- CSRF protection
- Secure API communication

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

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your configuration
   ```

3. **Start Development Server**
   ```bash
   npm run dev
   ```

4. **Access Application**
   - Open browser to `http://localhost:3000`
   - Use test account credentials for development

5. **Development Workflow**
   - Make changes to components
   - Test in browser with HMR
   - Run linting and tests
   - Commit changes with descriptive messages

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
