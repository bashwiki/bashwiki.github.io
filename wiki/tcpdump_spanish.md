# [Linux] Bash tcpdump uso: Captura de paquetes de red

## Overview
El comando `tcpdump` es una herramienta de línea de comandos utilizada para capturar y analizar el tráfico de red que pasa a través de una interfaz de red específica. Es especialmente útil para la depuración de problemas de red y el análisis de seguridad.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
tcpdump [opciones] [argumentos]
```

## Common Options
- `-i <interfaz>`: Especifica la interfaz de red a utilizar para la captura.
- `-n`: No resuelve direcciones IP a nombres de host.
- `-c <número>`: Captura solo un número específico de paquetes.
- `-w <archivo>`: Escribe la salida de la captura en un archivo en lugar de mostrarla en la pantalla.
- `-r <archivo>`: Lee paquetes de un archivo en lugar de capturarlos en tiempo real.

## Common Examples
A continuación, se presentan algunos ejemplos prácticos del uso de `tcpdump`:

1. Capturar paquetes en la interfaz `eth0`:
   ```bash
   tcpdump -i eth0
   ```

2. Capturar solo 10 paquetes y no resolver nombres de host:
   ```bash
   tcpdump -i eth0 -n -c 10
   ```

3. Guardar la captura de paquetes en un archivo llamado `captura.pcap`:
   ```bash
   tcpdump -i eth0 -w captura.pcap
   ```

4. Leer paquetes desde un archivo de captura:
   ```bash
   tcpdump -r captura.pcap
   ```

5. Filtrar tráfico HTTP (puerto 80):
   ```bash
   tcpdump -i eth0 port 80
   ```

## Tips
- Asegúrate de tener permisos adecuados (puedes necesitar ejecutar `tcpdump` como superusuario).
- Usa la opción `-n` para evitar la resolución de nombres, lo que puede hacer que la captura sea más rápida.
- Filtra el tráfico para capturar solo lo que necesitas, lo que facilita el análisis posterior.
- Considera usar `-w` para guardar la captura y analizarla más tarde con herramientas como Wireshark.