# [Linux] Bash realpath uso equivalente: Resuelve rutas absolutas

## Overview
El comando `realpath` se utiliza para resolver rutas absolutas de archivos y directorios. Convierte rutas relativas en rutas absolutas y elimina cualquier referencia a directorios parentales (como `..`).

## Usage
La sintaxis básica del comando es la siguiente:

```bash
realpath [opciones] [argumentos]
```

## Common Options
- `-m`, `--canonicalize-missing`: Devuelve la ruta canónica, incluso si los archivos no existen.
- `-e`, `--canonicalize-existing`: Resuelve la ruta canónica solo si los archivos existen.
- `-q`, `--quiet`: Suprime los mensajes de error.

## Common Examples

1. **Convertir una ruta relativa a absoluta:**
   ```bash
   realpath ./mi_directorio
   ```

2. **Resolver una ruta con directorios parentales:**
   ```bash
   realpath ../mi_archivo.txt
   ```

3. **Obtener la ruta canónica de un archivo existente:**
   ```bash
   realpath -e /ruta/a/mi_archivo.txt
   ```

4. **Obtener la ruta canónica de un archivo que puede no existir:**
   ```bash
   realpath -m /ruta/a/mi_archivo_que_no_existe.txt
   ```

5. **Suprimir mensajes de error:**
   ```bash
   realpath -q /ruta/a/mi_archivo_que_no_existe.txt
   ```

## Tips
- Utiliza `realpath` en scripts para asegurar que siempre trabajas con rutas absolutas, lo que puede ayudar a evitar errores de ruta.
- Combina `realpath` con otros comandos como `cd` para navegar a directorios de manera más efectiva.
- Recuerda que `realpath` puede ser útil en entornos donde las rutas relativas pueden cambiar, como en scripts de automatización.