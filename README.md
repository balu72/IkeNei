### IkeNei

A comprehensive 360-degree feedback and survey management platform that helps individuals and organizations drive professional development through data-driven insights.

## 🚀 Overview

IkeNei is an innovative tool that combines traditional 360-degree feedback methodologies with data analytics to deliver comprehensive feedback insights. The platform enables accounts to gather feedback from subjects and respondents, then leverages analytics to provide detailed reports and insights that accelerate professional growth.

## ✨ Key Features

### 🔐 Account Management
- **Secure Registration & Authentication**: Easy onboarding with robust security measures
- **Role-based Access Control**: Three distinct account roles (Account, Domain Admin, System Admin)
- **Profile Management**: Comprehensive account profiles with organizational information

### 📊 360-Degree Feedback System
- **Multi-source Feedback Collection**: Gather insights from supervisors, peers, direct reports, and self-assessments
- **Customizable Assessment Templates**: Industry-specific and role-based feedback questionnaires
- **Anonymous Feedback Options**: Ensure honest and constructive feedback
- **Real-time Progress Tracking**: Monitor feedback collection status and completion rates

### 📊 Subject & Respondent Management
- **Subject Management**: Manage individuals being assessed within each account
- **Respondent Management**: Organize feedback providers for each subject
- **Relationship Mapping**: Define relationships between subjects and respondents
- **Feedback Collection**: Streamlined process for gathering multi-source feedback

### 📈 Analytics & Reporting
- **Comprehensive Dashboards**: Visual insights into feedback trends and survey results
- **Competency Mapping**: Track skills assessment across various competencies
- **Survey Analytics**: Detailed analysis of survey responses and patterns
- **Export Capabilities**: Generate reports for management and organizational review

### 💰 Billing & Usage Tracking
- **Survey Usage Monitoring**: Track surveys conducted by each account
- **Billing Management**: Automated billing based on survey usage
- **Usage Analytics**: Detailed statistics on platform utilization
- **Payment Processing**: Secure billing and payment status tracking

## 👥 Account Roles

### 🎯 Account
- **Primary role** managing subjects and respondents
- **Survey execution** and feedback collection
- **Access to** survey results and feedback reports
- **Subject/respondent management** and relationship tracking

### 👨‍💼 Domain Admin
- **Manages accounts** within their domain
- **Survey creation** and template management
- **Competency definition** and trait management
- **Domain-level analytics** and reporting

### ⚙️ System Admin
- **System administration** and account management
- **Platform-wide analytics** and reporting
- **Configuration** of system settings and parameters
- **Billing management** and usage monitoring

## 🛠️ Technology Stack

### Frontend
- **Framework**: React with Vite
- **Styling**: Custom CSS with magenta theme
- **State Management**: React Context API
- **Routing**: React Router
- **Icons**: Heroicons
- **Testing**: Jest and Cypress

### Backend
- **Runtime**: Python
- **Framework**: Flask
- **Authentication**: JWT (JSON Web Tokens)
- **Testing**: Pytest
- **Documentation**: OpenAPI/Swagger

### Database & Storage
- **Primary Database**: MongoDB
- **ORM**: SQLAlchemy
- **Caching**: Redis
- **Data Security**: Encryption in transit and at rest

### Analytics & Insights
- **Data Processing**: Python-based analytics
- **Feedback Analysis**: Statistical analysis and pattern recognition
- **Survey Analytics**: Comprehensive survey response analysis
- **Reporting Engine**: Automated report generation

### Infrastructure & Security
- **Containerization**: Docker
- **Security**: Enterprise-grade security measures
- **Privacy Compliance**: GDPR compliant
- **Monitoring**: Application performance monitoring

## 📁 Project Structure

```
IkeNei/
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
└── src/
    ├── backend/                 # Python/Flask backend API
    │   ├── app.py               # Main Flask application
    │   ├── config.py            # Application configuration
    │   ├── requirements.txt     # Python dependencies
    │   ├── README.md            # Backend documentation
    │   ├── IMPLEMENTATION_STATUS.md # Implementation progress
    │   ├── controllers/         # API route handlers
    │   │   ├── accounts_controller.py
    │   │   ├── analytics_controller.py
    │   │   ├── auth_controller.py
    │   │   ├── billing_controller.py
    │   │   ├── categories_controller.py
    │   │   ├── dashboard_controller.py
    │   │   ├── files_controller.py
    │   │   ├── notifications_controller.py
    │   │   ├── reports_controller.py
    │   │   ├── respondents_controller.py
    │   │   ├── settings_controller.py
    │   │   ├── subjects_controller.py
    │   │   ├── surveys_controller.py
    │   │   └── traits_controller.py
    │   ├── middleware/           # Authentication & request middleware
    │   │   └── auth_middleware.py
    │   └── routes/              # API route definitions
    │       ├── accounts_routes.py
    │       ├── analytics_routes.py
    │       ├── auth_routes.py
    │       ├── billing_routes.py
    │       ├── categories_routes.py
    │       ├── dashboard_routes.py
    │       ├── files_routes.py
    │       ├── notifications_routes.py
    │       ├── reports_routes.py
    │       ├── respondents_routes.py
    │       ├── settings_routes.py
    │       ├── subjects_routes.py
    │       ├── surveys_routes.py
    │       └── traits_routes.py
    ├── database/                # MongoDB database layer
    │   ├── README.md            # Database documentation
    │   ├── SETUP.md             # Database setup instructions
    │   ├── base_model.py        # Base model class
    │   ├── connection.py        # Database connection
    │   ├── config/              # Database configuration
    │   │   ├── docker-compose.yml # MongoDB Docker setup
    │   │   └── mongo-init.js    # MongoDB initialization
    │   ├── models/              # Data models
    │   │   ├── account_model.py
    │   │   ├── respondent_model.py
    │   │   ├── subject_model.py
    │   │   ├── survey_model.py
    │   │   └── trait_model.py
    │   ├── repositories/        # Data access layer
    │   │   ├── account_repository.py
    │   │   ├── respondent_repository.py
    │   │   ├── subject_repository.py
    │   │   ├── survey_repository.py
    │   │   └── trait_repository.py
    │   └── seeds/               # Sample data
    │       └── development_seeds.py
    ├── frontend/                # React frontend application
    │   ├── package.json         # Frontend dependencies
    │   ├── package-lock.json    # Dependency lock file
    │   ├── vite.config.js       # Vite configuration
    │   ├── eslint.config.js     # ESLint configuration
    │   ├── README.md            # Frontend documentation
    │   ├── .gitignore           # Frontend git ignore
    │   ├── index.html           # HTML template
    │   ├── main.jsx             # Application entry point
    │   ├── App.jsx              # Main application component
    │   ├── App.css              # Application styles
    │   ├── index.css            # Global styles
    │   ├── components/          # Reusable React components
    │   │   ├── CreateRespondantModal.jsx
    │   │   ├── CreateSubjectModal.jsx
    │   │   ├── CreateSurveyModal.jsx
    │   │   ├── Layout.jsx
    │   │   ├── Login.jsx
    │   │   └── Sidebar.jsx
    │   ├── contexts/            # React context providers
    │   │   └── AuthContext.jsx
    │   ├── pages/               # Page components
    │   │   ├── Home.jsx
    │   │   ├── account_management_pages/
    │   │   │   ├── AccountHome.jsx
    │   │   │   ├── ProfileUpdate.jsx
    │   │   │   ├── RunSurvey.jsx
    │   │   │   └── Survey.jsx
    │   │   ├── domain_admin_pages/
    │   │   │   ├── CreateSurvey.jsx
    │   │   │   ├── CreateTrait.jsx
    │   │   │   ├── DefineReport.jsx
    │   │   │   ├── DomainAdminHome.jsx
    │   │   │   ├── DomainReports.jsx
    │   │   │   ├── DomainSurveys.jsx
    │   │   │   └── DomainTraits.jsx
    │   │   └── sys_admin_pages/
    │   │       ├── Accounts.jsx
    │   │       ├── CreateAccount.jsx
    │   │       ├── Settings.jsx
    │   │       ├── Surveys.jsx
    │   │       └── SysAdminHome.jsx
    │   └── services/            # API service layer
    │       └── api.js
    └── utils/                   # Shared utilities
        ├── logger.py            # Logging utilities
        ├── pagination.py        # Pagination helpers
        ├── response_helpers.py  # API response helpers
        └── route_logger.py      # Route logging middleware
```

## 🚀 Getting Started

### Prerequisites
- **Node.js** (v18 or higher)
- **Python** (v3.9 or higher)
- **MongoDB** (v5.0 or higher)
- **Git** for version control

### Development Setup

1. **Clone the repository**
   ```bash
   git clon https://github.com/balu72/IkeNei.git
   cd IkeNei
   ```

2. **Frontend Setup**
   ```bash
   cd src/frontend
   npm install
   npm run dev
   ```

3. **Backend Setup**
   ```bash
   cd src/backend
   pip install flask flask-cors flask-jwt-extended python-dotenv
   python app.py
   ```
   Backend will start on `http://localhost:5000`

4. **API Integration**
   - Frontend automatically connects to backend at `http://localhost:5000/api`
   - All API endpoints are functional with mock data
   - JWT authentication is implemented and working
   - Demo users available for testing all roles

### Demo Access

The frontend includes demo credentials for testing:
- **Account**: account@example.com / password
- **Domain Admin**: domainadmin@example.com / password
- **System Admin**: sysadmin@example.com / password

## 📋 How It Works

### Step 1: Account Setup
- Create your account with organizational information
- Set up subjects and respondents within your account
- Define relationships and feedback networks

### Step 2: Survey Creation & Management
- Create customized surveys and feedback forms
- Define competencies and traits for assessment
- Configure survey settings and parameters

### Step 3: Feedback Collection
- Launch surveys with selected subjects and respondents
- Monitor collection progress and completion rates
- Ensure anonymous and confidential feedback submission

### Step 4: Analytics & Reporting
- Access comprehensive feedback analysis and insights
- Generate detailed reports on survey results
- Track competency assessments and development areas
- Export data for organizational review and planning

## 🏗️ Architecture Overview

The IkeNei follows a layered architecture pattern:

1. **Presentation Layer** (`frontend/`) - User interface and user experience
2. **Business Logic Layer** (`backend/`) - API endpoints, business rules, and data processing
3. **Data Layer** (`database/`) - Data storage, retrieval, and management
4. **Shared Layer** (`shared/`) - Common utilities, types, and constants
5. **Testing Layer** (`tests/`) - Comprehensive test coverage
6. **Documentation Layer** (`docs/`) - Technical specifications and guides

## � Privacy & Security

- **Data Encryption**: All data encrypted in transit and at rest
- **Privacy Compliance**: GDPR and other privacy regulation compliant
- **Anonymous Feedback**: Option for completely anonymous feedback submission
- **Access Controls**: Strict role-based access to sensitive information
- **Audit Trails**: Complete logging of all system activities

## 🧪 Development Guidelines

- Each layer should be loosely coupled and highly cohesive
- Use the shared directory for code that needs to be used across multiple layers
- Follow consistent naming conventions across all directories
- Maintain comprehensive test coverage for all business logic
- Document all APIs and architectural decisions

## 🔄 Roadmap

### ✅ Completed
- Frontend application with role-based authentication
- User persona system (Assessee, Coach, Admin)
- Responsive UI with magenta theme
- Basic navigation and dashboard structure

### ✅ Recently Completed
- **Complete Backend API**: 13 controllers with full CRUD operations
- **Frontend-Backend Integration**: Frontend now calls backend REST APIs
- **Authentication System**: JWT-based authentication with role management
- **Mock Data Implementation**: Comprehensive mock data for testing
- **API Service Layer**: Centralized API calls with error handling

### 🚧 In Progress
- Database integration (replacing mock data with MongoDB)
- JWT middleware implementation for protected routes
- Input validation and sanitization

### 📅 Upcoming Features
- Mobile application for iOS and Android
- Integration with popular HRIS systems
- Advanced analytics and insights
- Team-based feedback and organizational reporting
- Multi-language support
- API for third-party integrations

## 📞 Support & Contact

- **Documentation**: Comprehensive user guides and tutorials
- **Help Center**: FAQ and troubleshooting resources
- **Customer Support**: Dedicated support team for technical assistance
- **Training**: Onboarding and training sessions for organizations

## 📄 License

This project is proprietary software. All rights reserved.

## 🤝 Contributing

For information about contributing to this project or partnership opportunities, please contact our development team.

---

**Transform your professional development with comprehensive 360-degree feedback and data-driven insights.**

*IkeNei - Where feedback meets analytics for organizational growth.*
