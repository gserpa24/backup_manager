import os
import psutil
import json
import subprocess
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.timezone import now
from tasks.models import Backup
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def home(request):
    # Estadísticas de disco
    disk_usage = psutil.disk_usage('/')
    total_disk = disk_usage.total // (1024 ** 3)  # en GB
    used_disk = disk_usage.used // (1024 ** 3)  # en GB
    free_disk = disk_usage.free // (1024 ** 3)  # en GB
    disk_percent = disk_usage.percent

    # Estadísticas de RAM
    memory = psutil.virtual_memory()
    total_ram = memory.total // (1024 ** 2)  # en MB
    used_ram = memory.used // (1024 ** 2)  # en MB
    free_ram = memory.available // (1024 ** 2)  # en MB
    ram_percent = memory.percent

    # Estadísticas de red
    net_io = psutil.net_io_counters()
    sent_data = net_io.bytes_sent // (1024 ** 2)  # en MB
    received_data = net_io.bytes_recv // (1024 ** 2)  # en MB

    context = {
        'disk': {
            'total': total_disk,
            'used': used_disk,
            'free': free_disk,
            'percent': disk_percent,
        },
        'ram': {
            'total': total_ram,
            'used': used_ram,
            'free': free_ram,
            'percent': ram_percent,
        },
        'network': {
            'sent': sent_data,
            'received': received_data,
        }
    }
    return render(request, 'home.html', context)

@login_required
def get_stats(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Lógica de datos como antes
        disk_usage = psutil.disk_usage('/')
        memory = psutil.virtual_memory()
        net_io = psutil.net_io_counters()

        data = {
            'disk': {
                'total': disk_usage.total // (1024 ** 3),  # GB
                'used': disk_usage.used // (1024 ** 3),  # GB
                'free': disk_usage.free // (1024 ** 3),  # GB
                'percent': disk_usage.percent,
            },
            'ram': {
                'total': memory.total // (1024 ** 2),  # MB
                'used': memory.used // (1024 ** 2),  # MB
                'free': memory.available // (1024 ** 2),  # MB
                'percent': memory.percent,
            },
            'network': {
                'sent': net_io.bytes_sent // (1024 ** 2),  # MB
                'received': net_io.bytes_recv // (1024 ** 2),  # MB
            }
        }
        return JsonResponse(data)

    # Redirigir a la página principal si no es AJAX
    return redirect('home')

@login_required
def list_vms_view(request):
    output = ''
    error = ''
    vms = []

    try:
        # Ejecutar el comando govc para listar las máquinas virtuales
        result = subprocess.run(
            ['govc', 'find', '-type', 'm'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        output = result.stdout
        error = result.stderr

    except subprocess.CalledProcessError as e:
        error = f"Ocurrió un error al ejecutar el comando govc: {e.stderr}"

    except FileNotFoundError:
        error = "La herramienta no está instalada o no es accesible desde este servidor."

    # Procesar la salida si no hay errores
    if not error:
        # Dividir la salida por líneas y extraer nombres de VM
        lines = output.splitlines()
        vms = [line.split('/')[-1] for line in lines if line]

    return render(request, 'list_vms.html', {'vms': vms, 'error': error})

@login_required
def get_vm_details(request, vm_id):
    print(f"Recibiendo solicitud para VM con ID: {vm_id}")
    try:
        # Comando para obtener los detalles de la VM usando govc
        command = [
            "govc",
            "vm.info",
            "-json",
            vm_id
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        vm_info = result.stdout

        # Parsear el resultado (verificar si es JSON válido)
        vm_data = json.loads(vm_info)

        # Validar la estructura de los datos
        if not vm_data.get("virtualMachines"):
            raise ValueError("No se encontraron máquinas virtuales en la respuesta.")

        # Extraer los datos relevantes
        vm = vm_data["virtualMachines"][0]

        # Tamaño ocupado (en GB)
        committed_size = vm.get("summary", {}).get("storage", {}).get("committed", 0) // (1024 ** 3)

        vm_details = {
            "name": vm.get("name", "Desconocida"),
            "os": vm.get("config", {}).get("guestFullName", "Desconocido"),
            "cpu": vm.get("config", {}).get("hardware", {}).get("numCPU", 0),
            "memory": f"{vm.get('config', {}).get('hardware', {}).get('memoryMB', 0) // 1024} GB",
            "storage": f"{committed_size} GB",
        }

        # Devolver los detalles como JSON
        return JsonResponse(vm_details)

    except subprocess.CalledProcessError as e:
        return JsonResponse({"error": f"Error al ejecutar govc: {e.stderr}"}, status=500)
    except json.JSONDecodeError:
        return JsonResponse({"error": "La salida de govc no es un JSON válido."}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@login_required
def execute_vm_script(request, vm):
    output = ''
    error = ''
    vm_name = vm
    start_time = now()

    # Decodificar la ruta de la VM
    #vm_name = base64.urlsafe_b64decode(vm.encode()).decode()

    # Configurar variables de entorno para govc
    os.environ['GOVC_URL'] = settings.GOVC_URL
    os.environ['GOVC_USERNAME'] = settings.GOVC_USERNAME
    os.environ['GOVC_PASSWORD'] = settings.GOVC_PASSWORD
    os.environ['GOVC_INSECURE'] = settings.GOVC_INSECURE

    # Verificar que las variables de entorno estén configuradas (para depuración)
    print({vm_name: vm})

    try:
        # Apagar la VM
        power_off_cmd = ["govc", "vm.power", "-off", "-force", vm_name]
        result = subprocess.run(power_off_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Apagar VM: {result.stdout.decode().strip()}") #Mensaje de depuracion

        # Definir rutas y variables para la exportación
        export_path = f"/tmp/{vm_name}"
        os.makedirs(export_path, exist_ok=True)
        print(f"Directorio de exportacion creado: {export_path}")

        # Verificar si el archivo OVF ya existe
        ovf_file_path = os.path.join(export_path, f"{vm_name}/{vm_name}.ovf")
        if not os.path.exists(ovf_file_path):
            export_cmd = ["govc", "export.ovf", "-sha=256", "-vm", vm_name, export_path]
            result = subprocess.run(export_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Exportar OVF: {result.stdout.decode().strip()}")  # Mensaje de depuración
        else:
            print(f"El archivo OVF ya existe: {ovf_file_path}. Saltando la exportación.")

        # Comprimir la exportación
        tar_file = f"/tmp/{vm_name}.tar.gz"
        tar_cmd = ["tar", "-czvf", tar_file, "-C", export_path, "."]
        result = subprocess.run(tar_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Comprimir: {result.stdout.decode().strip()}")  # Mensaje de depuración

        print(f"Ruta del archivo tar: {tar_file}")  # Imprimir la ruta del archivo tar

        #Tamaño de archivo exportado
        vm_size = os.stat(tar_file).st_size


        #Tiempo de ejecucion
        execution_time = now() - start_time

        #Registrar respaldo en bd
        backup = Backup.objects.create(
            vm_name=vm_name,
            user=request.user,
            execution_time=execution_time,
            vm_size=vm_size,
            backup_file_path=tar_file,
            success=True,
        )
        print(f"Respaldo registardo: {backup}")

        os.chdir("/tmp")
        # Enviar el archivo al NAS
        nas_path = "//192.168.50.6/Public"  # Reemplaza con la IP y carpeta del NAS
        tar = f"/tmp/{vm_name}.tar.gz"
        #nas_user = "<usuario_nas>"  # Reemplaza con el usuario NAS
        #nas_pass = "<password_nas>"  # Reemplaza con la contraseña NAS

        # print("Directorio de trabajo actual:", os.getcwd())

        if not os.path.exists(tar):
            print(f"El archivo {tar} no existe.")
        else:
            smb_cmd = ["smbclient", nas_path, "-N", "-c", f"put {vm_name}.tar.gz"]
            try:
                result = subprocess.run(smb_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"Enviado al NAS {result.stdout.decode().strip()}")  # Mensaje de depuración
            except subprocess.CalledProcessError as e:
                print(f"Error al enviar al NAS {e.stderr.decode().strip()}")

        # Limpiar archivos temporales
        subprocess.run(["rm", "-rf", export_path], check=True)
        subprocess.run(["rm", "-f", tar_file], check=True)

        #Encender vm
        power_on_cmd = ["govc", "vm.power", "-on", vm_name]
        result = subprocess.run(power_on_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Encender VM: {result.stdout.decode().strip()}")  # Mensaje de depuracion

        output = "Proceso completado con éxito."

    except subprocess.CalledProcessError as e:
        output = "Error en el proceso."
        error = f"Comando fallido: {e.cmd}. Salida de error: {e.stderr}"

        backup = Backup.objects.create(
            vm_name=vm_name,
            user=request.user,
            execution_time=now() - start_time,
            vm_size=0,
            backup_file_path=tar_file,
            success=False,
            error_message=error,
        )

    return render(request, 'execute_vm_script.html', {'output': output, 'error': error})

@login_required
def backup_reports(request):
    backups = Backup.objects.all().order_by('-backup_date')

    return render(request, 'backup_reports.html', {'backups': backups})