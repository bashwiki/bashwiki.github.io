# [리눅스] Bash sed 사용법

## Overview
El comando `sed`, que significa "stream editor", es una herramienta poderosa en Bash utilizada para realizar transformaciones de texto en un flujo de datos. Su propósito principal es permitir la edición de archivos de texto de manera no interactiva, lo que significa que puedes modificar el contenido de un archivo sin abrirlo en un editor de texto. `sed` es especialmente útil para tareas como reemplazar texto, eliminar líneas o insertar contenido en archivos.

## Usage
La sintaxis básica del comando `sed` es la siguiente:

```bash
sed [opciones] 'comando' archivo
```

### Opciones Comunes:
- `-e`: Permite agregar múltiples comandos en una sola invocación de `sed`.
- `-i`: Edita archivos en su lugar (modifica el archivo original).
- `-n`: Suprime la salida automática, permitiendo que solo se muestren las líneas que se especifican con el comando `p`.
- `-f`: Permite leer comandos desde un archivo.

## Examples
### Ejemplo 1: Reemplazar texto
Supongamos que tienes un archivo llamado `archivo.txt` que contiene la siguiente línea:

```
Hola mundo
```

Si deseas reemplazar "mundo" por "sed", puedes usar el siguiente comando:

```bash
sed 's/mundo/sed/' archivo.txt
```

Esto producirá la salida:

```
Hola sed
```

### Ejemplo 2: Eliminar líneas
Si deseas eliminar todas las líneas que contienen la palabra "eliminar" en un archivo llamado `texto.txt`, puedes usar:

```bash
sed '/eliminar/d' texto.txt
```

Este comando eliminará todas las líneas que contengan "eliminar" y mostrará el resto del contenido.

## Tips
- Siempre es recomendable hacer una copia de seguridad de tus archivos antes de usar la opción `-i`, ya que los cambios son irreversibles.
- Puedes combinar múltiples comandos usando `-e`. Por ejemplo:

```bash
sed -e 's/mundo/sed/' -e '/eliminar/d' archivo.txt
```

- Para pruebas, utiliza la opción `-n` junto con `p` para ver solo las líneas que deseas modificar sin afectar el archivo original:

```bash
sed -n 's/mundo/sed/p' archivo.txt
```

Esto mostrará solo las líneas donde se realizó el reemplazo, sin modificar el archivo.