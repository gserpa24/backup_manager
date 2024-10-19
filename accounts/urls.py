from django.urls import path
from .views import login_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),  # Ruta para login
    path('logout/', logout_view, name='logout'),
]
