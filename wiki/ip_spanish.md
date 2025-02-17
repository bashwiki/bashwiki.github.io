# [Linux] Bash ip uso: [gestionar redes y direcciones IP]

## Overview
El comando `ip` es una herramienta poderosa utilizada en sistemas Linux para gestionar y configurar redes y direcciones IP. Permite a los usuarios realizar diversas tareas relacionadas con la red, como la visualización y modificación de la configuración de interfaces de red, rutas y direcciones.

## Usage
La sintaxis básica del comando `ip` es la siguiente:

```bash
ip [opciones] [argumentos]
```

## Common Options
Aquí hay algunas opciones comunes que se pueden usar con el comando `ip`:

- `link`: Muestra o manipula interfaces de red.
- `addr`: Muestra o manipula direcciones IP.
- `route`: Muestra o manipula la tabla de rutas.
- `neigh`: Muestra o manipula la tabla de vecinos (ARP).

## Common Examples
A continuación, se presentan algunos ejemplos prácticos del uso del comando `ip`:

1. **Mostrar todas las interfaces de red:**
   ```bash
   ip link show
   ```

2. **Mostrar direcciones IP asignadas a las interfaces:**
   ```bash
   ip addr show
   ```

3. **Agregar una dirección IP a una interfaz:**
   ```bash
   ip addr add 192.168.1.10/24 dev eth0
   ```

4. **Eliminar una dirección IP de una interfaz:**
   ```bash
   ip addr del 192.168.1.10/24 dev eth0
   ```

5. **Mostrar la tabla de rutas:**
   ```bash
   ip route show
   ```

6. **Agregar una ruta estática:**
   ```bash
   ip route add 10.0.0.0/24 via 192.168.1.1
   ```

## Tips
- Siempre verifica la configuración de red después de realizar cambios usando `ip addr show` o `ip route show`.
- Utiliza `ip -h` para obtener ayuda sobre las opciones disponibles.
- Asegúrate de tener privilegios de superusuario (root) para realizar cambios en la configuración de red.