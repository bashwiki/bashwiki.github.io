# [Linux] Bash rm Uso: Eliminar archivos y directorios

## Overview
El comando `rm` se utiliza en sistemas Unix y Linux para eliminar archivos y directorios. Es una herramienta poderosa que permite a los usuarios gestionar su sistema de archivos eliminando elementos no deseados.

## Usage
La sintaxis básica del comando `rm` es la siguiente:

```
rm [opciones] [argumentos]
```

## Common Options
- `-f`: Fuerza la eliminación sin pedir confirmación.
- `-i`: Solicita confirmación antes de eliminar cada archivo.
- `-r`: Elimina directorios y su contenido de manera recursiva.
- `-v`: Muestra información detallada sobre los archivos que se están eliminando.

## Common Examples
1. **Eliminar un archivo específico:**
   ```bash
   rm archivo.txt
   ```

2. **Eliminar varios archivos:**
   ```bash
   rm archivo1.txt archivo2.txt archivo3.txt
   ```

3. **Eliminar un directorio y su contenido de manera recursiva:**
   ```bash
   rm -r directorio/
   ```

4. **Eliminar un archivo sin pedir confirmación:**
   ```bash
   rm -f archivo.txt
   ```

5. **Eliminar archivos con confirmación:**
   ```bash
   rm -i archivo.txt
   ```

## Tips
- Siempre verifica el nombre del archivo o directorio que deseas eliminar para evitar pérdidas accidentales de datos.
- Utiliza la opción `-i` si no estás seguro de querer eliminar un archivo, ya que esto te dará una segunda oportunidad para confirmar la acción.
- Considera hacer una copia de seguridad de archivos importantes antes de eliminarlos, especialmente si usas la opción `-f`.