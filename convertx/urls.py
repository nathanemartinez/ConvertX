"""
https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from dotenv import load_dotenv
import os

CUR_FILE = os.path.abspath(os.path.dirname(__file__))
MY_DOTENV_PATH = os.path.join(CUR_FILE, 'env/.env')
load_dotenv(dotenv_path=MY_DOTENV_PATH)

ADMIN_URL = str(os.getenv('ADMIN_URL'))

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

