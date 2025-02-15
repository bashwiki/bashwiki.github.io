# [리눅스] Bash usermod 사용법

## Overview
El comando `usermod` en Bash se utiliza para modificar cuentas de usuario en sistemas Linux. Su propósito principal es permitir a los administradores del sistema realizar cambios en las configuraciones de los usuarios, como agregar o eliminar grupos, cambiar el nombre de usuario, modificar el directorio de inicio, entre otros.

## Usage
La sintaxis básica del comando `usermod` es la siguiente:

```bash
usermod [opciones] nombre_usuario
```

### Opciones Comunes
- `-aG grupo`: Agrega el usuario a un grupo adicional sin eliminarlo de otros grupos.
- `-d directorio`: Cambia el directorio de inicio del usuario.
- `-l nuevo_nombre`: Cambia el nombre de usuario a uno nuevo.
- `-s shell`: Cambia la shell predeterminada del usuario.
- `-e fecha`: Establece la fecha de expiración de la cuenta del usuario.

## Examples
### Ejemplo 1: Agregar un usuario a un grupo
Para agregar un usuario llamado `juan` al grupo `desarrolladores`, puedes usar el siguiente comando:

```bash
usermod -aG desarrolladores juan
```

### Ejemplo 2: Cambiar el nombre de usuario
Si deseas cambiar el nombre de usuario de `maria` a `maria_nueva`, puedes hacerlo con el siguiente comando:

```bash
usermod -l maria_nueva maria
```

## Tips
- Siempre realiza una copia de seguridad de los archivos de configuración antes de modificar cuentas de usuario.
- Asegúrate de que el usuario no esté conectado cuando realices cambios en su cuenta.
- Utiliza el comando `id nombre_usuario` para verificar los grupos y permisos del usuario después de realizar cambios.