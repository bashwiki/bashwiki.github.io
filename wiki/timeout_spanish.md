# [Linux] Bash timeout uso: Establecer un límite de tiempo para comandos

## Overview
El comando `timeout` en Bash se utiliza para ejecutar un comando y finalizarlo si no ha terminado dentro de un tiempo especificado. Esto es útil para evitar que procesos se queden colgados indefinidamente.

## Usage
La sintaxis básica del comando `timeout` es la siguiente:

```bash
timeout [opciones] duración comando [argumentos]
```

## Common Options
- `-k, --kill-after=DURACION`: Especifica un tiempo adicional después del cual se enviará una señal de terminación al proceso si aún está en ejecución.
- `--preserve-status`: Mantiene el código de salida del comando original en lugar de devolver el código de salida de `timeout`.
- `-s, --signal=SEÑAL`: Especifica la señal que se enviará al proceso al finalizar. Por defecto, se envía la señal `TERM`.

## Common Examples

1. **Ejecutar un comando con un límite de tiempo de 5 segundos:**

   ```bash
   timeout 5s sleep 10
   ```

   En este ejemplo, el comando `sleep 10` se finalizará después de 5 segundos.

2. **Usar `timeout` con una señal específica:**

   ```bash
   timeout -s SIGKILL 5s sleep 10
   ```

   Aquí, el comando `sleep 10` se finalizará con la señal `SIGKILL` después de 5 segundos.

3. **Preservar el estado de salida del comando:**

   ```bash
   timeout --preserve-status 5s false
   echo $?
   ```

   En este caso, el comando `false` se ejecuta y se finaliza después de 5 segundos, pero el código de salida de `false` se preserva.

4. **Finalizar un proceso después de un tiempo y enviar una señal de terminación adicional:**

   ```bash
   timeout -k 3s 5s sleep 10
   ```

   Este comando finalizará `sleep 10` después de 5 segundos y, si el proceso sigue en ejecución, enviará una señal de terminación 3 segundos después.

## Tips
- Siempre verifica el tiempo que necesitas para cada comando, ya que un tiempo demasiado corto puede interrumpir procesos importantes.
- Utiliza la opción `--preserve-status` si necesitas el código de salida del comando original para el manejo de errores.
- Considera el uso de señales personalizadas si necesitas un control más fino sobre cómo se finalizan los procesos.