# [리눅스] Bash groupmod 사용법

## Overview
El comando `groupmod` en Bash se utiliza para modificar las propiedades de un grupo existente en un sistema Linux. Su propósito principal es permitir a los administradores del sistema cambiar el nombre de un grupo o su identificador de grupo (GID), así como otras configuraciones relacionadas con el grupo.

## Usage
La sintaxis básica del comando `groupmod` es la siguiente:

```bash
groupmod [opciones] nombre_del_grupo
```

### Opciones Comunes:
- `-n, --new-name NUEVO_NOMBRE`: Cambia el nombre del grupo a `NUEVO_NOMBRE`.
- `-g, --gid NUEVO_GID`: Cambia el GID del grupo a `NUEVO_GID`.
- `-h, --help`: Muestra la ayuda y la lista de opciones disponibles.

## Examples
### Ejemplo 1: Cambiar el nombre de un grupo
Si deseas cambiar el nombre de un grupo llamado `desarrolladores` a `programadores`, puedes usar el siguiente comando:

```bash
groupmod -n programadores desarrolladores
```

### Ejemplo 2: Cambiar el GID de un grupo
Para cambiar el GID del grupo `programadores` a `1001`, el comando sería:

```bash
groupmod -g 1001 programadores
```

## Tips
- Asegúrate de que el nuevo nombre del grupo o el nuevo GID no esté ya en uso para evitar conflictos.
- Es recomendable realizar una copia de seguridad de los archivos de configuración de grupos antes de realizar modificaciones.
- Utiliza el comando `getent group` para verificar los grupos existentes y sus propiedades antes de realizar cambios.