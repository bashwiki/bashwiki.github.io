# [Linux] Bash bc Uso equivalente en español: Calculadora de precisión arbitraria

## Overview
El comando `bc` es una calculadora de precisión arbitraria que permite realizar cálculos matemáticos en la línea de comandos de Bash. Es especialmente útil para operaciones que requieren más precisión que la que ofrece la calculadora estándar de Bash.

## Usage
La sintaxis básica del comando `bc` es la siguiente:

```bash
bc [opciones] [argumentos]
```

## Common Options
- `-l`: Carga la biblioteca matemática estándar, que incluye funciones matemáticas como seno, coseno y logaritmo.
- `-q`: Inicia `bc` en modo silencioso, sin mostrar el banner de inicio.
- `-e`: Permite ejecutar un comando específico al iniciar `bc`.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `bc`:

### Ejemplo 1: Suma simple
```bash
echo "3 + 5" | bc
```
Este comando devuelve `8`, que es el resultado de sumar 3 y 5.

### Ejemplo 2: División con precisión
```bash
echo "scale=2; 10 / 3" | bc
```
Este comando establece la escala a 2, lo que significa que el resultado será `3.33`.

### Ejemplo 3: Usando la biblioteca matemática
```bash
echo "scale=4; s(1)" | bc -l
```
Este comando calcula el seno de 1 radian, devolviendo un resultado con 4 decimales.

### Ejemplo 4: Cálculo de potencias
```bash
echo "2^10" | bc
```
Este comando calcula `2` elevado a la `10`, devolviendo `1024`.

## Tips
- Siempre establece la escala antes de realizar divisiones para evitar resultados truncados.
- Puedes usar `bc` en scripts para automatizar cálculos complejos.
- Recuerda que `bc` trabaja con números enteros por defecto, así que especifica la escala para obtener decimales.