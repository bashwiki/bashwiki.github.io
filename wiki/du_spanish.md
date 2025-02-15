# [리눅스] Bash du 사용법

## Overview
El comando `du` (disk usage) se utiliza en sistemas operativos basados en Unix para estimar y mostrar el uso del espacio en disco de archivos y directorios. Su propósito principal es ayudar a los usuarios a identificar cuánto espacio en disco están utilizando diferentes archivos y directorios, lo que es útil para la gestión del almacenamiento y la optimización del uso del espacio.

## Usage
La sintaxis básica del comando `du` es la siguiente:

```bash
du [opciones] [archivo o directorio]
```

### Opciones Comunes
- `-h`: Muestra el tamaño en un formato legible por humanos (por ejemplo, KB, MB, GB).
- `-s`: Muestra solo el total para cada argumento, sin listar los tamaños de los subdirectorios.
- `-a`: Muestra el tamaño de todos los archivos, no solo de los directorios.
- `-c`: Muestra un total acumulado al final de la salida.
- `--max-depth=N`: Limita la profundidad de la lista de directorios que se muestra.

## Examples
### Ejemplo 1: Uso básico
Para ver el uso del espacio en disco de todos los archivos y directorios en el directorio actual, se puede usar:

```bash
du -h
```

### Ejemplo 2: Total de un directorio específico
Si deseas ver solo el total del espacio utilizado por un directorio específico, puedes usar la opción `-s`:

```bash
du -sh /ruta/al/directorio
```

Esto mostrará el tamaño total del directorio especificado en un formato legible por humanos.

## Tips
- Utiliza la opción `-c` junto con `-h` para obtener un resumen total del uso del disco de varios directorios de manera más clara.
- Si trabajas con directorios grandes y solo necesitas información sobre un nivel específico de subdirectorios, considera usar `--max-depth=1` para limitar la salida y hacerla más manejable.
- Recuerda que `du` puede tardar un tiempo en ejecutarse si se aplica a directorios muy grandes o con muchos archivos, así que ten paciencia mientras se recopilan los datos.