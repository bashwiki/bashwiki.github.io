# [Linux] Bash passwd uso: Cambiar contraseñas de usuario

## Overview
El comando `passwd` se utiliza en sistemas Linux y Unix para cambiar la contraseña de un usuario. Permite a los usuarios actualizar su propia contraseña o a un administrador cambiar la contraseña de otros usuarios.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
passwd [opciones] [usuario]
```

Si se ejecuta sin argumentos, cambiará la contraseña del usuario que está actualmente conectado.

## Common Options
- `-d`: Elimina la contraseña del usuario, permitiendo el acceso sin contraseña.
- `-e`: Fuerza al usuario a cambiar su contraseña en el próximo inicio de sesión.
- `-l`: Bloquea la cuenta del usuario.
- `-u`: Desbloquea la cuenta del usuario.
- `-S`: Muestra el estado de la contraseña del usuario.

## Common Examples
1. **Cambiar la contraseña del usuario actual:**
   ```bash
   passwd
   ```

2. **Cambiar la contraseña de un usuario específico (requiere privilegios de administrador):**
   ```bash
   sudo passwd nombre_usuario
   ```

3. **Eliminar la contraseña de un usuario:**
   ```bash
   sudo passwd -d nombre_usuario
   ```

4. **Forzar a un usuario a cambiar su contraseña en el próximo inicio de sesión:**
   ```bash
   sudo passwd -e nombre_usuario
   ```

5. **Bloquear la cuenta de un usuario:**
   ```bash
   sudo passwd -l nombre_usuario
   ```

## Tips
- Siempre elige contraseñas fuertes que incluyan una combinación de letras, números y símbolos.
- Cambia tu contraseña regularmente para mejorar la seguridad.
- Si eres un administrador, asegúrate de informar a los usuarios sobre la política de contraseñas de la organización.