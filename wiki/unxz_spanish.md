# [Linux] Bash unxz Uso: Descomprimir archivos .xz

## Overview
El comando `unxz` se utiliza para descomprimir archivos que han sido comprimidos con el formato `.xz`. Este formato es conocido por su alta tasa de compresión y es comúnmente utilizado en sistemas Linux para reducir el tamaño de archivos.

## Usage
La sintaxis básica del comando `unxz` es la siguiente:

```
unxz [opciones] [argumentos]
```

## Common Options
- `-k`, `--keep`: Mantiene el archivo original después de la descompresión.
- `-f`, `--force`: Fuerza la descompresión, sobrescribiendo archivos existentes sin preguntar.
- `-v`, `--verbose`: Muestra información detallada sobre el proceso de descompresión.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `unxz`:

1. **Descomprimir un archivo .xz**:
   ```bash
   unxz archivo.xz
   ```

2. **Descomprimir un archivo y mantener el original**:
   ```bash
   unxz -k archivo.xz
   ```

3. **Forzar la descompresión, sobrescribiendo archivos existentes**:
   ```bash
   unxz -f archivo.xz
   ```

4. **Descomprimir un archivo y mostrar información detallada**:
   ```bash
   unxz -v archivo.xz
   ```

## Tips
- Siempre verifica el espacio disponible en disco antes de descomprimir archivos grandes para evitar problemas de espacio.
- Si necesitas descomprimir múltiples archivos a la vez, puedes usar un comodín:
  ```bash
  unxz *.xz
  ```
- Considera usar la opción `-k` si no estás seguro de querer eliminar el archivo original, especialmente en archivos importantes.