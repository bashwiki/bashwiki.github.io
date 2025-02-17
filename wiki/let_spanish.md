# [Linux] Bash let uso: Realiza cálculos aritméticos

## Overview
El comando `let` en Bash se utiliza para realizar cálculos aritméticos de manera sencilla. Permite evaluar expresiones matemáticas y asignar resultados a variables sin necesidad de utilizar la sintaxis de `$((...))`.

## Usage
La sintaxis básica del comando `let` es la siguiente:

```bash
let [expresión]
```

## Common Options
El comando `let` no tiene muchas opciones, ya que su uso principal es la evaluación de expresiones. Sin embargo, se pueden mencionar algunas consideraciones:

- `-`: Se utiliza para restar.
- `+`: Se utiliza para sumar.
- `*`: Se utiliza para multiplicar.
- `/`: Se utiliza para dividir.
- `%`: Se utiliza para obtener el residuo de una división.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `let`:

1. **Suma de dos números:**
   ```bash
   let a=5
   let b=10
   let suma=a+b
   echo $suma  # Salida: 15
   ```

2. **Resta de dos números:**
   ```bash
   let a=20
   let b=8
   let resta=a-b
   echo $resta  # Salida: 12
   ```

3. **Multiplicación:**
   ```bash
   let a=4
   let b=3
   let producto=a*b
   echo $producto  # Salida: 12
   ```

4. **División:**
   ```bash
   let a=10
   let b=2
   let division=a/b
   echo $division  # Salida: 5
   ```

5. **Uso de variables en una expresión:**
   ```bash
   let x=5
   let y=3
   let resultado=x*y+10
   echo $resultado  # Salida: 25
   ```

## Tips
- Utiliza `let` cuando necesites realizar cálculos simples y no quieras usar la sintaxis más compleja de `$((...))`.
- Recuerda que `let` no requiere el uso de `$` antes de las variables dentro de la expresión.
- Si necesitas realizar operaciones más complejas o trabajar con números en punto flotante, considera usar `bc` o `awk` en su lugar.