# [Linux] Bash vmstat Uso: Monitoreo del rendimiento del sistema

## Overview
El comando `vmstat` (virtual memory statistics) se utiliza para mostrar información sobre el estado de la memoria virtual, procesos, entradas/salidas y el uso de la CPU en un sistema. Es una herramienta útil para diagnosticar problemas de rendimiento y obtener una visión general del estado del sistema.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
vmstat [opciones] [intervalo] [número]
```

## Common Options
- `-a`: Muestra información sobre la memoria activa y la memoria inactiva.
- `-m`: Muestra estadísticas sobre la memoria de las páginas.
- `-s`: Muestra un resumen de las estadísticas de memoria.
- `-d`: Muestra estadísticas de disco.
- `intervalo`: El tiempo en segundos entre cada actualización de la información.
- `número`: El número de actualizaciones que se mostrarán.

## Common Examples
1. **Mostrar estadísticas del sistema cada 2 segundos:**
   ```bash
   vmstat 2
   ```

2. **Mostrar estadísticas de memoria activa e inactiva:**
   ```bash
   vmstat -a
   ```

3. **Mostrar un resumen de las estadísticas de memoria:**
   ```bash
   vmstat -s
   ```

4. **Mostrar estadísticas de disco:**
   ```bash
   vmstat -d
   ```

5. **Mostrar estadísticas cada 5 segundos durante 10 actualizaciones:**
   ```bash
   vmstat 5 10
   ```

## Tips
- Utiliza `vmstat` junto con otros comandos como `top` o `iostat` para obtener un análisis más completo del rendimiento del sistema.
- Observa las métricas de CPU y memoria para identificar cuellos de botella en el rendimiento.
- Es recomendable ejecutar `vmstat` con privilegios de superusuario para obtener información más detallada.