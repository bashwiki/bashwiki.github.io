# [Linux] Bash last uso: Muestra el historial de sesiones de usuario

## Overview
El comando `last` se utiliza en sistemas Unix y Linux para mostrar un historial de las sesiones de usuario. Este comando lee el archivo de registro `/var/log/wtmp` y presenta información sobre los usuarios que han iniciado sesión, así como las sesiones que han terminado.

## Usage
La sintaxis básica del comando `last` es la siguiente:

```bash
last [opciones] [argumentos]
```

## Common Options
- `-a`: Muestra la dirección IP o el nombre del host del usuario que se ha conectado.
- `-n [número]`: Limita la salida a las últimas `n` entradas.
- `-x`: Muestra las sesiones de inicio y cierre, así como los eventos de apagado y reinicio.
- `-R`: Suprime la impresión de la dirección remota.

## Common Examples
1. **Mostrar el historial completo de sesiones:**
   ```bash
   last
   ```

2. **Limitar la salida a las últimas 10 sesiones:**
   ```bash
   last -n 10
   ```

3. **Mostrar sesiones con dirección IP:**
   ```bash
   last -a
   ```

4. **Incluir eventos de apagado y reinicio:**
   ```bash
   last -x
   ```

5. **Mostrar el historial de un usuario específico:**
   ```bash
   last nombre_usuario
   ```

## Tips
- Utiliza `last -n 5` para ver rápidamente las últimas 5 sesiones sin abrumarte con información.
- Si necesitas información sobre el tiempo de actividad del sistema, combina `last` con `uptime` para obtener un panorama completo.
- Recuerda que el archivo `/var/log/wtmp` puede ser limpiado por el sistema, así que la información puede no ser permanente.