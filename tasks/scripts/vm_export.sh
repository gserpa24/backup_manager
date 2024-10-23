#!/bin/bash

# Configuración de govc
export GOVC_URL='https://192.168.50.20/sdk'
export GOVC_USERNAME='root'
export GOVC_PASSWORD='UNSM2022a'
export GOVC_INSECURE=true

#Variables
VM_NAME="Prueba_Respaldo"
DESTINATION_PATH="/home/serpa/bk"

#Funcion para apagar la VM
shutdown_vm() {
    echo "Apagando la VM..."
    govc vm.power -off -force "/ha-datacenter/vm/$VM_NAME"
    if [ $? -ne 0 ]; then
        echo "Error al apagar la VM."
        exit 1
    fi
}

#Funcion pare realizar limpieza y desfragmentacion
export_vm() {
        echo "Exportando $VM_NAME a OVF..."
        govc export.ovf  -sha=256 -vm "/ha-datacenter/vm/$VM_NAME" "$DESTINATION_PATH"
}

#Encender VM
power_on() {
    echo "Encendiedno la VM"
    govc vm.power -on "/ha-datacenter/vm/$VM_NAME"
    if [ $? -eq 0 ]; then
        echo "VM encendida con exito."
    else
        echo "Error al encender la VM"
    fi
}

#Ejecutar instrucciones
shutdown_vm
export_vm
power_on

echo "Proceso completado."
