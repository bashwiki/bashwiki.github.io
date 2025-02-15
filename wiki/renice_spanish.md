# [리눅스] Bash renice 사용법

## Overview
El comando `renice` en Bash se utiliza para cambiar la prioridad de ejecución de uno o más procesos en un sistema operativo basado en Unix. La prioridad de un proceso determina cuán favorablemente el sistema operativo asigna recursos de CPU a ese proceso. Un valor de prioridad más bajo indica una mayor prioridad, mientras que un valor más alto indica una menor prioridad. Esto es útil para gestionar el rendimiento del sistema, especialmente cuando hay procesos que consumen muchos recursos.

## Usage
La sintaxis básica del comando `renice` es la siguiente:

```bash
renice [opciones] prioridad -p PID
```

### Opciones comunes:
- `prioridad`: Este es el nuevo valor de prioridad que deseas asignar al proceso. Puede ser un número entre -20 (máxima prioridad) y 19 (mínima prioridad).
- `-p`: Esta opción se utiliza para especificar el ID del proceso (PID) al que se le cambiará la prioridad.
- `-g`: Cambia la prioridad de todos los procesos en un grupo de procesos especificado.
- `-u`: Cambia la prioridad de todos los procesos pertenecientes a un usuario específico.

## Examples
### Ejemplo 1: Cambiar la prioridad de un proceso específico
Supongamos que tienes un proceso con el PID 1234 y deseas aumentar su prioridad a -10. Puedes hacerlo con el siguiente comando:

```bash
renice -10 -p 1234
```

### Ejemplo 2: Cambiar la prioridad de todos los procesos de un usuario
Si deseas cambiar la prioridad de todos los procesos que pertenecen al usuario "usuario1" a 5, puedes usar el siguiente comando:

```bash
renice 5 -u usuario1
```

## Tips
- **Verifica la prioridad actual**: Antes de cambiar la prioridad de un proceso, es útil verificar su prioridad actual usando el comando `ps` o `top`.
- **Usa con precaución**: Cambiar la prioridad de procesos críticos del sistema puede afectar negativamente el rendimiento del sistema. Asegúrate de entender las implicaciones de los cambios que realices.
- **Permisos**: Para cambiar la prioridad de un proceso que no es de tu propiedad, necesitarás permisos de superusuario. Puedes usar `sudo` para ejecutar `renice` con privilegios elevados.
- **Monitoreo**: Después de realizar cambios, monitorea el rendimiento del sistema para asegurarte de que los ajustes han tenido el efecto deseado.