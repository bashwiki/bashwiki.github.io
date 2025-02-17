# [Linux] Bash fdisk Uso: Herramienta para gestionar particiones de disco

## Overview
El comando `fdisk` es una herramienta de línea de comandos utilizada para crear, eliminar y gestionar particiones en discos duros. Es especialmente útil en sistemas Linux para manipular las tablas de particiones de dispositivos de almacenamiento.

## Usage
La sintaxis básica del comando `fdisk` es la siguiente:

```bash
fdisk [opciones] [dispositivo]
```

Donde `[dispositivo]` es el nombre del dispositivo que deseas gestionar, como `/dev/sda`.

## Common Options
- `-l`: Lista todas las particiones de los dispositivos.
- `-u`: Muestra el tamaño de las particiones en sectores.
- `-n`: Crea una nueva partición.
- `-d`: Elimina una partición existente.
- `-t`: Cambia el tipo de una partición.

## Common Examples
1. **Listar particiones de un disco**:
   ```bash
   fdisk -l /dev/sda
   ```

2. **Crear una nueva partición**:
   ```bash
   fdisk /dev/sda
   ```
   Luego, dentro de la interfaz de `fdisk`, usa el comando `n` para crear una nueva partición.

3. **Eliminar una partición**:
   ```bash
   fdisk /dev/sda
   ```
   Dentro de `fdisk`, usa el comando `d` y selecciona el número de la partición que deseas eliminar.

4. **Cambiar el tipo de una partición**:
   ```bash
   fdisk /dev/sda
   ```
   Dentro de `fdisk`, usa el comando `t` y especifica el número de la partición y el nuevo tipo.

## Tips
- Siempre realiza una copia de seguridad de tus datos antes de modificar particiones.
- Utiliza `parted` o `gparted` si prefieres una interfaz gráfica para gestionar particiones.
- Asegúrate de desmontar cualquier partición que vayas a modificar para evitar problemas de datos.