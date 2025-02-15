# [리눅스] Bash fgrep 사용법

## Overview
El comando `fgrep` es una herramienta de búsqueda en texto que forma parte de la suite de comandos de Unix/Linux. Su propósito principal es buscar cadenas de texto específicas en archivos o en la entrada estándar. A diferencia de otros comandos de búsqueda como `grep`, `fgrep` no interpreta expresiones regulares, lo que significa que busca literalmente la cadena que se le proporciona. Esto lo hace especialmente útil cuando se necesita buscar texto que contenga caracteres especiales que normalmente tendrían un significado en expresiones regulares.

## Usage
La sintaxis básica del comando `fgrep` es la siguiente:

```bash
fgrep [opciones] patrón [archivo...]
```

### Opciones Comunes:
- `-i`: Ignorar mayúsculas y minúsculas durante la búsqueda.
- `-v`: Invertir la búsqueda, mostrando las líneas que no coinciden con el patrón.
- `-c`: Contar el número de líneas que coinciden con el patrón.
- `-n`: Mostrar el número de línea junto con las líneas coincidentes.
- `-r`: Buscar recursivamente en directorios.

## Examples
### Ejemplo 1: Búsqueda simple
Supongamos que tienes un archivo llamado `datos.txt` y deseas buscar la cadena "error" en él. Puedes usar el siguiente comando:

```bash
fgrep "error" datos.txt
```

Este comando mostrará todas las líneas en `datos.txt` que contienen la palabra "error".

### Ejemplo 2: Ignorar mayúsculas y minúsculas
Si deseas buscar la cadena "Error" sin importar si está en mayúsculas o minúsculas, puedes usar la opción `-i`:

```bash
fgrep -i "error" datos.txt
```

Este comando devolverá todas las líneas que contengan "error", "Error", "ERROR", etc.

## Tips
- Utiliza `fgrep` cuando necesites realizar búsquedas literales y no quieras preocuparte por la interpretación de caracteres especiales.
- Si estás trabajando con archivos grandes, considera combinar `fgrep` con otras herramientas como `less` para facilitar la lectura de los resultados. Por ejemplo:

```bash
fgrep "error" datos.txt | less
```

- Recuerda que `fgrep` es más eficiente que `grep` cuando se trata de búsquedas literales, ya que no tiene que procesar expresiones regulares.