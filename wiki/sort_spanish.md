# [Linux] Bash sort uso: Ordenar líneas de texto

## Overview
El comando `sort` en Bash se utiliza para ordenar líneas de texto en archivos o en la entrada estándar. Es una herramienta poderosa que permite organizar datos de manera ascendente o descendente, facilitando la búsqueda y el análisis de información.

## Usage
La sintaxis básica del comando `sort` es la siguiente:

```bash
sort [opciones] [argumentos]
```

## Common Options
Aquí hay algunas opciones comunes que puedes usar con el comando `sort`:

- `-r`: Ordenar en orden descendente.
- `-n`: Ordenar numéricamente.
- `-k`: Especificar la clave de ordenación (por ejemplo, la columna).
- `-u`: Eliminar líneas duplicadas.
- `-o`: Especificar un archivo de salida para guardar el resultado.

## Common Examples
A continuación, se presentan algunos ejemplos prácticos del uso del comando `sort`:

1. **Ordenar un archivo de texto en orden ascendente:**

   ```bash
   sort archivo.txt
   ```

2. **Ordenar un archivo de texto en orden descendente:**

   ```bash
   sort -r archivo.txt
   ```

3. **Ordenar numéricamente:**

   ```bash
   sort -n numeros.txt
   ```

4. **Ordenar por la segunda columna de un archivo:**

   ```bash
   sort -k2 archivo.txt
   ```

5. **Eliminar líneas duplicadas y ordenar:**

   ```bash
   sort -u archivo.txt
   ```

6. **Guardar el resultado en un nuevo archivo:**

   ```bash
   sort archivo.txt -o archivo_ordenado.txt
   ```

## Tips
- Siempre verifica el contenido de tu archivo original antes de aplicar `sort`, especialmente si usas la opción `-o`, ya que sobrescribirá el archivo.
- Utiliza la opción `-k` para ordenar por columnas específicas, lo que es útil en archivos delimitados por comas o tabulaciones.
- Combina `sort` con otros comandos como `uniq` para obtener resultados más refinados, especialmente al trabajar con datos que contienen duplicados.