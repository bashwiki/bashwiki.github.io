# [리눅스] Bash shutdown 사용법

## Overview
El comando `shutdown` en Bash se utiliza para apagar o reiniciar un sistema Linux de manera controlada. Su propósito principal es permitir a los administradores del sistema realizar un cierre seguro, asegurando que todos los procesos se terminen adecuadamente y que no se pierda información.

## Usage
La sintaxis básica del comando `shutdown` es la siguiente:

```bash
shutdown [opciones] [tiempo] [mensaje]
```

### Opciones Comunes:
- `-h`: Apagar el sistema.
- `-r`: Reiniciar el sistema.
- `now`: Indica que la acción debe llevarse a cabo inmediatamente.
- `+m`: Indica que la acción debe llevarse a cabo después de `m` minutos.
- `hh:mm`: Especifica la hora exacta en formato de 24 horas para realizar el apagado o reinicio.
- `-c`: Cancelar un apagado programado.

## Examples
### Ejemplo 1: Apagar el sistema inmediatamente
Para apagar el sistema de inmediato, se puede usar el siguiente comando:

```bash
shutdown -h now
```

### Ejemplo 2: Reiniciar el sistema en 10 minutos
Si deseas reiniciar el sistema en 10 minutos, puedes ejecutar:

```bash
shutdown -r +10
```

## Tips
- Siempre es recomendable notificar a los usuarios sobre el apagado o reinicio programado utilizando el argumento `mensaje`. Por ejemplo:

```bash
shutdown -h +5 "El sistema se apagará en 5 minutos. Por favor, guarden su trabajo."
```

- Para cancelar un apagado programado, utiliza el comando:

```bash
shutdown -c
```

- Asegúrate de tener los permisos necesarios para ejecutar el comando `shutdown`, ya que generalmente se requiere acceso de superusuario.