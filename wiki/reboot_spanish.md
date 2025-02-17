# [Linux] Bash reboot uso: reiniciar el sistema

El comando `reboot` se utiliza para reiniciar el sistema operativo de manera segura.

## Overview
El comando `reboot` permite reiniciar el sistema de manera controlada. Esto es útil para aplicar actualizaciones, solucionar problemas o simplemente reiniciar el sistema por cualquier motivo. Al ejecutar este comando, el sistema cierra todas las aplicaciones y servicios en ejecución antes de reiniciarse.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
reboot [opciones] [argumentos]
```

## Common Options
- `-f`: Fuerza el reinicio sin realizar un apagado limpio.
- `-p`: Apaga el sistema después de reiniciar.
- `--halt`: Detiene el sistema sin reiniciarlo.
- `--reboot`: Reinicia el sistema (comportamiento predeterminado).

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `reboot`:

1. **Reiniciar el sistema de forma normal:**
   ```bash
   reboot
   ```

2. **Reiniciar el sistema forzadamente:**
   ```bash
   reboot -f
   ```

3. **Reiniciar el sistema y apagar después:**
   ```bash
   reboot -p
   ```

4. **Reiniciar el sistema desde un entorno gráfico (si tienes privilegios):**
   ```bash
   gnome-session-quit --reboot
   ```

## Tips
- Asegúrate de guardar todo tu trabajo antes de ejecutar el comando `reboot`, ya que cerrará todas las aplicaciones.
- Utiliza la opción `-f` con precaución, ya que puede provocar pérdida de datos si hay aplicaciones en ejecución que no se cierran correctamente.
- Si estás en un entorno multiusuario, considera avisar a otros usuarios antes de reiniciar el sistema para evitar interrupciones inesperadas.