# [Linux] Bash awk uso: Procesamiento de texto y datos

## Overview
El comando `awk` es una herramienta poderosa en Bash utilizada para el procesamiento de texto y datos. Permite manipular y analizar archivos de texto, extrayendo información y realizando operaciones en columnas específicas de datos.

## Usage
La sintaxis básica del comando `awk` es la siguiente:

```bash
awk [opciones] [argumentos]
```

## Common Options
- `-F`: Especifica el delimitador de campo. Por defecto, `awk` utiliza espacios en blanco.
- `-v`: Permite definir variables de entorno que pueden ser utilizadas dentro del script `awk`.
- `-f`: Indica que el siguiente argumento es un archivo que contiene un script `awk`.

## Common Examples

1. **Imprimir la primera columna de un archivo:**
   ```bash
   awk '{print $1}' archivo.txt
   ```

2. **Usar un delimitador diferente (por ejemplo, coma):**
   ```bash
   awk -F, '{print $2}' archivo.csv
   ```

3. **Filtrar líneas que contienen una palabra específica:**
   ```bash
   awk '/palabra/' archivo.txt
   ```

4. **Contar el número de líneas en un archivo:**
   ```bash
   awk 'END {print NR}' archivo.txt
   ```

5. **Sumar valores en la segunda columna:**
   ```bash
   awk '{sum += $2} END {print sum}' archivo.txt
   ```

## Tips
- Utiliza `-F` para definir delimitadores personalizados cuando trabajes con archivos que no usan espacios en blanco.
- Aprovecha las variables de entorno con `-v` para hacer tus scripts más dinámicos.
- Recuerda que `awk` procesa línea por línea, lo que lo hace eficiente para archivos grandes.