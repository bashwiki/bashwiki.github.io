# [Linux] Bash grep Uso equivalente: Buscar texto en archivos

## Overview
El comando `grep` se utiliza en Bash para buscar patrones de texto dentro de archivos. Es una herramienta poderosa que permite filtrar y encontrar líneas que coinciden con una expresión regular, facilitando la búsqueda de información específica en grandes volúmenes de datos.

## Usage
La sintaxis básica del comando `grep` es la siguiente:

```bash
grep [opciones] [patrón] [archivo]
```

## Common Options
- `-i`: Ignora la distinción entre mayúsculas y minúsculas.
- `-r`: Busca de manera recursiva en todos los archivos de un directorio.
- `-v`: Muestra las líneas que **no** coinciden con el patrón.
- `-n`: Muestra el número de línea junto con las líneas coincidentes.
- `-l`: Muestra solo los nombres de los archivos que contienen el patrón.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `grep`:

1. **Buscar una palabra en un archivo:**
   ```bash
   grep "texto" archivo.txt
   ```

2. **Buscar sin distinguir entre mayúsculas y minúsculas:**
   ```bash
   grep -i "texto" archivo.txt
   ```

3. **Buscar recursivamente en un directorio:**
   ```bash
   grep -r "texto" /ruta/al/directorio
   ```

4. **Mostrar líneas que no contienen el patrón:**
   ```bash
   grep -v "texto" archivo.txt
   ```

5. **Mostrar el número de línea de las coincidencias:**
   ```bash
   grep -n "texto" archivo.txt
   ```

6. **Listar solo los nombres de archivos que contienen el patrón:**
   ```bash
   grep -l "texto" *.txt
   ```

## Tips
- Utiliza `grep` en combinación con otros comandos mediante tuberías (`|`) para filtrar la salida de otros programas.
- Asegúrate de usar comillas alrededor de patrones que contengan espacios o caracteres especiales.
- Familiarízate con las expresiones regulares para aprovechar al máximo las capacidades de búsqueda de `grep`.