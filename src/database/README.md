# Database Layer - 360+AI Planner

This directory contains all database-related files including schemas, migrations, seeds, and queries for the 360+AI Planner application.

## Directory Structure

```
database/
├── migrations/         # Database migration scripts
├── seeds/             # Initial data and test data
├── schemas/           # Database schema definitions
├── queries/           # Complex SQL queries and stored procedures
└── config/            # Database configuration files
```

## Database Design

### Core Entities

#### Users & Organizations
- **users** - User accounts, profiles, and authentication data
- **organizations** - Company/organization information
- **user_organizations** - Many-to-many relationship between users and organizations
- **roles** - User roles and permissions
- **user_roles** - User role assignments

#### 360-Degree Feedback System
- **feedback_forms** - Feedback form templates and configurations
- **feedback_questions** - Individual questions within forms
- **feedback_cycles** - Feedback collection periods
- **feedback_invitations** - Invitations sent to feedback providers
- **feedback_responses** - Individual feedback submissions
- **feedback_ratings** - Numerical ratings for competencies

#### Competency Framework
- **competencies** - Skills and competency definitions
- **competency_categories** - Grouping of related competencies
- **competency_levels** - Proficiency levels for each competency
- **user_competencies** - User's current competency levels

#### AI-Powered Learning Plans
- **learning_plans** - AI-generated personalized learning plans
- **learning_objectives** - Specific learning goals and targets
- **learning_resources** - External learning materials and courses
- **learning_progress** - User progress tracking
- **recommendations** - AI-generated recommendations

#### Analytics & Reporting
- **analytics_events** - User interaction tracking
- **reports** - Generated reports and their metadata
- **dashboard_widgets** - Customizable dashboard configurations

## Schema Definitions

### Users Table
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    job_title VARCHAR(200),
    department VARCHAR(100),
    manager_id UUID REFERENCES users(id),
    profile_image_url TEXT,
    is_active BOOLEAN DEFAULT true,
    email_verified BOOLEAN DEFAULT false,
    last_login_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Organizations Table
```sql
CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(100) UNIQUE,
    industry VARCHAR(100),
    size_category VARCHAR(50),
    logo_url TEXT,
    settings JSONB DEFAULT '{}',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Feedback Forms Table
```sql
CREATE TABLE feedback_forms (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    form_type VARCHAR(50) DEFAULT 'standard',
    is_anonymous BOOLEAN DEFAULT false,
    is_active BOOLEAN DEFAULT true,
    settings JSONB DEFAULT '{}',
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Competencies Table
```sql
CREATE TABLE competencies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id UUID REFERENCES competency_categories(id),
    weight DECIMAL(3,2) DEFAULT 1.0,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Learning Plans Table
```sql
CREATE TABLE learning_plans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    ai_analysis JSONB,
    status VARCHAR(50) DEFAULT 'active',
    start_date DATE,
    target_completion_date DATE,
    actual_completion_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Migration Strategy

### Migration Files Naming Convention
```
YYYYMMDD_HHMMSS_description.sql
```

Example:
- `20240101_120000_create_users_table.sql`
- `20240101_130000_create_organizations_table.sql`
- `20240101_140000_create_feedback_forms_table.sql`

### Migration Structure
```sql
-- Up Migration
-- Description: Create users table
-- Date: 2024-01-01

CREATE TABLE users (
    -- table definition
);

-- Create indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_organization ON users(organization_id);

-- Down Migration (for rollback)
-- DROP TABLE users;
```

## Seed Data

### Development Seeds
- Sample organizations
- Test user accounts
- Default competency frameworks
- Sample feedback forms
- Mock feedback responses

### Production Seeds
- Default system roles
- Standard competency categories
- Default learning resource types
- System configuration data

## Query Optimization

### Indexes Strategy
```sql
-- User lookup optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_active ON users(is_active) WHERE is_active = true;

-- Feedback system optimization
CREATE INDEX idx_feedback_responses_form_cycle ON feedback_responses(form_id, cycle_id);
CREATE INDEX idx_feedback_responses_user ON feedback_responses(target_user_id);

-- Learning plan optimization
CREATE INDEX idx_learning_plans_user_status ON learning_plans(user_id, status);
CREATE INDEX idx_learning_progress_plan ON learning_progress(plan_id, completed_at);
```

### Complex Queries

#### Feedback Analysis Query
```sql
-- Get aggregated feedback scores for a user
SELECT 
    c.name as competency_name,
    AVG(fr.rating) as average_rating,
    COUNT(fr.id) as response_count,
    STDDEV(fr.rating) as rating_variance
FROM feedback_responses fr
JOIN feedback_questions fq ON fr.question_id = fq.id
JOIN competencies c ON fq.competency_id = c.id
WHERE fr.target_user_id = $1
    AND fr.cycle_id = $2
GROUP BY c.id, c.name
ORDER BY average_rating DESC;
```

#### Learning Progress Query
```sql
-- Get user's learning progress summary
SELECT 
    lp.title as plan_title,
    COUNT(lo.id) as total_objectives,
    COUNT(CASE WHEN lo.status = 'completed' THEN 1 END) as completed_objectives,
    ROUND(
        COUNT(CASE WHEN lo.status = 'completed' THEN 1 END) * 100.0 / COUNT(lo.id), 
        2
    ) as completion_percentage
FROM learning_plans lp
LEFT JOIN learning_objectives lo ON lp.id = lo.plan_id
WHERE lp.user_id = $1
    AND lp.status = 'active'
GROUP BY lp.id, lp.title;
```

## Data Privacy & Security

### Sensitive Data Handling
- Password hashing with bcrypt
- PII encryption for sensitive fields
- Audit trails for data access
- Data retention policies

### GDPR Compliance
- User data export functionality
- Right to be forgotten implementation
- Consent tracking
- Data processing logs

## Backup & Recovery

### Backup Strategy
- Daily automated backups
- Point-in-time recovery capability
- Cross-region backup replication
- Backup integrity verification

### Recovery Procedures
- Database restoration scripts
- Data consistency checks
- Rollback procedures
- Disaster recovery protocols

## Performance Monitoring

### Key Metrics
- Query execution times
- Index usage statistics
- Connection pool utilization
- Storage growth trends

### Optimization Tools
- Query plan analysis
- Index recommendation engine
- Performance baseline tracking
- Automated optimization alerts

## Development Guidelines

1. **Schema Changes**
   - Always use migrations for schema changes
   - Test migrations on staging environment
   - Include rollback scripts
   - Document breaking changes

2. **Query Performance**
   - Use EXPLAIN ANALYZE for complex queries
   - Implement proper indexing strategy
   - Avoid N+1 query problems
   - Use connection pooling

3. **Data Integrity**
   - Implement proper foreign key constraints
   - Use transactions for multi-table operations
   - Validate data at database level
   - Implement soft deletes where appropriate

## Getting Started

1. Set up database connection
2. Run initial migrations: `npm run migrate`
3. Seed development data: `npm run seed:dev`
4. Verify database setup: `npm run db:verify`
5. Run database tests: `npm run test:db`

## Environment Configuration

```env
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=360planner_dev
DB_USER=postgres
DB_PASSWORD=your_password
DB_SSL=false

# Connection Pool
DB_POOL_MIN=2
DB_POOL_MAX=10
DB_POOL_IDLE_TIMEOUT=30000

# Backup Configuration
BACKUP_SCHEDULE=0 2 * * *
BACKUP_RETENTION_DAYS=30
