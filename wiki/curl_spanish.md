# [Linux] Bash curl uso: Herramienta para transferir datos

## Overview
El comando `curl` es una herramienta de línea de comandos utilizada para transferir datos a o desde un servidor. Soporta varios protocolos, incluyendo HTTP, HTTPS, FTP y más. Es especialmente útil para realizar solicitudes web y descargar archivos.

## Usage
La sintaxis básica del comando `curl` es la siguiente:

```bash
curl [opciones] [argumentos]
```

## Common Options
- `-X`: Especifica el método HTTP a utilizar (por ejemplo, GET, POST).
- `-d`: Envía datos en una solicitud POST.
- `-H`: Añade un encabezado HTTP a la solicitud.
- `-o`: Guarda la salida en un archivo en lugar de mostrarla en la consola.
- `-I`: Muestra solo los encabezados de la respuesta.

## Common Examples
1. **Realizar una solicitud GET a una URL:**
   ```bash
   curl http://example.com
   ```

2. **Descargar un archivo y guardarlo con un nombre específico:**
   ```bash
   curl -o archivo.html http://example.com
   ```

3. **Enviar datos en una solicitud POST:**
   ```bash
   curl -X POST -d "nombre=valor" http://example.com/api
   ```

4. **Añadir un encabezado personalizado a la solicitud:**
   ```bash
   curl -H "Authorization: Bearer token" http://example.com/protegido
   ```

5. **Mostrar solo los encabezados de la respuesta:**
   ```bash
   curl -I http://example.com
   ```

## Tips
- Utiliza la opción `-o` para guardar archivos directamente y evitar la salida en la consola.
- Para depurar problemas de conexión, añade la opción `-v` para obtener información detallada sobre la solicitud.
- Si trabajas con APIs, asegúrate de manejar correctamente los encabezados de autenticación y tipo de contenido.