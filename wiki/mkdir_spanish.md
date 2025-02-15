# [리눅스] Bash mkdir 사용법

## Overview
El comando `mkdir` (make directory) se utiliza en sistemas operativos basados en Unix, como Linux, para crear nuevos directorios. Su propósito principal es facilitar la organización de archivos y carpetas en el sistema de archivos, permitiendo a los usuarios estructurar sus datos de manera eficiente.

## Usage
La sintaxis básica del comando `mkdir` es la siguiente:

```bash
mkdir [opciones] nombre_del_directorio
```

### Opciones Comunes:
- `-p`: Crea directorios padres según sea necesario. Si los directorios intermedios no existen, `mkdir` los creará automáticamente.
- `-v`: Muestra un mensaje de confirmación por cada directorio creado.
- `-m`: Permite establecer permisos específicos para el nuevo directorio utilizando una notación octal.

## Examples
### Ejemplo 1: Crear un solo directorio
Para crear un directorio llamado "proyecto":

```bash
mkdir proyecto
```

### Ejemplo 2: Crear directorios anidados
Para crear un directorio "proyecto" con un subdirectorio "src" y otro "bin", utilizando la opción `-p`:

```bash
mkdir -p proyecto/src proyecto/bin
```

## Tips
- Utiliza la opción `-v` para obtener un feedback visual sobre los directorios que se están creando, lo que puede ser útil en scripts o para verificar la creación de múltiples directorios.
- Al usar la opción `-p`, asegúrate de que la ruta que estás creando sea la deseada, ya que puede crear múltiples directorios si no existen, lo que podría no ser lo que esperabas.
- Considera establecer permisos adecuados al crear directorios, especialmente si otros usuarios tendrán acceso a ellos, utilizando la opción `-m` para definir permisos específicos desde el inicio.