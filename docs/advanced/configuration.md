# Configuración avanzada

### **Variables de entorno para el usuario**
Si quieres que las variables sean accesibles solo para tu usuario, debes agregarlas al archivo `~/.bashrc` o `~/.bash_profile`.

```bash
nano ~/.bashrc
```
Agrega las variables al final del archivo, con el prefijo `export`:
```bash
export GOVC_URL="https://<host>:<port>/sdk"
export GOVC_USERNAME="username"
export GOVC_PASSWORD="password"
export GOVC_INSECURE="true"
export GOVC_DATACENTER="MyDataCenter"
export GOVC_DATASTORE="MyDataStore"
export GOVC_NETWORK="VM Network"
```
Guarda el archivo y sal (`CTRL + O`, luego `CTRL + X`).

Recarga el archivo para aplicar los cambios:
```bash
source ~/.bashrc
```
Verifica que las variables estén configuradas:
```bash
env | grep GOVC
```
>**Nota:** Reinicia el sistema y vuelve a verificar las variables para confirmar la correcta confeiguracion de las variables.
### **GOVC_DATACENTER**
Define el centro de datos en el que deseas realizar las operaciones. Si no se especifica, `govc` usará el centro de datos predeterminado.

```bash
export GOVC_DATACENTER="Datacenter1"
```

### **GOVC_DATASTORE** 
Esta variable es opcional y se utiliza para definir el datastore en el que se almacenarán las máquinas virtuales, discos o archivos ISO. Si no se especifica, se usará el datastore predeterminado.

```bash
export GOVC_DATASTORE="Datastore1"
```
    
### **GOVC_NETWORK**
Permite especificar la red a la que se conectarán las máquinas virtuales. Esta variable se usa principalmente cuando se está configurando una máquina virtual nueva o realizando operaciones relacionadas con la red.

```bash
export GOVC_NETWORK="VM Network"
```