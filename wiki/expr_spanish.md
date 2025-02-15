# [리눅스] Bash expr 사용법

## Overview
El comando `expr` en Bash es una herramienta utilizada para evaluar expresiones aritméticas, lógicas y de comparación. Su propósito principal es realizar cálculos simples y manipular cadenas de texto desde la línea de comandos. Aunque su uso ha disminuido con la llegada de herramientas más modernas, sigue siendo útil en scripts donde se necesita realizar operaciones básicas.

## Usage
La sintaxis básica del comando `expr` es la siguiente:

```bash
expr EXPRESIÓN
```

Donde `EXPRESIÓN` puede ser una operación aritmética, lógica o de comparación. Aquí hay algunas opciones comunes que puedes utilizar con `expr`:

- **Aritmética**: Puedes realizar operaciones como suma (`+`), resta (`-`), multiplicación (`*`), división (`/`) y módulo (`%`).
- **Comparación**: Puedes comparar valores usando operadores como `=` (igual), `!=` (diferente), `<` (menor que), `>` (mayor que), `<=` (menor o igual que), `>=` (mayor o igual que).
- **Cadenas**: Puedes evaluar cadenas para verificar su longitud o compararlas.

## Examples
Aquí hay algunos ejemplos prácticos de cómo usar el comando `expr`:

1. **Suma de dos números**:
   ```bash
   resultado=$(expr 5 + 3)
   echo "La suma es: $resultado"
   ```
   Este comando suma 5 y 3, y almacena el resultado en la variable `resultado`, que luego se imprime en la consola.

2. **Comparación de cadenas**:
   ```bash
   cadena1="hola"
   cadena2="mundo"
   if expr "$cadena1" = "$cadena2" >/dev/null; then
       echo "Las cadenas son iguales"
   else
       echo "Las cadenas son diferentes"
   fi
   ```
   Este ejemplo compara dos cadenas y muestra un mensaje dependiendo de si son iguales o no.

## Tips
- **Uso de comillas**: Es recomendable usar comillas alrededor de las variables y cadenas para evitar errores, especialmente si contienen espacios.
- **Evitar espacios**: Asegúrate de no dejar espacios alrededor de los operadores, ya que esto puede causar errores en la evaluación.
- **Alternativas**: Considera usar `(( ))` para operaciones aritméticas más complejas o `[[ ]]` para comparaciones, ya que son más modernas y ofrecen más funcionalidades.

El comando `expr` es una herramienta simple pero poderosa para realizar cálculos y comparaciones en Bash, ideal para scripts rápidos y eficientes.