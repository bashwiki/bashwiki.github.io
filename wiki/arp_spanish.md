# [리눅스] Bash arp 사용법

## Overview
El comando `arp` en Bash se utiliza para manipular la tabla ARP (Address Resolution Protocol) de un sistema. Su propósito principal es permitir a los usuarios ver, agregar o eliminar entradas en la tabla ARP, que asocia direcciones IP con direcciones MAC en una red local. Esto es esencial para la comunicación en redes, ya que permite a los dispositivos encontrar la dirección física correspondiente a una dirección IP.

## Usage
La sintaxis básica del comando `arp` es la siguiente:

```bash
arp [opciones] [dirección]
```

### Opciones Comunes:
- `-a`: Muestra la tabla ARP completa en un formato legible.
- `-d dirección`: Elimina la entrada ARP para la dirección especificada.
- `-s dirección dirección_mac`: Agrega una entrada estática a la tabla ARP, asociando una dirección IP con una dirección MAC.

## Examples
### Ejemplo 1: Ver la tabla ARP
Para mostrar todas las entradas en la tabla ARP, puedes usar el siguiente comando:

```bash
arp -a
```

Este comando listará todas las direcciones IP y sus correspondientes direcciones MAC en la red local.

### Ejemplo 2: Agregar una entrada ARP
Si deseas agregar una entrada estática a la tabla ARP, puedes usar el siguiente comando:

```bash
arp -s 192.168.1.10 00:1A:2B:3C:4D:5E
```

Este comando asocia la dirección IP `192.168.1.10` con la dirección MAC `00:1A:2B:3C:4D:5E`.

## Tips
- Asegúrate de tener privilegios de administrador (root) para agregar o eliminar entradas en la tabla ARP.
- Utiliza el comando `arp -a` regularmente para monitorear la tabla ARP y detectar entradas no deseadas o inconsistencias.
- Recuerda que las entradas ARP dinámicas pueden expirar; considera agregar entradas estáticas para dispositivos que necesiten una asociación constante.