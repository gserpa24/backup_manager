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

    # Diccionario para mapear nombres de scripts a sus rutas
    scripts = {
        'script1': os.path.join('tasks', 'scripts', 'comprimir.bat'),
        'script2': os.path.join('tasks', 'scripts', 'script2.bat'),
        'script3': os.path.join('tasks', 'scripts', 'script3.bat'),
    }

    if request.method == 'POST':
        script_name = request.POST.get('script_name')
        script_path = scripts.get(script_name)

        if script_path:
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

    return render(request, 'mi_template.html', {'output': output, 'error': error, 'scripts': scripts})