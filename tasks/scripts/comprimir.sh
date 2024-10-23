#!/bin/bash

#Variables
RUTA_ALMACENAMIENTO="/home/serpa/tar"
#Leer ruta del directorio
read -p "Ingresa la ruta del directorio a comprimir: " DIRECTORIO

#Leer el nombre del archivo comprimido
read -p "Ingresa el nombre con el que almacenara el archivo: " NOMBRE_ARCHIVO

#Comprimir el directorio
ZIP_ARCHIVO="$RUTA_ALMACENAMIENTO/$NOMBRE_ARCHIVO.zip"

#Verificar si tiene archivos
if [ -z "$(ls -A "$DIRECTORIO")" ]; then
    echo "El directorio esta vacio. No se puede comprimir."
    exit 1
fi

#Cambia a directorio especificado
cd "$DIRECTORIO" || exit
zip -r - . | pv -s $(du -sb "$DIRECTORIO" | awk '{print $1}') > "$ZIP_ARCHIVO"

#Verificar si compresion fue exitora
if [ $? -eq 0 ]; then
    echo "Directorio comprimido en $ZIP_ARCHIVO"
else
    echo "Error al comprimir el directorio"
fi
