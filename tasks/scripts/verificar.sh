#!/bin/bash

#Ruta de backups.
backup_dir="/home/serpa/bk"

#Verficar directorio  existente
if [ ! -d "$backup_dir" ]; then
    echo "La ruta es incorrecta. Intente nuevamente."
    exit 1
fi

#Lista todas las carpetas del directorio.
echo "Carpetas disponibles en el directorio:"
folders=($(ls -d "$backup_dir"/*/))

#Verifica si hay carpetas en el directorio:
if [ ${#folders[@]} -eq 0 ]; then
    echo "No se encontraron carpetas"
    exit 1
fi

#Muestra las carpetas enumeradas
for i in "${!folders[@]}"; do
    folder_name=$(basename "${folders[$i]}")
    echo "$((i+1)). $folder_name"
done

#Solicita al usuario que seleccione una carpeta
echo "Seleccione una carpeta ingresando numero:"
read selected_number

#Verifica si la seleccion es valida
if [ "$selected_number" -lt 1 ] || [ "$selected_number" -gt "${#folders[@]}" ]; then
    echo "Seleccion invalida. Intente nuevamente."
    exit 1
fi

#Obtiene carpeta seleccionada
selected_folder="${folders[$((selected_number-1))]}"
echo "Has seleccionado la carpeta: $selected_folder"

#Busca archivo .mf en carpeta selccionada.
mf_file="$selected_folder/*.mf"
echo "Buscando archivo .mf en la carpeta seleccionada..."

#Verificar si archivo .mf existe
if ls $mf_file 1> /dev/null 2>&1; then
    mf_file=$(ls $selected_folder/*.mf | head -n 1) #Toma el primer archivo .mf
    echo "Archivo .mf encontrado: $mf_file"
else
    echo "No se encontró ningun archivo .mf"
    exit 1
fi

#Lee el archivo .mf y verifica los hacshes de los archivos
echo "Validando hashes..."
while read -r line; do
    #Extrae el algorimo, archivo y hash
    algorithm=$(echo "$line" | cut -d'(' -f1)
    file=$(echo "$line" | cut -d'(' -f2 | cut -d')' -f1)
    expected_hash=$(echo "$line" | cut -d'=' -f2 | tr -d ' ')

    #Contruye la ruta completa del archivo utilizando el directorio del archivo
    full_file_path="$selected_folder/$file"

    #Muestra detalles de las rutas.
    echo "Archivo esperado desde .mf: $file"
    echo "Ruta completa construida: $full_file_path"

    #Verifica que sea SHA256(Configurable)
    if [ "$algorithm" = "SHA256" ]; then
        if [ ! -f "$full_file_path" ]; then
            echo "El archivo $file no existe en ela ruta: $full_file_path."
            continue
        fi

        #Genera el hash real
        real_hash=$(sha256sum "$full_file_path" | awk '{print $1}')

        #Compara hashes
        if [ "$real_hash" = "$expected_hash" ]; then
            echo "$file: El hash coincide."
        else
            echo "$file: El hash NO coincide."
        fi
    fi
done < "$mf_file"

echo "Validacion de hashes completada."
