"""
This module defines basic settings used on both: development and production
configuration settings.
"""
import os


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
    # GeekPlanner applications
    'mainapp',
    'authapp',
    'plannerapp',
    'adminapp',
    # 3rd-party applications
    'rest_framework',
    'django_registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
# Django-registration settings
# ============================================================================
# How long (in days) after signup an account has in which to activate
ACCOUNT_ACTIVATION_DAYS = 7
# A bool indicating whether registration of new accounts is currently permitted
REGISTRATION_OPEN = True
# An additional “salt” used in the process of generating signed activation keys.
REGISTRATION_SALT = '8hb+6v_7TT3'
