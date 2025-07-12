# 360+AI Planner

A comprehensive 360-degree feedback and AI-powered personalized learning platform that helps individuals and organizations drive professional development through data-driven insights.

## 🚀 Overview

360+AI Planner is an innovative tool that combines traditional 360-degree feedback methodologies with cutting-edge artificial intelligence to deliver personalized learning experiences. The platform enables users to gather comprehensive feedback from peers, supervisors, and subordinates, then leverages AI to create tailored development plans that accelerate professional growth.

## ✨ Key Features

### 🔐 User Management
- **Secure Registration & Authentication**: Easy onboarding with robust security measures
- **Role-based Access Control**: Three distinct user personas (Assessee, Coach, Admin)
- **Profile Management**: Comprehensive user profiles with professional information

### 📊 360-Degree Feedback System
- **Multi-source Feedback Collection**: Gather insights from supervisors, peers, direct reports, and self-assessments
- **Customizable Assessment Templates**: Industry-specific and role-based feedback questionnaires
- **Anonymous Feedback Options**: Ensure honest and constructive feedback
- **Real-time Progress Tracking**: Monitor feedback collection status and completion rates

### 🤖 AI-Powered Learning Plans
- **Intelligent Analysis**: AI processes feedback data to identify strengths and development areas
- **Personalized Recommendations**: Custom learning paths based on individual feedback patterns
- **Adaptive Learning**: Plans that evolve based on progress and new feedback
- **Resource Integration**: Curated learning materials, courses, and development activities

### 📈 Analytics & Reporting
- **Comprehensive Dashboards**: Visual insights into feedback trends and development progress
- **Competency Mapping**: Track skills development across various competencies
- **Progress Metrics**: Quantifiable measures of improvement over time
- **Export Capabilities**: Generate reports for HR and management review

## 👥 User Personas

### 🎯 Assessee
- **Primary user** receiving 360-degree feedback
- **Personal dashboard** with development journey tracking
- **Access to** feedback results and AI-generated learning plans
- **Progress monitoring** and goal setting capabilities

### 👨‍💼 Coach
- **Guides and supports** assessees through development
- **Aggregated insights** (no raw feedback data for privacy)
- **Coaching tools** and AI-powered recommendations
- **Team progress** monitoring and reporting

### ⚙️ Admin
- **System administration** and user management
- **Platform-wide analytics** and reporting
- **Configuration** of feedback forms and competency frameworks
- **System health** monitoring and maintenance

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

### AI/ML & Analytics
- **AI Engine**: Ollama (Local LLM integration)
- **Data Processing**: Python-based analytics
- **Feedback Analysis**: Natural language processing
- **Learning Recommendations**: Machine learning algorithms

### Infrastructure & Security
- **Containerization**: Docker
- **Security**: Enterprise-grade security measures
- **Privacy Compliance**: GDPR compliant
- **Monitoring**: Application performance monitoring

## 📁 Project Structure

```
360+AI-Planner/
├── README.md                    # This file
├── .gitignore                   # Git ignore rules
└── src/
    ├── frontend/                # React frontend application
    │   ├── components/          # Reusable React components
    │   ├── contexts/            # React context providers
    │   ├── pages/               # Page components
    │   ├── assets/              # Static assets
    │   ├── App.jsx              # Main application component
    │   ├── main.jsx             # Application entry point
    │   └── index.html           # HTML template
    ├── backend/                 # Python/Flask backend API
    │   ├── config/              # Configuration files
    │   ├── controllers/         # API route handlers
    │   ├── models/              # Data models
    │   ├── services/            # Business logic
    │   └── utils/               # Utility functions
    ├── database/                # MongoDB schemas and migrations
    │   ├── schemas/             # Database schemas
    │   ├── migrations/          # Database migrations
    │   └── seeds/               # Sample data
    ├── shared/                  # Shared code and utilities
    │   ├── constants/           # Application constants
    │   ├── types/               # Type definitions
    │   └── validators/          # Data validation
    ├── tests/                   # Test suites
    │   ├── unit/                # Unit tests
    │   ├── integration/         # Integration tests
    │   └── e2e/                 # End-to-end tests
    └── docs/                    # Technical documentation
        ├── api/                 # API documentation
        ├── architecture/        # System architecture
        └── deployment/          # Deployment guides
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
   git clone https://github.com/balu72/360-Plus-AI-Planner.git
   cd 360+AI-Planner
   ```

2. **Frontend Setup**
   ```bash
   cd src/frontend
   npm install
   npm run dev
   ```

3. **Backend Setup** (Coming Soon)
   ```bash
   cd src/backend
   pip install -r requirements.txt
   python app.py
   ```

4. **Database Setup** (Coming Soon)
   ```bash
   # MongoDB setup instructions
   ```

### Demo Access

The frontend includes demo credentials for testing:
- **Assessee**: assessee@example.com / password
- **Coach**: coach@example.com / password
- **Admin**: admin@example.com / password

## 📋 How It Works

### Step 1: Registration & Setup
- Create your account with basic professional information
- Set up your profile and preferences
- Define your feedback network (supervisors, peers, direct reports)

### Step 2: 360-Degree Feedback Collection
- Launch a feedback cycle with customized questionnaires
- Invite feedback providers through the platform
- Monitor collection progress and send reminders
- Ensure anonymous and confidential feedback submission

### Step 3: AI Analysis & Insights
- AI processes all feedback data to identify patterns
- Generates comprehensive analysis of strengths and development areas
- Creates competency-based insights and recommendations

### Step 4: Personalized Learning Plan
- Receive AI-generated development recommendations
- Access curated learning resources and activities
- Set goals and track progress over time
- Schedule follow-up feedback cycles for continuous improvement

## 🏗️ Architecture Overview

The 360+AI Planner follows a layered architecture pattern:

1. **Presentation Layer** (`frontend/`) - User interface and user experience
2. **Business Logic Layer** (`backend/`) - API endpoints, business rules, and data processing
3. **Data Layer** (`database/`) - Data storage, retrieval, and management
4. **Shared Layer** (`shared/`) - Common utilities, types, and constants
5. **Testing Layer** (`tests/`) - Comprehensive test coverage
6. **Documentation Layer** (`docs/`) - Technical specifications and guides

## 🔒 Privacy & Security

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

### 🚧 In Progress
- Backend API development
- Database schema implementation
- AI integration with Ollama

### 📅 Upcoming Features
- Mobile application for iOS and Android
- Integration with popular HRIS systems
- Advanced AI coaching recommendations
- Team-based feedback and development plans
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

**Transform your professional development with data-driven insights and AI-powered learning plans.**

*360+AI Planner - Where feedback meets intelligence for accelerated growth.*
