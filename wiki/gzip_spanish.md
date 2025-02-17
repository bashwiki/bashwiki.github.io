# [Linux] Bash gzip Uso: Comprimir y descomprimir archivos

## Overview
El comando `gzip` se utiliza para comprimir archivos en sistemas Unix y Linux. Su principal función es reducir el tamaño de los archivos, lo que facilita su almacenamiento y transferencia. `gzip` utiliza el algoritmo de compresión DEFLATE, que es eficiente y ampliamente utilizado.

## Usage
La sintaxis básica del comando `gzip` es la siguiente:

```bash
gzip [opciones] [argumentos]
```

## Common Options
- `-d`, `--decompress`: Descomprime un archivo.
- `-k`, `--keep`: Mantiene el archivo original después de la compresión.
- `-v`, `--verbose`: Muestra información detallada sobre el proceso de compresión.
- `-f`, `--force`: Fuerza la compresión, sobrescribiendo archivos existentes.
- `-r`, `--recursive`: Comprime archivos en directorios de manera recursiva.

## Common Examples
1. **Comprimir un archivo:**
   ```bash
   gzip archivo.txt
   ```
   Este comando comprimirá `archivo.txt` y generará `archivo.txt.gz`.

2. **Descomprimir un archivo:**
   ```bash
   gzip -d archivo.txt.gz
   ```
   Esto descomprimirá `archivo.txt.gz` y restaurará el archivo original.

3. **Comprimir manteniendo el archivo original:**
   ```bash
   gzip -k archivo.txt
   ```
   Este comando comprimirá `archivo.txt` a `archivo.txt.gz` y mantendrá `archivo.txt` sin cambios.

4. **Comprimir todos los archivos en un directorio:**
   ```bash
   gzip *.txt
   ```
   Comprime todos los archivos con extensión `.txt` en el directorio actual.

5. **Descomprimir todos los archivos en un directorio de manera recursiva:**
   ```bash
   gzip -dr directorio/
   ```
   Descomprime todos los archivos `.gz` en el directorio especificado y sus subdirectorios.

## Tips
- Siempre verifica el tamaño del archivo original y el comprimido para asegurarte de que la compresión fue efectiva.
- Usa la opción `-v` para obtener información sobre la tasa de compresión y el tamaño del archivo.
- Si trabajas con archivos grandes, considera usar la opción `-f` para evitar problemas al sobrescribir archivos existentes.