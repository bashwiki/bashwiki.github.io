# [리눅스] Bash fdisk 사용법

## Overview
El comando `fdisk` es una herramienta de línea de comandos utilizada en sistemas Linux y Unix para manipular tablas de particiones en discos duros. Su propósito principal es permitir a los usuarios crear, eliminar, redimensionar y gestionar particiones en dispositivos de almacenamiento. `fdisk` es especialmente útil para la administración de particiones en discos que utilizan el sistema de archivos MBR (Master Boot Record).

## Usage
La sintaxis básica del comando `fdisk` es la siguiente:

```
fdisk [opciones] [dispositivo]
```

Donde `[dispositivo]` es el archivo del dispositivo que se desea modificar (por ejemplo, `/dev/sda`).

### Opciones Comunes
- `-l`: Lista las particiones de todos los discos disponibles.
- `-u`: Muestra el tamaño de las particiones en sectores en lugar de en cilindros.
- `-n`: Crea una nueva partición.
- `-d`: Elimina una partición existente.
- `-t`: Cambia el tipo de sistema de archivos de una partición.

## Examples
### Ejemplo 1: Listar particiones
Para listar todas las particiones en el disco `/dev/sda`, se puede usar el siguiente comando:

```bash
sudo fdisk -l /dev/sda
```

Este comando mostrará información detallada sobre las particiones existentes en el disco especificado.

### Ejemplo 2: Crear una nueva partición
Para crear una nueva partición en `/dev/sda`, primero se inicia `fdisk` con el siguiente comando:

```bash
sudo fdisk /dev/sda
```

Luego, dentro de la interfaz de `fdisk`, se pueden utilizar los siguientes comandos:
1. Presiona `n` para crear una nueva partición.
2. Selecciona el tipo de partición (primaria o extendida).
3. Especifica el número de partición y el tamaño deseado.
4. Finalmente, presiona `w` para escribir los cambios en el disco.

## Tips
- **Realiza copias de seguridad**: Antes de modificar las particiones, es recomendable hacer una copia de seguridad de los datos importantes para evitar pérdidas accidentales.
- **Usa con precaución**: `fdisk` es una herramienta poderosa y puede causar daños en el sistema si se usa incorrectamente. Asegúrate de entender los comandos que estás utilizando.
- **Verifica el dispositivo**: Siempre verifica que estás trabajando en el dispositivo correcto para evitar la modificación accidental de particiones en otros discos.
- **Consulta la documentación**: Utiliza `man fdisk` para acceder a la página del manual y obtener más información sobre las opciones y el uso del comando.