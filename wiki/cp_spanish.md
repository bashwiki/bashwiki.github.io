# [Linux] Bash cp Uso: Copiar archivos y directorios

## Overview
El comando `cp` se utiliza en Bash para copiar archivos y directorios de una ubicación a otra. Permite duplicar contenido de manera rápida y eficiente, lo que es fundamental en la gestión de archivos en sistemas operativos basados en Unix.

## Usage
La sintaxis básica del comando `cp` es la siguiente:

```bash
cp [opciones] [origen] [destino]
```

## Common Options
- `-r`: Copia directorios de manera recursiva.
- `-i`: Pregunta antes de sobrescribir archivos existentes.
- `-u`: Copia solo si el archivo de origen es más reciente que el archivo de destino o si el archivo de destino no existe.
- `-v`: Muestra los archivos que se están copiando (modo verbose).
- `-a`: Copia archivos y directorios de manera recursiva, preservando atributos como permisos y timestamps.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `cp`:

1. **Copiar un archivo a otro directorio**:
   ```bash
   cp archivo.txt /ruta/al/destino/
   ```

2. **Copiar un directorio de manera recursiva**:
   ```bash
   cp -r /ruta/al/directorio/ /ruta/al/destino/
   ```

3. **Copiar un archivo y preguntar antes de sobrescribir**:
   ```bash
   cp -i archivo.txt /ruta/al/destino/
   ```

4. **Copiar solo archivos más recientes**:
   ```bash
   cp -u archivo.txt /ruta/al/destino/
   ```

5. **Copiar con detalles de progreso**:
   ```bash
   cp -v archivo.txt /ruta/al/destino/
   ```

## Tips
- Siempre verifica la ruta de destino para evitar sobrescribir archivos importantes.
- Utiliza la opción `-i` si no estás seguro de si un archivo será sobrescrito.
- Para copias de seguridad, considera usar la opción `-a` para preservar atributos de archivos.
- Si trabajas con muchos archivos, el uso de `-v` puede ayudarte a seguir el progreso de la copia.