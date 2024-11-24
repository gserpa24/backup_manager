# Guía de Uso del Sistema de Backups

Este sistema ha sido diseñado para gestionar y monitorear de manera eficiente las máquinas virtuales (VMs) de tu entorno, permitiéndote realizar backups, verificar estados, y generar reportes detallados. Aquí se describe cómo utilizar cada una de las funcionalidades.

---

## **Vista Principal: Estado de la Máquina Virtual Anfitriona**

### Descripción
En esta vista puedes ver información clave sobre la máquina anfitriona (el servidor principal que aloja las máquinas virtuales).

### Información Mostrada:
- **Uso de CPU**: Porcentaje de uso actual.
- **Uso de RAM**: Memoria RAM total y disponible.
- **Espacio en Disco**: Espacio usado y disponible.
- **Actividad de Red**: Velocidad de carga y descarga.

### Propósito
Proporcionar una visión general del estado del sistema anfitrión para garantizar su buen funcionamiento.

---

## **Vista de Máquinas Virtuales**

Esta vista lista todas las máquinas virtuales disponibles en tu entorno. Para cada VM, hay opciones de interacción y detalles relevantes.

### **Funciones Disponibles:**

**Lista de Máquinas Virtuales**:

   - Muestra el nombre de cada VM junto con información básica.

**Botón "Verificar Estado"**:

- Al hacer clic, se abre un **modal** con información detallada de la máquina virtual seleccionada:
  - Nombre de la máquina.
  - Sistema operativo.
  - Tamaño del disco.
  - Número de CPUs.
  - Memoria RAM.
  - Estado actual (encendida/apagada/suspendida).

**Botón "Backup"**:

   - Inicia el proceso de respaldo para la máquina virtual seleccionada.
   - Una vez finalizado el backup, el sistema almacena automáticamente un registro en la sección de **Reportes**.

---

## **Vista de Reportes**

### Descripción
Esta sección almacena un historial completo de los backups realizados, proporcionando detalles importantes para su seguimiento.

### Información Mostrada:
- **Nombre de la VM**: La máquina virtual para la cual se realizó el backup.
- **Estado**: Indica si el backup fue exitoso o si ocurrió algún error.
- **Fecha y Hora**: Momento en que se inició el backup.
- **Duración**: Tiempo que tomó completar el proceso.
- **Tamaño**: Tamaño total del archivo de respaldo (en MB o GB).
- **Usuario**: Nombre del usuario que ejecutó el backup.

### Funciones:
- **Filtro por Fecha**: Permite buscar backups realizados en un rango de fechas específico.
- **Exportar Reporte**: Opción para descargar un archivo con los reportes (en formato PDF o CSV).

---

## **Cómo Usar el Sistema**

**Inicio del Sistema**:

   - Accede al sistema desde el navegador ingresando la URL proporcionada.

**Autenticacion de Usuario**:

   - Accede al sistema con las credenciales de acceso validas.

**Monitorear el Estado del Anfitrión**:

   - Ve a la vista principal para verificar que el anfitrión tenga suficientes recursos disponibles antes de realizar backups.

**Realizar Backups**:

   - Ve a la lista de máquinas virtuales.
   - Encuentra la máquina deseada y presiona el botón **"Backup"**.
   - Monitorea el estado del proceso y espera la notificación de finalización.

**Verificar el Estado de una VM**:

   - En la misma lista, presiona el botón **"Estado"** de la máquina que deseas inspeccionar.

**Revisar Reportes**:

   - Dirígete a la sección de **Reportes** para consultar el historial de backups.
   - Filtra y descarga información según sea necesario.

---

## **Recomendaciones Generales**

- Realiza backups regularmente para garantizar la seguridad de tus datos.
- Antes de realizar un backup, verifica el estado del anfitrión para asegurarte de que hay suficiente espacio y recursos disponibles.
- Consulta los reportes periódicamente para asegurarte de que todos los procesos de backup se han completado exitosamente.

---

## **Soporte Técnico**

Si encuentras problemas o tienes dudas sobre el sistema, contacta al equipo de soporte en **gusserpa02@gmail.com**.
