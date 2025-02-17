# [Linux] Bash tune2fs uso: Modificar parámetros de sistemas de archivos ext2/ext3/ext4

## Overview
El comando `tune2fs` se utiliza para ajustar y modificar parámetros de sistemas de archivos ext2, ext3 y ext4 en Linux. Permite a los administradores de sistemas optimizar el rendimiento y la funcionalidad del sistema de archivos, así como realizar tareas de mantenimiento.

## Usage
La sintaxis básica del comando `tune2fs` es la siguiente:

```bash
tune2fs [opciones] [argumentos]
```

## Common Options
- `-c <número>`: Establece el número máximo de montajes antes de que se realice una verificación del sistema de archivos.
- `-i <intervalo>`: Define el intervalo de tiempo entre verificaciones del sistema de archivos.
- `-m <porcentaje>`: Establece el porcentaje de espacio reservado para el usuario root.
- `-O <opciones>`: Activa características específicas del sistema de archivos.
- `-L <etiqueta>`: Cambia la etiqueta del sistema de archivos.
- `-E <opciones>`: Establece opciones adicionales específicas del sistema de archivos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `tune2fs`:

1. **Establecer el número máximo de montajes**:
   ```bash
   tune2fs -c 30 /dev/sda1
   ```

2. **Definir el intervalo de tiempo entre verificaciones**:
   ```bash
   tune2fs -i 2w /dev/sda1
   ```

3. **Reservar un porcentaje de espacio para el usuario root**:
   ```bash
   tune2fs -m 5 /dev/sda1
   ```

4. **Activar la característica de journaling**:
   ```bash
   tune2fs -O has_journal /dev/sda1
   ```

5. **Cambiar la etiqueta del sistema de archivos**:
   ```bash
   tune2fs -L "MiEtiqueta" /dev/sda1
   ```

## Tips
- Siempre realiza una copia de seguridad de tus datos antes de modificar parámetros del sistema de archivos.
- Utiliza el comando `dumpe2fs` para obtener información detallada sobre el sistema de archivos antes de realizar cambios.
- Asegúrate de que el sistema de archivos no esté montado o esté en modo de solo lectura al usar `tune2fs` para evitar daños.