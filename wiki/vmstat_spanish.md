# [리눅스] Bash vmstat 사용법

## Overview
El comando `vmstat` (Virtual Memory Statistics) se utiliza en sistemas Unix y Linux para reportar información sobre la memoria virtual, procesos, paginación, bloqueos de E/S y el uso de la CPU. Su propósito principal es proporcionar una visión general del rendimiento del sistema, lo que permite a los ingenieros y desarrolladores identificar cuellos de botella y problemas de rendimiento en tiempo real.

## Usage
La sintaxis básica del comando `vmstat` es la siguiente:

```bash
vmstat [opciones] [intervalo] [número]
```

### Opciones Comunes:
- `-a`: Muestra información sobre la memoria activa y inactiva.
- `-m`: Muestra estadísticas sobre la memoria de páginas.
- `-s`: Muestra un resumen de las estadísticas de memoria.
- `intervalo`: Especifica el tiempo en segundos entre cada actualización de la salida.
- `número`: Especifica cuántas veces se debe mostrar la salida.

## Examples
### Ejemplo 1: Monitorear el rendimiento del sistema
Para monitorear el rendimiento del sistema cada 5 segundos, puedes usar el siguiente comando:

```bash
vmstat 5
```

Este comando mostrará estadísticas del sistema cada 5 segundos hasta que se interrumpa.

### Ejemplo 2: Resumen de estadísticas de memoria
Para obtener un resumen de las estadísticas de memoria, puedes ejecutar:

```bash
vmstat -s
```

Este comando proporcionará un resumen detallado de la memoria, incluyendo la cantidad total de memoria, la memoria libre y la memoria utilizada.

## Tips
- Utiliza `vmstat` en combinación con otros comandos como `top` o `iostat` para obtener una visión más completa del rendimiento del sistema.
- Observa las métricas de CPU y memoria a lo largo del tiempo para identificar patrones o problemas recurrentes.
- Si estás monitoreando un sistema en producción, considera redirigir la salida a un archivo para su análisis posterior:

```bash
vmstat 5 > vmstat_output.txt
```

Esto te permitirá revisar los datos más tarde sin perder información valiosa.