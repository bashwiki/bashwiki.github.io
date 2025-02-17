# [Linux] Bash tail uso: Muestra las últimas líneas de un archivo

## Overview
El comando `tail` se utiliza en Bash para mostrar las últimas líneas de un archivo de texto. Es especialmente útil para monitorear archivos de registro en tiempo real o para ver la parte final de archivos grandes sin necesidad de abrirlos completamente.

## Usage
La sintaxis básica del comando `tail` es la siguiente:

```bash
tail [opciones] [archivo]
```

## Common Options
- `-n [número]`: Muestra las últimas `n` líneas del archivo. Por defecto, muestra 10 líneas.
- `-f`: Sigue el archivo en tiempo real, mostrando nuevas líneas a medida que se añaden.
- `-c [número]`: Muestra los últimos `n` bytes del archivo.
- `--help`: Muestra la ayuda sobre el comando y sus opciones.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `tail`:

1. **Mostrar las últimas 10 líneas de un archivo:**
   ```bash
   tail archivo.txt
   ```

2. **Mostrar las últimas 20 líneas de un archivo:**
   ```bash
   tail -n 20 archivo.txt
   ```

3. **Seguir un archivo de registro en tiempo real:**
   ```bash
   tail -f /var/log/syslog
   ```

4. **Mostrar los últimos 100 bytes de un archivo:**
   ```bash
   tail -c 100 archivo.txt
   ```

5. **Combinar opciones para seguir un archivo y mostrar más líneas:**
   ```bash
   tail -n 50 -f archivo.log
   ```

## Tips
- Utiliza `tail -f` para monitorear archivos de registro en tiempo real, lo que es útil para depuración.
- Puedes combinar `tail` con otros comandos utilizando tuberías (`|`) para filtrar o procesar la salida.
- Si necesitas ver las últimas líneas de varios archivos, simplemente lista los nombres de los archivos después del comando `tail`.