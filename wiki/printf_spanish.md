# [Linux] Bash printf Uso: Formatear y mostrar texto

## Overview
El comando `printf` en Bash se utiliza para formatear y mostrar texto en la salida estándar. Es similar a la función `printf` en lenguajes de programación como C, permitiendo un control preciso sobre la presentación de los datos.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
printf [opciones] [argumentos]
```

## Common Options
- `-v nombre`: Asigna el resultado a una variable en lugar de imprimirlo.
- `--help`: Muestra la ayuda sobre el uso del comando.
- `--version`: Muestra la versión del comando `printf`.

## Common Examples

1. **Imprimir texto simple:**
   ```bash
   printf "Hola, mundo!\n"
   ```

2. **Formatear números:**
   ```bash
   printf "Número: %.2f\n" 3.14159
   ```

3. **Imprimir múltiples líneas:**
   ```bash
   printf "Línea 1\nLínea 2\nLínea 3\n"
   ```

4. **Alinear texto:**
   ```bash
   printf "|%-10s|%10s|\n" "Izquierda" "Derecha"
   ```

5. **Asignar a una variable:**
   ```bash
   printf -v mensaje "El resultado es: %d" 42
   echo "$mensaje"
   ```

## Tips
- Utiliza `\n` para insertar saltos de línea en el texto.
- Aprovecha el formateo de números para controlar la cantidad de decimales.
- Recuerda que `printf` no añade automáticamente un salto de línea al final, a diferencia de `echo`.