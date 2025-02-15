# [리눅스] Bash cd 사용법

## Overview
El comando `cd` (change directory) se utiliza en Bash para cambiar el directorio de trabajo actual en el sistema de archivos. Su propósito principal es permitir a los usuarios navegar entre diferentes carpetas y directorios en la línea de comandos, facilitando así la gestión de archivos y la ejecución de comandos en ubicaciones específicas.

## Usage
La sintaxis básica del comando `cd` es la siguiente:

```bash
cd [opciones] [directorio]
```

### Opciones Comunes
- `..`: Cambia al directorio padre del directorio actual.
- `-`: Cambia al directorio anterior en el que se encontraba el usuario.
- `~`: Cambia al directorio home del usuario actual.

## Examples
### Ejemplo 1: Cambiar al directorio padre
Para cambiar al directorio padre del directorio actual, puedes usar:

```bash
cd ..
```

### Ejemplo 2: Cambiar al directorio home
Para regresar al directorio home del usuario actual, simplemente utiliza:

```bash
cd ~
```

### Ejemplo 3: Cambiar al directorio anterior
Si deseas volver al directorio en el que estabas anteriormente, puedes usar:

```bash
cd -
```

## Tips
- Utiliza `cd` sin argumentos para regresar directamente al directorio home.
- Puedes usar la tecla `Tab` para autocompletar nombres de directorios, lo que puede ahorrar tiempo y evitar errores tipográficos.
- Recuerda que los nombres de directorios son sensibles a mayúsculas y minúsculas en sistemas basados en Unix, así que asegúrate de escribirlos correctamente.
- Para ver el directorio actual en el que te encuentras, puedes usar el comando `pwd` (print working directory) después de cambiar de directorio.