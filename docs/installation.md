# Instalación

A continuación, se describen los pasos necesarios para instalar y configurar **Backup Manager** en tu entorno.

## Requisitos previos
- Python 3.8 o superior.
- `govc` instalado y configurado.
- Acceso al servidor donde se ejecutarán los respaldos.

## Pasos de instalación
1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/usuario/backup_manager.git
   cd backup_manager
   ```

2. **Creacion de entorno virtual**:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```
   
3. **Instalacion de dependencias**:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configuracion de variables de entorno**:
     ```bash
     GOVC_USERNAME="usuario"
     GOVC_PASSWORD="contraseña"
     GOVC_URL="https://servidor-vcenter" 
     ```
