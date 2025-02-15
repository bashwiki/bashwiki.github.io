# [리눅스] Bash tune2fs 사용법

## Overview
El comando `tune2fs` es una herramienta utilizada en sistemas Linux para ajustar y modificar parámetros de sistemas de archivos ext2, ext3 y ext4. Su propósito principal es permitir a los administradores de sistemas y desarrolladores optimizar el rendimiento y la configuración de estos sistemas de archivos, así como realizar tareas de mantenimiento y recuperación.

## Usage
La sintaxis básica del comando `tune2fs` es la siguiente:

```bash
tune2fs [opciones] dispositivo
```

Donde `dispositivo` es el nombre del dispositivo que contiene el sistema de archivos que se desea modificar. Algunas de las opciones más comunes incluyen:

- `-c <número>`: Establece el número máximo de montajes antes de que el sistema de archivos sea revisado.
- `-i <tiempo>`: Establece el intervalo de tiempo entre revisiones del sistema de archivos.
- `-m <porcentaje>`: Establece el porcentaje de espacio reservado para el usuario root.
- `-O <opciones>`: Habilita características específicas en el sistema de archivos.
- `-L <etiqueta>`: Cambia la etiqueta del sistema de archivos.

## Examples
### Ejemplo 1: Establecer el número máximo de montajes
Para establecer el número máximo de montajes en 20 para un sistema de archivos en `/dev/sda1`, se puede usar el siguiente comando:

```bash
sudo tune2fs -c 20 /dev/sda1
```

### Ejemplo 2: Cambiar la etiqueta del sistema de archivos
Para cambiar la etiqueta del sistema de archivos en `/dev/sda1` a "MiSistema", se utilizaría el siguiente comando:

```bash
sudo tune2fs -L MiSistema /dev/sda1
```

## Tips
- **Realiza copias de seguridad**: Antes de realizar cambios significativos en un sistema de archivos, siempre es recomendable hacer una copia de seguridad de los datos importantes.
- **Verifica el sistema de archivos**: Utiliza `fsck` para verificar la integridad del sistema de archivos antes y después de usar `tune2fs`.
- **Consulta la documentación**: Para obtener más información sobre las opciones disponibles, consulta la página de manual de `tune2fs` ejecutando `man tune2fs` en la terminal.