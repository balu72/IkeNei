# 360+AI Planner - Source Code Structure

This directory contains all the source code for the 360+AI Planner application, organized into distinct layers for maintainability and scalability.

## Directory Structure

```
src/
├── frontend/           # Frontend application (React/Vue/Angular)
├── backend/            # Backend API server (Python/Flask)
├── database/           # Database schemas, migrations, and queries (MongoDB)
├── shared/             # Shared code between frontend and backend
├── tests/              # Test suites (unit, integration, e2e)
└── docs/               # Technical documentation
```

## Architecture Overview

The 360+AI Planner follows a layered architecture pattern:

1. **Presentation Layer** (`frontend/`) - User interface and user experience
2. **Business Logic Layer** (`backend/`) - API endpoints, business rules, and data processing
3. **Data Layer** (`database/`) - Data storage, retrieval, and management
4. **Shared Layer** (`shared/`) - Common utilities, types, and constants
5. **Testing Layer** (`tests/`) - Comprehensive test coverage
6. **Documentation Layer** (`docs/`) - Technical specifications and guides

## Development Guidelines

- Each layer should be loosely coupled and highly cohesive
- Use the shared directory for code that needs to be used across multiple layers
- Follow consistent naming conventions across all directories
- Maintain comprehensive test coverage for all business logic
- Document all APIs and architectural decisions

## Getting Started

1. Navigate to the specific layer directory you want to work on
2. Follow the README instructions in each directory
3. Ensure you understand the dependencies between layers
4. Run tests before making any changes

For detailed information about each layer, refer to the README files in the respective directories.
