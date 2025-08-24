"""
WSGI config for poornimax project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poornimax.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    # Log the error for production debugging
    import logging
    logging.error(f"Failed to load WSGI application: {e}")
    raise
