# [Linux] Bash mount uso: Montar sistemas de archivos

## Overview
El comando `mount` en Bash se utiliza para montar sistemas de archivos en un directorio específico del sistema. Esto permite acceder a dispositivos de almacenamiento, como discos duros, unidades USB y particiones, integrándolos en el sistema de archivos del sistema operativo.

## Usage
La sintaxis básica del comando `mount` es la siguiente:

```bash
mount [opciones] [dispositivo] [punto_de_montaje]
```

## Common Options
- `-t tipo`: Especifica el tipo de sistema de archivos (por ejemplo, `ext4`, `ntfs`).
- `-o opciones`: Permite establecer opciones adicionales como `ro` (solo lectura) o `rw` (lectura y escritura).
- `-a`: Monta todos los sistemas de archivos especificados en `/etc/fstab`.
- `-r`: Monta el sistema de archivos en modo solo lectura.

## Common Examples
1. **Montar un dispositivo USB**:
   ```bash
   mount /dev/sdb1 /mnt/usb
   ```

2. **Montar un sistema de archivos NTFS**:
   ```bash
   mount -t ntfs-3g /dev/sdc1 /mnt/ntfs
   ```

3. **Montar un sistema de archivos en modo solo lectura**:
   ```bash
   mount -o ro /dev/sda1 /mnt/readonly
   ```

4. **Montar todos los sistemas de archivos de /etc/fstab**:
   ```bash
   mount -a
   ```

## Tips
- Asegúrate de que el punto de montaje exista antes de intentar montar un dispositivo.
- Utiliza el comando `umount` para desmontar un sistema de archivos cuando ya no lo necesites.
- Verifica los sistemas de archivos montados con el comando `df -h` para asegurarte de que se montaron correctamente.