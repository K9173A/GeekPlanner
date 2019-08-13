"""
This module defines basic settings used on both: development and production
configuration settings.
"""
import os
import datetime

from corsheaders.defaults import default_headers


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'm-$8#^xgw-ctn!bah#2jw!!2=_%@b(kof#$-@7-_p0@e8zd9!8'

# ============================================================================
# Application definition
# ============================================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd-party applications
    'rest_framework',
    'djoser',
    'corsheaders',
    # GeekPlanner applications
    'api.authapp',
    'api.plannerapp',
    # 'api.adminapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GeekPlanner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'GeekPlanner.wsgi.application'

# ============================================================================
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# ============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'geekplanner',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# ============================================================================
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# ============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================================================
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# ============================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ============================================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# ============================================================================
# Root URL for static content
STATIC_URL = '/static/'
# Directories for static content
STATICFILES_ROOT = os.path.join(BASE_DIR, '../static')
STATICFILES_DIRS = (STATICFILES_ROOT,)
# URL for media content: 127.0.0.1:8000/media/
MEDIA_URL = '/media/'
# Project root directory of media content
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
# Project thumbnails are stored in the /media/project_thumbnails/ directory
PROJECT_THUMBNAILS_DIR = 'project_thumbnails'
# User avatars are stored in the /media/user_avatars/ directory
USER_AVATARS_DIR = 'user_avatars'

# ============================================================================
# Authentication
# ============================================================================
# List of backends used for user authentication
AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend',)
)
# Model which we use for authentication
AUTH_USER_MODEL = 'authapp.User'

# ============================================================================
# Django REST framework settings
# ============================================================================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

# ============================================================================
# djoser settings
# ============================================================================
DJOSER = {
    # URL to the frontend password reset page
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    # URL to the frontend username reset page
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    # URL to the frontend activation page
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    # User will be required to click activation link sent in email after
    # creating an account and updating their email
    'SEND_ACTIVATION_EMAIL': True,
    # Dictionary which maps djoser serializer names to serializer classes
    'SERIALIZERS': {},
    'EMAIL': {
        'activation': 'api.authapp.views.ActivationEmailView',
    }
}

# Custom djoser settings needed to override some views, because by default
# djoser uses Backend (Django rest) domain, but we need to connect to the
# Frontend application which is located on a different port (and possibly
# address).
DJOSER_GEEKPLANNER = {
    'protocol': 'http',
    'domain_address': 'localhost:8080',
    'domain_name': 'geekplanner.com',
}

# ============================================================================
# djangorestframework_simplejwt settings
# ============================================================================
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=24),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=30),
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# ============================================================================
# django-cors-headers settings
# ============================================================================
# If True, the whitelist will not be used and all origins will be accepted.
CORS_ORIGIN_ALLOW_ALL = True
# If True, cookies will be allowed to be included in cross-site HTTP requests.
CORS_ALLOW_CREDENTIALS = False

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:8080',  # Frontend application (Vue.js)
#     'http://10.0.2.15:8080',
# ]
#
# CORS_ALLOW_HEADERS = list(default_headers) + [
#     'Authorization',
# ]
