# [Linux] Bash en at: Programar tareas para ejecutar más tarde

## Overview
El comando `at` se utiliza en sistemas Unix y Linux para programar la ejecución de comandos o scripts en un momento específico en el futuro. Es útil para tareas que no necesitan ejecutarse de inmediato, permitiendo a los usuarios planificar su ejecución.

## Usage
La sintaxis básica del comando `at` es la siguiente:

```bash
at [opciones] [hora]
```

## Common Options
- `-f archivo`: Permite especificar un archivo que contiene el comando a ejecutar.
- `-m`: Envía un correo electrónico al usuario después de que se ejecute el comando, incluso si no hay salida.
- `-q cola`: Permite especificar una cola de trabajos diferente.
- `-l`: Lista los trabajos programados para el usuario actual.
- `-d`: Elimina un trabajo programado.

## Common Examples
Aquí hay algunos ejemplos prácticos de cómo usar el comando `at`:

1. **Programar un comando para ejecutarse a las 3 PM:**
   ```bash
   echo "echo 'Hola, mundo'" | at 15:00
   ```

2. **Ejecutar un script a las 10:30 AM:**
   ```bash
   at 10:30 -f /ruta/al/script.sh
   ```

3. **Programar un comando para ejecutarse en 5 minutos:**
   ```bash
   echo "backup.sh" | at now + 5 minutes
   ```

4. **Listar trabajos programados:**
   ```bash
   at -l
   ```

5. **Eliminar un trabajo programado (suponiendo que el ID del trabajo es 2):**
   ```bash
   atrm 2
   ```

## Tips
- Asegúrate de que el servicio `atd` esté en ejecución en tu sistema para que los trabajos programados se ejecuten.
- Usa `at -l` para verificar tus trabajos programados y asegurarte de que todo esté en orden.
- Recuerda que los comandos programados se ejecutan en el contexto del usuario que los creó, así que asegúrate de tener los permisos necesarios para ejecutar los comandos o scripts.