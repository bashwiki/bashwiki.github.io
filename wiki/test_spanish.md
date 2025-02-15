# [리눅스] Bash test 사용법

## Overview
El comando `test` en Bash se utiliza para evaluar expresiones condicionales. Su propósito principal es permitir a los scripts de shell realizar pruebas sobre archivos, cadenas y valores numéricos. Dependiendo del resultado de la evaluación, el comando devuelve un código de salida que puede ser utilizado para tomar decisiones dentro de un script.

## Usage
La sintaxis básica del comando `test` es la siguiente:

```bash
test EXPRESIÓN
```

O, alternativamente, se puede utilizar el corchete:

```bash
[ EXPRESIÓN ]
```

### Opciones Comunes
- `-e archivo`: Verifica si el archivo existe.
- `-d archivo`: Comprueba si el archivo es un directorio.
- `-f archivo`: Verifica si el archivo es un archivo regular.
- `-z cadena`: Comprueba si la longitud de la cadena es cero.
- `-n cadena`: Verifica si la longitud de la cadena es mayor que cero.
- `NUM1 -eq NUM2`: Comprueba si NUM1 es igual a NUM2.
- `NUM1 -ne NUM2`: Comprueba si NUM1 no es igual a NUM2.
- `NUM1 -lt NUM2`: Comprueba si NUM1 es menor que NUM2.
- `NUM1 -gt NUM2`: Comprueba si NUM1 es mayor que NUM2.

## Examples
### Ejemplo 1: Verificar la existencia de un archivo
```bash
if test -e archivo.txt; then
    echo "El archivo existe."
else
    echo "El archivo no existe."
fi
```

### Ejemplo 2: Comparar dos números
```bash
num1=10
num2=20

if test $num1 -lt $num2; then
    echo "$num1 es menor que $num2."
else
    echo "$num1 no es menor que $num2."
fi
```

## Tips
- Utiliza el comando `test` dentro de estructuras de control como `if` para tomar decisiones basadas en las evaluaciones.
- Recuerda que el comando `test` devuelve un código de salida de 0 si la prueba es verdadera y 1 si es falsa. Esto es útil para encadenar condiciones en scripts más complejos.
- Puedes usar corchetes `[` y `]` como una forma más legible de escribir el comando `test`, pero asegúrate de dejar un espacio después de `[` y antes de `]`.