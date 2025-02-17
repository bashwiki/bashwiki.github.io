# [Linux] Bash mapfile Uso: Leer líneas de un archivo en un array

## Overview
El comando `mapfile` en Bash se utiliza para leer líneas de un archivo y almacenarlas en un array. Es especialmente útil cuando se necesita manipular múltiples líneas de texto de manera eficiente.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
mapfile [options] [array_name]
```

## Common Options
- `-n N`: Lee solo las primeras N líneas del archivo.
- `-s N`: Omite las primeras N líneas del archivo.
- `-t`: Elimina el carácter de nueva línea al final de cada línea leída.

## Common Examples

### Ejemplo 1: Leer un archivo en un array
```bash
mapfile lineas < archivo.txt
```
Este comando lee todas las líneas de `archivo.txt` y las almacena en el array `lineas`.

### Ejemplo 2: Leer solo las primeras 3 líneas
```bash
mapfile -n 3 lineas < archivo.txt
```
Aquí, solo se leen las primeras 3 líneas de `archivo.txt` y se almacenan en el array `lineas`.

### Ejemplo 3: Omitir las primeras 2 líneas
```bash
mapfile -s 2 lineas < archivo.txt
```
Este comando omite las dos primeras líneas de `archivo.txt` y almacena el resto en el array `lineas`.

### Ejemplo 4: Eliminar caracteres de nueva línea
```bash
mapfile -t lineas < archivo.txt
```
Con esta opción, las líneas leídas se almacenan en el array `lineas` sin los caracteres de nueva línea al final.

## Tips
- Asegúrate de que el archivo que estás leyendo existe y tiene permisos de lectura.
- Puedes combinar opciones para personalizar la lectura de líneas según tus necesidades.
- Recuerda que el array creado es accesible mediante índices, por ejemplo, `${lineas[0]}` para acceder a la primera línea.