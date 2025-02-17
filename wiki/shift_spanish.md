# [Linux] Bash shift uso equivalente en español: Desplazar parámetros a la izquierda

El comando `shift` se utiliza en Bash para desplazar los parámetros posicionales a la izquierda, lo que permite acceder a los argumentos de un script de manera más sencilla.

## Overview
El comando `shift` permite desplazar los parámetros posicionales de un script de Bash. Esto significa que el primer parámetro se elimina y todos los demás se desplazan una posición hacia la izquierda. Es útil cuando se procesan argumentos en un bucle.

## Usage
La sintaxis básica del comando `shift` es la siguiente:

```bash
shift [n]
```

Donde `n` es el número de posiciones que se desea desplazar. Si no se especifica `n`, el valor predeterminado es 1.

## Common Options
- `n`: Especifica cuántas posiciones se deben desplazar. Si se omite, se desplaza solo una posición.

## Common Examples

### Ejemplo 1: Desplazar un parámetro
```bash
#!/bin/bash
echo "Primer parámetro: $1"
shift
echo "Nuevo primer parámetro: $1"
```
Si ejecutas este script con `./script.sh uno dos tres`, la salida será:
```
Primer parámetro: uno
Nuevo primer parámetro: dos
```

### Ejemplo 2: Desplazar múltiples parámetros
```bash
#!/bin/bash
echo "Parámetros originales: $1 $2 $3"
shift 2
echo "Parámetros después de desplazar: $1 $2"
```
Si ejecutas este script con `./script.sh uno dos tres`, la salida será:
```
Parámetros originales: uno dos tres
Parámetros después de desplazar: tres
```

### Ejemplo 3: Procesar todos los parámetros
```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Parámetro: $1"
    shift
done
```
Si ejecutas este script con `./script.sh uno dos tres`, la salida será:
```
Parámetro: uno
Parámetro: dos
Parámetro: tres
```

## Tips
- Utiliza `shift` dentro de bucles para procesar todos los argumentos de manera eficiente.
- Asegúrate de que hay suficientes parámetros antes de usar `shift` para evitar errores.
- Puedes combinar `shift` con otros comandos para crear scripts más complejos que manejen múltiples argumentos.