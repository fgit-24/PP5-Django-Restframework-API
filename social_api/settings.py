"""
Django settings for social_api project.

Generated by 'django-admin startproject' using Django 4.2.
"""

from pathlib import Path
import os
import re
from dotenv import load_dotenv
load_dotenv()

import dj_database_url

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEV = os.getenv('DEV', 'False').lower() in ['true', '1', 't']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
    'DATETIME_FORMAT': '%d %b %Y',
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_SECURE': True,
    'JWT_AUTH_COOKIE': 'my-app-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
    'JWT_AUTH_SAMESITE': 'None',
    'USER_DETAILS_SERIALIZER': 'social_api.serializers.CurrentUserSerializer',
}

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'c53alz!78l9e1!#hf^=nfs@+iy@lyr3nuc6%6#nfun8ct)2-*+'

# SECRET_KEY = os.getenv('SECRET_KEY')
# os.environ['SECRET_KEY'] = 'SECRET_KEY'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'social-api-f-f73ebdfcae43.herokuapp.com',
    '8000-fgit24-pp5djangorestfra-8jjaed52v4m.ws.codeinstitute-ide.net',
    '3000-fgit24-reactsocialmedia-a4v7twszff8.ws.codeinstitute-ide.net',
    'social-frontent-pp5-bbb72fd984a6.herokuapp.com',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'taggit',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
    'django_extensions',
    'social_api',
    'profiles',
    'posts',
    'comments',
    'likes',
]

SITE_ID = 1
TAGGIT_CASE_INSENSITIVE = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(
        r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''),
        re.IGNORECASE
    ).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'social_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'social_api.wsgi.application'

# Database
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3"))
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CSRF_TRUSTED_ORIGINS = [
    "https://social-api-f-f73ebdfcae43.herokuapp.com",
    "https://8000-fgit24-pp5djangorestfra-8jjaed52v4m.ws.codeinstitute-ide.net",
    "https://3000-fgit24-reactsocialmedia-a4v7twszff8.ws.codeinstitute-ide.net",
    "https://social-frontent-pp5-bbb72fd984a6.herokuapp.com",
]

CORS_ALLOWED_ORIGINS = [
    "https://social-api-f-f73ebdfcae43.herokuapp.com",
    "https://8000-fgit24-pp5djangorestfra-8jjaed52v4m.ws.codeinstitute-ide.net",
    "https://3000-fgit24-reactsocialmedia-a4v7twszff8.ws.codeinstitute-ide.net",
    "https://social-frontent-pp5-bbb72fd984a6.herokuapp.com",
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'