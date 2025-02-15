# [리눅스] Bash head 사용법

## Overview
El comando `head` en Bash se utiliza para mostrar las primeras líneas de un archivo de texto. Su propósito principal es permitir a los usuarios ver rápidamente el contenido inicial de un archivo sin necesidad de abrirlo completamente. Esto es especialmente útil para archivos grandes donde solo se necesita una vista previa de los datos.

## Usage
La sintaxis básica del comando `head` es la siguiente:

```bash
head [opciones] [archivo]
```

### Opciones Comunes:
- `-n N`: Muestra las primeras N líneas del archivo. Si no se especifica, el valor predeterminado es 10.
- `-c N`: Muestra los primeros N bytes del archivo.
- `-q`: Suprime la cabecera que muestra el nombre del archivo cuando se están procesando múltiples archivos.
- `-v`: Muestra la cabecera del archivo incluso si solo se está procesando un archivo.

## Examples
### Ejemplo 1: Mostrar las primeras 10 líneas de un archivo
Para ver las primeras 10 líneas de un archivo llamado `archivo.txt`, simplemente se usa:

```bash
head archivo.txt
```

### Ejemplo 2: Mostrar las primeras 5 líneas de un archivo
Si deseas ver solo las primeras 5 líneas, puedes especificar la opción `-n`:

```bash
head -n 5 archivo.txt
```

### Ejemplo 3: Mostrar los primeros 20 bytes de un archivo
Para mostrar los primeros 20 bytes de un archivo, se utiliza la opción `-c`:

```bash
head -c 20 archivo.txt
```

## Tips
- Utiliza `head` en combinación con otros comandos de Unix, como `grep` o `sort`, para obtener resultados más específicos. Por ejemplo, puedes usar `grep` para filtrar líneas y luego `head` para limitar la salida.
- Si estás trabajando con archivos grandes, `head` es una herramienta eficiente para obtener una vista previa rápida sin cargar todo el archivo en memoria.
- Recuerda que `head` puede procesar múltiples archivos a la vez, lo que te permite comparar rápidamente las primeras líneas de varios archivos al mismo tiempo.