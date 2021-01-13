"""
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('env/.env')
load_dotenv(dotenv_path=env_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('CONVERTX_SETTINGS'))
application = get_asgi_application()
