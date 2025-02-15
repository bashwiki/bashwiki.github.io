# [리눅스] Bash mapfile 사용법

## Overview
El comando `mapfile` en Bash se utiliza para leer líneas de un archivo o de la entrada estándar y almacenarlas en un array. Su propósito principal es facilitar la manipulación de datos en forma de líneas, permitiendo a los desarrolladores y a los ingenieros trabajar con colecciones de texto de manera más eficiente.

## Usage
La sintaxis básica del comando `mapfile` es la siguiente:

```bash
mapfile [-n count] [-s count] [-t] [array]
```

### Opciones comunes:
- `-n count`: Especifica el número de líneas que se deben leer. Por defecto, `mapfile` lee todas las líneas disponibles.
- `-s count`: Omite las primeras `count` líneas del archivo o de la entrada estándar.
- `-t`: Elimina el carácter de nueva línea al final de cada línea leída.
- `array`: El nombre del array donde se almacenarán las líneas leídas. Si no se especifica, se utiliza la variable `MAPFILE` por defecto.

## Examples
### Ejemplo 1: Leer un archivo en un array
Supongamos que tenemos un archivo llamado `datos.txt` con el siguiente contenido:

```
Línea 1
Línea 2
Línea 3
```

Podemos leer este archivo en un array llamado `lineas` de la siguiente manera:

```bash
mapfile lineas < datos.txt
echo "${lineas[@]}"
```

Esto imprimirá:

```
Línea 1 Línea 2 Línea 3
```

### Ejemplo 2: Leer desde la entrada estándar
También podemos usar `mapfile` para leer líneas desde la entrada estándar. Por ejemplo:

```bash
echo -e "Línea A\nLínea B\nLínea C" | mapfile -t lineas
echo "${lineas[@]}"
```

Esto imprimirá:

```
Línea A Línea B Línea C
```

## Tips
- Utiliza la opción `-t` si no deseas que se incluyan los caracteres de nueva línea al final de cada línea en el array.
- Recuerda que `mapfile` es especialmente útil cuando trabajas con archivos grandes, ya que permite manejar datos de manera eficiente sin necesidad de bucles adicionales.
- Puedes combinar `mapfile` con otras herramientas de Bash para procesar datos de forma más avanzada, como `grep` o `awk`, para filtrar líneas antes de almacenarlas en el array.