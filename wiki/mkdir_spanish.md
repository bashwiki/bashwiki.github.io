# [Linux] Bash mkdir Uso: Crear directorios en el sistema de archivos

## Overview
El comando `mkdir` se utiliza en Bash para crear nuevos directorios en el sistema de archivos. Es una herramienta fundamental para organizar archivos y carpetas en entornos de línea de comandos.

## Usage
La sintaxis básica del comando `mkdir` es la siguiente:

```bash
mkdir [opciones] [argumentos]
```

## Common Options
- `-p`: Crea directorios padres según sea necesario. Si el directorio padre no existe, se creará automáticamente.
- `-v`: Muestra un mensaje por cada directorio que se crea, útil para verificar la ejecución del comando.
- `-m`: Establece los permisos del nuevo directorio en lugar de los permisos predeterminados.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `mkdir`:

1. **Crear un solo directorio:**
   ```bash
   mkdir mi_directorio
   ```

2. **Crear varios directorios a la vez:**
   ```bash
   mkdir directorio1 directorio2 directorio3
   ```

3. **Crear un directorio y sus padres:**
   ```bash
   mkdir -p /ruta/a/nuevo/directorio
   ```

4. **Crear un directorio y mostrar un mensaje:**
   ```bash
   mkdir -v mi_directorio
   ```

5. **Crear un directorio con permisos específicos:**
   ```bash
   mkdir -m 755 mi_directorio
   ```

## Tips
- Utiliza la opción `-p` para evitar errores al intentar crear directorios que ya existen.
- Es recomendable usar nombres de directorios descriptivos para facilitar la organización de archivos.
- Verifica los permisos de los directorios creados, especialmente si se comparten con otros usuarios.