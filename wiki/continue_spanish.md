# [Linux] Bash continue uso equivalente: Continuar con el siguiente ciclo en un bucle

## Overview
El comando `continue` en Bash se utiliza dentro de estructuras de control de bucle, como `for`, `while` o `until`. Su función principal es omitir el resto del código en la iteración actual del bucle y continuar con la siguiente iteración.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
continue [n]
```

Donde `n` es un número opcional que indica cuántos niveles de bucle se deben omitir. Si no se especifica, `continue` omite el bucle más interno.

## Common Options
- `n`: Un número que especifica cuántos niveles de bucle se deben omitir. Por defecto, se omite solo el bucle más interno.

## Common Examples

### Ejemplo 1: Usar continue en un bucle for
Este ejemplo muestra cómo usar `continue` para omitir los números pares en un bucle `for`.

```bash
for i in {1..10}; do
    if (( i % 2 == 0 )); then
        continue
    fi
    echo $i
done
```
*Salida:*
```
1
3
5
7
9
```

### Ejemplo 2: Usar continue en un bucle while
En este ejemplo, se utiliza `continue` para saltar los valores negativos en un bucle `while`.

```bash
count=0
while [ $count -lt 10 ]; do
    count=$((count - 1))
    if [ $count -lt 0 ]; then
        continue
    fi
    echo $count
done
```
*Salida:*
```
0
```

### Ejemplo 3: Usar continue con un número
Este ejemplo muestra cómo omitir un nivel de bucle específico usando un número.

```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            continue 1
        fi
        echo "i: $i, j: $j"
    done
done
```
*Salida:*
```
i: 1, j: 1
i: 1, j: 3
i: 2, j: 1
i: 2, j: 3
i: 3, j: 1
i: 3, j: 3
```

## Tips
- Utiliza `continue` para mejorar la legibilidad de tu código al evitar anidamientos innecesarios.
- Asegúrate de que el uso de `continue` no cause un bucle infinito; revisa las condiciones de salida de tus bucles.
- Es útil para filtrar datos en bucles, permitiendo que tu script se enfoque solo en los elementos que necesitas procesar.