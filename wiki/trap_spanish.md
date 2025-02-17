# [Linux] Bash trap uso: Captura señales y limpia recursos

## Overview
El comando `trap` en Bash se utiliza para capturar señales y ejecutar comandos específicos cuando se reciben estas señales. Esto es especialmente útil para limpiar recursos o realizar acciones específicas antes de que un script termine o sea interrumpido.

## Usage
La sintaxis básica del comando `trap` es la siguiente:

```bash
trap [opciones] [comando] [señal]
```

## Common Options
- `-l`: Lista todas las señales disponibles.
- `-p`: Muestra las acciones actuales de `trap` para cada señal.
- `SIGNAL`: Puede ser un número de señal o un nombre de señal (por ejemplo, `SIGINT`, `SIGTERM`).

## Common Examples

### Ejemplo 1: Limpiar archivos temporales
Este ejemplo muestra cómo usar `trap` para eliminar un archivo temporal cuando el script se interrumpe.

```bash
#!/bin/bash
tempfile="/tmp/mi_archivo_temp.txt"
trap "rm -f $tempfile" EXIT

echo "Creando un archivo temporal..."
touch $tempfile
# Simulando trabajo
sleep 10
```

### Ejemplo 2: Capturar la interrupción del usuario
Aquí se captura la señal de interrupción (Ctrl+C) y se muestra un mensaje antes de salir.

```bash
#!/bin/bash
trap "echo 'Interrupción recibida. Saliendo...'; exit" SIGINT

echo "Presiona Ctrl+C para interrumpir el script."
while true; do
    sleep 1
done
```

### Ejemplo 3: Manejo de señales de terminación
Este ejemplo muestra cómo manejar la señal de terminación para realizar una acción antes de que el script se cierre.

```bash
#!/bin/bash
trap "echo 'Recibiendo señal de terminación...'; exit" SIGTERM

echo "El script está en ejecución. Envíe SIGTERM para terminar."
while true; do
    sleep 1
done
```

## Tips
- Siempre es buena práctica usar `trap` para limpiar recursos, especialmente en scripts que crean archivos temporales o conexiones de red.
- Puedes usar múltiples señales en un solo comando `trap`, separándolas con espacios.
- Recuerda que algunas señales no pueden ser capturadas o ignoradas, como `SIGKILL`.