# [리눅스] Bash at 사용법

## Overview
El comando `at` en Bash se utiliza para programar la ejecución de tareas en un momento específico en el futuro. Es especialmente útil para los usuarios que desean automatizar tareas que deben realizarse una sola vez en un horario determinado. `at` permite a los ingenieros y desarrolladores ejecutar scripts, comandos o programas sin necesidad de estar presentes en la terminal.

## Usage
La sintaxis básica del comando `at` es la siguiente:

```
at [opciones] [hora]
```

### Opciones Comunes
- `-f archivo`: Permite especificar un archivo que contiene los comandos a ejecutar.
- `-m`: Envía un correo electrónico al usuario después de que se ejecute el comando, incluso si no hay salida.
- `-q cola`: Permite especificar la cola de trabajo en la que se debe colocar el trabajo programado.
- `-v`: Muestra la hora programada para la ejecución del trabajo.

## Examples
### Ejemplo 1: Programar un comando simple
Para programar la ejecución del comando `echo "Hola, mundo"` para que se ejecute a las 15:00 del día actual, puedes usar el siguiente comando:

```bash
echo "echo 'Hola, mundo'" | at 15:00
```

### Ejemplo 2: Ejecutar un script
Si tienes un script llamado `backup.sh` que deseas ejecutar a las 2 de la mañana, puedes hacerlo de la siguiente manera:

```bash
at 02:00 -f /ruta/al/script/backup.sh
```

## Tips
- Asegúrate de que el servicio `atd` esté en ejecución en tu sistema, ya que es necesario para que `at` funcione correctamente.
- Puedes listar los trabajos programados usando el comando `atq`.
- Para eliminar un trabajo programado, utiliza el comando `atrm` seguido del número de trabajo que obtuviste con `atq`.
- Es recomendable utilizar rutas absolutas en los scripts o comandos que se programan para evitar problemas de localización.