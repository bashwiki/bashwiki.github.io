# [리눅스] Bash inotifywait 사용법

## Overview
El comando `inotifywait` es una herramienta de línea de comandos que forma parte del paquete `inotify-tools` en sistemas Linux. Su propósito principal es monitorizar cambios en el sistema de archivos en tiempo real. Permite a los usuarios observar eventos específicos, como la creación, modificación o eliminación de archivos y directorios, lo que resulta útil para tareas de automatización, scripts de vigilancia y desarrollo de aplicaciones que requieren reactividad ante cambios en el sistema de archivos.

## Usage
La sintaxis básica del comando `inotifywait` es la siguiente:

```bash
inotifywait [opciones] [ruta]
```

### Opciones Comunes:
- `-m` o `--monitor`: Mantiene el comando en ejecución, permitiendo la monitorización continua de los eventos.
- `-r` o `--recursive`: Monitorea directorios de forma recursiva.
- `-e` o `--event`: Especifica el tipo de evento a monitorizar (por ejemplo, `create`, `modify`, `delete`).
- `-q` o `--quiet`: Suprime la salida de eventos no relevantes.
- `--format`: Permite personalizar el formato de salida.

## Examples
### Ejemplo 1: Monitorizar un directorio específico
Para monitorizar un directorio llamado `mi_directorio` y observar eventos de creación y modificación de archivos, puedes usar el siguiente comando:

```bash
inotifywait -m -e create,modify mi_directorio
```

Este comando permanecerá en ejecución y mostrará en la terminal cada vez que se cree o modifique un archivo dentro de `mi_directorio`.

### Ejemplo 2: Monitorizar recursivamente un directorio
Si deseas monitorizar todos los subdirectorios de `mi_directorio`, puedes añadir la opción `-r`:

```bash
inotifywait -m -r -e delete mi_directorio
```

Este comando mostrará en la terminal cada vez que se elimine un archivo o directorio dentro de `mi_directorio` y sus subdirectorios.

## Tips
- **Combina con Scripts**: Puedes utilizar `inotifywait` en scripts de shell para ejecutar automáticamente acciones cuando se detectan cambios en el sistema de archivos. Por ejemplo, puedes hacer que se compile un proyecto cada vez que se modifique un archivo de código fuente.
- **Filtra Eventos**: Utiliza la opción `-e` para filtrar solo los eventos que te interesan, lo que puede ayudar a reducir el ruido en la salida y hacer que sea más fácil de manejar.
- **Uso de `--format`**: Personaliza la salida con `--format` para incluir información adicional como la ruta del archivo afectado o el tipo de evento, lo que puede ser útil para el registro o la depuración.

Con estos conocimientos, podrás utilizar `inotifywait` de manera efectiva para monitorizar cambios en el sistema de archivos y automatizar tareas en tus proyectos de desarrollo.