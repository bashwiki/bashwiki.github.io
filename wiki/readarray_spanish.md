# [Linux] Bash readarray uso: Leer líneas en un array

## Overview
El comando `readarray` en Bash se utiliza para leer líneas de un archivo o de la entrada estándar y almacenarlas en un array. Es especialmente útil para manejar datos en formato de texto donde cada línea representa un elemento.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
readarray [opciones] [nombre_del_array]
```

## Common Options
- `-n N`: Lee solo las primeras N líneas.
- `-s N`: Omite las primeras N líneas al leer.
- `-t`: Elimina el carácter de nueva línea al final de cada línea.

## Common Examples

### Ejemplo 1: Leer un archivo en un array
```bash
readarray lineas < archivo.txt
```
Este comando lee todas las líneas del archivo `archivo.txt` y las almacena en el array `lineas`.

### Ejemplo 2: Leer solo las primeras 3 líneas
```bash
readarray -n 3 lineas < archivo.txt
```
Aquí, solo se leen las primeras 3 líneas del archivo `archivo.txt`.

### Ejemplo 3: Ignorar las primeras 2 líneas
```bash
readarray -s 2 lineas < archivo.txt
```
Este comando omite las primeras 2 líneas del archivo y lee el resto en el array `lineas`.

### Ejemplo 4: Eliminar los caracteres de nueva línea
```bash
readarray -t lineas < archivo.txt
```
Con esta opción, las líneas leídas se almacenan en el array `lineas` sin los caracteres de nueva línea al final.

## Tips
- Asegúrate de que el archivo que estás leyendo tenga el formato correcto, ya que `readarray` separa las líneas basándose en los saltos de línea.
- Puedes acceder a los elementos del array utilizando la sintaxis `${lineas[i]}`, donde `i` es el índice del elemento.
- Si necesitas procesar cada línea individualmente, considera usar un bucle `for` para iterar sobre el array después de haberlo leído.