# [리눅스] Bash users 사용법

## Overview
El comando `users` en Bash se utiliza para mostrar una lista de los nombres de usuario de los usuarios que están actualmente conectados al sistema. Su principal propósito es proporcionar una visión rápida de quiénes están activos en el sistema en un momento dado, lo que puede ser útil para la administración del sistema y el monitoreo de la actividad de los usuarios.

## Usage
La sintaxis básica del comando `users` es la siguiente:

```bash
users [opciones]
```

### Opciones Comunes
El comando `users` no tiene muchas opciones, ya que su funcionalidad es bastante simple. Sin embargo, puedes usarlo en combinación con otros comandos para obtener más información. Algunas opciones que pueden ser útiles incluyen:

- `-n`: Muestra el número de usuarios conectados en lugar de sus nombres.

## Examples
Aquí hay algunos ejemplos prácticos de cómo usar el comando `users`:

1. **Mostrar usuarios conectados**:
   Para ver una lista de los usuarios que están actualmente conectados al sistema, simplemente ejecuta:

   ```bash
   users
   ```

   Esto devolverá una lista de nombres de usuario separados por espacios.

2. **Contar usuarios conectados**:
   Si deseas contar cuántos usuarios están conectados, puedes combinar el comando `users` con `wc` (word count) de la siguiente manera:

   ```bash
   users | wc -w
   ```

   Este comando mostrará el número total de usuarios conectados al sistema.

## Tips
- Utiliza el comando `users` en scripts de administración de sistemas para monitorear la actividad de los usuarios y tomar decisiones informadas sobre la gestión de recursos.
- Combina `users` con otros comandos como `who` o `w` para obtener información más detallada sobre la actividad de los usuarios, incluyendo el tiempo de conexión y la actividad actual.
- Recuerda que el comando `users` solo mostrará los usuarios que están conectados en el momento de la ejecución, por lo que es útil para obtener un estado instantáneo del sistema.