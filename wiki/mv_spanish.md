# [Linux] Bash mv Uso: Mover o renombrar archivos y directorios

## Overview
El comando `mv` se utiliza en Bash para mover o renombrar archivos y directorios. Es una herramienta esencial para la gestión de archivos en sistemas Unix y Linux.

## Usage
La sintaxis básica del comando `mv` es la siguiente:

```bash
mv [opciones] [origen] [destino]
```

## Common Options
- `-i`: Pregunta antes de sobrescribir un archivo existente.
- `-u`: Mueve solo si el archivo de origen es más nuevo que el archivo de destino o si el archivo de destino no existe.
- `-v`: Muestra el proceso de movimiento de archivos, proporcionando información detallada sobre lo que se está haciendo.

## Common Examples
1. **Mover un archivo a un directorio:**
   ```bash
   mv archivo.txt /ruta/al/directorio/
   ```

2. **Renombrar un archivo:**
   ```bash
   mv archivo.txt nuevo_nombre.txt
   ```

3. **Mover y renombrar un archivo al mismo tiempo:**
   ```bash
   mv archivo.txt /ruta/al/directorio/nuevo_nombre.txt
   ```

4. **Mover un directorio:**
   ```bash
   mv /ruta/al/directorio1 /ruta/al/directorio2/
   ```

5. **Mover un archivo y preguntar antes de sobrescribir:**
   ```bash
   mv -i archivo.txt /ruta/al/directorio/
   ```

## Tips
- Siempre verifica la ruta de destino antes de mover archivos para evitar pérdidas accidentales.
- Utiliza la opción `-v` para tener un registro claro de las operaciones realizadas, especialmente cuando trabajas con múltiples archivos.
- Considera usar la opción `-u` para evitar sobrescribir archivos más recientes sin querer.