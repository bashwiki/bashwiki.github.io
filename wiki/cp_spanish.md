# [리눅스] Bash cp 사용법

## Overview
El comando `cp` en Bash se utiliza para copiar archivos y directorios. Su propósito principal es permitir a los usuarios duplicar contenido de un lugar a otro en el sistema de archivos, facilitando la gestión y organización de datos.

## Usage
La sintaxis básica del comando `cp` es la siguiente:

```
cp [opciones] origen destino
```

Donde:
- `origen`: Especifica el archivo o directorio que se desea copiar.
- `destino`: Especifica la ubicación donde se desea copiar el archivo o directorio.

### Opciones Comunes
- `-r`: Copia directorios de manera recursiva. Necesario al copiar directorios.
- `-i`: Solicita confirmación antes de sobrescribir archivos existentes.
- `-u`: Copia solo si el archivo de origen es más reciente que el archivo de destino o si el archivo de destino no existe.
- `-v`: Muestra el progreso de la copia, indicando qué archivos se están copiando.

## Examples
### Ejemplo 1: Copiar un archivo
Para copiar un archivo llamado `documento.txt` a un nuevo archivo llamado `copia_documento.txt`, se puede usar el siguiente comando:

```bash
cp documento.txt copia_documento.txt
```

### Ejemplo 2: Copiar un directorio
Para copiar un directorio llamado `proyecto` y todo su contenido a un nuevo directorio llamado `copia_proyecto`, se utilizaría el siguiente comando:

```bash
cp -r proyecto copia_proyecto
```

## Tips
- Siempre es recomendable usar la opción `-i` para evitar sobrescribir archivos accidentalmente.
- Al copiar directorios, asegúrate de usar la opción `-r` para que la copia se realice de manera recursiva.
- Utiliza la opción `-v` para tener un feedback visual sobre el proceso de copia, especialmente útil cuando se copian múltiples archivos o directorios.