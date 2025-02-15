# [리눅스] Bash free 사용법

## Overview
El comando `free` en Bash se utiliza para mostrar la cantidad de memoria libre y utilizada en el sistema. Su propósito principal es proporcionar una visión general del uso de la memoria en el sistema, incluyendo la memoria física, la memoria de intercambio (swap) y la memoria total disponible. Esto es especialmente útil para ingenieros y desarrolladores que necesitan monitorear el rendimiento del sistema y optimizar el uso de recursos.

## Usage
La sintaxis básica del comando `free` es la siguiente:

```
free [opciones]
```

### Opciones Comunes:
- `-h`: Muestra los valores en un formato legible para humanos (por ejemplo, en KB, MB o GB).
- `-m`: Muestra la memoria en megabytes.
- `-g`: Muestra la memoria en gigabytes.
- `-s <segundos>`: Actualiza la salida cada <segundos> especificados.
- `-t`: Muestra la memoria total, incluyendo la memoria utilizada y libre.

## Examples
### Ejemplo 1: Uso básico
Para ver la memoria utilizada y libre en un formato legible para humanos, puedes usar el siguiente comando:

```bash
free -h
```

Este comando mostrará la memoria total, utilizada, libre, compartida, en caché y la memoria de intercambio de manera clara y comprensible.

### Ejemplo 2: Actualización periódica
Si deseas monitorear el uso de la memoria en tiempo real, puedes utilizar la opción `-s` para actualizar la salida cada 5 segundos:

```bash
free -h -s 5
```

Esto te permitirá observar cómo cambia el uso de la memoria a lo largo del tiempo.

## Tips
- Utiliza la opción `-h` para facilitar la lectura de los datos, especialmente en sistemas con grandes cantidades de memoria.
- Combina `free` con otros comandos como `watch` para obtener actualizaciones en tiempo real de manera más visual. Por ejemplo:

```bash
watch free -h
```

- Recuerda que el uso de memoria puede variar dependiendo de las aplicaciones en ejecución, así que es útil ejecutar `free` en diferentes momentos para obtener una visión más completa del rendimiento del sistema.