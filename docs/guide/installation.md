# Instalación

## Requisitos del Sistema
### Sistema Operativo
- Ubuntu Server (recomendado).
- Compatible con distribuciones basadas en Debian.

### Requisitos de Hardware
- Procesador: 2 núcleos o más.
- Memoria RAM: 4 GB mínimo.
- Espacio en disco: 20 GB o más.

## Dependencias Necesarias
- **govc**: Herramienta de línea de comandos para VMware.
- **Python**: Versión 3.8 o superior.
- Librerías de Python:
  - `django`
  - `requests`
  - `psycopg2`

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
