"""
General project settings
https://docs.djangoproject.com/en/3.1/topics/settings/
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('env') / '.env'
load_dotenv(dotenv_path=env_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
ALLAUTH_DIR = os.path.join(BASE_DIR, 'templates', 'allauth')
DATABASE_DIR = os.path.join(BASE_DIR, 'db.sqlite3')
SECRET_KEY = os.environ.get('convertx_secret_key')
STATIC_PATH = os.path.join(BASE_DIR, 'static')
DEBUG = os.environ.get('DEBUG_VALUE')

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

REQUIREMENT_APPS = [
    'crispy_forms',
    'defender',
]

PROJECT_APPS = [
    'home.apps.HomeConfig',
    # 'demo.apps.DemoConfig',
    'users.apps.UsersConfig',
]

DJANGO_ALLAUTH_APPS = [
    'allauth',
    'allauth.account',
]

INSTALLED_APPS = DJANGO_APPS + REQUIREMENT_APPS + PROJECT_APPS + DJANGO_ALLAUTH_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'defender.middleware.FailedLoginMiddleware',
]

ROOT_URLCONF = 'convertx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ALLAUTH_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',  # django-allauth
            ],
            'builtins': ['django.templatetags.static']
        },
    },
]

WSGI_APPLICATION = 'convertx.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_DIR,
    }
}


# django-allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# allauth, ref: https://django-allauth.readthedocs.io/en/latest/configuration.html
SITE_ID = os.getenv('SITE_ID')
ACCOUNT_AUTHENTICATION_METHOD = os.getenv('ACCOUNT_AUTHENTICATION_METHOD')
ACCOUNT_EMAIL_REQUIRED = os.getenv('ACCOUNT_EMAIL_REQUIRED')
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = os.getenv('ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS')
ACCOUNT_EMAIL_VERIFICATION = os.getenv('ACCOUNT_EMAIL_VERIFICATION')
ACCOUNT_MAX_EMAIL_ADDRESSES = os.getenv('ACCOUNT_MAX_EMAIL_ADDRESSES')
ACCOUNT_LOGOUT_REDIRECT_URL = os.getenv('ACCOUNT_LOGOUT_REDIRECT_URL')
ACCOUNT_PRESERVE_USERNAME_CASING = os.getenv('ACCOUNT_PRESERVE_USERNAME_CASING')  # username is stored in lowercase
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = os.getenv('ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE')  # enter email twice to avoid typos
# todo pushing to heroku produces an error - it might be due to a previous file version - in pictures
ACCOUNT_USERNAME_BLACKLIST = eval(os.getenv('ACCOUNT_USERNAME_BLACKLIST'))  # usernames that can't be used
ACCOUNT_USERNAME_MIN_LENGTH = os.getenv('ACCOUNT_USERNAME_MIN_LENGTH')  # minimum length of username

# defender, ref: https://django-defender.readthedocs.io/en/latest/
DEFENDER_LOCKOUT_TEMPLATE = os.getenv('DEFENDER_LOCKOUT_TEMPLATE')
DEFENDER_LOCKOUT_URL = os.getenv('DEFENDER_LOCKOUT_URL')
DEFENDER_REDIS_URL = os.getenv('DEFENDER_REDIS_URL')

# Internationalization https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [STATIC_PATH, ALLAUTH_DIR]  # ***You might not want to include this in deployment

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
