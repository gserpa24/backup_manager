# Restablecimiento Manual de Máquinas Virtuales desde Archivos Exportados

Este documento describe los pasos detallados para restablecer manualmente máquinas virtuales (VMs) en un hipervisor, utilizando archivos exportados (OVF/OVA) y realizando ajustes en los archivos `.ovf` para especificar la ubicación de la ISO.

---

## **1. Requisitos Previos**

Antes de iniciar el proceso, asegúrate de contar con lo siguiente:

1. **Archivos Exportados**:
   - Archivos `.ovf` (Open Virtualization Format) que definen la configuración de la máquina virtual.
   - Archivos `.vmdk` o equivalentes, que contienen el disco virtual.
   - Opcionalmente, archivos `.mf` (contienen sumas de verificación) o `.cert` (certificados).

2. **Acceso al Hipervisor**:
   - Cliente de administración del hipervisor (vSphere, VMware Workstation, etc.).
   - Credenciales para acceso.

3. **Herramientas de Edición de Texto**:
   - Editor de texto plano (como `vim`, `nano`, o Notepad++).

---

## **2. Subir Archivos Exportados al Hipervisor**

1. **Conectar al Hipervisor**:
   - Accede al hipervisor (por ejemplo, ESXi) usando el cliente web o SSH.

2. **Cargar los Archivos**:
   - Usa el cliente de administración para subir los archivos `.ovf` y `.vmdk` al almacenamiento de datos del hipervisor.

   **Ejemplo con ESXi**:
   - Accede a la sección *Storage* (almacenamiento).
   - Selecciona el almacén de datos donde deseas guardar los archivos.
   - Carga los archivos mediante el botón de *Upload Files*.

---

## **3. Modificar el Archivo `.ovf`**

1. **Abrir el Archivo `.ovf`**:
   - Localiza el archivo `.ovf` en el almacenamiento de datos y descárgalo a tu máquina local.
   - Abre el archivo con tu editor de texto.

2. **Agregar o Modificar la Ruta de la ISO**:
   - Busca la sección `<References>` en el archivo `.ovf`.
   - Elimina una entrada para la ISO.

   **Referencia ISO a eliminar**:
   ```xml
   <References>
       <File ovf:href="your_iso_file.iso" ovf:id="isoFile" />
       <File ovf:href="your_disk.vmdk" ovf:id="diskFile" />
   </References>
