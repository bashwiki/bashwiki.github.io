# [리눅스] Bash return 사용법

## Overview
El comando `return` en Bash se utiliza para finalizar la ejecución de una función y devolver un valor de estado a la llamada de la función. Este valor de estado es un número entero que puede ser utilizado para indicar el resultado de la ejecución de la función, donde un valor de `0` generalmente indica éxito y cualquier otro valor indica un error o un estado específico.

## Usage
La sintaxis básica del comando `return` es la siguiente:

```bash
return [n]
```

Donde `n` es un número entero que representa el valor de retorno. Si no se especifica un valor, `return` devolverá el valor de estado de la última instrucción ejecutada en la función.

### Opciones Comunes
- `n`: Un número entero entre `0` y `255`. Este número se convierte en el valor de retorno de la función.
- Si se utiliza `return` fuera de una función, se generará un error.

## Examples
### Ejemplo 1: Uso básico de return
```bash
mi_funcion() {
    echo "Ejecutando la función..."
    return 42
}

mi_funcion
echo "Valor de retorno: $?"  # Muestra el valor de retorno de la función
```
En este ejemplo, la función `mi_funcion` se ejecuta y devuelve el valor `42`. Luego, el valor de retorno se puede acceder utilizando `$?`, que mostrará `42`.

### Ejemplo 2: Control de flujo con return
```bash
verificar_numero() {
    if [ $1 -gt 10 ]; then
        return 1  # Número mayor que 10
    else
        return 0  # Número menor o igual a 10
    fi
}

verificar_numero 15
if [ $? -eq 1 ]; then
    echo "El número es mayor que 10."
else
    echo "El número es menor o igual a 10."
fi
```
En este caso, la función `verificar_numero` devuelve `1` si el número es mayor que `10` y `0` en caso contrario. Dependiendo del valor de retorno, se imprime un mensaje correspondiente.

## Tips
- Siempre utiliza `return` dentro de funciones para asegurar que el valor de retorno sea claro y significativo.
- Recuerda que el valor de retorno debe ser un número entero entre `0` y `255`. Cualquier otro valor puede no ser manejado correctamente.
- Utiliza `$?` inmediatamente después de llamar a una función para capturar el valor de retorno, ya que este valor se sobrescribirá con el siguiente comando ejecutado.