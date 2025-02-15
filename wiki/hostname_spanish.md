# [리눅스] Bash hostname 사용법

## Overview
El comando `hostname` en Bash se utiliza para mostrar o establecer el nombre del host del sistema. El nombre del host es una etiqueta que identifica de manera única un dispositivo en una red. Este comando es fundamental para la administración de sistemas, ya que permite a los administradores y desarrolladores conocer y configurar la identidad de su máquina en un entorno de red.

## Usage
La sintaxis básica del comando `hostname` es la siguiente:

```bash
hostname [opciones] [nuevo_nombre]
```

### Opciones comunes:
- `-a`, `--alias`: Muestra el alias del host.
- `-d`, `--domain`: Muestra el nombre del dominio del host.
- `-f`, `--fqdn`: Muestra el nombre de dominio completamente calificado (FQDN).
- `-i`, `--ip-address`: Muestra la dirección IP del host.
- `-s`, `--short`: Muestra solo el nombre corto del host.
- `nuevo_nombre`: Si se proporciona un nuevo nombre, el comando cambiará el nombre del host a este valor (requiere privilegios de superusuario).

## Examples
### Ejemplo 1: Mostrar el nombre del host actual
Para ver el nombre del host actual, simplemente ejecuta:

```bash
hostname
```

Este comando devolverá el nombre del host configurado en el sistema.

### Ejemplo 2: Cambiar el nombre del host
Para cambiar el nombre del host a "mi-nueva-maquina", puedes usar el siguiente comando (requiere permisos de superusuario):

```bash
sudo hostname mi-nueva-maquina
```

Después de ejecutar este comando, el nombre del host se actualizará y podrás verificarlo nuevamente con:

```bash
hostname
```

## Tips
- Es recomendable cambiar el nombre del host en un entorno de prueba antes de hacerlo en producción, para evitar conflictos de red.
- Después de cambiar el nombre del host, es posible que necesites reiniciar el sistema o reiniciar ciertos servicios para que los cambios surtan efecto completamente.
- Utiliza el comando `hostname -f` para verificar que el nombre de dominio completamente calificado esté configurado correctamente, especialmente en entornos de red complejos.