# [Linux] Bash dirname Uso: Extraer el directorio de una ruta

## Overview
El comando `dirname` se utiliza en Bash para extraer el directorio de una ruta de archivo dada. Es útil para obtener la parte del directorio de una ruta completa, permitiendo manipular rutas de archivos de manera más efectiva.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
dirname [opciones] [argumentos]
```

## Common Options
- `-z`: Trata los argumentos como cadenas de longitud cero.
- `--help`: Muestra la ayuda sobre el uso del comando.
- `--version`: Muestra la versión del comando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `dirname`:

1. **Extraer el directorio de una ruta completa:**
   ```bash
   dirname /home/usuario/documentos/archivo.txt
   ```
   Salida:
   ```
   /home/usuario/documentos
   ```

2. **Usar dirname con una ruta relativa:**
   ```bash
   dirname ./documentos/archivo.txt
   ```
   Salida:
   ```
   ./documentos
   ```

3. **Extraer el directorio de un archivo en el directorio actual:**
   ```bash
   dirname archivo.txt
   ```
   Salida:
   ```
   .
   ```

4. **Combinar dirname con otros comandos:**
   ```bash
   dirname $(pwd)/archivo.txt
   ```
   Salida:
   ```
   /ruta/al/directorio/actual
   ```

## Tips
- Utiliza `dirname` en combinación con otros comandos como `basename` para manipular rutas de archivos de manera más efectiva.
- Recuerda que `dirname` devuelve un punto (`.`) si el archivo está en el directorio actual.
- Puedes usar `dirname` en scripts de Bash para automatizar tareas que requieren la manipulación de rutas de archivos.