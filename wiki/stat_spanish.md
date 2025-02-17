# [Linux] Bash stat uso equivalente: Muestra información sobre archivos y sistemas de archivos

## Overview
El comando `stat` en Bash se utiliza para mostrar información detallada sobre archivos y sistemas de archivos. Proporciona datos como el tamaño del archivo, las fechas de acceso y modificación, y los permisos de archivo.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
stat [opciones] [argumentos]
```

## Common Options
- `-c, --format=FORMATO`: Permite especificar un formato de salida personalizado.
- `-f, --file-system`: Muestra información sobre el sistema de archivos en lugar del archivo.
- `--help`: Muestra la ayuda sobre el uso del comando.
- `--version`: Muestra la versión del comando `stat`.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `stat`:

1. **Mostrar información básica de un archivo:**
   ```bash
   stat archivo.txt
   ```

2. **Mostrar información de un directorio:**
   ```bash
   stat /ruta/al/directorio
   ```

3. **Usar un formato personalizado para mostrar solo el tamaño y la fecha de modificación:**
   ```bash
   stat -c "Tamaño: %s bytes, Modificado: %y" archivo.txt
   ```

4. **Mostrar información del sistema de archivos:**
   ```bash
   stat -f /
   ```

## Tips
- Utiliza la opción `-c` para personalizar la salida y hacerla más legible según tus necesidades.
- Si necesitas información sobre varios archivos, puedes listar múltiples archivos en el mismo comando.
- Recuerda que `stat` puede ser útil para scripts donde necesitas verificar propiedades de archivos antes de realizar operaciones.