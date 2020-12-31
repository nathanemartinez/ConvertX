"""
General project settings
https://docs.djangoproject.com/en/3.1/topics/settings/
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASE_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
DATABASE_DIR = os.path.join(BASE_DIR, 'db.sqlite3')
SECRET_KEY = os.environ.get('convertx_secret_key')
DEBUG = os.environ.get('DEBUG_VALUE')

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

REQUIREMENT_APPS = [

]

PROJECT_APPS = [
    'home.apps.HomeConfig',
    'demo.apps.DemoConfig',
    'users.apps.UsersConfig',
]

INSTALLED_APPS = DJANGO_APPS + REQUIREMENT_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'convertx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
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
# ***You might not want to include this in deployment
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

"""
deploy
"""

