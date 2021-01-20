"""
https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from dotenv import load_dotenv
from pathlib import Path
import os

DOTENV_PATH = Path(__file__).parent.parent / 'env/.env'
load_dotenv(dotenv_path=DOTENV_PATH)

ADMIN_URL = os.getenv('ADMIN_URL')

# Package urls
urlpatterns = [
    path(f'{ADMIN_URL}/', admin.site.urls),  # normal admin
    # low get rid of defender url - it just shows a detail view of defender
    path(F'{ADMIN_URL}/defender/', include('defender.urls')),  # defender admin
    path('accounts/', include('allauth.urls')),
]

# App urls
urlpatterns += [
    path('', include('home.urls')),
    path('', include('users.urls')),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path(f'debug/', include(debug_toolbar.urls)),
    ]

handler400 = 'home.views.error_400'
handler403 = 'home.views.error_403'
handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'

