# [리눅스] Bash scp 사용법

## Overview
El comando `scp` (Secure Copy Protocol) se utiliza para transferir archivos de manera segura entre un sistema local y un sistema remoto, o entre dos sistemas remotos. Este comando utiliza el protocolo SSH (Secure Shell) para garantizar que los datos se transfieran de forma segura, cifrando la información durante el proceso. Es una herramienta esencial para ingenieros y desarrolladores que necesitan mover archivos entre servidores o entre su máquina local y un servidor remoto.

## Usage
La sintaxis básica del comando `scp` es la siguiente:

```
scp [opciones] origen destino
```

### Opciones comunes:
- `-r`: Copia directorios de forma recursiva.
- `-P`: Especifica el puerto SSH a utilizar (por defecto es el puerto 22).
- `-i`: Especifica un archivo de clave privada para la autenticación.
- `-v`: Muestra información detallada sobre el proceso de copia (modo verbose).
- `-C`: Habilita la compresión durante la transferencia.

## Examples
### Ejemplo 1: Copiar un archivo desde el sistema local a un servidor remoto
Para copiar un archivo llamado `archivo.txt` desde tu máquina local a un servidor remoto con la dirección IP `192.168.1.10`, puedes usar el siguiente comando:

```bash
scp archivo.txt usuario@192.168.1.10:/ruta/destino/
```

### Ejemplo 2: Copiar un directorio completo a un servidor remoto
Si deseas copiar un directorio llamado `mi_directorio` de tu máquina local a un servidor remoto, puedes usar la opción `-r` para hacerlo de forma recursiva:

```bash
scp -r mi_directorio usuario@192.168.1.10:/ruta/destino/
```

## Tips
- Asegúrate de tener acceso SSH al servidor remoto y de que el servicio SSH esté en funcionamiento.
- Utiliza la opción `-v` para depurar problemas de conexión o transferencia.
- Considera usar claves SSH para una autenticación más segura y evitar tener que ingresar tu contraseña cada vez que uses `scp`.
- Si transfieres archivos grandes o muchos archivos, considera usar la opción `-C` para habilitar la compresión y acelerar la transferencia.