# [리눅스] Bash lsusb 사용법

## Overview
El comando `lsusb` es una herramienta de línea de comandos en sistemas Linux que permite listar todos los dispositivos USB conectados al sistema. Su propósito principal es proporcionar información sobre los dispositivos USB, incluyendo detalles como el ID del fabricante, el ID del producto y la descripción del dispositivo. Esto es especialmente útil para ingenieros y desarrolladores que necesitan diagnosticar problemas de hardware o verificar la conexión de dispositivos USB.

## Usage
La sintaxis básica del comando `lsusb` es la siguiente:

```bash
lsusb [opciones]
```

### Opciones Comunes
- `-v`: Muestra información detallada sobre cada dispositivo USB.
- `-t`: Muestra la topología del bus USB en un formato de árbol.
- `-s [bus]:[dispositivo]`: Muestra información solo para el dispositivo específico en el bus USB indicado.
- `-D [archivo]`: Lee la información de un dispositivo USB desde un archivo específico.

## Examples
### Ejemplo 1: Listar todos los dispositivos USB
Para listar todos los dispositivos USB conectados, simplemente ejecuta:

```bash
lsusb
```

Esto mostrará una lista de todos los dispositivos USB, junto con sus IDs de fabricante y producto.

### Ejemplo 2: Obtener información detallada de un dispositivo específico
Si deseas obtener información detallada sobre un dispositivo específico, puedes usar la opción `-v`. Por ejemplo:

```bash
lsusb -v -s 001:002
```

En este caso, `001:002` representa el bus y el número de dispositivo del USB que deseas inspeccionar.

## Tips
- Utiliza la opción `-v` con precaución, ya que puede generar una gran cantidad de información, lo que puede ser abrumador si hay muchos dispositivos conectados.
- Para una mejor legibilidad, considera redirigir la salida a un archivo de texto usando `lsusb > dispositivos_usb.txt`.
- Si trabajas frecuentemente con dispositivos USB, puedes crear un alias en tu archivo `.bashrc` para simplificar el uso del comando, por ejemplo: `alias usb='lsusb -v'`.

Con esta guía, deberías estar bien equipado para utilizar el comando `lsusb` y obtener información valiosa sobre los dispositivos USB conectados a tu sistema.