# [리눅스] Bash mpstat 사용법

## Overview
El comando `mpstat` es una herramienta de monitoreo de rendimiento en sistemas Linux que forma parte del paquete `sysstat`. Su propósito principal es mostrar estadísticas de uso de CPU en sistemas multiprocesador, permitiendo a los ingenieros y desarrolladores analizar el rendimiento del sistema en tiempo real. `mpstat` proporciona información detallada sobre la carga de trabajo de cada CPU, lo que ayuda a identificar cuellos de botella y optimizar el rendimiento del sistema.

## Usage
La sintaxis básica del comando `mpstat` es la siguiente:

```bash
mpstat [opciones] [intervalo] [número de repeticiones]
```

### Opciones Comunes:
- `-P ALL`: Muestra estadísticas para todas las CPUs. Si no se especifica, solo se muestra la CPU 0.
- `-u`: Muestra el uso de la CPU en porcentaje (esta opción es predeterminada).
- `-h`: Muestra la salida en un formato más legible.
- `-V`: Muestra la versión de `mpstat`.

## Examples
### Ejemplo 1: Monitorear el uso de CPU en tiempo real
Para ver el uso de CPU de todas las CPUs cada 2 segundos, puedes usar el siguiente comando:

```bash
mpstat -P ALL 2
```

Este comando mostrará las estadísticas de uso de CPU para cada procesador en intervalos de 2 segundos.

### Ejemplo 2: Mostrar estadísticas de la CPU 0
Si solo deseas ver las estadísticas de la CPU 0, puedes ejecutar:

```bash
mpstat -P 0 1 5
```

Esto mostrará las estadísticas de la CPU 0 cada segundo durante 5 segundos.

## Tips
- Utiliza la opción `-h` para mejorar la legibilidad de la salida, especialmente si estás analizando datos en un entorno con muchas CPUs.
- Combina `mpstat` con otras herramientas como `grep` o `awk` para filtrar y procesar la salida según tus necesidades específicas.
- Realiza un monitoreo continuo y guarda la salida en un archivo para análisis posterior, utilizando la redirección de salida, por ejemplo:

```bash
mpstat -P ALL 2 > mpstat_output.txt
```

Esto te permitirá revisar el rendimiento de la CPU en un momento posterior.