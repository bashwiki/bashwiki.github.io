# [Linux] Bash return uso equivalente: devolver el estado de salida de un comando

## Overview
El comando `return` en Bash se utiliza para devolver un estado de salida de una función. Este estado de salida es un número entero que indica si la función se ejecutó correctamente o si ocurrió un error. Por convención, un estado de salida de `0` indica éxito, mientras que cualquier otro número indica un error.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
return [número]
```

Donde `[número]` es el estado de salida que deseas devolver.

## Common Options
El comando `return` no tiene opciones específicas, ya que su funcionalidad se basa en el número que se le pasa como argumento. Sin embargo, aquí hay algunas consideraciones:

- Si no se proporciona un número, `return` devolverá el estado de salida de la última instrucción ejecutada en la función.

## Common Examples

### Ejemplo 1: Devolver un estado de éxito
```bash
function mi_funcion {
    # Código de la función
    return 0  # Indica que la función se ejecutó correctamente
}
```

### Ejemplo 2: Devolver un estado de error
```bash
function mi_funcion {
    # Código de la función
    return 1  # Indica que ocurrió un error
}
```

### Ejemplo 3: Usar el estado de salida de la última instrucción
```bash
function mi_funcion {
    ls /ruta/no/existente
    return $?  # Devuelve el estado de salida del comando 'ls'
}
```

## Tips
- Siempre es buena práctica devolver un estado de salida explícito en tus funciones para facilitar la depuración.
- Utiliza `return 0` al final de una función si todo se ejecutó correctamente, y diferentes números para diferentes tipos de errores.
- Puedes utilizar el comando `echo $?` después de llamar a una función para verificar el estado de salida devuelto.