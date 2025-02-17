# [Linux] Bash groupmod uso: Modificar grupos de usuarios

## Overview
El comando `groupmod` se utiliza en sistemas Linux para modificar las propiedades de un grupo existente. Permite cambiar el nombre del grupo o su identificador (GID), facilitando la administración de grupos de usuarios en el sistema.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
groupmod [opciones] [argumentos]
```

## Common Options
- `-n, --new-name NOMBRE`: Cambia el nombre del grupo a NOMBRE.
- `-g, --gid GID`: Cambia el identificador del grupo a GID.
- `-h, --help`: Muestra la ayuda sobre el comando y sus opciones.
- `-o, --non-unique`: Permite asignar un GID que no sea único.

## Common Examples

1. **Cambiar el nombre de un grupo:**
   Para cambiar el nombre del grupo `viejo_grupo` a `nuevo_grupo`, se utiliza el siguiente comando:
   ```bash
   groupmod -n nuevo_grupo viejo_grupo
   ```

2. **Cambiar el GID de un grupo:**
   Para cambiar el GID del grupo `mi_grupo` a `1050`, se puede usar:
   ```bash
   groupmod -g 1050 mi_grupo
   ```

3. **Cambiar el nombre y el GID de un grupo:**
   Para cambiar tanto el nombre como el GID del grupo `grupo_antiguo` a `grupo_nuevo` con un GID de `2000`:
   ```bash
   groupmod -n grupo_nuevo -g 2000 grupo_antiguo
   ```

## Tips
- Asegúrate de que no haya procesos en ejecución que dependan del grupo que estás modificando, ya que esto podría causar problemas.
- Siempre verifica los cambios con el comando `getent group` para asegurarte de que se han aplicado correctamente.
- Utiliza el comando `man groupmod` para obtener más información sobre las opciones disponibles y su uso.