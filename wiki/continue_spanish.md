# [리눅스] Bash continue 사용법

## Overview
El comando `continue` en Bash se utiliza dentro de bucles (como `for`, `while` y `until`) para omitir la iteración actual y continuar con la siguiente. Su propósito principal es permitir que el flujo de ejecución del bucle continúe sin ejecutar el resto del código en la iteración actual, lo que puede ser útil para evitar la ejecución de ciertas instrucciones bajo condiciones específicas.

## Usage
La sintaxis básica del comando `continue` es la siguiente:

```bash
continue [N]
```

- `N` es un número opcional que especifica el nivel del bucle al que se aplica el comando. Si se omite, `continue` afecta al bucle más interno. Si se proporciona un número, `continue N` afecta al bucle que está `N` niveles hacia arriba en la jerarquía de bucles.

## Examples
### Ejemplo 1: Uso básico de `continue`
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "Número: $i"
done
```
**Salida:**
```
Número: 1
Número: 2
Número: 4
Número: 5
```
En este ejemplo, cuando `i` es igual a 3, el comando `continue` omite la impresión de ese número y continúa con la siguiente iteración.

### Ejemplo 2: Usando `continue` con un bucle `while`
```bash
count=0
while [ $count -lt 5 ]; do
    count=$((count + 1))
    if [ $count -eq 2 ]; then
        continue
    fi
    echo "Contador: $count"
done
```
**Salida:**
```
Contador: 1
Contador: 3
Contador: 4
Contador: 5
```
En este caso, el bucle `while` omite la impresión del contador cuando es igual a 2.

## Tips
- Utiliza `continue` para simplificar la lógica de tus bucles, evitando la necesidad de anidar condicionales.
- Asegúrate de que el uso de `continue` no cause un bucle infinito; verifica las condiciones que llevan a la ejecución del comando.
- Puedes usar `continue` en combinación con otros comandos de control de flujo, como `if`, para crear scripts más legibles y eficientes.