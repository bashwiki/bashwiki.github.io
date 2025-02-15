# [리눅스] Bash iostat 사용법

## Overview
El comando `iostat` es una herramienta de monitoreo del sistema que se utiliza para reportar estadísticas de entrada/salida (I/O) de dispositivos y particiones. Su propósito principal es ayudar a los administradores de sistemas y desarrolladores a evaluar el rendimiento de los dispositivos de almacenamiento y a identificar posibles cuellos de botella en el sistema. `iostat` proporciona información sobre el uso de CPU y las estadísticas de I/O, lo que permite un análisis más profundo del rendimiento del sistema.

## Usage
La sintaxis básica del comando `iostat` es la siguiente:

```bash
iostat [opciones] [intervalo] [número de repeticiones]
```

### Opciones Comunes:
- `-c`: Muestra estadísticas de CPU.
- `-d`: Muestra estadísticas de dispositivos.
- `-x`: Muestra estadísticas extendidas de dispositivos.
- `-h`: Muestra las estadísticas en un formato legible (human-readable).
- `-p`: Muestra estadísticas de particiones (por ejemplo, `-p ALL` para todas las particiones).

## Examples
### Ejemplo 1: Monitorear estadísticas de CPU y dispositivos
Para obtener un informe de estadísticas de CPU y dispositivos cada 5 segundos, puedes usar el siguiente comando:

```bash
iostat -c -d 5
```

Este comando mostrará las estadísticas de CPU y de dispositivos de almacenamiento cada 5 segundos.

### Ejemplo 2: Estadísticas extendidas de dispositivos
Si deseas ver estadísticas extendidas de I/O para todos los dispositivos, puedes ejecutar:

```bash
iostat -x -h 2 3
```

Este comando mostrará estadísticas extendidas en un formato legible cada 2 segundos, repitiéndose 3 veces.

## Tips
- Utiliza la opción `-h` para facilitar la lectura de las estadísticas, especialmente en sistemas con grandes volúmenes de datos.
- Combina `iostat` con otras herramientas como `vmstat` y `mpstat` para obtener una visión más completa del rendimiento del sistema.
- Si estás analizando un problema de rendimiento, toma nota de las estadísticas en momentos de alta carga para identificar patrones o anomalías.
- Considera redirigir la salida a un archivo para un análisis posterior, utilizando la sintaxis `iostat -x -h 2 3 > salida.txt`. 

Con estas herramientas y ejemplos, podrás utilizar `iostat` de manera efectiva para monitorear y optimizar el rendimiento de tu sistema.