"""
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

CUR_FILE = os.path.abspath(os.path.dirname(__file__))
MY_DOTENV_PATH = os.path.join(CUR_FILE, 'env/.env')
load_dotenv(dotenv_path=MY_DOTENV_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', str(os.getenv('CONVERTX_SETTINGS')))
application = get_asgi_application()
