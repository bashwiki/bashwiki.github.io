# [Linux] Bash blkid Uso: Identificar dispositivos de almacenamiento

## Overview
El comando `blkid` se utiliza en sistemas Linux para identificar y mostrar información sobre los dispositivos de almacenamiento conectados, como discos duros, particiones y unidades USB. Proporciona detalles como el tipo de sistema de archivos, el UUID (Identificador Único Universal) y la etiqueta del dispositivo.

## Usage
La sintaxis básica del comando `blkid` es la siguiente:

```bash
blkid [options] [arguments]
```

## Common Options
- `-o, --output`: Especifica el formato de salida (por ejemplo, `value`, `full`, `list`).
- `-s, --match-tag`: Filtra la salida para mostrar solo las etiquetas especificadas.
- `-p, --probe`: Fuerza la detección de sistemas de archivos en dispositivos que no están montados.
- `-c, --cache`: Utiliza un archivo de caché para acelerar la búsqueda de dispositivos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `blkid`:

1. **Listar todos los dispositivos de almacenamiento:**
   ```bash
   blkid
   ```

2. **Mostrar información detallada de un dispositivo específico:**
   ```bash
   blkid /dev/sda1
   ```

3. **Filtrar la salida para mostrar solo el UUID:**
   ```bash
   blkid -o value -s UUID /dev/sda1
   ```

4. **Usar el formato de salida de lista:**
   ```bash
   blkid -o list
   ```

5. **Forzar la detección de sistemas de archivos:**
   ```bash
   blkid -p /dev/sdb
   ```

## Tips
- Asegúrate de ejecutar `blkid` con privilegios de superusuario (usando `sudo`) si no obtienes información completa sobre los dispositivos.
- Utiliza la opción `-o value` para obtener una salida más limpia y fácil de procesar en scripts.
- Revisa el archivo de caché de `blkid` en `/etc/blkid.tab` para ver información almacenada sobre dispositivos previamente detectados.