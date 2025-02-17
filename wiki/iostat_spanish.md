# [Linux] Bash iostat Uso: Monitoreo del rendimiento de entrada/salida

## Overview
El comando `iostat` se utiliza para monitorear el rendimiento de entrada/salida de los dispositivos de almacenamiento y del sistema en general. Proporciona estadísticas sobre la utilización de la CPU y la actividad de los dispositivos de bloque, lo que ayuda a identificar cuellos de botella en el rendimiento.

## Usage
La sintaxis básica del comando `iostat` es la siguiente:

```bash
iostat [opciones] [intervalo] [número de informes]
```

## Common Options
- `-c`: Muestra estadísticas de la CPU.
- `-d`: Muestra estadísticas de los dispositivos de bloque.
- `-x`: Muestra estadísticas extendidas de los dispositivos.
- `-h`: Muestra los resultados en un formato legible (con unidades).
- `-p`: Muestra estadísticas para particiones específicas.

## Common Examples

1. **Mostrar estadísticas de CPU y dispositivos:**
   ```bash
   iostat
   ```

2. **Mostrar estadísticas de CPU cada 5 segundos:**
   ```bash
   iostat -c 5
   ```

3. **Mostrar estadísticas de dispositivos de bloque:**
   ```bash
   iostat -d
   ```

4. **Mostrar estadísticas extendidas de dispositivos:**
   ```bash
   iostat -x 2 3
   ```

5. **Mostrar estadísticas con formato legible:**
   ```bash
   iostat -h
   ```

## Tips
- Utiliza `iostat` junto con otros comandos como `vmstat` y `mpstat` para obtener una visión más completa del rendimiento del sistema.
- Monitorea el rendimiento durante períodos de alta carga para identificar problemas potenciales.
- Considera redirigir la salida a un archivo para análisis posterior, usando `iostat > salida.txt`.