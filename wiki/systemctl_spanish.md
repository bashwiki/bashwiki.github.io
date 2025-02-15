# [리눅스] Bash systemctl 사용법

## Overview
El comando `systemctl` es una herramienta de gestión de servicios y unidades en sistemas que utilizan el sistema de inicialización `systemd`. Su propósito principal es permitir a los administradores y desarrolladores controlar el estado de los servicios, así como gestionar el inicio, parada y configuración de estos. `systemctl` también permite gestionar unidades de otros tipos, como montajes de sistemas de archivos y sockets.

## Usage
La sintaxis básica del comando `systemctl` es la siguiente:

```
systemctl [opciones] [comando] [unidad]
```

### Comandos Comunes
- `start`: Inicia una unidad.
- `stop`: Detiene una unidad.
- `restart`: Reinicia una unidad.
- `status`: Muestra el estado de una unidad.
- `enable`: Habilita una unidad para que se inicie automáticamente al arrancar el sistema.
- `disable`: Deshabilita una unidad para que no se inicie automáticamente.
- `list-units`: Lista las unidades activas.

### Opciones Comunes
- `--now`: Aplica el comando y también afecta a las unidades que están habilitadas o deshabilitadas.
- `--quiet`: Suprime la salida de mensajes innecesarios.

## Examples
### Ejemplo 1: Iniciar un Servicio
Para iniciar el servicio de `nginx`, se puede usar el siguiente comando:

```bash
sudo systemctl start nginx
```

### Ejemplo 2: Ver el Estado de un Servicio
Para verificar el estado del servicio de `nginx`, se puede ejecutar:

```bash
systemctl status nginx
```

Este comando mostrará información sobre el estado actual del servicio, incluyendo si está activo o inactivo.

## Tips
- Siempre usa `sudo` para ejecutar comandos `systemctl` que requieren privilegios de administrador.
- Utiliza `systemctl list-units` para obtener una visión general de todos los servicios y unidades activas en el sistema.
- Para obtener más información sobre una unidad específica, puedes usar `systemctl show [unidad]`, lo que proporciona detalles adicionales sobre la configuración y el estado de la unidad.
- Recuerda que los cambios en la configuración de los servicios pueden requerir un reinicio del servicio o incluso del sistema para que surtan efecto.