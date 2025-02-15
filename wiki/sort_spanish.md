# [리눅스] Bash sort 사용법

## Overview
El comando `sort` en Bash se utiliza para ordenar líneas de texto en un archivo o en la entrada estándar. Su propósito principal es organizar datos de manera que sean más fáciles de leer o procesar. `sort` puede manejar diferentes tipos de datos y permite ordenar en orden ascendente o descendente, así como aplicar diversas opciones para personalizar el proceso de ordenación.

## Usage
La sintaxis básica del comando `sort` es la siguiente:

```bash
sort [opciones] [archivo]
```

### Opciones Comunes:
- `-r`: Ordenar en orden descendente.
- `-n`: Ordenar numéricamente en lugar de alfabéticamente.
- `-k`: Especificar la clave de ordenación (por ejemplo, la columna a ordenar).
- `-u`: Eliminar líneas duplicadas en el resultado.
- `-o`: Especificar un archivo de salida para guardar el resultado ordenado.

## Examples
### Ejemplo 1: Ordenar un archivo de texto
Supongamos que tenemos un archivo llamado `nombres.txt` que contiene una lista de nombres:

```
Carlos
Ana
Luis
Beatriz
```

Para ordenar este archivo alfabéticamente, se puede usar el siguiente comando:

```bash
sort nombres.txt
```

La salida será:

```
Ana
Beatriz
Carlos
Luis
```

### Ejemplo 2: Ordenar numéricamente
Si tenemos un archivo llamado `numeros.txt` que contiene una lista de números:

```
10
2
33
1
```

Para ordenar estos números de forma ascendente, se puede usar:

```bash
sort -n numeros.txt
```

La salida será:

```
1
2
10
33
```

## Tips
- Al usar `sort`, es útil redirigir la salida a un nuevo archivo utilizando la opción `-o`, por ejemplo: `sort nombres.txt -o nombres_ordenados.txt`.
- Para ordenar por una columna específica en un archivo delimitado por espacios o comas, utiliza la opción `-k`. Por ejemplo, `sort -k2 archivo.txt` ordenará por la segunda columna.
- Si deseas eliminar duplicados mientras ordenas, combina las opciones `-u` y `-r` para obtener una lista única en orden descendente: `sort -u -r archivo.txt`.

Con estos conocimientos, podrás utilizar el comando `sort` de manera efectiva para organizar tus datos en Bash.