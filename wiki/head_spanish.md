# [Linux] Bash head uso: Muestra las primeras líneas de un archivo

## Overview
El comando `head` en Bash se utiliza para mostrar las primeras líneas de uno o más archivos de texto. Es especialmente útil para obtener una vista rápida del contenido de un archivo sin necesidad de abrirlo completamente.

## Usage
La sintaxis básica del comando `head` es la siguiente:

```bash
head [opciones] [argumentos]
```

## Common Options
- `-n [número]`: Especifica el número de líneas que se mostrarán. Por defecto, muestra las primeras 10 líneas.
- `-c [número]`: Muestra el número de bytes especificado en lugar de líneas.
- `-q`: Suprime la salida del encabezado de los archivos cuando se muestran múltiples archivos.
- `-v`: Muestra el encabezado de cada archivo incluso si solo hay un archivo.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `head`:

1. Mostrar las primeras 10 líneas de un archivo:
   ```bash
   head archivo.txt
   ```

2. Mostrar las primeras 5 líneas de un archivo:
   ```bash
   head -n 5 archivo.txt
   ```

3. Mostrar los primeros 20 bytes de un archivo:
   ```bash
   head -c 20 archivo.txt
   ```

4. Mostrar las primeras 10 líneas de múltiples archivos:
   ```bash
   head archivo1.txt archivo2.txt
   ```

5. Mostrar las primeras 10 líneas de un archivo y su encabezado:
   ```bash
   head -v archivo.txt
   ```

## Tips
- Utiliza `head` en combinación con otros comandos, como `grep`, para filtrar resultados. Por ejemplo: `grep "error" archivo.log | head -n 10` muestra los primeros 10 errores encontrados en un archivo de registro.
- Recuerda que puedes cambiar el número de líneas que deseas ver usando la opción `-n`.
- Si necesitas ver las últimas líneas de un archivo, considera usar el comando `tail`, que es complementario a `head`.