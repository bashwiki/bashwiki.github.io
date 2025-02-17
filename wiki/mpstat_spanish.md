# [Linux] Bash mpstat Uso: Monitoreo del rendimiento de la CPU

## Overview
El comando `mpstat` se utiliza para mostrar estadísticas de uso de la CPU en sistemas Linux. Permite a los usuarios obtener información detallada sobre la carga de trabajo de cada procesador, lo que es útil para el análisis del rendimiento y la optimización del sistema.

## Usage
La sintaxis básica del comando `mpstat` es la siguiente:

```bash
mpstat [opciones] [intervalo] [número de repeticiones]
```

## Common Options
- `-P ALL`: Muestra estadísticas para todas las CPUs.
- `-u`: Muestra el uso de la CPU en porcentaje.
- `-h`: Muestra la salida en un formato legible (human-readable).
- `-V`: Muestra la versión del comando `mpstat`.

## Common Examples
1. **Mostrar estadísticas de todas las CPUs cada 2 segundos:**
   ```bash
   mpstat -P ALL 2
   ```

2. **Mostrar uso de CPU en porcentaje:**
   ```bash
   mpstat -u 1 5
   ```

3. **Mostrar la versión del comando `mpstat`:**
   ```bash
   mpstat -V
   ```

4. **Mostrar estadísticas de la CPU 0 cada 5 segundos:**
   ```bash
   mpstat -P 0 5
   ```

## Tips
- Utiliza `mpstat` en combinación con otros comandos como `grep` para filtrar resultados específicos.
- Ejecuta `mpstat` con el intervalo y el número de repeticiones adecuados para obtener una visión más clara del rendimiento a lo largo del tiempo.
- Revisa las estadísticas en momentos de alta carga para identificar cuellos de botella en el rendimiento de la CPU.