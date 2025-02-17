# [Linux] Bash killall Uso: Terminar procesos por nombre

El comando `killall` se utiliza para terminar procesos en ejecución basados en su nombre.

## Overview
El comando `killall` permite enviar señales a todos los procesos que coinciden con un nombre específico. Es útil para gestionar y finalizar aplicaciones que no responden o que se están ejecutando en segundo plano.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
killall [opciones] [nombre_del_proceso]
```

## Common Options
- `-u, --user`: Especifica el usuario cuyos procesos se desean terminar.
- `-i, --interactive`: Pide confirmación antes de terminar cada proceso.
- `-q, --quiet`: No muestra mensajes de error si no se encuentran procesos.
- `-s, --signal`: Especifica la señal a enviar (por defecto es SIGTERM).

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `killall`:

1. Terminar todos los procesos de Firefox:
   ```bash
   killall firefox
   ```

2. Terminar todos los procesos de un usuario específico:
   ```bash
   killall -u nombre_usuario
   ```

3. Terminar un proceso y pedir confirmación antes de cada uno:
   ```bash
   killall -i nombre_del_proceso
   ```

4. Enviar una señal diferente (por ejemplo, SIGKILL) a un proceso:
   ```bash
   killall -s SIGKILL nombre_del_proceso
   ```

## Tips
- Asegúrate de tener los permisos necesarios para terminar procesos de otros usuarios.
- Usa la opción `-q` si deseas evitar mensajes de error innecesarios.
- Ten cuidado al usar `killall`, ya que puede terminar múltiples instancias de un proceso si no se especifica correctamente el nombre.