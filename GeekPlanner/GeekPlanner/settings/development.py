"""
This module implements settings used for development purposes.
Consider using it in your testing environment.
"""
import os

from .base import BASE_DIR


# ============================================================================
# Hosts & Domains
# ============================================================================
ALLOWED_HOSTS = ['*']
DOMAIN_NAME = 'http://localhost:8000'

# ============================================================================
# Debug settings
# ============================================================================
DEBUG = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
DATA_DIR = os.path.join(BASE_DIR, '../../testing_data')

# ============================================================================
# Email
# ============================================================================
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_HOST_USER = 'admin@geekplanner.local'
EMAIL_HOST_PASSWORD = 'admin'
EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/emails/'
