# [Linux] Bash rmdir Uso: Eliminar directorios vacíos

## Overview
El comando `rmdir` se utiliza en Bash para eliminar directorios que están vacíos. Si intentas eliminar un directorio que contiene archivos o subdirectorios, el comando fallará y no realizará ninguna acción.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
rmdir [opciones] [argumentos]
```

## Common Options
- `--ignore-fail-on-non-empty`: Ignora los errores si el directorio no está vacío.
- `--parents`: Elimina directorios de forma recursiva, eliminando también los directorios padres si están vacíos.
- `-p`: Sinónimo de `--parents`.

## Common Examples
1. **Eliminar un directorio vacío:**
   ```bash
   rmdir mi_directorio
   ```

2. **Eliminar varios directorios vacíos a la vez:**
   ```bash
   rmdir directorio1 directorio2 directorio3
   ```

3. **Eliminar un directorio y sus padres vacíos:**
   ```bash
   rmdir -p padre/hijo
   ```

4. **Ignorar errores si el directorio no está vacío:**
   ```bash
   rmdir --ignore-fail-on-non-empty directorio_no_vacio
   ```

## Tips
- Asegúrate de que el directorio esté vacío antes de usar `rmdir`, ya que de lo contrario, el comando no funcionará.
- Usa `ls` para verificar el contenido del directorio antes de intentar eliminarlo.
- Si necesitas eliminar un directorio que no está vacío, considera usar el comando `rm -r` en su lugar, pero ten cuidado, ya que este comando eliminará todo el contenido del directorio de forma irreversible.