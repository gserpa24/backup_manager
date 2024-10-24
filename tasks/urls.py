from django.urls import path
from .views import home, script_view, list_vms_view

urlpatterns = [
    path('home/', home, name='home'),
    path('ejecutar-script/', script_view, name='script_view'),
    path('listar-vms/', list_vms_view, name='list_vms'),
]
