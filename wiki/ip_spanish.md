# [리눅스] Bash ip 사용법

## Overview
El comando `ip` es una herramienta de administración de red en sistemas Linux que permite a los usuarios y administradores gestionar y configurar interfaces de red, rutas y direcciones IP. Es parte del paquete `iproute2`, que reemplaza a las antiguas herramientas de red como `ifconfig` y `route`. Su propósito principal es proporcionar una interfaz unificada y más poderosa para la configuración de la red.

## Usage
La sintaxis básica del comando `ip` es la siguiente:

```
ip [ opciones ] objeto [ subobjeto ] [ acciones ]
```

Donde:
- **opciones**: Son modificadores que alteran el comportamiento del comando.
- **objeto**: Especifica el tipo de recurso de red que se va a gestionar, como `link`, `addr`, `route`, etc.
- **subobjeto**: Especifica un recurso más específico dentro del objeto.
- **acciones**: Especifica la acción que se desea realizar, como `add`, `del`, `show`, etc.

### Comandos Comunes
- `ip link`: Muestra o manipula las interfaces de red.
- `ip addr`: Muestra o manipula las direcciones IP asignadas a las interfaces.
- `ip route`: Muestra o manipula la tabla de rutas.

## Examples
### Ejemplo 1: Mostrar interfaces de red
Para listar todas las interfaces de red disponibles en el sistema, puedes usar el siguiente comando:

```bash
ip link show
```

Este comando mostrará información sobre cada interfaz, incluyendo su estado (up o down) y su dirección MAC.

### Ejemplo 2: Añadir una dirección IP a una interfaz
Para agregar una dirección IP a una interfaz específica, utiliza el siguiente comando:

```bash
ip addr add 192.168.1.10/24 dev eth0
```

Este comando asigna la dirección IP `192.168.1.10` con una máscara de subred de `24` bits a la interfaz `eth0`.

## Tips
- Siempre verifica el estado de tus interfaces de red después de realizar cambios utilizando `ip link show`.
- Usa `ip addr` para asegurarte de que las direcciones IP se han configurado correctamente.
- Recuerda que los cambios realizados con el comando `ip` no son persistentes a menos que se configuren en los archivos de configuración de red del sistema.
- Familiarízate con las opciones de ayuda del comando usando `ip --help` para obtener más información sobre las funcionalidades disponibles.