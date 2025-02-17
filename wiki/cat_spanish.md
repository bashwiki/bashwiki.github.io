# [Linux] Bash cat uso: Muestra el contenido de archivos

## Overview
El comando `cat` en Bash se utiliza para concatenar y mostrar el contenido de archivos. Es una herramienta sencilla pero poderosa que permite leer archivos de texto directamente en la terminal.

## Usage
La sintaxis básica del comando `cat` es la siguiente:

```bash
cat [opciones] [argumentos]
```

## Common Options
- `-n`: Numera todas las líneas de la salida.
- `-b`: Numera solo las líneas no vacías.
- `-E`: Muestra el carácter de fin de línea `$` al final de cada línea.
- `-s`: Suprime las líneas vacías consecutivas.

## Common Examples
1. **Mostrar el contenido de un archivo:**
   ```bash
   cat archivo.txt
   ```

2. **Concatenar varios archivos y mostrar su contenido:**
   ```bash
   cat archivo1.txt archivo2.txt
   ```

3. **Crear un nuevo archivo con contenido:**
   ```bash
   cat > nuevo_archivo.txt
   ```
   (Escribe el contenido y presiona `CTRL+D` para guardar).

4. **Numerar todas las líneas del archivo:**
   ```bash
   cat -n archivo.txt
   ```

5. **Suprimir líneas vacías en la salida:**
   ```bash
   cat -s archivo.txt
   ```

## Tips
- Utiliza `cat` en combinación con otros comandos mediante tuberías (`|`) para procesar la salida.
- Evita usar `cat` para archivos muy grandes, ya que puede saturar la terminal. En su lugar, considera usar `less` o `more`.
- Recuerda que `cat` puede ser útil para combinar archivos, pero asegúrate de que el orden de los archivos sea el correcto.