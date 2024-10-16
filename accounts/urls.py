from django.urls import path
from .views import login_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),  # Ruta para login
    path('register/', register_view, name='register'),  # Ruta para register
]