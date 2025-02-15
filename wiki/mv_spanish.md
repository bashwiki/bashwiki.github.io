# [리눅스] Bash mv 사용법

## Overview
El comando `mv` en Bash se utiliza para mover archivos y directorios de una ubicación a otra. Además de su función principal de mover, también se puede utilizar para renombrar archivos y directorios. Es una herramienta esencial para la gestión de archivos en sistemas Unix y Linux.

## Usage
La sintaxis básica del comando `mv` es la siguiente:

```bash
mv [opciones] origen destino
```

### Opciones Comunes:
- `-i`: Pregunta antes de sobrescribir un archivo existente.
- `-u`: Mueve solo si el archivo de origen es más nuevo que el archivo de destino o si el archivo de destino no existe.
- `-v`: Muestra el progreso de la operación, indicando qué archivos se están moviendo.
- `-n`: No sobrescribe archivos existentes.

## Examples
### Ejemplo 1: Mover un archivo
Para mover un archivo llamado `documento.txt` a un directorio llamado `documentos`, se puede usar el siguiente comando:

```bash
mv documento.txt documentos/
```

### Ejemplo 2: Renombrar un archivo
Para renombrar un archivo de `viejo_nombre.txt` a `nuevo_nombre.txt`, se utiliza el siguiente comando:

```bash
mv viejo_nombre.txt nuevo_nombre.txt
```

## Tips
- Siempre es recomendable usar la opción `-i` si no estás seguro de sobrescribir archivos existentes, ya que esto te dará una advertencia antes de realizar la acción.
- Utiliza la opción `-v` para tener un registro visual de los archivos que se están moviendo, lo que puede ser útil en operaciones con múltiples archivos.
- Asegúrate de tener los permisos necesarios para mover o renombrar archivos, especialmente cuando trabajas en directorios del sistema o en archivos de otros usuarios.