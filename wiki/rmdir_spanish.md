# [리눅스] Bash rmdir 사용법

## Overview
El comando `rmdir` se utiliza en Bash para eliminar directorios vacíos. Su propósito principal es permitir a los usuarios gestionar la estructura de directorios en un sistema de archivos, eliminando aquellos directorios que no contienen archivos ni otros directorios. Es importante notar que `rmdir` solo puede eliminar directorios que estén completamente vacíos; si un directorio contiene archivos o subdirectorios, el comando fallará.

## Usage
La sintaxis básica del comando `rmdir` es la siguiente:

```bash
rmdir [opciones] directorio
```

### Opciones Comunes
- `-p`: Elimina el directorio especificado y sus directorios padres si están vacíos.
- `--ignore-fail-on-non-empty`: Ignora el error si el directorio no está vacío.

## Examples
### Ejemplo 1: Eliminar un directorio vacío
Para eliminar un directorio vacío llamado `mi_directorio`, puedes usar el siguiente comando:

```bash
rmdir mi_directorio
```

Si `mi_directorio` está vacío, se eliminará sin problemas. Si no lo está, recibirás un mensaje de error.

### Ejemplo 2: Eliminar un directorio y sus padres vacíos
Si deseas eliminar un directorio llamado `subdirectorio` y también su directorio padre `mi_directorio` (si ambos están vacíos), puedes usar la opción `-p` de la siguiente manera:

```bash
rmdir -p mi_directorio/subdirectorio
```

Este comando eliminará `subdirectorio` y, si `mi_directorio` queda vacío después de esa operación, también lo eliminará.

## Tips
- Asegúrate de que el directorio que deseas eliminar esté completamente vacío antes de usar `rmdir`, ya que de lo contrario el comando fallará.
- Utiliza `ls` para verificar el contenido de un directorio antes de intentar eliminarlo.
- Si necesitas eliminar un directorio que contiene archivos o subdirectorios, considera usar el comando `rm -r` en su lugar, pero ten cuidado, ya que este comando eliminará todo el contenido de manera recursiva.