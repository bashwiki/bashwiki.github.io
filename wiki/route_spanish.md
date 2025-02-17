# [Linux] Bash route uso equivalente: gestionar tablas de enrutamiento

## Overview
El comando `route` se utiliza para mostrar y manipular la tabla de enrutamiento del kernel de Linux. Permite a los administradores de sistemas gestionar las rutas de red, lo que es fundamental para el funcionamiento de las conexiones de red en un sistema.

## Usage
La sintaxis básica del comando `route` es la siguiente:

```bash
route [options] [arguments]
```

## Common Options
- `-n`: Muestra las direcciones IP en lugar de intentar resolver los nombres de host.
- `add`: Agrega una nueva ruta a la tabla de enrutamiento.
- `del`: Elimina una ruta existente de la tabla de enrutamiento.
- `-e`: Muestra la tabla de enrutamiento de manera detallada.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `route`:

1. **Mostrar la tabla de enrutamiento actual:**
   ```bash
   route -n
   ```

2. **Agregar una nueva ruta:**
   ```bash
   route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.0.1
   ```

3. **Eliminar una ruta existente:**
   ```bash
   route del -net 192.168.1.0 netmask 255.255.255.0
   ```

4. **Mostrar la tabla de enrutamiento con detalles:**
   ```bash
   route -e
   ```

## Tips
- Siempre utiliza la opción `-n` para obtener resultados más rápidos al mostrar la tabla de enrutamiento, ya que evita la resolución de nombres.
- Asegúrate de tener privilegios de administrador (root) para agregar o eliminar rutas.
- Verifica la tabla de enrutamiento después de realizar cambios para asegurarte de que se aplicaron correctamente.