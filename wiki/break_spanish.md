# [Linux] Bash break uso equivalente: Finaliza un bucle

## Overview
El comando `break` en Bash se utiliza para salir de un bucle, ya sea un bucle `for`, `while` o `until`. Cuando se ejecuta `break`, el control del programa se transfiere a la siguiente línea de código después del bucle.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
break [n]
```

Donde `n` es un número opcional que indica cuántos niveles de bucles se deben romper. Si no se especifica, `break` saldrá del bucle más interno.

## Common Options
- `n`: Un número que especifica cuántos niveles de bucles se deben romper. Por defecto, se rompe solo el bucle más interno.

## Common Examples

### Ejemplo 1: Romper un bucle `for`
```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    break
  fi
  echo "Número: $i"
done
```
**Salida:**
```
Número: 1
Número: 2
```

### Ejemplo 2: Romper un bucle `while`
```bash
contador=1
while [ $contador -le 5 ]; do
  if [ $contador -eq 4 ]; then
    break
  fi
  echo "Contador: $contador"
  contador=$((contador + 1))
done
```
**Salida:**
```
Contador: 1
Contador: 2
Contador: 3
```

### Ejemplo 3: Romper múltiples niveles de bucles
```bash
for i in {1..3}; do
  for j in {1..3}; do
    if [ $j -eq 2 ]; then
      break 2
    fi
    echo "i: $i, j: $j"
  done
done
```
**Salida:**
```
i: 1, j: 1
```

## Tips
- Utiliza `break` cuando necesites salir de un bucle basado en una condición específica para evitar iteraciones innecesarias.
- Si estás usando bucles anidados, especifica el número de niveles que deseas romper para un control más preciso.
- Recuerda que el uso excesivo de `break` puede dificultar la lectura del código; asegúrate de que su uso sea claro y justificado.