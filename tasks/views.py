from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import subprocess
import os
from django.conf import settings
# Tareas disponibles
TASKS = {
    'exportar_vm': 'vm_Exporter.sh',
    'verificar_mf': 'verificar.sh',
    'comprimir_vm': 'comprimir.bat',
    'enviar_nas': 'scp_nas.sh'
}


@login_required
def home(request):
    return render(request, 'home.html')


def script_view(request):
    output = ''
    error = ''

    # Ruta del script
    script_path = os.path.join('tasks', 'scripts', 'comprimir.bat')

    if request.method == 'POST':
        try:
            # Ejecutar el script y capturar la salida
            result = subprocess.run(['cmd', '/c', script_path],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True,
                                    shell=True,
                                    check=True)
            output = result.stdout
            error = result.stderr
        except subprocess.CalledProcessError as e:
            output = e.stdout
            error = e.stderr

    return render(request, 'mi_template.html', {'output': output, 'error': error})