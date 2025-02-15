# [리눅스] Bash bc 사용법

## Overview
El comando `bc` (Basic Calculator) es una calculadora de precisión arbitraria que se utiliza en sistemas Unix y Linux. Su propósito principal es realizar cálculos matemáticos complejos y operaciones aritméticas en la línea de comandos. `bc` es especialmente útil para ingenieros y desarrolladores que necesitan realizar cálculos precisos y que requieren más funcionalidad que la que ofrece la calculadora básica de Bash.

## Usage
La sintaxis básica del comando `bc` es la siguiente:

```bash
bc [opciones] [archivo]
```

### Opciones comunes:
- `-l`: Carga la biblioteca matemática estándar, que incluye funciones matemáticas como seno, coseno, logaritmo, etc.
- `-q`: Inicia `bc` en modo silencioso, sin mostrar el banner de inicio.
- `-e`: Permite ejecutar expresiones directamente desde la línea de comandos.

## Examples
### Ejemplo 1: Cálculo simple
Para realizar un cálculo simple, puedes usar `bc` directamente en la línea de comandos:

```bash
echo "3 + 5" | bc
```
Este comando devolverá `8`, que es el resultado de la suma.

### Ejemplo 2: Usando la biblioteca matemática
Si deseas realizar cálculos más complejos, como calcular el seno de un ángulo, puedes utilizar la opción `-l`:

```bash
echo "scale=4; s(1)" | bc -l
```
Este comando calculará el seno de 1 radian, y el resultado será `0.8415`, redondeado a cuatro decimales.

## Tips
- **Escala**: Usa la variable `scale` para definir el número de decimales en los resultados. Por ejemplo, `scale=2; 10/3` devolverá `3.33`.
- **Uso de variables**: Puedes asignar valores a variables en `bc` para simplificar cálculos complejos. Por ejemplo:
  ```bash
  echo "a=5; b=10; a*b" | bc
  ```
  Esto devolverá `50`.
- **Modo interactivo**: Puedes iniciar `bc` sin argumentos para entrar en un modo interactivo donde puedes realizar cálculos de forma continua hasta que decidas salir escribiendo `quit`.

Con estos conceptos y ejemplos, podrás utilizar `bc` de manera efectiva para realizar cálculos en tus proyectos de ingeniería y desarrollo.