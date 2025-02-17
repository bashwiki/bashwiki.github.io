# [Linux] Bash du uso: Muestra el uso del disco de archivos y directorios

## Overview
El comando `du` (disk usage) se utiliza para estimar y mostrar el uso del espacio en disco de archivos y directorios en sistemas operativos tipo Unix. Es una herramienta útil para identificar qué archivos o carpetas están ocupando más espacio en el sistema.

## Usage
La sintaxis básica del comando `du` es la siguiente:

```bash
du [opciones] [argumentos]
```

## Common Options
- `-h`: Muestra el tamaño en un formato legible por humanos (por ejemplo, KB, MB).
- `-s`: Muestra solo el total para cada argumento, sin listar los subdirectorios.
- `-a`: Incluye archivos individuales en la salida, no solo directorios.
- `-c`: Muestra un total acumulado al final de la salida.
- `--max-depth=N`: Limita la profundidad de los subdirectorios que se muestran.

## Common Examples
1. **Mostrar el uso del disco de un directorio específico:**
   ```bash
   du /ruta/al/directorio
   ```

2. **Mostrar el uso del disco en un formato legible por humanos:**
   ```bash
   du -h /ruta/al/directorio
   ```

3. **Mostrar solo el total del uso del disco de un directorio:**
   ```bash
   du -sh /ruta/al/directorio
   ```

4. **Incluir archivos individuales en la salida:**
   ```bash
   du -ah /ruta/al/directorio
   ```

5. **Mostrar el uso del disco con un total acumulado:**
   ```bash
   du -ch /ruta/al/directorio
   ```

6. **Limitar la profundidad de los subdirectorios mostrados:**
   ```bash
   du --max-depth=1 /ruta/al/directorio
   ```

## Tips
- Utiliza la opción `-h` para facilitar la lectura de los tamaños, especialmente en directorios grandes.
- Combina `-s` y `-h` para obtener un resumen rápido del tamaño total de un directorio.
- Si deseas analizar el uso del disco de manera más detallada, considera usar `du -ah` para incluir todos los archivos.
- Recuerda que `du` puede tardar un tiempo en ejecutarse en directorios muy grandes, así que ten paciencia.