# [Linux] Bash journalctl uso: Visualizar registros del sistema

## Overview
El comando `journalctl` se utiliza para acceder y mostrar los registros del sistema que son gestionados por el sistema de registro `systemd`. Permite a los usuarios ver mensajes de log de diferentes servicios y del propio sistema, facilitando la depuración y el monitoreo del estado del sistema.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
journalctl [opciones] [argumentos]
```

## Common Options
- `-b`: Muestra los registros desde el último arranque.
- `-f`: Sigue los registros en tiempo real, similar a `tail -f`.
- `--since "fecha"`: Muestra registros desde una fecha específica.
- `--until "fecha"`: Muestra registros hasta una fecha específica.
- `-u nombre_servicio`: Filtra los registros para un servicio específico.

## Common Examples
- Mostrar todos los registros desde el último arranque:

```bash
journalctl -b
```

- Seguir los registros en tiempo real:

```bash
journalctl -f
```

- Mostrar registros desde una fecha específica:

```bash
journalctl --since "2023-10-01"
```

- Mostrar registros hasta una fecha específica:

```bash
journalctl --until "2023-10-10"
```

- Filtrar registros para un servicio específico, por ejemplo, `ssh.service`:

```bash
journalctl -u ssh.service
```

## Tips
- Utiliza `-n` seguido de un número para limitar la cantidad de registros mostrados, por ejemplo, `journalctl -n 100` para ver los últimos 100 registros.
- Combina opciones para obtener resultados más específicos, como `journalctl -b -u nombre_servicio`.
- Recuerda que puedes usar `man journalctl` para acceder a la página de manual y explorar más opciones y detalles sobre el comando.