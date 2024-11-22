## Requisitos del Sistema
### Sistema Operativo
- Ubuntu Server.

### Requisitos de Hardware
- Procesador: 2 núcleos o más.
- Memoria RAM: 8 GB mínimo.
- Espacio en disco: 20 GB a más(adaptable a los requerimientos).

### Base de datos
- PostgreSQL 14.x

## Dependencias Necesarias
- **govc**: Herramienta de línea de comandos para VMware.
- **Python**: Versión 3.10 o superior.

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

    > **Nota:** Las credenciales de acceso deben ser alojadas dentro de un archivo .env en la raiz del repositorio.
    
    El archivo `.env` debe quedar de la siguiente forma:

     ```bash
     GOVC_URL=https://servidor-vcenter
     GOVC_USERNAME=usuario
     GOVC_PASSWORD=contraseña
     GOVC_INSECURE=1
     ```
    
    ### **GOVC_URL**
    Esta variable define la URL del vCenter o servidor ESXi al que se quiere conectar. La URL puede incluir el protocolo `https` y el puerto si es necesario.

    ```bash
    export GOVC_URL="https://<host>:<port>/sdk"
    ```

    ### **GOVC_USERNAME**
    Define el nombre de usuario que se utilizará para autenticar en vCenter o ESXi. Este usuario debe tener permisos suficientes para las operaciones que necesitas realizar.

    ```bash
    export GOVC_USERNAME="username"
    ```
   
    ### **GOVC_PASSWORD**
    Especifica la contraseña asociada al usuario `GOVC_USERNAME`. Esta contraseña se utilizará para autenticarse al realizar operaciones.

    ```bash
    export GOVC_PASSWORD="password"
    ```
    
    ### **GOVC_INSECURE**
    Esta variable de entorno permite ignorar los errores de certificado SSL al conectarse a vCenter o ESXi. Esto es útil si tienes un certificado autofirmado o no confiable. Se le asigna el valor de `true` o `false`.

    ```bash
    export GOVC_INSECURE="true/false"
    ```
    
    ## **Pasos para Configurar las Variables de Entorno de `govc`**
    
    Sigue los siguientes pasos para configurar las variables de entorno de `govc` en tu sistema:
    
    ### **Establece las Variables de Entorno**
    En una terminal, utiliza el comando `export` para definir las variables de entorno.

    ```bash
    export GOVC_URL="https://<host>:<port>/sdk"
    export GOVC_USERNAME="username"
    export GOVC_PASSWORD="password"
    export GOVC_INSECURE="true"
    ```
    >**Nota:** Recuerda que puedes incluir estas configuraciones en los archivos de inicio de tu shell (por ejemplo, `.bashrc` o `.zshrc` en Linux/macOS) para que se apliquen automáticamente cada vez que inicies sesión.

    ### **Verifica la Configuración**
    Para asegurar que las variables de entorno estén correctamente configuradas, puedes usar el siguiente comando para comprobar la conexión a el servidor vCenter o ESXi. Este comando debería mostrarte detalles sobre la versión de vCenter o ESXi a la que estás conectado, lo que indica que las variables están correctamente configuradas:
    
    ```bash
    govc about
    ```

