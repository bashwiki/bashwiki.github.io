# [Linux] Bash time uso: Mide el tiempo de ejecución de comandos

## Overview
El comando `time` en Bash se utiliza para medir el tiempo que tarda en ejecutarse un comando específico. Proporciona información sobre el tiempo real, el tiempo de CPU y el tiempo de sistema, lo que puede ser útil para optimizar scripts y procesos.

## Usage
La sintaxis básica del comando `time` es la siguiente:

```bash
time [opciones] [argumentos]
```

## Common Options
- `-p`: Muestra el tiempo en un formato más legible.
- `-o archivo`: Guarda la salida del tiempo en un archivo especificado.
- `-v`: Muestra información detallada sobre el tiempo de ejecución.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `time`:

1. Medir el tiempo de ejecución de un comando simple:
   ```bash
   time ls -l
   ```

2. Guardar la salida del tiempo en un archivo:
   ```bash
   time -o tiempo.txt sleep 2
   ```

3. Usar la opción de formato legible:
   ```bash
   time -p sleep 3
   ```

4. Obtener información detallada sobre el tiempo de ejecución:
   ```bash
   time -v find / -name "*.txt"
   ```

## Tips
- Utiliza `time` para identificar cuellos de botella en tus scripts y optimizar su rendimiento.
- Recuerda que el tiempo de ejecución puede variar según la carga del sistema y otros procesos en ejecución.
- Experimenta con diferentes opciones para obtener la información que mejor se adapte a tus necesidades.