# [리눅스] Bash wget 사용법

## Overview
`wget` es una herramienta de línea de comandos utilizada para descargar archivos desde la web. Su principal propósito es facilitar la descarga de contenido a través de protocolos como HTTP, HTTPS y FTP. `wget` es especialmente útil para descargar archivos grandes o múltiples archivos a la vez, y puede funcionar en segundo plano, lo que permite continuar con otras tareas mientras se realiza la descarga.

## Usage
La sintaxis básica del comando `wget` es la siguiente:

```bash
wget [opciones] [URL]
```

### Opciones Comunes:
- `-O [archivo]`: Especifica el nombre del archivo de salida.
- `-c`: Continúa una descarga interrumpida.
- `-q`: Modo silencioso; no muestra mensajes de progreso.
- `-r`: Descarga recursivamente todos los archivos de un directorio.
- `--limit-rate=[tasa]`: Limita la velocidad de descarga a la tasa especificada (por ejemplo, 200k para 200 kilobytes por segundo).

## Examples
### Ejemplo 1: Descargar un archivo simple
Para descargar un archivo desde una URL, puedes usar el siguiente comando:

```bash
wget https://example.com/archivo.zip
```

Este comando descargará `archivo.zip` en el directorio actual.

### Ejemplo 2: Continuar una descarga interrumpida
Si una descarga se interrumpe, puedes reanudarla con la opción `-c`:

```bash
wget -c https://example.com/archivo.zip
```

Esto reanudará la descarga desde donde se detuvo.

## Tips
- Utiliza la opción `-q` si deseas que `wget` funcione en segundo plano sin mostrar mensajes, lo cual es útil para scripts automatizados.
- Si descargas múltiples archivos, considera usar la opción `-r` para descargar todo un sitio web o un directorio completo.
- Asegúrate de tener suficiente espacio en disco antes de iniciar descargas grandes o múltiples para evitar errores de espacio insuficiente.