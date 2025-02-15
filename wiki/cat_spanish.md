# [리눅스] Bash cat 사용법

## Overview
El comando `cat` (concatenate) en Bash es una herramienta fundamental utilizada para leer, concatenar y mostrar el contenido de archivos de texto en la salida estándar. Su propósito principal es permitir a los usuarios visualizar el contenido de uno o más archivos de texto de manera rápida y sencilla. Además, `cat` puede ser utilizado para combinar archivos y redirigir su contenido a otros archivos o comandos.

## Usage
La sintaxis básica del comando `cat` es la siguiente:

```bash
cat [opciones] [archivo...]
```

### Opciones Comunes:
- `-n`: Numera todas las líneas de la salida.
- `-b`: Numera solo las líneas no vacías.
- `-E`: Muestra un símbolo `$` al final de cada línea.
- `-s`: Suprime las líneas vacías consecutivas.
- `-A`: Muestra caracteres no imprimibles en una forma legible.

## Examples
### Ejemplo 1: Mostrar el contenido de un archivo
Para mostrar el contenido de un archivo llamado `archivo.txt`, simplemente puedes usar:

```bash
cat archivo.txt
```

### Ejemplo 2: Concatenar múltiples archivos
Si deseas combinar el contenido de `archivo1.txt` y `archivo2.txt` y mostrarlo en la salida estándar, puedes usar:

```bash
cat archivo1.txt archivo2.txt
```

Si deseas guardar la salida combinada en un nuevo archivo llamado `archivo_combinado.txt`, puedes redirigir la salida:

```bash
cat archivo1.txt archivo2.txt > archivo_combinado.txt
```

## Tips
- Utiliza `cat` en combinación con otros comandos a través de tuberías (`|`) para procesar la salida. Por ejemplo, puedes usar `cat archivo.txt | grep "texto"` para buscar una cadena específica en el archivo.
- Para archivos muy grandes, considera usar `less` o `more` en lugar de `cat`, ya que te permitirán navegar por el contenido sin saturar la terminal.
- Al usar la opción `-n`, ten en cuenta que se numerarán todas las líneas, incluidas las vacías. Si solo deseas numerar las líneas con contenido, utiliza `-b` en su lugar.