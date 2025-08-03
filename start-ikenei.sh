#!/bin/bash

# IkeNei Application Startup Script
# This script starts MongoDB, Backend API, and Frontend in the correct order

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[IkeNei]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[IkeNei]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[IkeNei]${NC} $1"
}

print_error() {
    echo -e "${RED}[IkeNei]${NC} $1"
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check if a port is in use
port_in_use() {
    lsof -i :$1 >/dev/null 2>&1
}

# Function to wait for a service to be ready
wait_for_service() {
    local url=$1
    local service_name=$2
    local max_attempts=30
    local attempt=1
    
    print_status "Waiting for $service_name to be ready..."
    
    while [ $attempt -le $max_attempts ]; do
        if curl -s "$url" >/dev/null 2>&1; then
            print_success "$service_name is ready!"
            return 0
        fi
        
        echo -n "."
        sleep 2
        attempt=$((attempt + 1))
    done
    
    print_error "$service_name failed to start within $((max_attempts * 2)) seconds"
    return 1
}

# Function to cleanup on exit
cleanup() {
    print_warning "Shutting down IkeNei application..."
    
    # Kill background processes
    if [ ! -z "$BACKEND_PID" ]; then
        print_status "Stopping backend server (PID: $BACKEND_PID)..."
        kill $BACKEND_PID 2>/dev/null || true
    fi
    
    if [ ! -z "$FRONTEND_PID" ]; then
        print_status "Stopping frontend server (PID: $FRONTEND_PID)..."
        kill $FRONTEND_PID 2>/dev/null || true
    fi
    
    # Stop MongoDB container
    print_status "Stopping MongoDB container..."
    docker-compose -f src/database/config/docker-compose.yml down
    
    print_success "IkeNei application stopped."
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

print_success "Starting IkeNei Application..."
print_status "========================================"

# Check prerequisites
print_status "Checking prerequisites..."

if ! command_exists docker; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command_exists docker-compose; then
    print_error "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

if ! command_exists python3; then
    print_error "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

if ! command_exists npm; then
    print_error "Node.js/npm is not installed. Please install Node.js first."
    exit 1
fi

print_success "All prerequisites are available."

# Step 1: Start MongoDB
print_status "========================================"
print_status "Step 1: Starting MongoDB..."

# Check if MongoDB is already running
if port_in_use 27017; then
    print_warning "Port 27017 is already in use. Stopping existing MongoDB..."
    docker-compose -f src/database/config/docker-compose.yml down 2>/dev/null || true
    sleep 2
fi

# Start MongoDB container
cd src/database/config
docker-compose up -d
cd ../../..

# Wait for MongoDB to be ready
if wait_for_service "http://localhost:27017" "MongoDB"; then
    print_success "MongoDB is running on port 27017"
else
    print_error "Failed to start MongoDB"
    exit 1
fi

# Step 2: Start Backend API
print_status "========================================"
print_status "Step 2: Starting Backend API..."

# Check if backend port is in use
if port_in_use 5000; then
    print_error "Port 5000 is already in use. Please stop the service using port 5000."
    exit 1
fi

# Install Python dependencies if needed
if [ ! -d "src/backend/venv" ]; then
    print_status "Creating Python virtual environment..."
    cd src/backend
    python3 -m venv venv
    cd ../..
fi

print_status "Installing/updating Python dependencies..."
cd src/backend
source venv/bin/activate
pip install -r requirements.txt
cd ../..

# Start backend server
print_status "Starting Flask backend server..."
cd src/backend
source venv/bin/activate
python app.py &
BACKEND_PID=$!
cd ../..

# Wait for backend to be ready
if wait_for_service "http://localhost:5000/api/health" "Backend API"; then
    print_success "Backend API is running on port 5000"
else
    print_error "Failed to start Backend API"
    cleanup
    exit 1
fi

# Step 3: Start Frontend
print_status "========================================"
print_status "Step 3: Starting Frontend..."

# Check if frontend port is in use
if port_in_use 5173; then
    print_error "Port 5173 is already in use. Please stop the service using port 5173."
    cleanup
    exit 1
fi

# Install Node.js dependencies if needed
if [ ! -d "src/frontend/node_modules" ]; then
    print_status "Installing Node.js dependencies..."
    cd src/frontend
    npm install
    cd ../..
fi

# Start frontend development server
print_status "Starting Vite frontend server..."
cd src/frontend
npm run dev &
FRONTEND_PID=$!
cd ../..

# Wait for frontend to be ready
if wait_for_service "http://localhost:5173" "Frontend"; then
    print_success "Frontend is running on port 5173"
else
    print_error "Failed to start Frontend"
    cleanup
    exit 1
fi

# All services started successfully
print_status "========================================"
print_success "🎉 IkeNei Application is now running!"
print_status "========================================"
print_status "Services:"
print_status "  📊 MongoDB:    http://localhost:27017"
print_status "  🔧 Backend:    http://localhost:5000"
print_status "  🌐 Frontend:   http://localhost:5173"
print_status "========================================"
print_status "Demo Users:"
print_status "  👤 Account:      uat@ikenei.ai / uat123"
print_status "  👨‍💼 Domain Admin: dom@ikenei.ai / dom123"
print_status "  🔐 System Admin: su@ikenei.ai / su123"
print_status "========================================"
print_warning "Press Ctrl+C to stop all services"

# Keep the script running and wait for user to stop
while true; do
    sleep 1
done
