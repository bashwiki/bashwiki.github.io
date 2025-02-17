# [Linux] Bash uname Uso: Muestra información del sistema

## Overview
El comando `uname` se utiliza en sistemas Unix y Linux para mostrar información sobre el sistema operativo y el hardware en el que se está ejecutando. Es una herramienta útil para obtener detalles sobre la versión del kernel, el nombre del sistema y otros aspectos relevantes del entorno.

## Usage
La sintaxis básica del comando `uname` es la siguiente:

```bash
uname [opciones] [argumentos]
```

## Common Options
A continuación se presentan algunas de las opciones más comunes que se pueden utilizar con el comando `uname`:

- `-a`: Muestra toda la información disponible del sistema.
- `-s`: Muestra el nombre del sistema operativo.
- `-n`: Muestra el nombre del nodo de red.
- `-r`: Muestra la versión del kernel.
- `-v`: Muestra la fecha de compilación del kernel.
- `-m`: Muestra la arquitectura de la máquina.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `uname`:

1. **Mostrar toda la información del sistema:**

   ```bash
   uname -a
   ```

2. **Mostrar solo el nombre del sistema operativo:**

   ```bash
   uname -s
   ```

3. **Mostrar la versión del kernel:**

   ```bash
   uname -r
   ```

4. **Mostrar la arquitectura de la máquina:**

   ```bash
   uname -m
   ```

5. **Mostrar el nombre del nodo de red:**

   ```bash
   uname -n
   ```

## Tips
- Utiliza `uname -a` para obtener un resumen completo de la información del sistema en una sola línea.
- Combina `uname` con otros comandos como `grep` para filtrar información específica.
- Recuerda que algunas opciones pueden no estar disponibles en todos los sistemas, así que verifica la documentación de tu sistema si encuentras algún problema.