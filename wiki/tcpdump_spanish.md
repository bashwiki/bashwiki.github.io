# [리눅스] Bash tcpdump 사용법

## Overview
El comando `tcpdump` es una herramienta de captura de paquetes de red que permite a los usuarios interceptar y analizar el tráfico que pasa a través de una red. Su propósito principal es ayudar a los ingenieros y desarrolladores a diagnosticar problemas de red, monitorear el tráfico y realizar análisis de seguridad. `tcpdump` es especialmente útil para capturar y visualizar paquetes en tiempo real, así como para guardar datos para un análisis posterior.

## Usage
La sintaxis básica del comando `tcpdump` es la siguiente:

```bash
tcpdump [opciones] [filtro]
```

### Opciones Comunes:
- `-i <interfaz>`: Especifica la interfaz de red a utilizar (por ejemplo, `eth0`, `wlan0`).
- `-n`: No resuelve nombres de host ni direcciones IP, mostrando solo direcciones numéricas.
- `-v`, `-vv`, `-vvv`: Aumenta el nivel de verbosidad de la salida.
- `-c <n>`: Captura solo `n` paquetes y luego se detiene.
- `-w <archivo>`: Guarda la captura en un archivo para un análisis posterior.
- `-r <archivo>`: Lee y analiza un archivo de captura previamente guardado.

## Examples
### Ejemplo 1: Capturar tráfico en tiempo real
Para capturar paquetes en la interfaz `eth0` y mostrar la salida en la consola, puedes usar el siguiente comando:

```bash
tcpdump -i eth0
```

### Ejemplo 2: Guardar la captura en un archivo
Si deseas guardar la captura de paquetes en un archivo llamado `captura.pcap`, puedes hacerlo con el siguiente comando:

```bash
tcpdump -i eth0 -w captura.pcap
```

## Tips
- Siempre ejecuta `tcpdump` con privilegios de superusuario (usando `sudo`) para asegurarte de que tienes los permisos necesarios para capturar paquetes.
- Utiliza filtros para limitar el tráfico capturado y hacer el análisis más manejable. Por ejemplo, para capturar solo tráfico HTTP, puedes usar:

```bash
tcpdump -i eth0 'tcp port 80'
```

- Recuerda que la captura de paquetes puede generar una gran cantidad de datos. Es recomendable usar la opción `-c` para limitar el número de paquetes capturados si solo necesitas una muestra.
- Familiarízate con los diferentes niveles de verbosidad (`-v`, `-vv`, `-vvv`) para obtener más información sobre los paquetes capturados según sea necesario.