#!/bin/bash

#Variables
DIRECTORIO_ORIGEN="/home/serpa/tar"
SERVIDOR_NAS="//192.168.50.6/Public"

#Listar archivos de directorio
echo "Archivos disponibles: "
shopt -s nullglob
FILES=("$DIRECTORIO_ORIGEN"/*.zip)

if [ ${#FILES[@]} -eq 0 ]; then
    echo "No hay archivos en $DIRECTORIO_ORIGEN:"
    exit 1
fi

select ARCHIVO in "${FILES[@]}"; do
    if [ -e "$ARCHIVO" ]; then
        echo "Has seleccionado: $ARCHIVO"
        break
    else
        echo "Opcion invalida, elige un indice valido."
    fi
done

# Enviar a NAS
read -p "¿Enviar al servidor NAS? (s/n): " RESP_NAS
if [ "$RESP_NAS" == "s" ]; then
    NOMBRE_ARCHIVO=$(basename "$ARCHIVO")

    echo "Enviando archivo: $ARCHIVO"

    smbclient "$SERVIDOR_NAS" -N -c "put \"$ARCHIVO\" \"$NOMBRE_ARCHIVO\""

    if [ $? -eq 0 ]; then
        echo "Archivo enviado al servidor NAS."
    else
        echo "Error al enviar el archivo."
    fi
fi
