# MongoDB Database Setup for IkeNei

This guide will help you set up the MongoDB database for the IkeNei application.

## Prerequisites

- Docker and Docker Compose installed
- Python 3.8+ with pip
- MongoDB dependencies installed (see requirements.txt)

## Quick Start

### 1. Start MongoDB with Docker

Navigate to the database config directory and start MongoDB:

```bash
cd src/database/config
docker-compose up -d
```

This will start:
- **MongoDB** on port `27017`
- **Mongo Express** (web UI) on port `8081`

### 2. Verify Database Connection

Check if MongoDB is running:

```bash
docker ps
```

You should see containers named:
- `ikenei_mongodb`
- `ikenei_mongo_express`

### 3. Access Mongo Express (Optional)

Open your browser and go to: http://localhost:8081

This provides a web interface to view and manage your MongoDB data.

### 4. Start the Backend Server

From the backend directory:

```bash
cd src/backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python app.py
```

The server will automatically:
- Connect to MongoDB
- Initialize the database
- Create indexes
- Be ready to accept requests

### 5. Seed Development Data (Optional)

To populate the database with sample data:

```bash
cd src/database/seeds
python development_seeds.py
```

## Database Configuration

### Connection Settings

The application uses these MongoDB connection settings:

```python
# Default settings (can be overridden with environment variables)
MONGO_URI = 'mongodb://localhost:27017/ikenei'
MONGODB_DB_NAME = 'ikenei'
```

### Environment Variables

You can customize the database connection using environment variables:

```bash
# MongoDB connection
export MONGO_URI="mongodb://localhost:27017/ikenei"
export MONGODB_DB_NAME="ikenei"

# For development
export DEV_MONGODB_URI="mongodb://localhost:27017/ikenei_dev"
export DEV_MONGODB_DB_NAME="ikenei_dev"

# For testing
export TEST_MONGODB_URI="mongodb://localhost:27017/ikenei_test"
export TEST_MONGODB_DB_NAME="ikenei_test"
```

## Database Structure

### Collections

The database includes the following collections:

1. **accounts** - User accounts and authentication
2. **subjects** - Individuals being assessed
3. **surveys** - Survey definitions and configurations
4. **respondents** - People providing feedback
5. **responses** - Survey response data
6. **traits** - Competencies and skills definitions

### Indexes

Optimized indexes are automatically created for:
- Account email lookups
- Subject-account relationships
- Survey status and date queries
- Response aggregations

## API Endpoints

### Health Checks

- **Application Health**: `GET /health`
- **Database Health**: `GET /health/database`

### Account Management

- **Get All Accounts**: `GET /api/accounts`
- **Create Account**: `POST /api/accounts`
- **Get Account**: `GET /api/accounts/{id}`
- **Update Account**: `PUT /api/accounts/{id}`
- **Delete Account**: `DELETE /api/accounts/{id}`

## Development Workflow

### 1. Database Changes

When making database schema changes:

1. Update the model in `src/database/models/`
2. Update the repository in `src/database/repositories/`
3. Update the MongoDB init script if needed
4. Test with development data

### 2. Adding New Models

To add a new model:

1. Create model file: `src/database/models/new_model.py`
2. Create repository file: `src/database/repositories/new_repository.py`
3. Update `src/database/__init__.py` to export the new classes
4. Add to seed data if needed

### 3. Testing

Run database tests:

```bash
cd src/database
python -m pytest tests/
```

## Troubleshooting

### MongoDB Connection Issues

1. **Check if MongoDB is running**:
   ```bash
   docker ps | grep mongodb
   ```

2. **Check MongoDB logs**:
   ```bash
   docker logs ikenei_mongodb
   ```

3. **Restart MongoDB**:
   ```bash
   cd src/database/config
   docker-compose restart mongodb
   ```

### Port Conflicts

If port 27017 is already in use:

1. Stop other MongoDB instances
2. Or change the port in `docker-compose.yml`
3. Update the connection string accordingly

### Permission Issues

If you get permission errors:

```bash
# Fix Docker permissions (Linux/Mac)
sudo chown -R $USER:$USER src/database/config

# Or run with sudo
sudo docker-compose up -d
```

### Database Reset

To completely reset the database:

```bash
cd src/database/config
docker-compose down -v  # This removes volumes (data)
docker-compose up -d
```

## Production Deployment

### MongoDB Atlas (Recommended)

1. Create a MongoDB Atlas cluster
2. Get the connection string
3. Set environment variables:
   ```bash
   export MONGO_URI="mongodb+srv://username:password@cluster.mongodb.net/ikenei"
   export MONGODB_DB_NAME="ikenei"
   ```

### Self-Hosted MongoDB

1. Install MongoDB on your server
2. Configure authentication and security
3. Set up backups and monitoring
4. Update connection settings

## Backup and Recovery

### Local Backup

```bash
# Backup
docker exec ikenei_mongodb mongodump --db ikenei --out /data/backup

# Restore
docker exec ikenei_mongodb mongorestore --db ikenei /data/backup/ikenei
```

### Automated Backups

Consider setting up automated backups using:
- MongoDB Atlas automated backups
- Cron jobs with mongodump
- Cloud storage integration

## Monitoring

### Performance Monitoring

Monitor these metrics:
- Connection pool usage
- Query execution times
- Index usage statistics
- Memory and disk usage

### Logging

Database operations are logged at various levels:
- Connection events
- Query performance
- Error conditions
- Authentication attempts

Check logs in the application output or configure log aggregation.

## Security

### Authentication

The MongoDB instance is configured with:
- Root user: `admin` / `admin123`
- Application user: `ikenei_user` / `ikenei_password`

### Best Practices

1. Change default passwords in production
2. Use SSL/TLS for connections
3. Implement proper network security
4. Regular security updates
5. Monitor access logs

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review application logs
3. Check MongoDB documentation
4. Contact the development team
