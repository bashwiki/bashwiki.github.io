# [리눅스] Bash wait 사용법

## Overview
El comando `wait` en Bash se utiliza para pausar la ejecución de un script hasta que uno o más procesos en segundo plano hayan finalizado. Su propósito principal es permitir que un script espere a que se completen tareas asíncronas, facilitando la sincronización entre procesos. Esto es especialmente útil en situaciones donde se lanzan múltiples tareas en paralelo y se necesita asegurar que todas hayan terminado antes de continuar con la ejecución del script.

## Usage
La sintaxis básica del comando `wait` es la siguiente:

```bash
wait [PID...]
```

- **PID**: Es el identificador del proceso (Process ID) de uno o más procesos en segundo plano que se desea esperar. Si no se especifica ningún PID, `wait` esperará a que todos los procesos en segundo plano finalicen.

### Opciones Comunes
- Sin opciones: Si se ejecuta `wait` sin argumentos, espera a que todos los procesos en segundo plano terminen.
- Con PID: Al proporcionar uno o más PIDs, `wait` solo espera a que esos procesos específicos finalicen.

## Examples

### Ejemplo 1: Esperar a todos los procesos en segundo plano
```bash
#!/bin/bash

# Iniciar dos procesos en segundo plano
sleep 5 &
sleep 3 &

# Esperar a que ambos procesos terminen
wait

echo "Todos los procesos han finalizado."
```
En este ejemplo, el script inicia dos procesos de `sleep` en segundo plano y luego utiliza `wait` para pausar la ejecución hasta que ambos procesos hayan terminado.

### Ejemplo 2: Esperar a un proceso específico
```bash
#!/bin/bash

# Iniciar un proceso en segundo plano
sleep 10 &
PID=$!

echo "Esperando a que el proceso con PID $PID termine..."

# Esperar solo al proceso específico
wait $PID

echo "El proceso ha finalizado."
```
Aquí, el script inicia un proceso de `sleep` en segundo plano y almacena su PID. Luego, utiliza `wait` con ese PID específico para esperar a que solo ese proceso termine.

## Tips
- Utiliza `wait` al final de un script que lanza múltiples procesos en segundo plano para asegurarte de que todos hayan finalizado antes de que el script termine.
- Al manejar múltiples procesos, considera capturar y manejar los códigos de salida de los procesos utilizando `wait` para obtener información sobre su éxito o fracaso.
- Recuerda que si un proceso en segundo plano termina antes de que se ejecute el comando `wait`, el comando `wait` devolverá inmediatamente el estado de ese proceso.