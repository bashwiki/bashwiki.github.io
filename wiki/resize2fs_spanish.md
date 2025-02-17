# [Linux] Bash resize2fs Uso: Redimensionar sistemas de archivos ext2/ext3/ext4

## Overview
El comando `resize2fs` se utiliza para redimensionar sistemas de archivos ext2, ext3 y ext4. Permite aumentar o disminuir el tamaño de un sistema de archivos, lo que puede ser útil al cambiar el tamaño de las particiones en un disco.

## Usage
La sintaxis básica del comando `resize2fs` es la siguiente:

```bash
resize2fs [opciones] [argumentos]
```

## Common Options
- `-f`: Forzar el redimensionamiento, incluso si el sistema de archivos parece estar dañado.
- `-p`: Mostrar el progreso durante el redimensionamiento.
- `-s`: Redimensionar el sistema de archivos a un tamaño específico.
- `-M`: Reducir el sistema de archivos al tamaño mínimo posible.

## Common Examples
1. **Aumentar el tamaño del sistema de archivos**:
   ```bash
   resize2fs /dev/sda1
   ```
   Este comando ajusta el sistema de archivos en `/dev/sda1` para utilizar todo el espacio disponible en la partición.

2. **Reducir el tamaño del sistema de archivos a un tamaño específico**:
   ```bash
   resize2fs /dev/sda1 20G
   ```
   Aquí, el sistema de archivos en `/dev/sda1` se reduce a 20 gigabytes.

3. **Forzar el redimensionamiento**:
   ```bash
   resize2fs -f /dev/sda1
   ```
   Este comando fuerza el redimensionamiento del sistema de archivos en `/dev/sda1`, incluso si hay errores.

4. **Mostrar el progreso**:
   ```bash
   resize2fs -p /dev/sda1
   ```
   Con esta opción, se mostrará el progreso del redimensionamiento mientras se ejecuta el comando.

## Tips
- **Siempre realiza una copia de seguridad**: Antes de redimensionar un sistema de archivos, asegúrate de tener una copia de seguridad de tus datos.
- **Desmontar el sistema de archivos**: Es recomendable desmontar el sistema de archivos antes de redimensionarlo para evitar daños.
- **Verifica el sistema de archivos**: Utiliza `e2fsck` para verificar y reparar el sistema de archivos antes de redimensionar.