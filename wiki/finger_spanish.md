# [Linux] Bash finger uso: Muestra información sobre usuarios del sistema

## Overview
El comando `finger` se utiliza para mostrar información sobre los usuarios del sistema, incluyendo detalles como el nombre completo, la hora de inicio de sesión, el estado de la sesión y más. Es una herramienta útil para obtener información rápida sobre los usuarios activos en un sistema.

## Usage
La sintaxis básica del comando `finger` es la siguiente:

```
finger [opciones] [argumentos]
```

## Common Options
- `-l`: Muestra la información en un formato largo, proporcionando más detalles sobre cada usuario.
- `-m`: Permite buscar usuarios por nombre de usuario en lugar de por nombre completo.
- `-s`: Muestra la información en un formato corto, que incluye solo el nombre de usuario y el estado de la sesión.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `finger`:

1. **Mostrar información de todos los usuarios:**
   ```bash
   finger
   ```

2. **Mostrar información detallada de un usuario específico:**
   ```bash
   finger nombre_usuario
   ```

3. **Mostrar información en formato largo:**
   ```bash
   finger -l nombre_usuario
   ```

4. **Buscar un usuario por nombre de usuario:**
   ```bash
   finger -m nombre_usuario
   ```

5. **Mostrar información en formato corto:**
   ```bash
   finger -s
   ```

## Tips
- Utiliza `finger` en sistemas donde esté instalado, ya que no está disponible por defecto en todas las distribuciones de Linux.
- Combina `finger` con otros comandos como `grep` para filtrar resultados específicos.
- Ten en cuenta que la información mostrada por `finger` puede depender de la configuración del sistema y de los permisos de los usuarios.