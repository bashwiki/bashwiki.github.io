# [Linux] Usuarios de Bash: Muestra información sobre los usuarios del sistema

## Overview
El comando `users` se utiliza en sistemas Unix y Linux para mostrar los nombres de los usuarios que están actualmente conectados al sistema. Es una herramienta simple pero útil para obtener información rápida sobre la actividad de los usuarios.

## Usage
La sintaxis básica del comando es la siguiente:

```
users [opciones]
```

## Common Options
- `-n`: Muestra solo el número de usuarios conectados.
- `-r`: Muestra solo los usuarios que están conectados de forma remota.

## Common Examples
A continuación se presentan algunos ejemplos prácticos del uso del comando `users`:

1. **Mostrar usuarios conectados:**
   ```bash
   users
   ```

2. **Contar el número de usuarios conectados:**
   ```bash
   users -n
   ```

3. **Mostrar usuarios conectados de forma remota:**
   ```bash
   users -r
   ```

## Tips
- Utiliza el comando `who` para obtener información más detallada sobre los usuarios conectados, como la hora de inicio de sesión y el terminal utilizado.
- Combina `users` con otros comandos como `wc -w` para contar el número de usuarios conectados:
  ```bash
  users | wc -w
  ```
- Recuerda que el comando `users` solo muestra los usuarios que están activos en el momento de la ejecución.