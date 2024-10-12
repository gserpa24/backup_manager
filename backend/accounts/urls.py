# accounts/urls.py

from django.urls import path
from .views import login_view, register_view, home_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', home_view, name='home'),  # Vista de inicio
]
