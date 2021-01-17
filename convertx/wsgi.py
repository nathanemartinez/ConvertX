"""
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

CUR_FILE = os.path.abspath(os.path.dirname(__file__))
MY_DOTENV_PATH = os.path.join(CUR_FILE, 'env/.env')
load_dotenv(dotenv_path=MY_DOTENV_PATH)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', str(os.getenv('CONVERTX_SETTINGS')))
application = get_wsgi_application()
