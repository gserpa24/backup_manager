# Sistema de Backup

## Descripción

El **Sistema de Backup** es una solución automatizada que permite realizar copias de seguridad de máquinas virtuales y restaurarlas en caso de fallos. Está diseñado para integrarse con entornos de virtualización como **VMware ESXi** y servidores **NAS** para la transferencia y almacenamiento de archivos. El sistema incluye funcionalidades de exportación de máquinas virtuales, verificación de integridad de archivos, compresión de datos y envío a servidores de almacenamiento remoto.

## Características

- **Exportación de VMs**: Exporta máquinas virtuales en formatos OVF/OVA mediante `govc`.
- **Verificación de Integridad**: Verifica la integridad de los archivos exportados (.mf) antes de la compresión.
- **Compresión**: Comprime los archivos exportados en formato `.zip` para optimizar el espacio de almacenamiento.
- **Transferencia a NAS**: Envío automatizado de archivos comprimidos a servidores NAS usando `smbclient` para transferencia segura.
- **Automatización con Scripts**: Los procesos de copia y restauración están automatizados mediante scripts en bash.

## Instalación

Sigue estos pasos para instalar el sistema en tu entorno local:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/gserpa24/backup_manager.git
   cd backup_manager

## Uso
1. **Ingresar a la carpeta scripts**
   ```bash
   cd scripts
2. **Exportar una Máquina Virtual**
   ```bash
   ./vm_export.sh
3. **Verificar Integridad de archivos**
   ```bash
   ./verificar.sh
4. **Comprimir archivos exportados**
   ```bash
   ./comprimir.sh
5. **Enviar archivos al NAS**
   ```bash
   ./scp_nas.sh

## Autores

- **[Gustavo Luis Serpa Rengifo]** - Desarrollador principal - [GitHub][(https://github.com/gserpa24)]

## Tecnologías Utilizadas

- **Bash**: Scripts automatizados para realizar las tareas de backup.
- **VMware ESXi**: Para la gestión de las máquinas virtuales y exportación de OVF/OVA con `govc`.
- **smbclient**: Utilizado para la transferencia de archivos a servidores NAS.
- **Linux (Ubuntu)**: Sistema operativo base para ejecutar los scripts y automatizaciones.
