# [리눅스] Bash read 사용법

## Overview
El comando `read` en Bash se utiliza para leer la entrada del usuario desde la línea de comandos. Su propósito principal es capturar datos introducidos por el usuario y almacenarlos en variables para su posterior uso en scripts. Esto permite la interacción dinámica con los usuarios, facilitando la creación de scripts más flexibles y adaptables.

## Usage
La sintaxis básica del comando `read` es la siguiente:

```bash
read [opciones] [nombre_variable ...]
```

### Opciones comunes:
- `-p`: Permite mostrar un mensaje de aviso antes de la entrada del usuario.
- `-s`: Silencia la entrada, útil para contraseñas.
- `-a`: Lee la entrada en un array.
- `-t`: Establece un tiempo de espera (timeout) para la entrada.

## Examples
### Ejemplo 1: Leer una sola línea de entrada
```bash
#!/bin/bash
echo "Por favor, introduce tu nombre:"
read nombre
echo "Hola, $nombre!"
```
En este ejemplo, el script solicita al usuario que introduzca su nombre y luego lo saluda.

### Ejemplo 2: Leer múltiples variables
```bash
#!/bin/bash
echo "Introduce tu nombre y edad:"
read nombre edad
echo "Hola, $nombre. Tienes $edad años."
```
Aquí, el script lee tanto el nombre como la edad del usuario en una sola línea.

## Tips
- Utiliza la opción `-p` para proporcionar un mensaje claro al usuario sobre qué información se espera.
- Si necesitas leer una contraseña, usa la opción `-s` para ocultar la entrada.
- Considera establecer un tiempo de espera con `-t` para evitar que el script se quede esperando indefinidamente.
- Siempre valida la entrada del usuario para asegurar que los datos sean correctos y evitar errores en el script.