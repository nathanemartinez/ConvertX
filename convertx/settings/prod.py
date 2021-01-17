"""
Production settings
"""

from .base import *
from dotenv import load_dotenv
import django_heroku
import os

CUR_FILE = os.path.abspath(os.path.dirname(__file__))
MY_DOTENV_PATH = os.path.join(CUR_FILE, 'env/.env')
load_dotenv(dotenv_path=MY_DOTENV_PATH)

DEBUG = False
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
DEFAULT_FROM_EMAIL = str(os.getenv('ADMIN_EMAIL'))
SERVER_EMAIL = str(os.getenv('ADMIN_EMAIL'))

# allauth
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

# defender
DEFENDER_COOLOFF_TIME = 300

django_heroku.settings(locals())
