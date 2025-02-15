# [리눅스] Bash mount 사용법

## Overview
El comando `mount` en Bash se utiliza para montar sistemas de archivos en un punto de montaje en el sistema operativo Linux. Su propósito principal es permitir que el sistema operativo acceda a dispositivos de almacenamiento, como discos duros, unidades USB y particiones, integrándolos en el sistema de archivos existente. Esto es esencial para que los usuarios y las aplicaciones puedan leer y escribir datos en estos dispositivos.

## Usage
La sintaxis básica del comando `mount` es la siguiente:

```bash
mount [opciones] dispositivo punto_de_montaje
```

### Opciones Comunes:
- `-t tipo`: Especifica el tipo de sistema de archivos (por ejemplo, `ext4`, `ntfs`, `vfat`, etc.).
- `-o opciones`: Permite especificar opciones adicionales, como `ro` (solo lectura), `rw` (lectura y escritura), entre otras.
- `-a`: Monta todos los sistemas de archivos mencionados en el archivo `/etc/fstab`.
- `-r`: Monta el sistema de archivos en modo solo lectura.

## Examples
### Ejemplo 1: Montar una unidad USB
Para montar una unidad USB con el dispositivo `/dev/sdb1` en el directorio `/mnt/usb`, puedes usar el siguiente comando:

```bash
sudo mount /dev/sdb1 /mnt/usb
```

### Ejemplo 2: Montar un sistema de archivos NTFS
Si deseas montar un sistema de archivos NTFS en modo lectura y escritura, puedes hacerlo especificando el tipo de sistema de archivos:

```bash
sudo mount -t ntfs-3g -o rw /dev/sdc1 /mnt/ntfs
```

## Tips
- Asegúrate de que el punto de montaje (por ejemplo, `/mnt/usb`) exista antes de intentar montar el dispositivo. Puedes crear un directorio usando `mkdir`.
- Para desmontar un sistema de archivos montado, utiliza el comando `umount` seguido del punto de montaje o el dispositivo.
- Verifica los sistemas de archivos montados actualmente con el comando `df -h` o `mount` sin argumentos.
- Siempre es recomendable desmontar un dispositivo antes de desconectarlo físicamente para evitar la pérdida de datos.