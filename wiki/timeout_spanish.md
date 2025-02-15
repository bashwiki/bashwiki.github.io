# [리눅스] Bash timeout 사용법

## Overview
El comando `timeout` en Bash se utiliza para ejecutar un comando y limitar el tiempo que este puede estar en ejecución. Si el comando no finaliza dentro del tiempo especificado, `timeout` lo termina automáticamente. Esta herramienta es especialmente útil para evitar que procesos se queden colgados o consuman recursos indefinidamente.

## Usage
La sintaxis básica del comando `timeout` es la siguiente:

```bash
timeout [DURACIÓN] [COMANDO] [ARGUMENTOS...]
```

### Opciones Comunes:
- `DURACIÓN`: Especifica el tiempo máximo que el comando puede ejecutarse. Puede ser un número seguido de una unidad de tiempo, como `s` (segundos), `m` (minutos), `h` (horas) o `d` (días). Por ejemplo, `5s` para cinco segundos o `2m` para dos minutos.
- `COMANDO`: El comando que deseas ejecutar.
- `ARGUMENTOS`: Cualquier argumento adicional que necesite el comando.

### Ejemplo de uso:
```bash
timeout 10s sleep 20
```
En este ejemplo, el comando `sleep 20` se ejecuta, pero `timeout` lo detendrá después de 10 segundos.

## Examples
### Ejemplo 1: Ejecutar un comando con límite de tiempo
```bash
timeout 30s ping google.com
```
Este comando intentará hacer ping a google.com durante un máximo de 30 segundos. Si el comando no termina antes de ese tiempo, se interrumpirá.

### Ejemplo 2: Usar con un script
```bash
timeout 1m ./mi_script.sh
```
Aquí, `mi_script.sh` se ejecutará durante un máximo de 1 minuto. Si no finaliza en ese tiempo, `timeout` lo terminará.

## Tips
- **Manejo de señales**: Por defecto, `timeout` envía la señal `SIGTERM` al proceso que termina. Si deseas enviar una señal diferente, puedes usar la opción `-s`. Por ejemplo, `timeout -s KILL 5s comando` enviará `SIGKILL` después de 5 segundos.
- **Comprobación de salida**: Puedes verificar el código de salida del comando después de que `timeout` lo haya terminado. Si el comando fue terminado por `timeout`, el código de salida será 124.
- **Usar en scripts**: `timeout` es muy útil en scripts para asegurarte de que los procesos no se queden colgados, especialmente en entornos de producción.

Con estos conocimientos, podrás utilizar el comando `timeout` de manera efectiva para gestionar la ejecución de tus procesos en Bash.