"""
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv
from convertx.constants import DOTENV_PATH
import os

load_dotenv(dotenv_path=DOTENV_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('CONVERTX_SETTINGS'))
application = get_asgi_application()
