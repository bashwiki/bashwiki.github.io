# [Linux] Bash source uso equivalente: Ejecutar comandos de un archivo en el entorno actual

## Overview
El comando `source` en Bash se utiliza para ejecutar comandos desde un archivo en el contexto del shell actual. Esto es especialmente útil para cargar configuraciones o funciones definidas en scripts sin iniciar un nuevo proceso de shell.

## Usage
La sintaxis básica del comando `source` es la siguiente:

```bash
source [opciones] [archivo]
```

## Common Options
- `-h`, `--help`: Muestra la ayuda sobre el comando.
- `-V`, `--version`: Muestra la versión del shell.

## Common Examples

### Cargar un archivo de configuración
Para cargar un archivo de configuración, como `.bashrc`, puedes usar:

```bash
source ~/.bashrc
```

### Ejecutar un script
Si tienes un script llamado `script.sh` que contiene varias funciones, puedes ejecutarlo con:

```bash
source script.sh
```

### Actualizar variables de entorno
Si has modificado un archivo que define variables de entorno, puedes actualizar el entorno actual con:

```bash
source variables.sh
```

## Tips
- Asegúrate de que el archivo que estás cargando tenga permisos de lectura.
- Utiliza `source` en lugar de `.` (punto) para mayor claridad, aunque ambos cumplen la misma función.
- Es buena práctica verificar que el archivo existe antes de intentar cargarlo para evitar errores.