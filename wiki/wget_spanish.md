# [Linux] Bash wget Uso: Descarga archivos desde la web

## Overview
El comando `wget` es una herramienta de línea de comandos utilizada para descargar archivos de la web. Es especialmente útil para obtener contenido de sitios web, archivos y recursos de manera no interactiva, lo que significa que puede ejecutarse en segundo plano y continuar la descarga incluso si se cierra la sesión.

## Usage
La sintaxis básica del comando `wget` es la siguiente:

```
wget [opciones] [URL]
```

## Common Options
A continuación se presentan algunas de las opciones más comunes que se pueden utilizar con `wget`:

- `-O [archivo]`: Especifica el nombre del archivo de salida.
- `-c`: Continúa una descarga interrumpida.
- `-q`: Ejecuta el comando en modo silencioso, sin mostrar información en la consola.
- `--limit-rate=[velocidad]`: Limita la velocidad de descarga a la cantidad especificada.
- `-r`: Descarga recursivamente todos los archivos de un directorio.

## Common Examples
Aquí hay algunos ejemplos prácticos de cómo usar `wget`:

1. **Descargar un archivo simple:**
   ```bash
   wget https://ejemplo.com/archivo.zip
   ```

2. **Descargar un archivo y renombrarlo:**
   ```bash
   wget -O nuevo_nombre.zip https://ejemplo.com/archivo.zip
   ```

3. **Continuar una descarga interrumpida:**
   ```bash
   wget -c https://ejemplo.com/archivo.zip
   ```

4. **Descargar un sitio web de forma recursiva:**
   ```bash
   wget -r https://ejemplo.com
   ```

5. **Limitar la velocidad de descarga:**
   ```bash
   wget --limit-rate=200k https://ejemplo.com/archivo.zip
   ```

## Tips
- Utiliza la opción `-q` para evitar la salida de información si estás descargando múltiples archivos y deseas mantener la consola limpia.
- Si necesitas descargar un sitio web completo, asegúrate de usar la opción `-r` junto con `-np` (no parent) para evitar descargar archivos de directorios superiores.
- Considera usar `-N` para descargar solo archivos que han cambiado desde la última descarga, lo que puede ahorrar tiempo y ancho de banda.