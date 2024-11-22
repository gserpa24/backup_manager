# Configuración avanzada

## Variables de entorno
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