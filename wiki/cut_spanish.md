# [Linux] Bash cut uso equivalente: Extraer secciones de líneas de texto

## Overview
El comando `cut` se utiliza en Bash para extraer secciones específicas de líneas de texto. Es especialmente útil para procesar archivos de texto y datos delimitados, permitiendo seleccionar columnas o partes de líneas basadas en delimitadores.

## Usage
La sintaxis básica del comando `cut` es la siguiente:

```bash
cut [opciones] [argumentos]
```

## Common Options
- `-f`: Especifica los campos que se desean extraer, separados por un delimitador.
- `-d`: Define el delimitador que se utiliza para separar los campos (por defecto es la tabulación).
- `-c`: Selecciona caracteres específicos de cada línea.
- `--complement`: Devuelve todo menos los campos especificados.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `cut`:

1. **Extraer el primer campo de un archivo CSV**:
   ```bash
   cut -d ',' -f 1 archivo.csv
   ```

2. **Extraer múltiples campos de un archivo de texto**:
   ```bash
   cut -d ' ' -f 1,3 archivo.txt
   ```

3. **Extraer caracteres específicos de una línea**:
   ```bash
   echo "Hola Mundo" | cut -c 1-4
   ```

4. **Invertir la selección de campos**:
   ```bash
   cut -d ':' -f 1 --complement /etc/passwd
   ```

## Tips
- Siempre verifica el delimitador de tus archivos antes de usar `cut`, ya que el comportamiento por defecto es la tabulación.
- Usa `-n` junto con `-f` para evitar que `cut` omita líneas que no contienen el delimitador especificado.
- Combina `cut` con otros comandos como `grep` o `sort` para un procesamiento de texto más avanzado.