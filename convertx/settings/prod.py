"""
Production settings
"""
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://0bc78e59b9bb44eba1120c0db30145c9@o507754.ingest.sentry.io/5599284",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

from .base import *
from dotenv import load_dotenv
from convertx.constants import DOTENV_PATH
import django_heroku
import os

load_dotenv(dotenv_path=DOTENV_PATH)

DEBUG = False
ALLOWED_HOSTS = [os.environ.get('HEROKUAPP_HOST'), os.environ.get('DOMAIN_HOST')] # low maybe add: , os.environ.get('DOMAIN_HOST_WWW')

# EXTRA_APPS = [
#     'storages',
# ]

# INSTALLED_APPS += EXTRA_APPS

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

# django-storages
DEFAULT_FILE_STORAGE = 'convertx.storage_backends.MediaStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = bool(os.getenv('AWS_S3_FILE_OVERWRITE'))

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
DEFENDER_REDIS_URL = os.getenv('REDIS_URL')

django_heroku.settings(locals())
