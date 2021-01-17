"""
Production settings
"""

from .base import *
from dotenv import load_dotenv
from pathlib import Path
import django_heroku
import os

env_path = Path('env') / '.env'
load_dotenv(dotenv_path=env_path)

ALLOWED_HOSTS = [os.environ.get('HEROKUAPP_HOST'), os.environ.get('DOMAIN_HOST'), os.environ.get('DOMAIN_HOST_WWW')]

EXTRA_APPS = [

]


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


# https://docs.djangoproject.com/en/3.1/topics/security/
# SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Emails
DEFAULT_FROM_EMAIL = os.getenv('ADMIN_EMAIL')
SERVER_EMAIL = os.getenv('ADMIN_EMAIL')

# allauth
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

# defender
DEFENDER_COOLOFF_TIME = 300

django_heroku.settings(locals())
