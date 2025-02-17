# [Linux] Bash cal uso: Muestra un calendario

## Overview
El comando `cal` se utiliza en Bash para mostrar un calendario en la terminal. Permite visualizar el mes actual o cualquier mes y año específicos, facilitando la planificación y la organización de actividades.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
cal [opciones] [mes] [año]
```

## Common Options
- `-m`: Muestra el calendario en formato de mes.
- `-3`: Muestra el mes actual, el anterior y el siguiente.
- `-y`: Muestra el calendario del año completo.
- `-j`: Muestra el calendario con los días julianos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `cal`:

1. Mostrar el calendario del mes actual:
   ```bash
   cal
   ```

2. Mostrar el calendario de un mes específico (por ejemplo, marzo de 2023):
   ```bash
   cal 03 2023
   ```

3. Mostrar el calendario del año completo (por ejemplo, 2023):
   ```bash
   cal -y 2023
   ```

4. Mostrar el mes actual, el anterior y el siguiente:
   ```bash
   cal -3
   ```

5. Mostrar el calendario con días julianos para el mes actual:
   ```bash
   cal -j
   ```

## Tips
- Utiliza `cal -y` para obtener una visión general rápida de todo el año, lo que puede ser útil para planificar eventos a largo plazo.
- Combina `cal` con otros comandos como `grep` para buscar fechas específicas en el calendario.
- Recuerda que puedes usar `man cal` para acceder a la página de manual y obtener más información sobre las opciones disponibles.