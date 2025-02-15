# [리눅스] Bash df 사용법

## Overview
El comando `df` (disk free) se utiliza en sistemas Unix y Linux para mostrar información sobre el espacio en disco disponible en los sistemas de archivos montados. Su propósito principal es ayudar a los usuarios a monitorizar el uso del espacio en disco, permitiendo identificar cuánto espacio está ocupado y cuánto está disponible en cada sistema de archivos.

## Usage
La sintaxis básica del comando `df` es la siguiente:

```
df [opciones] [archivo]
```

### Opciones Comunes:
- `-h`: Muestra el tamaño en un formato legible para humanos (por ejemplo, en KB, MB o GB).
- `-T`: Muestra el tipo de sistema de archivos.
- `-a`: Incluye sistemas de archivos que tienen un tamaño de 0.
- `-i`: Muestra información sobre inodos en lugar de espacio en disco.

## Examples
Aquí hay un par de ejemplos prácticos de cómo usar el comando `df`.

1. **Mostrar el espacio en disco en un formato legible para humanos**:
   ```bash
   df -h
   ```
   Este comando mostrará el espacio en disco disponible y utilizado en todos los sistemas de archivos montados, utilizando unidades que son fáciles de entender.

2. **Mostrar información sobre inodos**:
   ```bash
   df -i
   ```
   Este comando proporciona un resumen del uso de inodos en los sistemas de archivos montados, lo cual es útil para entender la cantidad de archivos que se pueden crear en un sistema.

## Tips
- Utiliza la opción `-h` para facilitar la lectura de los resultados, especialmente en sistemas con grandes volúmenes de datos.
- Combinando `df` con `grep`, puedes filtrar la salida para buscar un sistema de archivos específico. Por ejemplo:
  ```bash
  df -h | grep /dev/sda1
  ```
- Es recomendable ejecutar `df` regularmente como parte de las tareas de mantenimiento del sistema para evitar problemas de espacio en disco que puedan afectar el rendimiento o la funcionalidad del sistema.