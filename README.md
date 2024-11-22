# Sistema de Backup

## Descripción
El **Sistema de Backup** es una solución automatizada que permite realizar copias de seguridad de máquinas virtuales y restaurarlas en caso de fallos. Está diseñado para integrarse con entornos de virtualización como **VMware ESXi** y servidores **NAS** para la transferencia y almacenamiento de archivos. El sistema incluye funcionalidades de exportación de máquinas virtuales, verificación de integridad de archivos, compresión de datos y envío a servidores de almacenamiento remoto.

**Documentacion:** https://gserpa24.github.io/backup_manager/

## Características

- **Exportación de VMs**: Exporta máquinas virtuales en formatos OVF/OVA mediante `govc`.
- **Verificación de Integridad**: Verifica la integridad de los archivos exportados (.mf) antes de la compresión.
- **Compresión**: Comprime los archivos exportados en formato `.zip` para optimizar el espacio de almacenamiento.
- **Transferencia a NAS**: Envío automatizado de archivos comprimidos a servidores NAS usando `smbclient` para transferencia segura.
- **Automatización con Scripts**: Los procesos de copia y restauración están automatizados mediante scripts en bash.

## Tecnologías Utilizadas

- **Bash**: Scripts automatizados para realizar las tareas de backup.
- **VMware ESXi**: Para la gestión de las máquinas virtuales y exportación de OVF/OVA con `govc`.
- **smbclient**: Utilizado para la transferencia de archivos a servidores NAS.
- **Linux (Ubuntu)**: Sistema operativo base para ejecutar los scripts y automatizaciones.
--- 
## Reglas de Contribución

- Mantén el código claro, legible y bien documentado.
- Asegúrate de que tus cambios no rompan la funcionalidad existente.
- Comunícate con el equipo del proyecto si tienes dudas o necesitas orientación.

## Reporte de Errores

Si encuentras un problema:

1. **Verifica** que no esté ya reportado en la pestaña ["Issues"](https://github.com/gserpa24/backup_manager/issues).
2. **Crea un nuevo reporte** proporcionando:
   - Una descripción clara del problema.
   - Pasos detallados para reproducir el error.
   - Información sobre tu entorno, incluyendo:
     - Sistema operativo.
     - Versión de Python.
     - Otros datos relevantes.


## Autores

- **[Gustavo Luis Serpa Rengifo]** - Desarrollador principal - [GitHub][(https://github.com/gserpa24)]
