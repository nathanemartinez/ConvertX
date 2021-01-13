"""
https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('env/.env')
load_dotenv(dotenv_path=env_path)

ADMIN = os.getenv('ADMIN')
DEBUG = os.getenv('DEBUG')

# Package urls
urlpatterns = [
    path(f'{ADMIN}/', admin.site.urls),  # normal admin
    path(F'{ADMIN}/defender/', include('defender.urls')),  # defender admin
    path('accounts/', include('allauth.urls')),
]

# App urls
urlpatterns += [
    path('', include('home.urls')),
    path('', include('users.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path(f'{DEBUG}/', include(debug_toolbar.urls)),
    ]

handler400 = 'home.views.error_400'
handler403 = 'home.views.error_403'
handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'

