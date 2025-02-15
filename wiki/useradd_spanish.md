# [리눅스] Bash useradd 사용법

## Overview
El comando `useradd` en Bash se utiliza para crear nuevas cuentas de usuario en un sistema Linux. Su propósito principal es permitir a los administradores del sistema agregar usuarios al sistema, configurando sus propiedades básicas como el nombre de usuario, el directorio personal y el grupo al que pertenecen.

## Usage
La sintaxis básica del comando `useradd` es la siguiente:

```bash
useradd [opciones] nombre_usuario
```

### Opciones Comunes:
- `-m`: Crea el directorio personal del usuario si no existe.
- `-s`: Especifica el intérprete de comandos (shell) que se asignará al usuario.
- `-G`: Agrega el usuario a uno o más grupos adicionales.
- `-d`: Especifica el directorio personal del usuario.
- `-e`: Establece la fecha de expiración de la cuenta del usuario.

## Examples
### Ejemplo 1: Crear un usuario básico
Para crear un usuario llamado "juan" con un directorio personal y el shell por defecto, se puede usar el siguiente comando:

```bash
useradd -m juan
```

### Ejemplo 2: Crear un usuario con opciones específicas
Si deseas crear un usuario llamado "maria", asignarle un directorio personal específico y un shell diferente, puedes usar:

```bash
useradd -m -d /home/maria -s /bin/bash maria
```

## Tips
- Siempre verifica si el nombre de usuario que deseas crear ya está en uso para evitar conflictos.
- Considera usar la opción `-G` para agregar el usuario a grupos relevantes, lo que puede facilitar la gestión de permisos.
- Después de crear un usuario, es recomendable establecer una contraseña utilizando el comando `passwd nombre_usuario`.
- Revisa los archivos de configuración de usuarios, como `/etc/passwd` y `/etc/shadow`, para asegurarte de que la cuenta se haya creado correctamente.