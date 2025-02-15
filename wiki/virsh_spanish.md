# [리눅스] Bash virsh 사용법

## Overview
El comando `virsh` es una herramienta de línea de comandos que permite a los usuarios gestionar máquinas virtuales y entornos de virtualización en sistemas que utilizan el hipervisor KVM (Kernel-based Virtual Machine) y otros hipervisores compatibles con libvirt. Su propósito principal es proporcionar una interfaz para crear, pausar, detener, reiniciar, y eliminar máquinas virtuales, así como para gestionar redes y almacenamiento asociados.

## Usage
La sintaxis básica del comando `virsh` es la siguiente:

```
virsh [opciones] [comando] [argumentos]
```

### Comandos Comunes
- `list`: Muestra una lista de las máquinas virtuales activas.
- `start <nombre>`: Inicia una máquina virtual especificada por su nombre.
- `shutdown <nombre>`: Apaga una máquina virtual de manera ordenada.
- `destroy <nombre>`: Detiene una máquina virtual de forma abrupta.
- `create <archivo.xml>`: Crea y arranca una máquina virtual a partir de un archivo de definición XML.

### Opciones Comunes
- `--help`: Muestra la ayuda y la lista de comandos disponibles.
- `--version`: Muestra la versión de `virsh` instalada.

## Examples
### Ejemplo 1: Listar máquinas virtuales activas
Para ver todas las máquinas virtuales que están actualmente en ejecución, puedes usar el siguiente comando:

```bash
virsh list
```

### Ejemplo 2: Iniciar una máquina virtual
Si tienes una máquina virtual llamada "mi_vm", puedes iniciarla con el siguiente comando:

```bash
virsh start mi_vm
```

## Tips
- Asegúrate de tener los permisos adecuados para gestionar las máquinas virtuales; puede que necesites ejecutar `virsh` como superusuario (usando `sudo`).
- Utiliza el comando `virsh --help` para obtener una lista completa de comandos y opciones disponibles.
- Considera crear scripts que utilicen `virsh` para automatizar tareas comunes de gestión de máquinas virtuales.