# Database Layer - IkeNei

This directory contains all database-related files including schemas, migrations, seeds, and queries for the IkeNei application.

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

#### Accounts & Roles
- **accounts** - Account profiles and authentication data (individual or organizational)
- **roles** - Account roles and permissions
- **account_roles** - Account role assignments

#### 360-Degree Feedback System
- **subjects** - Individuals being assessed (each account has multiple subjects)
- **respondents** - Individuals providing feedback (each subject has multiple respondents)
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
- **account_competencies** - Account's current competency levels


#### Analytics & Reporting
- **analytics_events** - Account interaction tracking
- **reports** - Generated reports and their metadata
- **dashboard_widgets** - Customizable dashboard configurations

## Schema Definitions

### Accounts Table
```sql
CREATE TABLE accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    account_name VARCHAR(255) NOT NULL,
    account_type VARCHAR(50) DEFAULT 'standard',
    is_active BOOLEAN DEFAULT true,
    email_verified BOOLEAN DEFAULT false,
    last_login_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Subjects Table
```sql
CREATE TABLE subjects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID REFERENCES accounts(id),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    position VARCHAR(200),
    department VARCHAR(100),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Respondents Table
```sql
CREATE TABLE respondents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subject_id UUID REFERENCES subjects(id),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    relationship VARCHAR(100),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Feedback Forms Table
```sql
CREATE TABLE feedback_forms (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID REFERENCES accounts(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    form_type VARCHAR(50) DEFAULT 'standard',
    is_anonymous BOOLEAN DEFAULT false,
    is_active BOOLEAN DEFAULT true,
    settings JSONB DEFAULT '{}',
    created_by UUID REFERENCES accounts(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Competencies Table
```sql
CREATE TABLE competencies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID REFERENCES accounts(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id UUID REFERENCES competency_categories(id),
    weight DECIMAL(3,2) DEFAULT 1.0,
    is_active BOOLEAN DEFAULT true,
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
- `20240101_120000_create_accounts_table.sql`
- `20240101_130000_create_subjects_table.sql`
- `20240101_140000_create_respondents_table.sql`
- `20240101_150000_create_feedback_forms_table.sql`
- `20240101_160000_create_competencies_table.sql`

### Migration Structure
```sql
-- Up Migration
-- Description: Create accounts table
-- Date: 2024-01-01

CREATE TABLE accounts (
    -- table definition
);

-- Create indexes
CREATE INDEX idx_accounts_email ON accounts(email);
CREATE INDEX idx_accounts_type ON accounts(account_type);

-- Down Migration (for rollback)
-- DROP TABLE accounts;
```

## Seed Data

### Development Seeds
- Sample accounts (individual and organizational)
- Test subjects for each account
- Test respondents for each subject
- Default competency frameworks
- Sample feedback forms
- Mock feedback responses

### Production Seeds
- Default system roles
- Standard competency categories
- System configuration data

## Query Optimization

### Indexes Strategy
```sql
-- Account lookup optimization
CREATE INDEX idx_accounts_email ON accounts(email);
CREATE INDEX idx_accounts_active ON accounts(is_active) WHERE is_active = true;

-- Subject and respondent optimization
CREATE INDEX idx_subjects_account ON subjects(account_id);
CREATE INDEX idx_subjects_active ON subjects(is_active) WHERE is_active = true;
CREATE INDEX idx_respondents_subject ON respondents(subject_id);
CREATE INDEX idx_respondents_active ON respondents(is_active) WHERE is_active = true;

-- Feedback system optimization
CREATE INDEX idx_feedback_responses_form_cycle ON feedback_responses(form_id, cycle_id);
CREATE INDEX idx_feedback_responses_subject ON feedback_responses(target_subject_id);
```

### Complex Queries

#### Feedback Analysis Query
```sql
-- Get aggregated feedback scores for an account
SELECT 
    c.name as competency_name,
    AVG(fr.rating) as average_rating,
    COUNT(fr.id) as response_count,
    STDDEV(fr.rating) as rating_variance
FROM feedback_responses fr
JOIN feedback_questions fq ON fr.question_id = fq.id
JOIN competencies c ON fq.competency_id = c.id
WHERE fr.target_account_id = $1
    AND fr.cycle_id = $2
GROUP BY c.id, c.name
ORDER BY average_rating DESC;
```

## Data Privacy & Security

### Sensitive Data Handling
- Password hashing with bcrypt
- PII encryption for sensitive fields
- Audit trails for data access
- Data retention policies

### GDPR Compliance
- Account data export functionality
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
