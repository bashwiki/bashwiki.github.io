# [Linux] Bash xz Uso: Comprimir y descomprimir archivos

## Overview
El comando `xz` se utiliza para comprimir y descomprimir archivos utilizando el algoritmo de compresión LZMA. Es conocido por ofrecer una alta tasa de compresión, lo que lo hace ideal para reducir el tamaño de archivos grandes.

## Usage
La sintaxis básica del comando `xz` es la siguiente:

```bash
xz [opciones] [argumentos]
```

## Common Options
- `-d`, `--decompress`: Descomprime un archivo.
- `-k`, `--keep`: Mantiene el archivo original después de la compresión o descompresión.
- `-v`, `--verbose`: Muestra información detallada sobre el proceso de compresión o descompresión.
- `-9`: Utiliza el nivel máximo de compresión (puede tardar más tiempo).
- `-f`, `--force`: Fuerza la compresión o descompresión, sobrescribiendo archivos existentes.

## Common Examples
### Comprimir un archivo
Para comprimir un archivo llamado `archivo.txt`, puedes usar el siguiente comando:

```bash
xz archivo.txt
```

### Descomprimir un archivo
Para descomprimir un archivo comprimido llamado `archivo.txt.xz`, utiliza:

```bash
xz -d archivo.txt.xz
```

### Mantener el archivo original
Si deseas comprimir un archivo y mantener el original, ejecuta:

```bash
xz -k archivo.txt
```

### Comprimir con el nivel máximo
Para comprimir un archivo utilizando el nivel máximo de compresión, utiliza:

```bash
xz -9 archivo.txt
```

### Descomprimir y mostrar información
Para descomprimir un archivo y ver información detallada sobre el proceso, ejecuta:

```bash
xz -dv archivo.txt.xz
```

## Tips
- Considera usar `-k` si necesitas conservar el archivo original para futuras referencias.
- La compresión con `-9` puede ser más lenta, así que úsala solo si realmente necesitas el tamaño mínimo.
- Si trabajas con archivos grandes, verifica el espacio en disco antes de comprimir, ya que el proceso puede requerir espacio adicional temporalmente.