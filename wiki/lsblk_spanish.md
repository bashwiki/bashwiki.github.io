# [Linux] Bash lsblk Uso: Listar dispositivos de bloques

## Overview
El comando `lsblk` se utiliza para listar todos los dispositivos de bloques disponibles en el sistema, como discos duros, particiones y dispositivos de almacenamiento extraíbles. Proporciona información sobre la estructura de los dispositivos, incluyendo su tamaño, tipo y punto de montaje.

## Usage
La sintaxis básica del comando `lsblk` es la siguiente:

```bash
lsblk [opciones] [argumentos]
```

## Common Options
- `-a`, `--all`: Muestra todos los dispositivos, incluidos los que no tienen un punto de montaje.
- `-f`, `--fs`: Muestra información sobre el sistema de archivos de los dispositivos.
- `-l`, `--list`: Muestra la salida en formato de lista en lugar de árbol.
- `-o`, `--output`: Especifica las columnas que se deben mostrar en la salida.
- `-p`, `--paths`: Muestra las rutas completas de los dispositivos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `lsblk`:

1. **Listar todos los dispositivos de bloques:**
   ```bash
   lsblk
   ```

2. **Listar todos los dispositivos, incluidos los que no están montados:**
   ```bash
   lsblk -a
   ```

3. **Mostrar información del sistema de archivos:**
   ```bash
   lsblk -f
   ```

4. **Mostrar la salida en formato de lista:**
   ```bash
   lsblk -l
   ```

5. **Especificar columnas para mostrar:**
   ```bash
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

## Tips
- Utiliza `lsblk -f` para obtener información sobre el sistema de archivos, lo que puede ser útil para identificar el tipo de partición.
- Combina `lsblk` con otros comandos como `grep` para filtrar resultados específicos.
- Recuerda que `lsblk` no requiere privilegios de superusuario para mostrar la mayoría de la información, lo que lo hace accesible para todos los usuarios.