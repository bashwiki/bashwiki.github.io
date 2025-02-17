# [Linux] Bash local uso: Definir variables locales en funciones

## Overview
El comando `local` se utiliza en Bash para declarar variables que tienen un alcance limitado a la función en la que se definen. Esto significa que las variables locales no están disponibles fuera de la función, lo que ayuda a evitar conflictos con otras variables en el script.

## Usage
La sintaxis básica del comando `local` es la siguiente:

```bash
local [opciones] [nombre_variable]=[valor]
```

## Common Options
El comando `local` no tiene muchas opciones, ya que su propósito principal es la declaración de variables locales. Sin embargo, se pueden usar algunas opciones de Bash al definir variables:

- `-n`: Crea una variable que actúa como un puntero a otra variable.
- `-a`: Declara una variable como un array.
- `-i`: Declara una variable como un entero.

## Common Examples

### Ejemplo 1: Declarar una variable local simple
```bash
mi_funcion() {
    local mi_variable="Hola, mundo"
    echo $mi_variable
}

mi_funcion  # Salida: Hola, mundo
echo $mi_variable  # No hay salida, ya que la variable es local
```

### Ejemplo 2: Usar una variable local en un bucle
```bash
mi_funcion() {
    for i in {1..5}; do
        local numero=$i
        echo "Número: $numero"
    done
}

mi_funcion
```

### Ejemplo 3: Crear un array local
```bash
mi_funcion() {
    local -a mi_array=("uno" "dos" "tres")
    echo "Elemento 1: ${mi_array[0]}"
}

mi_funcion  # Salida: Elemento 1: uno
```

## Tips
- Siempre que necesites una variable que no interfiera con otras partes de tu script, usa `local`.
- Declara las variables locales al principio de la función para mejorar la legibilidad.
- Recuerda que las variables locales no son accesibles fuera de la función, lo que puede ser útil para evitar errores en scripts complejos.