# [Linux] Bash selinuxenabled uso: Comprobar el estado de SELinux

## Overview
El comando `selinuxenabled` se utiliza para verificar si el soporte de SELinux (Security-Enhanced Linux) está habilitado en el sistema. Este comando devuelve un código de salida que indica si SELinux está activo o no.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
selinuxenabled [opciones]
```

## Common Options
El comando `selinuxenabled` no tiene opciones comunes, ya que su función principal es simplemente comprobar el estado de SELinux. Sin embargo, puede ser útil en scripts para tomar decisiones basadas en su salida.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `selinuxenabled`:

1. **Comprobar si SELinux está habilitado:**
   ```bash
   selinuxenabled
   ```
   - Este comando no devuelve salida, pero el código de salida será `0` si SELinux está habilitado y `1` si no lo está.

2. **Usar en un script para tomar decisiones:**
   ```bash
   if selinuxenabled; then
       echo "SELinux está habilitado."
   else
       echo "SELinux no está habilitado."
   fi
   ```
   - Este script imprime un mensaje dependiendo del estado de SELinux.

## Tips
- Utiliza `selinuxenabled` en scripts de shell para asegurarte de que ciertas configuraciones o acciones solo se ejecuten si SELinux está habilitado.
- Recuerda que el código de salida es clave: `0` significa que SELinux está habilitado, mientras que `1` indica que no lo está.
- Puedes combinar `selinuxenabled` con otros comandos para crear condiciones más complejas en tus scripts.