from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import subprocess

# Tareas disponibles
TASKS = {
    'exportar_vm': 'vm_Exporter.sh',
    'verificar_mf': 'verificar.sh',
    'comprimir_vm': 'comprimir.sh',
    'enviar_nas': 'scp_nas.sh'
}

@login_required
def home(request):
    return render(request, 'home.html', {'tasks': TASKS})

@login_required
def run_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        script_path = f'tasks/scripts/{TASKS[task]}'  # Ruta a tus scripts

        try:
            # Ejecuta el script seleccionado
            subprocess.run([script_path], check=True)
            message = f"Tarea {task} ejecutada con éxito."
        except subprocess.CalledProcessError as e:
            message = f"Error al ejecutar la tarea {task}: {e}"

        return render(request, 'result.html', {'message': message})
    return render(request, 'home.html', {'tasks': TASKS})

