# [Linux] Bash bzip2 Uso: Comprimir y descomprimir archivos

## Overview
El comando `bzip2` se utiliza para comprimir y descomprimir archivos en sistemas Unix y Linux. Utiliza el algoritmo de compresión Burrows-Wheeler, que ofrece una alta tasa de compresión, especialmente para archivos de texto.

## Usage
La sintaxis básica del comando `bzip2` es la siguiente:

```bash
bzip2 [opciones] [argumentos]
```

## Common Options
- `-d`, `--decompress`: Descomprime un archivo.
- `-k`, `--keep`: Mantiene el archivo original después de la compresión.
- `-f`, `--force`: Fuerza la compresión o descompresión, sobrescribiendo archivos existentes.
- `-v`, `--verbose`: Muestra información detallada sobre el proceso de compresión o descompresión.
- `-z`, `--compress`: Comprime un archivo (opción predeterminada).

## Common Examples
1. **Comprimir un archivo**:
   ```bash
   bzip2 archivo.txt
   ```
   Esto creará un archivo llamado `archivo.txt.bz2` y eliminará el archivo original.

2. **Descomprimir un archivo**:
   ```bash
   bzip2 -d archivo.txt.bz2
   ```
   Esto restaurará el archivo original `archivo.txt` y eliminará el archivo comprimido.

3. **Mantener el archivo original al comprimir**:
   ```bash
   bzip2 -k archivo.txt
   ```
   Esto creará `archivo.txt.bz2` pero mantendrá `archivo.txt` sin cambios.

4. **Comprimir múltiples archivos**:
   ```bash
   bzip2 archivo1.txt archivo2.txt
   ```
   Esto comprimirá ambos archivos, creando `archivo1.txt.bz2` y `archivo2.txt.bz2`.

5. **Ver información detallada durante la compresión**:
   ```bash
   bzip2 -v archivo.txt
   ```
   Esto mostrará el progreso y detalles sobre el proceso de compresión.

## Tips
- Para comprimir directorios, puedes usar `tar` junto con `bzip2`:
  ```bash
  tar -cvjf archivo.tar.bz2 /ruta/al/directorio
  ```
- Siempre verifica el espacio en disco antes de comprimir archivos grandes para evitar problemas de almacenamiento.
- Utiliza la opción `-f` con precaución, ya que sobrescribirá archivos existentes sin advertencia.