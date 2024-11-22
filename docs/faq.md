# Preguntas Frecuentes (FAQ)

## 1. ¿Qué es este proyecto?
- **¿Cuál es el propósito de este proyecto?**

    El propósito es garantizar la seguridad de los datos de las máquinas virtuales mediante una solución sencilla que permita realizar backups automáticos o manuales. El proyecto facilita la administración y restauración de datos en caso de desastres o fallos.


- **¿Qué problemas resuelve este sistema de backup?**

    Este sistema resuelve los problemas relacionados con la protección de datos de máquinas virtuales, proporcionando una forma automatizada de realizar copias de seguridad y restaurar las máquinas virtuales rápidamente en caso de fallos.


- **¿Quién puede usar este proyecto?**
    Este proyecto está destinado a administradores de sistemas y equipos de infraestructura IT que gestionan entornos de virtualización VMware, y que necesitan una solución robusta y fácil de usar para hacer backups de sus máquinas virtuales.

## 2. Requisitos del Sistema
- **¿Qué sistemas operativos son compatibles con este proyecto?**

    Este sistema es compatible con sistemas operativos basados en Linux (como Ubuntu y CentOS), así como con macOS. Aunque también es posible ejecutarlo en Windows, se recomienda utilizar un sistema basado en Linux o macOS para un rendimiento óptimo.


- **¿Cuáles son los requisitos mínimos de hardware para ejecutar este sistema de backups?**

    Los requisitos mínimos incluyen:

    - Procesador de 2 núcleos.
    - 8 GB de RAM.
    - Espacio libre en disco suficiente para almacenar los backups de las máquinas virtuales.


- **¿Necesito tener acceso a una máquina virtual para usar este proyecto?**
    
    Sí, este proyecto está diseñado para crear y gestionar backups de máquinas virtuales, por lo que necesitas acceso a un entorno VMware donde puedas acceder y gestionar las máquinas virtuales que se respaldarán.

## 3. Instalación
- **¿Es necesario tener acceso a una infraestructura de VMware?**
    
    Sí, para que el proyecto funcione correctamente, es necesario tener acceso a un servidor VMware. El proyecto usa govc para interactuar con la infraestructura de VMware, por lo que debes asegurarte de tener las credenciales y permisos necesarios para acceder a la infraestructura de virtualización.

## 4. Configuración
- **¿Es necesario configurar algo en el servidor de backups?**
    
    Sí, es necesario configurar las credenciales de acceso a la infraestructura de VMware mediante las variables de entorno GOVC_URL, GOVC_USERNAME y GOVC_PASSWORD. Además, es recomendable revisar el sistema de almacenamiento para asegurarse de que hay suficiente espacio para los backups.

## 5. Uso del Sistema de Backups
- **¿Cómo se realiza un backup de una máquina virtual con este sistema?**

    Puedes verlo en la ["Guia de uso"](guide/usage.md)


- **¿Puedo programar backups automáticos de mis máquinas virtuales?**

    Sí, puedes configurar la programación de backups automáticos utilizando herramientas como cron en Linux. Esto te permitirá ejecutar el proceso de backup en intervalos regulares sin intervención manual.


- **¿Cómo puedo verificar el estado de una máquina virtual antes de realizar un backup?**

    Puedes verlo en la ["Guia de uso"](guide/usage.md)


- **¿Dónde se almacenan los archivos de backup?**

    Los archivos de backup se almacenan en la ubicación configurada en el sistema. Si no se especifica una ruta personalizada, se almacenarán en la ubicación predeterminada definida por el sistema.


- **¿Cómo puedo restaurar un backup?**

    Puedes verlo en la ["Guia de uso"](guide/usage.md)

## 6. Errores Comunes
- **¿Qué hacer si el sistema no reconoce las máquinas virtuales?**

    Verifica que las credenciales y las variables de entorno estén correctamente configuradas. Asegúrate de que el servidor VMware esté accesible y que las máquinas virtuales estén activas.


- **¿Por qué no puedo realizar un backup de una máquina virtual?**

    Revisa que la máquina virtual esté encendida y que puedas acceder a ella desde el servidor de VMware. Además, asegúrate de que las credenciales y la configuración de govc sean correctas.


- **¿Qué significa el error "No se encuentra el comando govc"?**

    Este error significa que la herramienta govc no está instalada o no está en el PATH del sistema. Asegúrate de haber instalado correctamente govc y de que sea accesible desde la terminal.


- **¿Por qué no se muestran los detalles de la máquina virtual en el sistema?**

    Esto puede ocurrir si las credenciales no están configuradas correctamente o si el servidor de VMware no es accesible. Verifica la configuración de govc y asegúrate de que el servidor de VMware esté funcionando correctamente.


## 7. Mantenimiento y Actualizaciones
- **¿Cómo actualizo el sistema de backups?**

    Para actualizar el sistema, puedes hacer un git pull del repositorio y luegoactualizar las dependencias con:
    ```bash
    pip install -r requirements.txt --upgrade
    ```
  
- **¿Es necesario reiniciar el servidor después de actualizar el sistema de backups?**

    No es necesario reiniciar el servidor, pero es recomendable reiniciar los servicios relacionados con los backups para asegurarte de que todos los cambios se apliquen correctamente.

## 8. Seguridad
- **¿Se cifran los backups?**

    El sistema de backups no cifra los archivos de forma predeterminada, pero puedes añadir cifrado como una capa adicional de seguridad para proteger los datos.


- **¿Cómo puedo realizar copias de seguridad seguras de las credenciales y variables de entorno?**

    Asegúrate de almacenar las credenciales y variables de entorno en un lugar seguro, como un archivo .env que no se suba a repositorios públicos. También puedes utilizar herramientas de gestión de secretos para manejar de manera segura las credenciales.

## 9. Contribución
- **¿Cómo puedo contribuir al desarrollo de este proyecto?**

    Puedes contribuir al proyecto realizando un fork del repositorio, haciendo cambios y enviando un pull request con tus modificaciones. Asegúrate de seguir las guías de contribución para mantener la coherencia del proyecto.


- **¿Cuál es el proceso para enviar una solicitud de extracción (Pull Request)?**

    Para enviar un pull request, realiza un fork del repositorio, realiza los cambios en tu fork y luego crea un pull request explicando los cambios que has realizado. Asegúrate de que el código esté probado y documentado.


- **¿Qué reglas debo seguir al contribuir al código?**

    Asegúrate de seguir las mejores prácticas de codificación, escribir pruebas para tu código y documentar los cambios realizados. También es importante mantener la coherencia con el estilo de codificación existente en el proyecto.

## 10. Licencia y Uso
- **¿Bajo qué licencia se distribuye este proyecto?**

    Este proyecto se distribuye bajo la licencia Apache 2.0, lo que permite su uso, modificación y distribución, siempre que se respeten los términos de la licencia.

## 11. Soporte
- **¿Dónde puedo obtener soporte si tengo problemas con el sistema?**

    Puedes obtener soporte a través de los problemas ["(issues)"](https://github.com/gserpa24/backup_manager/issues) del repositorio de GitHub o contactar con los mantenedores del proyecto para recibir ayuda.

## 12. Otros
- **¿Puedo usar este sistema para realizar backups de otros servicios, no solo de máquinas virtuales?**

    Este proyecto está diseñado específicamente para realizar backups de máquinas virtuales en entornos VMware, por lo que no es adecuado para respaldar otros tipos de servicios. Sin embargo, puedes modificar el código para adaptarlo a otros tipos de servicios.
