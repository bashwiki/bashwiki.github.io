# [Linux] Bash virsh Uso: Gestión de máquinas virtuales

## Overview
El comando `virsh` es una herramienta de línea de comandos que permite a los usuarios gestionar máquinas virtuales en entornos que utilizan la tecnología de virtualización de KVM (Kernel-based Virtual Machine) y otros hipervisores compatibles con libvirt. Con `virsh`, puedes crear, pausar, detener y eliminar máquinas virtuales, así como realizar otras tareas de gestión.

## Usage
La sintaxis básica del comando `virsh` es la siguiente:

```bash
virsh [opciones] [argumentos]
```

## Common Options
- `list`: Muestra una lista de las máquinas virtuales activas.
- `start <nombre>`: Inicia una máquina virtual especificada por su nombre.
- `shutdown <nombre>`: Apaga una máquina virtual de forma ordenada.
- `destroy <nombre>`: Fuerza la detención de una máquina virtual.
- `create <archivo.xml>`: Crea y arranca una nueva máquina virtual a partir de un archivo de definición XML.
- `define <archivo.xml>`: Define una nueva máquina virtual sin iniciarla.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `virsh`:

1. **Listar máquinas virtuales activas:**
   ```bash
   virsh list
   ```

2. **Iniciar una máquina virtual llamada "mi_vm":**
   ```bash
   virsh start mi_vm
   ```

3. **Apagar una máquina virtual llamada "mi_vm":**
   ```bash
   virsh shutdown mi_vm
   ```

4. **Forzar la detención de una máquina virtual llamada "mi_vm":**
   ```bash
   virsh destroy mi_vm
   ```

5. **Crear una nueva máquina virtual a partir de un archivo XML:**
   ```bash
   virsh create /ruta/a/mi_vm.xml
   ```

6. **Definir una nueva máquina virtual sin iniciarla:**
   ```bash
   virsh define /ruta/a/mi_vm.xml
   ```

## Tips
- Asegúrate de tener los permisos adecuados para gestionar las máquinas virtuales, ya que algunas operaciones pueden requerir privilegios de superusuario.
- Utiliza `virsh help` para obtener más información sobre los comandos y opciones disponibles.
- Considera crear scripts para automatizar tareas comunes de gestión de máquinas virtuales, lo que puede ahorrar tiempo y reducir errores.