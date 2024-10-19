from django.urls import path
from .views import home, script_view

urlpatterns = [
    path('home/', home, name='home'),
    path('ejecutar-script/', script_view, name='script_view'),
]
