# [리눅스] Bash netstat 사용법

## Overview
El comando `netstat` (abreviatura de "network statistics") es una herramienta de línea de comandos que se utiliza para mostrar información sobre las conexiones de red, las tablas de enrutamiento y las estadísticas de interfaz de red en sistemas operativos Unix y Linux. Su propósito principal es ayudar a los ingenieros y desarrolladores a diagnosticar problemas de red y a obtener información sobre el estado de las conexiones de red activas.

## Usage
La sintaxis básica del comando `netstat` es la siguiente:

```
netstat [opciones]
```

Algunas de las opciones más comunes que se pueden utilizar con `netstat` incluyen:

- `-a`: Muestra todas las conexiones y puertos de escucha.
- `-t`: Muestra solo las conexiones TCP.
- `-u`: Muestra solo las conexiones UDP.
- `-n`: Muestra las direcciones y números de puerto en formato numérico, evitando la resolución de nombres.
- `-l`: Muestra solo los puertos que están en estado de escucha.
- `-p`: Muestra el identificador del proceso (PID) y el nombre del programa que está utilizando cada conexión.

## Examples
Aquí hay un par de ejemplos prácticos de cómo utilizar el comando `netstat`:

1. Para ver todas las conexiones activas y los puertos de escucha, puedes usar el siguiente comando:

   ```bash
   netstat -a
   ```

   Este comando mostrará una lista completa de todas las conexiones y puertos en uso, junto con su estado.

2. Si deseas ver solo las conexiones TCP activas en formato numérico, puedes ejecutar:

   ```bash
   netstat -tn
   ```

   Este comando filtrará la salida para mostrar solo las conexiones TCP y evitará la resolución de nombres, mostrando direcciones IP y números de puerto.

## Tips
- Utiliza la opción `-p` para identificar qué procesos están utilizando conexiones específicas. Esto puede ser útil para la depuración de problemas de red.
- Combina opciones para obtener información más específica. Por ejemplo, `netstat -tunlp` mostrará todas las conexiones TCP y UDP en formato numérico, junto con los procesos asociados.
- Ten en cuenta que en algunas distribuciones de Linux, `netstat` puede no estar instalado por defecto y puede ser necesario instalar el paquete `net-tools`.
- Para obtener información más detallada sobre las interfaces de red, considera usar el comando `ifconfig` o `ip a` junto con `netstat`.