# [Linux] Bash su: Cambiar de usuario en la terminal

## Overview
El comando `su` (substitute user) se utiliza en sistemas Unix y Linux para cambiar de usuario en la terminal. Permite a un usuario autenticarse como otro usuario, lo que es especialmente útil para realizar tareas administrativas o acceder a cuentas con diferentes permisos.

## Usage
La sintaxis básica del comando `su` es la siguiente:

```
su [opciones] [usuario]
```

Si se omite el nombre de usuario, `su` cambiará al usuario root de forma predeterminada.

## Common Options
- `-l` o `--login`: Inicia una sesión de inicio de sesión como el usuario especificado.
- `-c`: Permite ejecutar un comando específico como el usuario indicado.
- `-s`: Especifica un shell diferente para la sesión.
- `-m` o `-p`: Mantiene el entorno del usuario actual en lugar de cambiarlo al del nuevo usuario.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `su`:

1. **Cambiar al usuario root:**
   ```bash
   su
   ```

2. **Cambiar a un usuario específico:**
   ```bash
   su juan
   ```

3. **Ejecutar un comando como otro usuario:**
   ```bash
   su -c "apt update" juan
   ```

4. **Iniciar una sesión de inicio de sesión como un usuario:**
   ```bash
   su - juan
   ```

5. **Cambiar a un usuario con un shell diferente:**
   ```bash
   su -s /bin/bash juan
   ```

## Tips
- Siempre usa `su` con cuidado, especialmente al cambiar a root, ya que puedes realizar cambios críticos en el sistema.
- Considera usar `sudo` en lugar de `su` para ejecutar comandos específicos con permisos elevados, ya que proporciona un registro de las acciones realizadas.
- Recuerda que necesitarás la contraseña del usuario al que intentas cambiar.