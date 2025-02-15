# [리눅스] Bash stat 사용법

## Overview
El comando `stat` en Bash se utiliza para mostrar información detallada sobre archivos y sistemas de archivos. Su propósito principal es proporcionar metadatos sobre un archivo, como su tamaño, permisos, propietario, grupo, y las fechas de creación, modificación y acceso. Esta información es útil para los desarrolladores y administradores de sistemas que necesitan gestionar y analizar archivos en un entorno Linux.

## Usage
La sintaxis básica del comando `stat` es la siguiente:

```bash
stat [opciones] [archivo]
```

### Opciones comunes:
- `-c`: Permite especificar un formato de salida personalizado. Por ejemplo, `%s` muestra el tamaño del archivo en bytes.
- `-f`: Muestra información sobre el sistema de archivos en lugar de un archivo específico.
- `--format`: Similar a `-c`, permite definir un formato de salida específico.
- `-L`: Sigue enlaces simbólicos y muestra información sobre el archivo al que apunta el enlace.

## Examples
### Ejemplo 1: Información básica de un archivo
Para obtener información detallada sobre un archivo llamado `ejemplo.txt`, puedes usar el siguiente comando:

```bash
stat ejemplo.txt
```

Este comando mostrará detalles como el tamaño del archivo, permisos, propietario, grupo y las fechas de acceso, modificación y cambio.

### Ejemplo 2: Formato personalizado
Si deseas obtener solo el tamaño del archivo en bytes, puedes utilizar la opción `-c` de la siguiente manera:

```bash
stat -c %s ejemplo.txt
```

Este comando devolverá únicamente el tamaño del archivo `ejemplo.txt`.

## Tips
- Utiliza la opción `-f` si necesitas información sobre el sistema de archivos en lugar de un archivo específico.
- Aprovecha las opciones de formato personalizadas para obtener solo la información que necesitas, lo que puede ser útil en scripts automatizados.
- Recuerda que `stat` puede mostrar información sobre enlaces simbólicos si utilizas la opción `-L`, lo que puede ser útil para la depuración de problemas relacionados con enlaces.