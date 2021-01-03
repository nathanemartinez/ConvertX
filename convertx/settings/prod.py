"""
Production settings
"""

from .base import *
import django_heroku

ALLOWED_HOSTS = ['convertxproject.herokuapp.com', 'convertxproject.com']


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
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# allauth
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

django_heroku.settings(locals())
