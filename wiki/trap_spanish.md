# [리눅스] Bash trap 사용법

## Overview
El comando `trap` en Bash se utiliza para especificar acciones que deben ejecutarse cuando el script recibe ciertas señales o cuando se producen eventos específicos. Su propósito principal es permitir a los desarrolladores manejar situaciones como la interrupción del script, la finalización o la recepción de señales, lo que ayuda a asegurar que se realicen tareas de limpieza o se registren mensajes antes de que el script termine.

## Usage
La sintaxis básica del comando `trap` es la siguiente:

```bash
trap COMMAND SIGNAL
```

- `COMMAND`: El comando o la serie de comandos que deseas ejecutar cuando se recibe la señal.
- `SIGNAL`: La señal que deseas capturar. Puede ser un número de señal (como `1` para SIGHUP) o un nombre de señal (como `SIGINT`).

Algunos ejemplos de señales comunes son:
- `SIGINT`: Interrupción (Ctrl+C).
- `SIGTERM`: Terminación.
- `EXIT`: Se ejecuta cuando el script finaliza, independientemente de cómo se termine.

## Examples
### Ejemplo 1: Manejo de SIGINT
Este ejemplo muestra cómo usar `trap` para manejar la señal de interrupción (Ctrl+C) y ejecutar un comando de limpieza antes de salir.

```bash
#!/bin/bash

trap 'echo "Script interrumpido. Limpiando..."; exit' SIGINT

while true; do
    echo "Ejecutando... (presiona Ctrl+C para interrumpir)"
    sleep 1
done
```

### Ejemplo 2: Limpieza al finalizar
En este ejemplo, se utiliza `trap` para realizar una acción de limpieza cuando el script termina.

```bash
#!/bin/bash

trap 'echo "Limpiando recursos..."; rm -f temp_file.txt' EXIT

echo "Creando un archivo temporal..."
touch temp_file.txt

# Simulación de trabajo
sleep 5

echo "Trabajo completado."
```

## Tips
- Siempre es recomendable manejar señales críticas como `SIGINT` y `SIGTERM` para evitar que los scripts dejen recursos abiertos o en un estado inconsistente.
- Puedes usar múltiples señales en un solo comando `trap`, separándolas con espacios. Por ejemplo: `trap 'echo "Limpiando..."; exit' SIGINT SIGTERM`.
- Considera usar `trap` con el comando `EXIT` para asegurarte de que se ejecuten tareas de limpieza, independientemente de cómo se termine el script.
- Recuerda que los comandos en `trap` se ejecutan en el contexto del script, por lo que las variables definidas en el script estarán disponibles.

El uso adecuado de `trap` puede mejorar la robustez y la confiabilidad de tus scripts de Bash, asegurando que se manejen adecuadamente las señales y eventos.