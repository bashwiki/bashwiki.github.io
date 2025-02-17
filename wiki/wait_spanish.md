# [Linux] Bash wait Uso equivalente: Esperar la finalización de procesos en segundo plano

## Overview
El comando `wait` en Bash se utiliza para esperar a que finalicen uno o más procesos en segundo plano. Este comando es especialmente útil cuando se desea sincronizar la ejecución de scripts o comandos que dependen de la finalización de otros procesos.

## Usage
La sintaxis básica del comando `wait` es la siguiente:

```bash
wait [opciones] [argumentos]
```

## Common Options
- `-n`: Espera a que finalice el siguiente proceso en segundo plano.
- `PID`: Especifica el identificador del proceso (PID) para el cual se desea esperar. Si no se proporciona ningún PID, `wait` espera a que finalicen todos los procesos en segundo plano.

## Common Examples

### Esperar a que finalicen todos los procesos en segundo plano
```bash
sleep 5 &
sleep 10 &
wait
echo "Todos los procesos han finalizado."
```

### Esperar a un proceso específico
```bash
sleep 5 &
PID=$!
echo "Esperando al proceso con PID: $PID"
wait $PID
echo "El proceso ha finalizado."
```

### Usar la opción -n
```bash
sleep 5 &
sleep 10 &
sleep 3 &
wait -n
echo "Un proceso en segundo plano ha finalizado."
```

## Tips
- Utiliza `wait` al final de un script para asegurarte de que todos los procesos en segundo plano hayan terminado antes de continuar.
- Almacena el PID de un proceso en una variable para poder usar `wait` en ese proceso específico más adelante.
- Recuerda que `wait` solo funciona con procesos que se han iniciado en segundo plano utilizando el operador `&`.