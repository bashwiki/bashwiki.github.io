# [Linux] Bash top uso: Muestra el uso de recursos del sistema

## Overview
El comando `top` es una herramienta de monitoreo en tiempo real que muestra los procesos en ejecución en un sistema Linux. Proporciona información sobre el uso de la CPU, la memoria y otros recursos del sistema, permitiendo a los usuarios identificar procesos que consumen muchos recursos.

## Usage
La sintaxis básica del comando `top` es la siguiente:

```bash
top [opciones]
```

## Common Options
- `-d <segundos>`: Establece el intervalo de actualización en segundos.
- `-n <número>`: Especifica el número de actualizaciones que se mostrarán antes de salir.
- `-u <usuario>`: Muestra solo los procesos de un usuario específico.
- `-p <PID>`: Muestra solo el proceso con el ID de proceso especificado.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `top`:

1. **Ejecutar top con actualización cada 2 segundos:**
   ```bash
   top -d 2
   ```

2. **Mostrar solo los procesos de un usuario específico:**
   ```bash
   top -u nombre_usuario
   ```

3. **Limitar la salida a un número específico de actualizaciones:**
   ```bash
   top -n 5
   ```

4. **Monitorear un proceso específico por su PID:**
   ```bash
   top -p 1234
   ```

## Tips
- Para salir de la interfaz de `top`, presiona `q`.
- Puedes presionar `h` dentro de `top` para ver una ayuda rápida sobre los comandos disponibles.
- Utiliza la tecla `M` para ordenar los procesos por uso de memoria y `P` para ordenarlos por uso de CPU.
- Considera usar `htop`, una versión más amigable de `top`, que proporciona una interfaz visual mejorada.