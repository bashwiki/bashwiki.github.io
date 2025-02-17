# [Linux] Bash df Uso: Muestra el uso del espacio en disco

## Overview
El comando `df` en Bash se utiliza para mostrar información sobre el uso del espacio en disco de los sistemas de archivos montados. Proporciona detalles como el tamaño total, el espacio utilizado y el espacio disponible en cada sistema de archivos.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
df [opciones] [argumentos]
```

## Common Options
- `-h`: Muestra los tamaños en un formato legible para humanos (por ejemplo, en KB, MB, GB).
- `-T`: Muestra el tipo de sistema de archivos.
- `-a`: Incluye sistemas de archivos que tienen un tamaño de 0.
- `-i`: Muestra información sobre inodos en lugar de bloques de disco.

## Common Examples
- Para mostrar el uso del espacio en disco en un formato legible para humanos:

```bash
df -h
```

- Para mostrar el tipo de sistema de archivos junto con el uso del espacio:

```bash
df -hT
```

- Para incluir todos los sistemas de archivos, incluso aquellos con tamaño 0:

```bash
df -a
```

- Para ver la información de inodos:

```bash
df -i
```

## Tips
- Utiliza la opción `-h` para facilitar la lectura de los datos, especialmente en sistemas con grandes volúmenes de datos.
- Revisa regularmente el uso del espacio en disco para evitar problemas de almacenamiento.
- Combina `df` con otros comandos como `grep` para filtrar resultados específicos, por ejemplo, para ver solo el uso de un sistema de archivos particular:

```bash
df -h | grep /dev/sda1
```