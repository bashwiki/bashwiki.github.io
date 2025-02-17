# [Linux] Bash ethtool Uso: Herramienta para gestionar interfaces de red

## Overview
El comando `ethtool` se utiliza para consultar y modificar las configuraciones de las interfaces de red Ethernet en sistemas Linux. Permite obtener información detallada sobre la conexión de red, así como ajustar parámetros como la velocidad, el modo dúplex y otras características del hardware de red.

## Usage
La sintaxis básica del comando `ethtool` es la siguiente:

```bash
ethtool [opciones] [argumentos]
```

## Common Options
- `-s`: Cambia la configuración de la interfaz de red.
- `-i`: Muestra información del controlador de la interfaz.
- `-p`: Parpadea el LED de la interfaz para identificarla.
- `-a`: Muestra las estadísticas de la interfaz.
- `-S`: Muestra estadísticas extendidas de la interfaz.

## Common Examples
- **Consultar información básica de una interfaz de red:**
  ```bash
  ethtool eth0
  ```

- **Ver el controlador de la interfaz:**
  ```bash
  ethtool -i eth0
  ```

- **Cambiar la velocidad y modo dúplex de la interfaz:**
  ```bash
  ethtool -s eth0 speed 100 duplex full
  ```

- **Parpadear el LED de la interfaz para identificarla:**
  ```bash
  ethtool -p eth0
  ```

- **Mostrar estadísticas extendidas de la interfaz:**
  ```bash
  ethtool -S eth0
  ```

## Tips
- Asegúrate de tener privilegios de superusuario (root) para realizar cambios en la configuración de la interfaz.
- Utiliza `ethtool` junto con otros comandos como `ifconfig` o `ip` para obtener una visión más completa de la configuración de red.
- Revisa la documentación de `ethtool` con `man ethtool` para explorar más opciones y configuraciones avanzadas.