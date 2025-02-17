# [Linux] Bash groups uso: Muestra los grupos de usuarios

## Overview
El comando `groups` en Bash se utiliza para mostrar los grupos a los que pertenece un usuario específico. Si se ejecuta sin argumentos, muestra los grupos del usuario actual. Este comando es útil para gestionar permisos y entender la organización de usuarios en un sistema.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
groups [opciones] [usuario]
```

## Common Options
- `-h`, `--help`: Muestra la ayuda del comando y sale.
- `-V`, `--version`: Muestra la versión del comando.

## Common Examples
1. **Mostrar grupos del usuario actual:**
   ```bash
   groups
   ```

2. **Mostrar grupos de un usuario específico:**
   ```bash
   groups nombre_usuario
   ```

3. **Mostrar grupos de varios usuarios:**
   ```bash
   groups usuario1 usuario2
   ```

## Tips
- Utiliza `groups` sin argumentos para verificar rápidamente los grupos del usuario que ha iniciado sesión.
- Si necesitas comprobar los grupos de otros usuarios, asegúrate de tener los permisos necesarios para evitar errores de acceso.
- Recuerda que los grupos son importantes para la gestión de permisos, así que verifica regularmente la pertenencia a grupos en sistemas multiusuario.