# [Linux] Bash declare uso: Declarar variables y atributos en Bash

## Overview
El comando `declare` en Bash se utiliza para declarar variables y establecer atributos para ellas. Permite definir variables de solo lectura, arrays y otros tipos de variables, lo que ayuda a gestionar el entorno de programación de manera más efectiva.

## Usage
La sintaxis básica del comando `declare` es la siguiente:

```bash
declare [opciones] [argumentos]
```

## Common Options
- `-r`: Marca la variable como de solo lectura, lo que impide que se modifique.
- `-a`: Declara una variable como un array.
- `-i`: Declara una variable como un entero, permitiendo operaciones matemáticas.
- `-x`: Exporta la variable al entorno, haciéndola disponible para procesos hijos.

## Common Examples

### Declarar una variable simple
```bash
declare nombre="Juan"
echo $nombre
```

### Declarar una variable de solo lectura
```bash
declare -r PI=3.14
echo $PI
# PI=3.15  # Esto generará un error, ya que PI es de solo lectura.
```

### Declarar un array
```bash
declare -a frutas=("manzana" "banana" "cereza")
echo ${frutas[1]}  # Salida: banana
```

### Declarar una variable entera
```bash
declare -i suma=5
suma+=10
echo $suma  # Salida: 15
```

### Exportar una variable
```bash
declare -x usuario="admin"
```

## Tips
- Utiliza `declare -r` para proteger variables críticas que no deben ser modificadas.
- Al trabajar con arrays, recuerda que los índices comienzan en 0.
- Es útil utilizar `declare -p` para imprimir las variables y sus atributos, lo que facilita la depuración.