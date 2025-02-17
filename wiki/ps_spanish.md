# [Linux] Bash ps Uso equivalente: [muestra procesos en ejecución]

## Overview
El comando `ps` se utiliza en sistemas Unix y Linux para mostrar información sobre los procesos en ejecución. Proporciona una instantánea de los procesos actuales, incluyendo detalles como el ID del proceso (PID), el estado y el uso de recursos.

## Usage
La sintaxis básica del comando `ps` es la siguiente:

```bash
ps [opciones] [argumentos]
```

## Common Options
A continuación se presentan algunas opciones comunes del comando `ps`:

- `-e`: Muestra todos los procesos en el sistema.
- `-f`: Muestra información completa sobre los procesos.
- `-u`: Muestra procesos de un usuario específico.
- `-aux`: Muestra todos los procesos con detalles adicionales.
- `--sort`: Permite ordenar la salida según un criterio específico.

## Common Examples

### Mostrar todos los procesos
Para ver todos los procesos en ejecución en el sistema, utiliza:

```bash
ps -e
```

### Mostrar procesos con detalles
Para obtener una lista más detallada de los procesos, puedes usar:

```bash
ps -ef
```

### Filtrar por usuario
Si deseas ver los procesos de un usuario específico, puedes usar:

```bash
ps -u nombre_usuario
```

### Mostrar procesos con uso de memoria
Para mostrar todos los procesos y ordenarlos por uso de memoria, puedes ejecutar:

```bash
ps aux --sort=-%mem
```

### Ver procesos en tiempo real
Para observar los procesos en tiempo real, puedes combinar `ps` con `watch`:

```bash
watch -n 1 'ps -e'
```

## Tips
- Utiliza `man ps` para acceder a la página de manual y conocer más opciones y detalles sobre el comando.
- Combina `ps` con otros comandos como `grep` para filtrar resultados específicos, por ejemplo: `ps -e | grep nombre_proceso`.
- Recuerda que `ps` muestra una instantánea de los procesos en el momento en que se ejecuta, por lo que puede ser útil combinarlo con herramientas como `top` o `htop` para un monitoreo más dinámico.