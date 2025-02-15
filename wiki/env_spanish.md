# [리눅스] Bash env 사용법

## Overview
El comando `env` en Bash se utiliza para mostrar o modificar el entorno de ejecución de un programa. Su propósito principal es permitir a los usuarios ver las variables de entorno actuales y ejecutar un comando en un entorno modificado. Esto es especialmente útil para probar diferentes configuraciones de entorno sin necesidad de cambiar permanentemente la configuración del sistema.

## Usage
La sintaxis básica del comando `env` es la siguiente:

```
env [opciones] [VARIABLE=valor] [comando]
```

### Opciones Comunes:
- `-i`: Inicia un entorno vacío, eliminando todas las variables de entorno existentes.
- `-u VARIABLE`: Elimina la variable de entorno especificada antes de ejecutar el comando.
- `-0`: Termina la salida con un carácter nulo en lugar de una nueva línea (útil para manejar nombres de archivos con espacios).

## Examples
### Ejemplo 1: Mostrar variables de entorno
Para ver todas las variables de entorno actuales, simplemente ejecuta:

```bash
env
```

Este comando listará todas las variables de entorno y sus valores en la terminal.

### Ejemplo 2: Ejecutar un comando con un entorno modificado
Si deseas ejecutar un comando con una variable de entorno específica, puedes hacerlo de la siguiente manera:

```bash
env MY_VAR=valor_comando my_command
```

En este caso, `MY_VAR` se establecerá en `valor_comando` solo para la ejecución de `my_command`.

## Tips
- Utiliza `env -i` para ejecutar un comando en un entorno completamente limpio, lo que puede ser útil para depurar problemas relacionados con variables de entorno no deseadas.
- Recuerda que las variables de entorno establecidas con `env` solo están disponibles para el comando que se ejecuta y no afectan al entorno global.
- Puedes combinar múltiples variables de entorno en una sola línea antes de ejecutar un comando, lo que te permite personalizar el entorno de ejecución de manera eficiente.