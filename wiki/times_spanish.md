# [Linux] Bash times en español: Muestra el tiempo de ejecución de los procesos

## Overview
El comando `times` en Bash se utiliza para mostrar el tiempo de CPU utilizado por los procesos en ejecución en la shell actual. Este comando es útil para medir el rendimiento y el tiempo que tardan los comandos en ejecutarse.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
times [opciones] [argumentos]
```

## Common Options
El comando `times` no tiene muchas opciones, pero aquí hay algunas que pueden ser útiles:

- `-p`: Muestra el tiempo en un formato más legible, que incluye el tiempo de usuario y el tiempo de sistema.

## Common Examples

### Ejemplo 1: Uso básico de times
Para ver el tiempo de CPU utilizado por los procesos en la shell actual, simplemente escribe:

```bash
times
```

### Ejemplo 2: Uso de times con el formato legible
Para obtener el tiempo en un formato más claro, puedes usar la opción `-p`:

```bash
times -p
```

### Ejemplo 3: Medir el tiempo de un comando específico
Puedes ejecutar un comando y luego usar `times` para ver cuánto tiempo ha tardado. Por ejemplo:

```bash
sleep 5
times
```

Esto mostrará el tiempo de CPU utilizado después de que el comando `sleep` haya finalizado.

## Tips
- Utiliza `times` después de ejecutar varios comandos para obtener una visión general del tiempo total de CPU utilizado.
- Recuerda que `times` solo muestra el tiempo de CPU utilizado por los procesos de la shell actual; no mostrará información sobre procesos en otras shells o terminales.
- Combina `times` con otros comandos para medir el rendimiento de scripts o tareas más complejas.