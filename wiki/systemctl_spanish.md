# [Linux] Bash systemctl uso: Controlar servicios y unidades del sistema

## Overview
El comando `systemctl` es una herramienta de gestión de servicios y unidades en sistemas que utilizan el sistema de inicio systemd. Permite a los usuarios iniciar, detener, reiniciar y verificar el estado de los servicios del sistema, así como gestionar otras unidades como montajes y sockets.

## Usage
La sintaxis básica del comando `systemctl` es la siguiente:

```bash
systemctl [opciones] [argumentos]
```

## Common Options
- `start`: Inicia una unidad o servicio.
- `stop`: Detiene una unidad o servicio en ejecución.
- `restart`: Reinicia una unidad o servicio.
- `status`: Muestra el estado de una unidad o servicio.
- `enable`: Habilita una unidad para que se inicie automáticamente al arrancar el sistema.
- `disable`: Deshabilita una unidad para que no se inicie automáticamente.
- `list-units`: Lista todas las unidades activas.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `systemctl`:

- Para iniciar un servicio, por ejemplo, el servidor web Apache:
  ```bash
  systemctl start apache2
  ```

- Para detener el mismo servicio:
  ```bash
  systemctl stop apache2
  ```

- Para reiniciar el servicio:
  ```bash
  systemctl restart apache2
  ```

- Para verificar el estado del servicio:
  ```bash
  systemctl status apache2
  ```

- Para habilitar el servicio para que se inicie automáticamente al arrancar:
  ```bash
  systemctl enable apache2
  ```

- Para deshabilitar el servicio:
  ```bash
  systemctl disable apache2
  ```

- Para listar todas las unidades activas:
  ```bash
  systemctl list-units
  ```

## Tips
- Siempre verifica el estado de un servicio después de iniciarlo o detenerlo para asegurarte de que se ha ejecutado correctamente.
- Utiliza `systemctl list-units --type=service` para filtrar y ver solo los servicios.
- Recuerda que algunas operaciones pueden requerir privilegios de superusuario, así que puede ser necesario anteponer `sudo` al comando.