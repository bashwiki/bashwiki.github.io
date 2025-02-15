# [리눅스] Bash chmod 사용법

## Overview
El comando `chmod` (change mode) en Bash se utiliza para cambiar los permisos de acceso a archivos y directorios en sistemas operativos tipo Unix. Su propósito principal es controlar quién puede leer, escribir o ejecutar un archivo, permitiendo así una gestión de la seguridad y el acceso a los recursos del sistema.

## Usage
La sintaxis básica del comando `chmod` es la siguiente:

```
chmod [opciones] modo archivo
```

### Opciones Comunes
- `-R`: Aplica los cambios de manera recursiva a todos los archivos y subdirectorios dentro del directorio especificado.
- `-v`: Muestra un mensaje detallado de los cambios realizados.
- `-c`: Muestra solo los archivos cuyos permisos han cambiado.

### Modo
El modo puede especificarse de dos maneras:
1. **Notación simbólica**: Utiliza letras para representar los permisos. Por ejemplo:
   - `u`: propietario (user)
   - `g`: grupo (group)
   - `o`: otros (others)
   - `r`: permiso de lectura (read)
   - `w`: permiso de escritura (write)
   - `x`: permiso de ejecución (execute)

   Ejemplo de uso: `chmod u+x archivo.txt` (agrega permiso de ejecución al propietario).

2. **Notación octal**: Utiliza números para representar los permisos. Cada permiso se representa con un número:
   - `4`: lectura (r)
   - `2`: escritura (w)
   - `1`: ejecución (x)

   Los permisos se suman para obtener el número octal. Por ejemplo, `chmod 755 archivo.txt` (permite lectura, escritura y ejecución al propietario, y lectura y ejecución al grupo y otros).

## Examples
### Ejemplo 1: Cambiar permisos de un archivo
Para agregar permiso de escritura al grupo en un archivo llamado `documento.txt`, puedes usar:

```bash
chmod g+w documento.txt
```

### Ejemplo 2: Cambiar permisos de un directorio de manera recursiva
Para dar permisos de lectura, escritura y ejecución al propietario y solo lectura y ejecución al grupo y otros en un directorio llamado `proyecto`, puedes usar:

```bash
chmod -R 755 proyecto
```

## Tips
- Siempre verifica los permisos actuales de un archivo o directorio usando `ls -l` antes de realizar cambios con `chmod`.
- Utiliza la opción `-v` para ver qué cambios se han realizado, especialmente cuando aplicas cambios recursivos.
- Ten cuidado al otorgar permisos de escritura y ejecución, ya que pueden comprometer la seguridad del sistema si se aplican incorrectamente.