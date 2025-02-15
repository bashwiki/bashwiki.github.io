# [리눅스] Bash realpath 사용법

## Overview
El comando `realpath` en Bash se utiliza para resolver y mostrar la ruta absoluta de un archivo o directorio. Su propósito principal es convertir rutas relativas o simbólicas en rutas absolutas, lo que facilita la referencia a archivos en scripts y comandos, asegurando que se esté trabajando con la ubicación correcta en el sistema de archivos.

## Usage
La sintaxis básica del comando `realpath` es la siguiente:

```bash
realpath [opciones] <ruta>
```

### Opciones comunes:
- `-m`, `--canonicalize-missing`: Esta opción permite que `realpath` devuelva una ruta canónica incluso si el archivo o directorio no existe.
- `-q`, `--quiet`: Suprime la salida de errores, útil cuando se desea evitar mensajes de error en la salida estándar.
- `-s`, `--strip`: Elimina el prefijo de la ruta canónica, lo que puede ser útil en ciertos contextos.

## Examples
### Ejemplo 1: Obtener la ruta absoluta de un archivo
Supongamos que tienes un archivo llamado `documento.txt` en un directorio llamado `proyectos`. Puedes usar `realpath` para obtener la ruta absoluta de este archivo:

```bash
cd proyectos
realpath documento.txt
```
Salida esperada:
```
/home/usuario/proyectos/documento.txt
```

### Ejemplo 2: Resolver una ruta simbólica
Si tienes un enlace simbólico llamado `enlace_a_documento` que apunta a `documento.txt`, puedes usar `realpath` para obtener la ruta real:

```bash
realpath enlace_a_documento
```
Salida esperada:
```
/home/usuario/proyectos/documento.txt
```

## Tips
- Siempre es recomendable usar `realpath` en scripts para asegurarte de que estás trabajando con rutas absolutas, lo que puede evitar errores relacionados con rutas relativas.
- Si trabajas en un entorno donde los archivos pueden ser movidos o eliminados, considera usar la opción `-m` para manejar situaciones en las que los archivos no existen, evitando así que tu script falle.
- Combina `realpath` con otros comandos como `cd` o `ln` para gestionar mejor las rutas en tus scripts de Bash.