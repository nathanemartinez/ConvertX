from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('400/', views.error_400, name='400'),
    path('403/', views.error_403, name='403'),
    path('404/', views.error_404, name='404'),
    path('500/', views.error_500, name='500'),
]
