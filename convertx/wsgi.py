"""
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
from pathlib import Path

DOTENV_PATH = Path(__file__).parent.parent / 'env/.env'
load_dotenv(dotenv_path=DOTENV_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('CONVERTX_SETTINGS'))
application = get_wsgi_application()
