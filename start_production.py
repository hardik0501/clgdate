#!/usr/bin/env python
"""
Production startup script for Poornimax Django application.
This script sets up the production environment and starts the server.
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_environment():
    """Set up production environment variables."""
    # Set production environment
    os.environ['DEBUG'] = 'False'
    os.environ['DJANGO_SETTINGS_MODULE'] = 'poornimax.settings'
    
    # Generate a secure secret key if not set
    if not os.environ.get('SECRET_KEY'):
        from django.core.management.utils import get_random_secret_key
        os.environ['SECRET_KEY'] = get_random_secret_key()
        print("Generated new SECRET_KEY for production")

def check_dependencies():
    """Check if all required packages are installed."""
    required_packages = [
        'django', 'channels', 'gunicorn', 'whitenoise', 
        'pillow', 'crispy_forms', 'crispy_bootstrap5'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("Please install missing packages: pip install -r requirements.txt")
        return False
    
    print("All required packages are installed")
    return True

def run_migrations():
    """Run database migrations."""
    try:
        subprocess.run([sys.executable, 'manage.py', 'migrate', '--noinput'], 
                      check=True, capture_output=True)
        print("Database migrations completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Migration failed: {e}")
        return False

def collect_static():
    """Collect static files for production."""
    try:
        subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput'], 
                      check=True, capture_output=True)
        print("Static files collected successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Static collection failed: {e}")
        return False

def start_production_server():
    """Start the production server using Gunicorn."""
    try:
        # Get port from environment or use default
        port = os.environ.get('PORT', '8000')
        
        print(f"Starting production server on port {port}")
        print("Use Ctrl+C to stop the server")
        
        # Start Gunicorn
        subprocess.run([
            'gunicorn', 'poornimax.wsgi:application',
            '--bind', f'0.0.0.0:{port}',
            '--workers', '3',
            '--timeout', '120',
            '--access-logfile', '-',
            '--error-logfile', '-'
        ])
        
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Server error: {e}")

def main():
    """Main function to set up and start production server."""
    print("🚀 Setting up Poornimax Production Environment...")
    
    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Setup environment
    setup_environment()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Run migrations
    if not run_migrations():
        print("Warning: Migrations failed, but continuing...")
    
    # Collect static files
    if not collect_static():
        print("Warning: Static collection failed, but continuing...")
    
    print("✅ Production environment setup complete!")
    print("🌐 Starting production server...")
    
    # Start production server
    start_production_server()

if __name__ == '__main__':
    main()
