# [리눅스] Bash lsblk 사용법

## Overview
El comando `lsblk` se utiliza en sistemas Linux para listar todos los dispositivos de bloques disponibles en el sistema. Esto incluye discos duros, particiones, y dispositivos de almacenamiento extraíbles. Su propósito principal es proporcionar una visión clara de la estructura de almacenamiento, mostrando cómo están organizados los dispositivos y sus particiones, así como su tamaño y tipo.

## Usage
La sintaxis básica del comando `lsblk` es la siguiente:

```bash
lsblk [opciones]
```

Algunas de las opciones más comunes que se pueden utilizar con `lsblk` son:

- `-a`, `--all`: Muestra todos los dispositivos, incluidos los que no están montados.
- `-f`, `--fs`: Muestra información sobre el sistema de archivos, como el tipo de sistema de archivos y la etiqueta.
- `-l`, `--list`: Muestra la salida en formato de lista en lugar de árbol.
- `-o`, `--output`: Permite especificar qué columnas mostrar en la salida.
- `-n`, `--noheadings`: Suprime los encabezados de columna en la salida.

## Examples
Aquí hay un par de ejemplos prácticos de cómo usar `lsblk`:

1. **Listar todos los dispositivos de bloques**:

```bash
lsblk
```
Este comando mostrará una lista de todos los dispositivos de bloques conectados, junto con sus particiones y tamaños.

2. **Mostrar información del sistema de archivos**:

```bash
lsblk -f
```
Este comando proporcionará información adicional sobre los sistemas de archivos de los dispositivos, incluyendo el tipo de sistema de archivos y las etiquetas.

## Tips
- Utiliza la opción `-o` para personalizar la salida y mostrar solo la información que necesitas. Por ejemplo, `lsblk -o NAME,SIZE,TYPE` mostrará solo el nombre, tamaño y tipo de cada dispositivo.
- Combina `lsblk` con otros comandos como `grep` para filtrar resultados específicos. Por ejemplo, `lsblk | grep sda` para buscar información sobre el dispositivo `sda`.
- Recuerda que `lsblk` no requiere privilegios de superusuario para ejecutarse, lo que lo hace accesible para todos los usuarios en el sistema.