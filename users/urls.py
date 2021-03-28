from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('lockout/', views.lockout, name='lockout'),
]
