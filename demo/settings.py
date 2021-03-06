"""
Django settings for demo project.

For more information on this file, see
https://docs.djangoproject.com/en/3.0
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# TODO: Remove to env
SECRET_KEY = 'secret-is-secret-secret-is-secret-secret-is-secret-!@#$'

CUSTOM_TOKEN = {
    'SIGNING_KEY': SECRET_KEY,
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPES': 'Bearer',
    'USER_ID_FIELD': 'id',
    'JTI_CLAIM': 'jti',
}

# TODO: Remove
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'rest_framework',
    'rest_framework_swagger',

    'demo.apps.articles',
    'demo.apps.authentication',
    'demo.apps.core',
    'demo.apps.profiles',
    'demo.apps.notifications'
]

#MIDDLEWARE_CLASSES = [
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

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

WSGI_APPLICATION = 'demo.wsgi.application'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'demo_django',
        'USER': 'root',
        'PASSWORD': 'abc@1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0
#https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0
#https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0
#https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# Tell Django about the custom `User` model we created. The string
# `authentication.User` tells Django we are referring to the `User` model in
# the `authentication` module. This module is registered above in a setting
# called `INSTALLED_APPS`.
AUTH_USER_MODEL = 'authentication.User'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema', 
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'demo.apps.authentication.backends.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'EXCEPTION_HANDLER': 'demo.apps.core.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'PAGE_SIZE': 20,
}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'SHOW_REQUEST_HEADERS' : True,
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'oauth2': {
            'type': 'apiKey',
            'description': 'Personal API Key authorization',
            'name': 'Authorization',
            'in': 'header',
        }
    },
    'APIS_SORTER': 'alpha',
    # "JSON_EDITOR": True,
    "SHOW_REQUEST_HEADERS": True,
    "VALIDATOR_URL": False,
}