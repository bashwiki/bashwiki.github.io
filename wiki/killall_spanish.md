# [리눅스] Bash killall 사용법

## Overview
El comando `killall` se utiliza en sistemas Unix y Linux para terminar procesos en ejecución. A diferencia del comando `kill`, que requiere el ID del proceso (PID), `killall` permite finalizar todos los procesos que coinciden con un nombre específico. Esto es útil para gestionar aplicaciones que pueden estar ejecutándose en múltiples instancias.

## Usage
La sintaxis básica del comando `killall` es la siguiente:

```bash
killall [opciones] nombre_del_proceso
```

### Opciones Comunes
- `-u usuario`: Termina solo los procesos que pertenecen al usuario especificado.
- `-9`: Envía una señal SIGKILL para forzar la terminación del proceso, ignorando cualquier limpieza que el proceso pueda necesitar realizar.
- `-v`: Muestra información detallada sobre los procesos que se están terminando.

## Examples
### Ejemplo 1: Terminar un proceso por nombre
Para finalizar todos los procesos de un programa llamado `firefox`, puedes usar el siguiente comando:

```bash
killall firefox
```

### Ejemplo 2: Forzar la terminación de un proceso
Si `firefox` no responde y deseas forzar su cierre, puedes utilizar:

```bash
killall -9 firefox
```

## Tips
- **Precaución**: Utiliza `killall` con cuidado, ya que puede terminar múltiples instancias de un proceso, lo que podría afectar el trabajo de otros usuarios o servicios.
- **Verificación**: Antes de usar `killall`, considera usar el comando `pgrep` para verificar qué procesos se verán afectados. Por ejemplo, `pgrep firefox` mostrará todos los PIDs de los procesos `firefox` en ejecución.
- **Uso de usuario**: Si trabajas en un entorno compartido, es recomendable usar la opción `-u` para evitar terminar procesos de otros usuarios accidentalmente.