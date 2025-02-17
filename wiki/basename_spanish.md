# [Linux] Bash basename Uso equivalente: Extraer el nombre de un archivo

## Overview
El comando `basename` se utiliza en Bash para extraer el nombre de un archivo o directorio de una ruta completa, eliminando cualquier prefijo de directorio. Esto es útil cuando se desea trabajar solo con el nombre del archivo sin su ruta.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
basename [opciones] [argumentos]
```

## Common Options
- `-a`: Trata cada argumento como un nombre de archivo y devuelve todos los nombres.
- `-s`: Elimina un sufijo específico del nombre del archivo.
- `--help`: Muestra la ayuda sobre el uso del comando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `basename`:

1. Extraer el nombre de un archivo de una ruta completa:

   ```bash
   basename /ruta/al/archivo.txt
   ```

   Salida:
   ```
   archivo.txt
   ```

2. Extraer el nombre de un archivo y eliminar un sufijo:

   ```bash
   basename /ruta/al/archivo.txt .txt
   ```

   Salida:
   ```
   archivo
   ```

3. Usar la opción `-a` para obtener múltiples nombres de archivos:

   ```bash
   basename -a /ruta/al/archivo1.txt /ruta/al/archivo2.txt
   ```

   Salida:
   ```
   archivo1.txt
   archivo2.txt
   ```

## Tips
- Utiliza `basename` en scripts para simplificar el manejo de nombres de archivos.
- Combina `basename` con otros comandos como `find` para procesar archivos de manera más eficiente.
- Recuerda que `basename` solo devuelve el nombre del archivo; si necesitas la ruta, considera usar `dirname` en su lugar.