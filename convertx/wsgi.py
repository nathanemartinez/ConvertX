"""
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
from convertx.constants import DOTENV_PATH

load_dotenv(dotenv_path=DOTENV_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('CONVERTX_SETTINGS'))
application = get_wsgi_application()
