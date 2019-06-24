"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^&mwd%1g02jrup+ek)0$jh0jskwjljnl(i5qmb7@9r#$d8ey79'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',  # required to enable standard registration (see links posted below for rest_auth & allauth)
    'django.contrib.staticfiles',

    # 3rd party
    'rest_framework',  # new
    # https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    # to use token configuration, you'll need to include 'rest_framework.authtoken' in your INSTALLED_APPS setting
    'rest_framework.authtoken',  # new
    # https://django-rest-auth.readthedocs.io/en/latest/
    # provides a set of REST API endpoints for Authentication and Registration
    'rest_auth',  # new
    # enable user registration by installing django-allauth
    'allauth', # new
    'allauth.account',  # new
    'rest_auth.registration',  # new

    # local
    'api.apps.ApiConfig',  # new
    'frontend.apps.FrontendConfig',  # new
    'todos.apps.TodosConfig',  # new
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # project level permissions
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
        #  To use the TokenAuthentication scheme you'll need to configure the authentication classes to include TokenAuthentication
        'rest_framework.authentication.TokenAuthentication',  # new

    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# Configure Django's staticfiles to serve the JS and CSS from create-react-app's build with these settings:
REACT_APP_DIR = os.path.join(BASE_DIR, 'frontend/static')