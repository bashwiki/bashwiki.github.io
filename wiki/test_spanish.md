# [Linux] Bash test uso: Evaluar expresiones

## Overview
El comando `test` en Bash se utiliza para evaluar expresiones condicionales. Permite comprobar condiciones como la existencia de archivos, comparaciones numéricas y de cadenas, y otros tipos de pruebas lógicas. Es fundamental en scripts para controlar el flujo de ejecución.

## Usage
La sintaxis básica del comando `test` es la siguiente:

```bash
test [opciones] [argumentos]
```

## Common Options
- `-e archivo`: Verifica si el archivo existe.
- `-f archivo`: Comprueba si el archivo es un archivo regular.
- `-d directorio`: Verifica si el directorio existe.
- `-z cadena`: Comprueba si la longitud de la cadena es cero.
- `-n cadena`: Verifica si la longitud de la cadena es mayor que cero.
- `==`: Compara dos cadenas para ver si son iguales.
- `-lt`: Comprueba si un número es menor que otro.
- `-gt`: Comprueba si un número es mayor que otro.

## Common Examples

### Verificar si un archivo existe
```bash
if test -e archivo.txt; then
    echo "El archivo existe."
else
    echo "El archivo no existe."
fi
```

### Comprobar si es un directorio
```bash
if test -d /ruta/al/directorio; then
    echo "Es un directorio."
else
    echo "No es un directorio."
fi
```

### Comparar cadenas
```bash
cadena1="hola"
cadena2="hola"

if test "$cadena1" == "$cadena2"; then
    echo "Las cadenas son iguales."
else
    echo "Las cadenas son diferentes."
fi
```

### Comparar números
```bash
numero1=5
numero2=10

if test $numero1 -lt $numero2; then
    echo "$numero1 es menor que $numero2."
else
    echo "$numero1 no es menor que $numero2."
fi
```

## Tips
- Utiliza `[[ ... ]]` en lugar de `test` para una sintaxis más moderna y flexible en Bash.
- Siempre usa comillas alrededor de las variables al comparar cadenas para evitar errores si la variable está vacía.
- Combina múltiples condiciones usando `&&` (y) o `||` (o) para crear expresiones más complejas.