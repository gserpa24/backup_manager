from django.urls import path
from .views import home, list_vms_view, execute_vm_script

urlpatterns = [
    path('home/', home, name='home'),
    path('vms/', list_vms_view, name='list_vms'),
    path('execute_vm_script/<str:vm>/', execute_vm_script, name='execute_vm_script'),
]
