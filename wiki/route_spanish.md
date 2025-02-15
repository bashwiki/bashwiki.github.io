# [리눅스] Bash route 사용법

## Overview
El comando `route` en Bash se utiliza para mostrar y manipular la tabla de enrutamiento del kernel de Linux. Su propósito principal es permitir a los administradores de sistemas y desarrolladores gestionar las rutas de red, lo que es esencial para el enrutamiento de paquetes en una red. A través de este comando, se pueden añadir, eliminar o modificar rutas, facilitando así la configuración de redes complejas.

## Usage
La sintaxis básica del comando `route` es la siguiente:

```bash
route [opciones] [comando] [destino] [puerta de enlace] [más opciones]
```

### Comandos Comunes:
- `add`: Añade una nueva ruta.
- `del`: Elimina una ruta existente.
- `show`: Muestra la tabla de enrutamiento actual.

### Opciones Comunes:
- `-n`: Muestra las direcciones IP en lugar de los nombres de host, lo que puede acelerar la salida.
- `-v`: Muestra información más detallada sobre el comando ejecutado.

## Examples
### Ejemplo 1: Mostrar la tabla de enrutamiento
Para ver la tabla de enrutamiento actual, puedes usar el siguiente comando:

```bash
route -n
```

Este comando mostrará la tabla de enrutamiento sin intentar resolver los nombres de host, lo que resulta en una salida más rápida.

### Ejemplo 2: Añadir una nueva ruta
Si deseas añadir una ruta a una red específica, puedes usar el siguiente comando:

```bash
sudo route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.0.1
```

Este comando añade una ruta para la red `192.168.1.0` con una máscara de red de `255.255.255.0`, utilizando `192.168.0.1` como puerta de enlace.

## Tips
- Asegúrate de tener privilegios de superusuario (root) al añadir o eliminar rutas, ya que estas acciones requieren permisos elevados.
- Utiliza la opción `-n` para evitar la resolución de nombres, especialmente en redes grandes, para mejorar la velocidad de la salida.
- Revisa la tabla de enrutamiento después de realizar cambios para confirmar que se han aplicado correctamente, utilizando `route -n` nuevamente.
- Considera el uso de `ip route` como una alternativa moderna al comando `route`, ya que proporciona más funcionalidades y es el método recomendado en sistemas más recientes.