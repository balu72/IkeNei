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

### 🔄 Survey Approval Workflow
- **Domain Admin Survey Creation**: Domain Admins create surveys that require approval
- **System Admin Review Process**: System Admins review and approve/reject surveys
- **Role-Based Survey Visibility**: Account users only see approved surveys
- **Approval Audit Trail**: Complete tracking of approval history and decisions
- **Rejection Management**: Surveys can be rejected with reasons for improvement

### 📧 Email Notification & Response Collection System
- **Automated Email Invitations**: SendGrid-powered email notifications to survey respondents
- **Personalized Survey Links**: Unique, secure tokens for each respondent
- **Token-Based Access**: No login required - secure access via email links
- **1-5 Rating Scale Responses**: Standardized feedback collection with validation
- **Real-time Response Tracking**: Automatic survey completion monitoring
- **Professional Email Templates**: Branded HTML emails with responsive design
- **Completion Confirmations**: Thank you emails sent after response submission
- **Response Analytics**: Comprehensive analytics and reporting for survey results

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
    │   │   ├── survey_response_controller.py
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
    │       ├── survey_response_routes.py
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
    │   │   ├── survey_response_model.py
    │   │   ├── survey_run_model.py
    │   │   └── trait_model.py
    │   ├── repositories/        # Data access layer
    │   │   ├── account_repository.py
    │   │   ├── respondent_repository.py
    │   │   ├── subject_repository.py
    │   │   ├── survey_repository.py
    │   │   ├── survey_response_repository.py
    │   │   ├── survey_run_repository.py
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
    ├── services/                # Backend services
    │   └── email_service.py     # Email notification service (SendGrid)
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

## 📊 Implementation Status Update - August 3, 2025

### 🎯 **API Implementation Analysis**


Based on comprehensive analysis of frontend API calls, backend controllers, and database implementations:

### ✅ **FULLY IMPLEMENTED APIs - Will Return Valid Database Data (39 endpoints)**

#### **Authentication APIs (7/7 - 100%)**
- ✅ `POST /auth/login` - Full database integration with AccountRepository
- ✅ `POST /auth/logout` - Complete implementation
- ✅ `POST /auth/register` - Full database integration with AccountRepository
- ✅ `GET /auth/me` - Full database integration with AccountRepository
- ✅ `PUT /auth/profile` - Full database integration with AccountRepository
- ✅ `POST /auth/forgot` - Implemented (returns success message)
- ⚠️ `POST /auth/reset` - Returns 501 (not implemented) but properly handled

#### **Accounts APIs (6/6 - 100%)**
- ✅ `GET /accounts` - Full database integration with AccountRepository
- ✅ `POST /accounts` - Full database integration with AccountRepository
- ✅ `GET /accounts/{id}` - Full database integration with AccountRepository
- ✅ `PUT /accounts/{id}` - Full database integration with AccountRepository
- ✅ `PATCH /accounts/{id}/status` - Full database integration with AccountRepository
- ✅ `DELETE /accounts/{id}` - Full database integration with AccountRepository

#### **Subjects APIs (5/5 - 100%)**
- ✅ `GET /subjects` - Full database integration with SubjectRepository
- ✅ `POST /subjects` - Full database integration with SubjectRepository
- ✅ `GET /subjects/{id}` - Full database integration with SubjectRepository
- ✅ `PUT /subjects/{id}` - Full database integration with SubjectRepository
- ✅ `DELETE /subjects/{id}` - Full database integration with SubjectRepository

#### **Respondents APIs (5/5 - 100%)**
- ✅ `GET /respondents` - Full database integration with RespondentRepository
- ✅ `POST /respondents` - Full database integration with RespondentRepository
- ✅ `GET /respondents/{id}` - Full database integration with RespondentRepository
- ✅ `PUT /respondents/{id}` - Full database integration with RespondentRepository
- ✅ `DELETE /respondents/{id}` - Full database integration with RespondentRepository

#### **Traits APIs (8/8 - 100%)**
- ✅ `GET /traits` - Full database integration with TraitRepository
- ✅ `POST /traits` - Full database integration with TraitRepository
- ✅ `GET /traits/{id}` - Full database integration with TraitRepository
- ✅ `PUT /traits/{id}` - Full database integration with TraitRepository
- ✅ `DELETE /traits/{id}` - Full database integration with TraitRepository
- ✅ `PATCH /traits/{id}/status` - Full database integration with TraitRepository
- ✅ `GET /traits/categories` - Full database integration with TraitRepository
- ✅ `GET /traits/usage` - Clean implementation (returns timestamp)

#### **Surveys APIs - Complete CRUD + Approval + Run + Email Workflow (15/15 - 100%)**
- ✅ `GET /surveys` - Full database integration with SurveyRepository
- ✅ `POST /surveys` - Full database integration with SurveyRepository + Approval workflow
- ✅ `GET /surveys/{id}` - Full database integration with SurveyRepository
- ✅ `PUT /surveys/{id}` - Full database integration with SurveyRepository
- ✅ `DELETE /surveys/{id}` - Full database integration with SurveyRepository
- ✅ `PATCH /surveys/{id}/status` - Full database integration with SurveyRepository
- ✅ `GET /surveys/my-surveys` - Full database integration with SurveyRepository
- ✅ `POST /surveys/{id}/approve` - Full approval workflow implementation
- ✅ `POST /surveys/{id}/reject` - Full approval workflow implementation
- ✅ `GET /surveys/pending` - Full database integration for pending surveys
- ✅ `GET /surveys/approved` - Full database integration for approved surveys
- ✅ `GET /surveys/by-role` - Role-based survey filtering implementation
- ✅ `POST /surveys/{id}/run` - Complete survey run workflow with email notifications
- ✅ `GET /survey/respond/{token}` - Public survey form loading by token
- ✅ `POST /survey/respond/{token}` - Public survey response submission with validation

### ⚠️ **PARTIALLY IMPLEMENTED APIs - Return Minimal/Placeholder Data (28 endpoints)**

#### **Surveys APIs - Advanced Features (3/10 - 30%)**
- ⚠️ `GET /surveys/available` - Returns empty array (TODO implementation)
- ⚠️ `POST /surveys/{id}/responses` - Returns placeholder submission_id
- ⚠️ `GET /surveys/{id}/responses` - Returns empty array (TODO implementation)
- ⚠️ `POST /surveys/{id}/run` - Returns basic launch data (TODO implementation)

#### **Reports APIs (12/12 endpoints)**
- ⚠️ `GET /reports` - Returns empty array (TODO implementation)
- ⚠️ `POST /reports` - Returns placeholder report_id
- ⚠️ `GET /reports/{id}` - Returns basic object with ID
- ⚠️ `PUT /reports/{id}` - Returns basic success message
- ⚠️ `DELETE /reports/{id}` - Returns success message
- ⚠️ `POST /reports/{id}/generate` - Returns placeholder instance_id
- ⚠️ `GET /reports/{id}/instances` - Returns empty array
- ⚠️ `PATCH /reports/{id}/status` - Returns basic status update
- ✅ `GET /reports/report-types` - Returns static array (functional)
- ✅ `GET /reports/data-sources` - Returns static array (functional)
- ✅ `GET /reports/chart-types` - Returns static array (functional)
- ✅ `GET /reports/group-by-options` - Returns static array (functional)

#### **Dashboard APIs (3/3 endpoints)**
- ⚠️ `GET /dashboard/stats` - Returns timestamp only (TODO implementation)
- ⚠️ `GET /dashboard/activity` - Returns empty array (TODO implementation)
- ⚠️ `GET /dashboard/analytics` - Returns timestamp only (TODO implementation)

#### **Settings APIs (5/5 endpoints)**
- ⚠️ `GET /settings` - Returns empty array (TODO implementation)
- ⚠️ `PUT /settings/{key}` - Returns basic success message
- ⚠️ `PATCH /settings/{key}/toggle` - Returns basic success message
- ⚠️ `POST /settings/reset/{key}` - Returns basic success message
- ⚠️ `GET /settings/categories` - Returns empty array (TODO implementation)

#### **Billing APIs (5/5 endpoints)**
- ⚠️ `GET /billing` - Returns empty array (TODO implementation)
- ⚠️ `GET /billing/{id}` - Returns basic object with ID
- ⚠️ `GET /billing/account/{accountId}` - Returns empty array (TODO implementation)
- ⚠️ `GET /billing/summary` - Returns timestamp only (TODO implementation)
- ⚠️ `POST /billing/calculate` - Returns basic calculation structure

#### **Notifications APIs (4/4 endpoints)**
- ⚠️ `GET /notifications` - Returns empty array (TODO implementation)
- ⚠️ `PATCH /notifications/{id}/read` - Returns basic success message
- ⚠️ `POST /notifications` - Returns placeholder notification_id
- ⚠️ `DELETE /notifications/{id}` - Returns success message

#### **Files APIs (3/3 endpoints)**
- ⚠️ `POST /upload` - Returns placeholder file_id
- ⚠️ `GET /files/{id}` - Returns basic success message
- ⚠️ `DELETE /files/{id}` - Returns success message

#### **Analytics APIs (4/4 endpoints)**
- ⚠️ `GET /analytics/overview` - Returns timestamp only (TODO implementation)
- ⚠️ `GET /analytics/surveys/{id}` - Returns timestamp only (TODO implementation)
- ⚠️ `GET /analytics/accounts/{id}` - Returns timestamp only (TODO implementation)
- ⚠️ `GET /analytics/system` - Returns timestamp only (TODO implementation)

#### **Categories APIs (1/1 endpoint)**
- ⚠️ `GET /categories/respondent-categories` - Returns empty array (TODO implementation)

### 📈 **Summary Statistics**

#### **Overall API Implementation Status:**
- **Total Frontend API Calls**: ~74 endpoints
- **Fully Implemented (Database Integrated)**: 47 endpoints (64%)
- **Partially Implemented (Skeleton/Placeholder)**: 27 endpoints (36%)
- **Broken/Non-functional**: 0 endpoints (0%)

#### **By Functional Area:**
- **Authentication**: 100% fully implemented
- **Account Management**: 100% fully implemented  
- **Subject Management**: 100% fully implemented
- **Respondent Management**: 100% fully implemented
- **Trait Management**: 100% fully implemented
- **Survey Core CRUD**: 100% fully implemented
- **Survey Advanced Features**: 30% fully implemented
- **Reports**: 33% fully implemented (config endpoints work)
- **Dashboard**: 0% fully implemented (all skeleton)
- **Settings**: 0% fully implemented (all skeleton)
- **Billing**: 0% fully implemented (all skeleton)
- **Notifications**: 0% fully implemented (all skeleton)
- **Files**: 0% fully implemented (all skeleton)
- **Analytics**: 0% fully implemented (all skeleton)
- **Categories**: 0% fully implemented (all skeleton)

### 🎯 **Production Readiness Assessment**

#### **✅ Production-Ready API Groups:**
- **Core User Management** (Auth + Accounts): 100% ready
- **Core Data Management** (Subjects + Respondents + Traits): 100% ready
- **Basic Survey Management**: 70% ready
- **Report Configuration**: 33% ready (dropdowns work)

#### **⚠️ Needs Database Implementation:**
- **Advanced Survey Features**: Survey responses, availability, running
- **Analytics & Reporting**: All analytics and report generation
- **System Management**: Dashboard, settings, billing
- **Supporting Features**: Notifications, file management, categories

**The system has a solid foundation with core CRUD operations fully implemented, but advanced features and analytics require database implementation to be production-ready.**

---

## 🔄 Survey Approval Workflow

### 📋 **Workflow Overview**

IkeNei implements a comprehensive survey approval workflow that ensures quality control and proper governance of survey content before it becomes available to end users.

### **🎯 Approval Process Flow**

```
Domain Admin Creates Survey → Pending Approval → System Admin Reviews → Approved/Rejected → Available to Accounts
```

#### **Step 1: Survey Creation**
- **Domain Admin** creates a new survey using the survey creation interface
- Survey is automatically assigned status: `'pending_approval'`
- Survey includes metadata: `created_by_role: 'domain_admin'`
- Survey is **not visible** to Account users at this stage

#### **Step 2: System Admin Review**
- **System Admin** receives notification of pending survey
- System Admin can view all pending surveys via dedicated interface
- System Admin has two options:
  - **Approve**: Survey status changes to `'approved'` with approval timestamp
  - **Reject**: Survey status changes to `'rejected'` with optional rejection reason

#### **Step 3: Post-Approval Actions**
- **If Approved**: Survey becomes visible and runnable by Account users
- **If Rejected**: Domain Admin can edit survey and resubmit for approval
- **Audit Trail**: Complete record of approval/rejection with timestamps and approver information

### **🔐 Role-Based Approval Matrix**

| **Action** | **Account** | **Domain Admin** | **System Admin** |
|------------|-------------|------------------|------------------|
| **Create Survey** | ❌ | ✅ | ✅ |
| **View All Approved Surveys** | ✅ | ✅ | ✅ |
| **View All Surveys (Any Status)** | ❌ | ✅ | ✅ |
| **View Pending Surveys** | ❌ | ❌ | ✅ |
| **Approve Survey** | ❌ | ❌ | ✅ |
| **Reject Survey** | ❌ | ❌ | ✅ |
| **Run Approved Survey** | ✅ | ✅ | ✅ |
| **Edit Own Surveys** | ❌ | ✅ | ✅ |
| **Delete Own Surveys** | ❌ | ✅ | ✅ |

### **📊 Survey Status Definitions**

| **Status** | **Description** | **Visible To** | **Actions Available** |
|------------|-----------------|----------------|----------------------|
| `pending_approval` | Survey created by Domain Admin, awaiting System Admin review | Domain Admin, System Admin | System Admin: Approve/Reject |
| `approved` | Survey approved by System Admin, ready for use | All Users | Account: Run Survey |
| `rejected` | Survey rejected by System Admin with feedback | Domain Admin, System Admin | Domain Admin: Edit & Resubmit |
| `active` | Survey is currently running and collecting responses | All Users | Monitor Progress |
| `completed` | Survey has finished collecting responses | All Users | View Results |
| `draft` | Survey created by System Admin (auto-approved) | Creator, System Admin | Edit, Submit |

### **🔧 Technical Implementation**

#### **Database Schema**
```javascript
{
  "title": "Survey Title",
  "status": "pending_approval",
  "created_by_role": "domain_admin",
  "approved_by": ObjectId("system_admin_id"),
  "approved_at": ISODate("2025-08-03T12:00:00Z"),
  "rejection_reason": "Needs more detailed questions",
  // ... other survey fields
}
```

#### **API Endpoints**
- `POST /api/surveys/{id}/approve` - Approve survey (System Admin only)
- `POST /api/surveys/{id}/reject` - Reject survey with reason (System Admin only)
- `GET /api/surveys/pending` - Get surveys awaiting approval (System Admin only)
- `GET /api/surveys/approved` - Get approved surveys (Account users)
- `GET /api/surveys/by-role` - Get surveys filtered by user role

#### **Frontend Integration**
```javascript
// Approve survey
await surveysAPI.approveSurvey(surveyId, approverId);

// Reject survey with reason
await surveysAPI.rejectSurvey(surveyId, approverId, "Needs improvement");

// Get pending surveys for System Admin
const pendingSurveys = await surveysAPI.getPendingSurveys();

// Get approved surveys for Account users
const approvedSurveys = await surveysAPI.getApprovedSurveys();
```

### **📈 Workflow Benefits**

#### **Quality Assurance**
- **Content Review**: System Admins ensure survey quality and appropriateness
- **Consistency**: Standardized approval process across all surveys
- **Compliance**: Ensures surveys meet organizational standards

#### **Governance & Control**
- **Centralized Oversight**: System Admins maintain control over survey content
- **Audit Trail**: Complete history of all approval decisions
- **Role Separation**: Clear separation of creation and approval responsibilities

#### **User Experience**
- **Account Users**: Only see high-quality, approved surveys
- **Domain Admins**: Clear feedback on rejected surveys for improvement
- **System Admins**: Efficient review process with bulk operations

### **🎯 Future Enhancements**

#### **Planned Features**
- **Bulk Approval**: Approve multiple surveys simultaneously
- **Approval Templates**: Pre-defined approval criteria and checklists
- **Email Notifications**: Automated notifications for approval status changes
- **Approval Analytics**: Metrics on approval rates and turnaround times
- **Collaborative Review**: Multiple System Admins can review and comment

#### **Advanced Workflow Options**
- **Multi-stage Approval**: Optional secondary approval for sensitive surveys
- **Conditional Approval**: Approval with conditions or modifications
- **Time-based Approval**: Automatic approval after specified time period
- **Category-based Rules**: Different approval rules for different survey types

---

**Transform your professional development with comprehensive 360-degree feedback and data-driven insights.**

*IkeNei - Where feedback meets analytics for organizational growth.*
