# [리눅스] Bash break 사용법

## Overview
El comando `break` en Bash se utiliza para salir de un bucle (loop) anticipadamente. Su propósito principal es interrumpir la ejecución de un bucle `for`, `while` o `until` cuando se cumple una condición específica, permitiendo así un control más preciso sobre el flujo de ejecución de los scripts.

## Usage
La sintaxis básica del comando `break` es la siguiente:

```bash
break [n]
```

- `n`: Este argumento opcional especifica el número de niveles de bucles que se deben romper. Si se omite, `break` saldrá del bucle más interno.

## Examples
### Ejemplo 1: Salir de un bucle `while`
```bash
#!/bin/bash

contador=1

while [ $contador -le 5 ]; do
  echo "Contador: $contador"
  if [ $contador -eq 3 ]; then
    break
  fi
  contador=$((contador + 1))
done
```
En este ejemplo, el bucle `while` imprime el valor del contador hasta que este llega a 3, momento en el cual se ejecuta el comando `break` y se sale del bucle.

### Ejemplo 2: Salir de un bucle `for`
```bash
#!/bin/bash

for i in {1..5}; do
  if [ $i -eq 4 ]; then
    break
  fi
  echo "Número: $i"
done
```
Aquí, el bucle `for` imprime los números del 1 al 5, pero se interrumpe cuando `i` es igual a 4, gracias al uso del comando `break`.

## Tips
- Utiliza `break` cuando necesites salir de un bucle basado en una condición específica para evitar la ejecución innecesaria de código.
- Si trabajas con bucles anidados, puedes usar el argumento `n` para especificar cuántos niveles de bucles deseas romper. Por ejemplo, `break 2` saldrá de dos niveles de bucles.
- Asegúrate de que el uso de `break` no interrumpa la lógica de tu script de manera inesperada, revisando las condiciones que lo activan.