# [리눅스] Bash nohup 사용법

## Overview
El comando `nohup` (no hang up) se utiliza en sistemas Unix y Linux para ejecutar un comando o un script de manera que no se detenga incluso si la sesión de terminal se cierra. Esto es especialmente útil para ejecutar procesos de larga duración que no deben ser interrumpidos por la desconexión del usuario. Al usar `nohup`, la salida estándar y la salida de error del comando se redirigen automáticamente a un archivo llamado `nohup.out`, a menos que se especifique lo contrario.

## Usage
La sintaxis básica del comando `nohup` es la siguiente:

```bash
nohup [opciones] comando [argumentos]
```

### Opciones Comunes
- `&`: Ejecuta el comando en segundo plano.
- `-h`: Muestra la ayuda sobre el uso del comando.
- `-p`: Permite especificar un archivo de salida diferente en lugar de `nohup.out`.

## Examples
### Ejemplo 1: Ejecutar un script en segundo plano
Supongamos que tienes un script llamado `mi_script.sh` que deseas ejecutar sin que se interrumpa al cerrar la terminal. Puedes usar el siguiente comando:

```bash
nohup bash mi_script.sh &
```

Este comando ejecutará `mi_script.sh` en segundo plano y redirigirá la salida a `nohup.out`.

### Ejemplo 2: Ejecutar un comando y redirigir la salida
Si deseas ejecutar un comando y redirigir la salida a un archivo específico, puedes hacerlo así:

```bash
nohup python mi_programa.py > salida.log 2>&1 &
```

En este caso, la salida estándar y la salida de error se redirigen al archivo `salida.log`.

## Tips
- Siempre verifica el archivo `nohup.out` o el archivo de salida que hayas especificado para asegurarte de que el comando se esté ejecutando correctamente y para revisar cualquier mensaje de error.
- Es recomendable usar `&` al final del comando para liberar la terminal y permitir que el proceso siga ejecutándose en segundo plano.
- Si planeas ejecutar múltiples instancias de un mismo comando, considera redirigir cada salida a un archivo diferente para evitar confusiones.
- Utiliza el comando `jobs` para ver los procesos en segundo plano y `fg` para traer uno de ellos de vuelta al primer plano si es necesario.