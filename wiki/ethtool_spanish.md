# [리눅스] Bash ethtool 사용법

## Overview
El comando `ethtool` es una herramienta de línea de comandos utilizada en sistemas Linux para consultar y modificar la configuración de interfaces de red Ethernet. Su propósito principal es proporcionar información sobre las capacidades de la tarjeta de red, así como permitir la configuración de parámetros como la velocidad, el modo dúplex y la activación o desactivación de funciones específicas.

## Usage
La sintaxis básica del comando `ethtool` es la siguiente:

```bash
ethtool [opciones] <interfaz>
```

Donde `<interfaz>` es el nombre de la interfaz de red que deseas consultar o modificar (por ejemplo, `eth0`, `enp3s0`, etc.).

### Opciones Comunes
- `-h`, `--help`: Muestra la ayuda y las opciones disponibles.
- `-i`, `--driver`: Muestra información sobre el controlador de la interfaz.
- `-s`, `--set`: Permite establecer parámetros específicos de la interfaz.
- `-p`, `--identify`: Hace parpadear el LED de la interfaz para identificarla.
- `-a`, `--show-autoneg`: Muestra el estado de la negociación automática.

## Examples
### Ejemplo 1: Consultar información de la interfaz
Para obtener información detallada sobre la interfaz de red `eth0`, puedes usar el siguiente comando:

```bash
ethtool eth0
```

Este comando mostrará información como la velocidad de la conexión, el modo dúplex, y las capacidades de la tarjeta de red.

### Ejemplo 2: Cambiar la velocidad y el modo dúplex
Si deseas establecer la velocidad de la interfaz `eth0` a 100 Mbps y el modo dúplex a completo, puedes ejecutar:

```bash
ethtool -s eth0 speed 100 duplex full
```

Este comando configura la interfaz para operar a la velocidad y modo especificados.

## Tips
- Asegúrate de tener privilegios de superusuario (root) para realizar cambios en la configuración de la interfaz.
- Utiliza `ethtool -i <interfaz>` para verificar el controlador y la versión del firmware de la tarjeta de red, lo que puede ser útil para la solución de problemas.
- Ten en cuenta que algunos cambios pueden requerir que la interfaz de red se reinicie para que tengan efecto.