# [리눅스] Bash diff 사용법

## Overview
El comando `diff` en Bash se utiliza para comparar archivos de texto línea por línea. Su propósito principal es identificar las diferencias entre dos archivos, mostrando qué líneas han sido añadidas, eliminadas o modificadas. Este comando es especialmente útil para desarrolladores y ingenieros que necesitan revisar cambios en el código fuente o en documentos de texto.

## Usage
La sintaxis básica del comando `diff` es la siguiente:

```bash
diff [opciones] archivo1 archivo2
```

### Opciones Comunes:
- `-u`: Muestra las diferencias en un formato unificado, que es más fácil de leer.
- `-c`: Muestra las diferencias en un formato de contexto, que incluye algunas líneas de contexto alrededor de las diferencias.
- `-i`: Ignora las diferencias entre mayúsculas y minúsculas.
- `-w`: Ignora los espacios en blanco al comparar líneas.
- `-r`: Compara directorios de manera recursiva.

## Examples
### Ejemplo 1: Comparar dos archivos de texto
Supongamos que tenemos dos archivos, `archivo1.txt` y `archivo2.txt`, y queremos ver las diferencias entre ellos.

```bash
diff archivo1.txt archivo2.txt
```

Este comando mostrará las líneas que difieren entre los dos archivos.

### Ejemplo 2: Usar formato unificado
Si queremos ver las diferencias en un formato más legible, podemos usar la opción `-u`:

```bash
diff -u archivo1.txt archivo2.txt
```

Esto mostrará las diferencias con un contexto adicional, facilitando la comprensión de los cambios.

## Tips
- Utiliza la opción `-u` para obtener un formato más amigable, especialmente cuando trabajas con cambios en el código.
- Si estás trabajando con archivos grandes, considera redirigir la salida a un archivo utilizando `>` para revisarlo más tarde:

```bash
diff -u archivo1.txt archivo2.txt > diferencias.txt
```

- Para comparar directorios completos, usa la opción `-r` para ver todas las diferencias en los archivos dentro de esos directorios.

El comando `diff` es una herramienta poderosa para cualquier desarrollador que necesite gestionar cambios en archivos de texto, y su correcta utilización puede facilitar enormemente el proceso de revisión y colaboración en proyectos.