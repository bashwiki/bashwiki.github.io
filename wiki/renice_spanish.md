# [Linux] Bash renice uso: Cambiar la prioridad de los procesos en ejecución

## Overview
El comando `renice` se utiliza en sistemas Unix y Linux para cambiar la prioridad de uno o más procesos en ejecución. La prioridad de un proceso determina cuánto tiempo de CPU se le asigna en comparación con otros procesos. Un valor de prioridad más bajo significa mayor prioridad.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
renice [opciones] [valores] [PID]
```

- `[valores]` es el nuevo valor de prioridad que deseas asignar.
- `[PID]` es el identificador del proceso al que deseas cambiar la prioridad.

## Common Options
- `-n, --priority`: Especifica el nuevo valor de prioridad.
- `-p, --pid`: Indica que se va a cambiar la prioridad de un proceso específico.
- `-g, --pgrp`: Cambia la prioridad de un grupo de procesos.
- `-u, --user`: Cambia la prioridad de todos los procesos de un usuario específico.

## Common Examples

1. Cambiar la prioridad de un proceso específico:
   ```bash
   renice -n 10 -p 1234
   ```
   Este comando establece la prioridad del proceso con PID 1234 a 10.

2. Cambiar la prioridad de todos los procesos de un usuario:
   ```bash
   renice -n 5 -u nombre_usuario
   ```
   Esto cambia la prioridad de todos los procesos del usuario `nombre_usuario` a 5.

3. Cambiar la prioridad de un grupo de procesos:
   ```bash
   renice -n -5 -g 5678
   ```
   Aquí, se establece la prioridad de todos los procesos en el grupo con GID 5678 a -5.

4. Verificar la prioridad actual de un proceso:
   ```bash
   ps -o pid,ni,cmd -p 1234
   ```
   Este comando muestra el PID, el valor de niceness (prioridad) y el comando del proceso con PID 1234.

## Tips
- Utiliza valores negativos para aumentar la prioridad de un proceso y valores positivos para disminuirla.
- Ten cuidado al cambiar la prioridad de procesos críticos del sistema, ya que esto puede afectar el rendimiento general.
- Es recomendable ejecutar `renice` con privilegios de superusuario (usando `sudo`) si estás cambiando la prioridad de procesos que no son de tu usuario.