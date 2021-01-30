"""
General project settings
https://docs.djangoproject.com/en/3.1/topics/settings/
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from dotenv import load_dotenv
from pathlib import Path
import os

DOTENV_PATH = Path(__file__).parent.parent.parent / 'env/.env'
load_dotenv(dotenv_path=DOTENV_PATH)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
ALLAUTH_DIR = os.path.join(BASE_DIR, 'templates', 'allauth')
DATABASE_DIR = os.path.join(BASE_DIR, 'db.sqlite3')
SECRET_KEY = os.environ.get('convertx_secret_key')  # high change secret key
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
    'tinymce',
    'simple_history',
    'guardian',
]

PROJECT_APPS = [
    'home.apps.HomeConfig',
    # 'demo.apps.DemoConfig',
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
]

DJANGO_ALLAUTH_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
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
    'simple_history.middleware.HistoryRequestMiddleware',
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
    'guardian.backends.ObjectPermissionBackend',
]

# Custom user model
AUTH_USER_MODEL = 'users.User'

# allauth, ref: https://django-allauth.readthedocs.io/en/latest/configuration.html
SITE_ID = int(os.getenv('SITE_ID'))
ACCOUNT_AUTHENTICATION_METHOD = os.getenv('ACCOUNT_AUTHENTICATION_METHOD')
ACCOUNT_EMAIL_REQUIRED = bool(os.getenv('ACCOUNT_EMAIL_REQUIRED'))
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = int(os.getenv('ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS'))
ACCOUNT_EMAIL_VERIFICATION = os.getenv('ACCOUNT_EMAIL_VERIFICATION')
ACCOUNT_MAX_EMAIL_ADDRESSES = int(os.getenv('ACCOUNT_MAX_EMAIL_ADDRESSES'))
ACCOUNT_LOGOUT_REDIRECT_URL = os.getenv('ACCOUNT_LOGOUT_REDIRECT_URL')
ACCOUNT_PRESERVE_USERNAME_CASING = bool(os.getenv('ACCOUNT_PRESERVE_USERNAME_CASING'))  # username is stored in lowercase
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = bool(os.getenv('ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE'))  # enter email twice to avoid typos
ACCOUNT_USERNAME_BLACKLIST = eval(os.getenv('ACCOUNT_USERNAME_BLACKLIST'))  # WARNING: this should not accept user import because "eval"
ACCOUNT_USERNAME_MIN_LENGTH = int(os.getenv('ACCOUNT_USERNAME_MIN_LENGTH'))  # minimum length of username

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

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'
