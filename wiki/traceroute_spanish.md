# [Linux] Bash traceroute uso: Muestra la ruta que toman los paquetes a un destino

## Overview
El comando `traceroute` se utiliza para rastrear la ruta que siguen los paquetes de datos desde el origen hasta un destino específico en una red. Este comando proporciona información sobre cada salto intermedio, lo que puede ser útil para diagnosticar problemas de conectividad y latencia en la red.

## Usage
La sintaxis básica del comando `traceroute` es la siguiente:

```bash
traceroute [opciones] [destino]
```

## Common Options
- `-m <n>`: Establece el número máximo de saltos que se intentarán.
- `-p <puerto>`: Especifica el puerto de destino a utilizar.
- `-w <n>`: Define el tiempo de espera en segundos para cada respuesta.
- `-n`: Muestra las direcciones IP en lugar de intentar resolver los nombres de host.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `traceroute`:

1. Rastrear la ruta a un sitio web:
   ```bash
   traceroute www.ejemplo.com
   ```

2. Rastrear la ruta a una dirección IP específica:
   ```bash
   traceroute 192.168.1.1
   ```

3. Establecer un número máximo de saltos:
   ```bash
   traceroute -m 15 www.ejemplo.com
   ```

4. Usar un puerto específico:
   ```bash
   traceroute -p 80 www.ejemplo.com
   ```

5. Mostrar direcciones IP sin resolver nombres de host:
   ```bash
   traceroute -n www.ejemplo.com
   ```

## Tips
- Utiliza el flag `-n` si deseas obtener resultados más rápidos al evitar la resolución de nombres de host.
- Si estás experimentando problemas de conectividad, observa los saltos donde el tiempo de respuesta se incrementa significativamente; esto puede indicar un punto de congestión.
- Recuerda que algunos routers pueden estar configurados para no responder a las solicitudes de `traceroute`, lo que puede resultar en saltos que no muestran información completa.