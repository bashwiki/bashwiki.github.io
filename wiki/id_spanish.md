# [Linux] Bash id uso: Muestra información del usuario

## Overview
El comando `id` en Bash se utiliza para mostrar la información del usuario actual o de un usuario específico. Proporciona detalles como el UID (identificador de usuario), GID (identificador de grupo) y los grupos a los que pertenece el usuario.

## Usage
La sintaxis básica del comando `id` es la siguiente:

```bash
id [opciones] [argumentos]
```

## Common Options
- `-u`: Muestra solo el UID del usuario.
- `-g`: Muestra solo el GID del grupo principal del usuario.
- `-G`: Muestra todos los GIDs de los grupos a los que pertenece el usuario.
- `-n`: Muestra el nombre del usuario o grupo en lugar de su ID numérico.
- `-r`: Muestra el GID real en lugar del efectivo.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `id`:

1. Mostrar información del usuario actual:
   ```bash
   id
   ```

2. Mostrar solo el UID del usuario actual:
   ```bash
   id -u
   ```

3. Mostrar solo el GID del grupo principal del usuario actual:
   ```bash
   id -g
   ```

4. Mostrar todos los grupos a los que pertenece el usuario actual:
   ```bash
   id -G
   ```

5. Mostrar información de un usuario específico (por ejemplo, "usuario1"):
   ```bash
   id usuario1
   ```

6. Mostrar el nombre del usuario en lugar del UID:
   ```bash
   id -n -u
   ```

## Tips
- Utiliza `id` sin opciones para obtener una visión general rápida de tu usuario y grupos.
- Combina opciones para obtener información más específica, como `id -u -n` para ver el nombre del usuario junto con su UID.
- Si trabajas en un entorno multiusuario, usar `id nombre_usuario` puede ayudarte a verificar los permisos y grupos de otros usuarios.