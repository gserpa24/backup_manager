#!/bin/bash

# Variables
VM_NAME=$1  # Nombre de la VM, se pasa como argumento al script
EXPORT_PATH="/tmp/${VM_NAME}"  # Ruta temporal para la exportación
OVF_FILE="${VM_NAME}.ovf"  # Nombre del archivo OVF exportado
TAR_FILE="${VM_NAME}.tar.gz"  # Nombre del archivo comprimido
NAS_PATH="//<NAS_IP>/<shared_folder>"  # Ruta del recurso compartido NAS
NAS_USER="<usuario_nas>"  # Usuario del NAS
NAS_PASS="<password_nas>"  # Contraseña del NAS

# Apagar la máquina virtual con la opción -force y la ruta completa
echo "Apagando la VM ${VM_NAME}..."
govc vm.power -off -force "/ha-datacenter/vm/${VM_NAME}"
if [ $? -ne 0 ]; then
    echo "Error al apagar la VM."
    exit 1
fi

# Exportar la VM a OVF
echo "Exportando la VM ${VM_NAME} a OVF..."
mkdir -p "$EXPORT_PATH"
govc vm.export -vm "${VM_NAME}" -dir "$EXPORT_PATH"
if [ $? -ne 0 ]; then
    echo "Error al exportar la VM."
    exit 1
fi

# Comprimir la exportación
echo "Comprimiendo la exportación a ${TAR_FILE}..."
tar -czvf "${TAR_FILE}" -C "$EXPORT_PATH" .
if [ $? -ne 0 ]; then
    echo "Error al comprimir la exportación."
    exit 1
fi

# Enviar la exportación comprimida al NAS
echo "Enviando ${TAR_FILE} al NAS..."
smbclient "${NAS_PATH}" -U "${NAS_USER}%${NAS_PASS}" -c "put ${TAR_FILE}"
if [ $? -ne 0 ]; then
    echo "Error al enviar el archivo al NAS."
    exit 1
fi

# Limpiar archivos temporales
echo "Limpiando archivos temporales..."
rm -rf "$EXPORT_PATH"
rm -f "${TAR_FILE}"

echo "Proceso completado con éxito."
