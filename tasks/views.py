from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Tareas disponibles
TASKS = {
    'exportar_vm': 'vm_Exporter.sh',
    'verificar_mf': 'verificar.sh',
    'comprimir_vm': 'comprimir.sh',
    'enviar_nas': 'scp_nas.sh'
}


@login_required
def home(request):
    return render(request, 'home.html')
