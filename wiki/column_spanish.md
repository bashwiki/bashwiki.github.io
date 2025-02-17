# [Linux] Bash column Uso: Formatear texto en columnas

## Overview
El comando `column` en Bash se utiliza para formatear texto en columnas, lo que facilita la lectura de datos tabulares. Este comando toma la entrada de texto y la organiza en un formato de columna, alineando los datos de manera ordenada.

## Usage
La sintaxis básica del comando `column` es la siguiente:

```bash
column [options] [arguments]
```

## Common Options
- `-t`: Alinea el texto en columnas utilizando tabulaciones como delimitadores.
- `-s`: Especifica un delimitador diferente para las columnas (por defecto es el espacio).
- `-n`: No numera las filas.
- `-x`: Organiza las columnas en un formato de varias filas.

## Common Examples

### Ejemplo 1: Formatear texto con tabulaciones
```bash
cat archivo.txt | column -t
```
Este comando toma el contenido de `archivo.txt` y lo formatea en columnas alineadas usando tabulaciones.

### Ejemplo 2: Usar un delimitador específico
```bash
cat datos.csv | column -s, -t
```
Aquí, el comando utiliza una coma como delimitador para organizar el contenido de `datos.csv` en columnas.

### Ejemplo 3: Organizar en múltiples filas
```bash
cat lista.txt | column -x
```
Este comando organiza el contenido de `lista.txt` en un formato de varias filas, lo que puede ser útil para listas largas.

## Tips
- Asegúrate de que los datos de entrada estén bien delimitados para obtener un mejor formato en las columnas.
- Puedes combinar `column` con otros comandos de Unix, como `sort` o `grep`, para procesar datos antes de formatearlos.
- Experimenta con diferentes delimitadores usando la opción `-s` para ver cuál se adapta mejor a tus datos.