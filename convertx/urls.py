"""
https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('debug/', include(debug_toolbar.urls)),
    ]

handler400 = 'home.views.error_400'
handler403 = 'home.views.error_403'
handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'
