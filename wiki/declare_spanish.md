# [리눅스] Bash declare 사용법

## Overview
El comando `declare` en Bash se utiliza para declarar variables y sus atributos. Permite a los desarrolladores y a los ingenieros definir variables con características específicas, como si son de solo lectura, arrays, o enteros. Esto ayuda a gestionar el comportamiento de las variables y a mejorar la legibilidad del código.

## Usage
La sintaxis básica del comando `declare` es la siguiente:

```bash
declare [opciones] nombre_variable
```

### Opciones comunes:
- `-r`: Marca la variable como de solo lectura. Una vez asignado un valor, no se puede cambiar.
- `-a`: Declara una variable como un array.
- `-i`: Declara una variable como un entero. Cualquier valor asignado se evaluará como un número.
- `-x`: Exporta la variable al entorno, haciéndola disponible para procesos hijos.

## Examples
### Ejemplo 1: Declarar una variable de solo lectura
```bash
declare -r PI=3.14
echo $PI  # Salida: 3.14
PI=3.14159  # Esto generará un error porque PI es de solo lectura.
```

### Ejemplo 2: Declarar un array y acceder a sus elementos
```bash
declare -a frutas=("manzana" "banana" "cereza")
echo ${frutas[1]}  # Salida: banana
```

## Tips
- Utiliza `declare -p` para imprimir la declaración de una variable, lo que es útil para depuración.
- Es recomendable usar `declare` para definir variables en scripts más grandes, ya que ayuda a mantener el código organizado y claro.
- Recuerda que las variables de solo lectura no se pueden modificar, así que úsalas para valores constantes que no deben cambiar a lo largo de la ejecución del script.