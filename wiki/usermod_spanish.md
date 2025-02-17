# [Linux] Bash usermod uso: Modificar cuentas de usuario en el sistema

## Overview
El comando `usermod` se utiliza para modificar las propiedades de una cuenta de usuario existente en un sistema Linux. Permite cambiar atributos como el nombre de usuario, el grupo principal, el directorio personal y más.

## Usage
La sintaxis básica del comando `usermod` es la siguiente:

```bash
usermod [opciones] [argumentos]
```

## Common Options
- `-l`: Cambia el nombre de usuario.
- `-d`: Cambia el directorio personal del usuario.
- `-m`: Mueve el contenido del directorio personal a la nueva ubicación.
- `-g`: Cambia el grupo principal del usuario.
- `-aG`: Añade el usuario a uno o más grupos secundarios.
- `-s`: Cambia el intérprete de comandos predeterminado del usuario.

## Common Examples
1. **Cambiar el nombre de usuario:**
   ```bash
   usermod -l nuevo_nombre viejo_nombre
   ```

2. **Cambiar el directorio personal:**
   ```bash
   usermod -d /nuevo/directorio viejo_nombre
   ```

3. **Mover el contenido del directorio personal:**
   ```bash
   usermod -d /nuevo/directorio -m viejo_nombre
   ```

4. **Cambiar el grupo principal:**
   ```bash
   usermod -g nuevo_grupo nombre_usuario
   ```

5. **Añadir un usuario a un grupo secundario:**
   ```bash
   usermod -aG grupo_secundario nombre_usuario
   ```

6. **Cambiar el intérprete de comandos:**
   ```bash
   usermod -s /bin/bash nombre_usuario
   ```

## Tips
- Siempre verifica que el nuevo nombre de usuario o directorio personal no esté en uso antes de realizar cambios.
- Utiliza `usermod` con precaución, ya que algunos cambios pueden afectar el acceso del usuario al sistema.
- Es recomendable realizar una copia de seguridad de los datos del usuario antes de modificar su cuenta.