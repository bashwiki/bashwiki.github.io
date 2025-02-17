# [Linux] Bash typeset uso: Definir variables y sus atributos

## Overview
El comando `typeset` en Bash se utiliza para declarar variables y establecer sus atributos. Permite definir variables locales en funciones, así como especificar características como la inmutabilidad o el tipo de datos.

## Usage
La sintaxis básica del comando `typeset` es la siguiente:

```bash
typeset [opciones] [argumentos]
```

## Common Options
- `-i`: Define la variable como un entero, permitiendo operaciones matemáticas.
- `-r`: Establece la variable como de solo lectura, impidiendo su modificación.
- `-a`: Declara la variable como un array.
- `-x`: Exporta la variable al entorno, haciéndola disponible para los procesos hijos.

## Common Examples

### Definir una variable entera
```bash
typeset -i numero=10
echo $numero  # Salida: 10
```

### Crear una variable de solo lectura
```bash
typeset -r constante="ValorInmutable"
echo $constante  # Salida: ValorInmutable
# constante="NuevoValor"  # Esto generará un error
```

### Declarar un array
```bash
typeset -a frutas
frutas=("manzana" "banana" "cereza")
echo ${frutas[1]}  # Salida: banana
```

### Exportar una variable
```bash
typeset -x variableExportada="Hola"
echo $variableExportada  # Salida: Hola
```

## Tips
- Utiliza `typeset` dentro de funciones para mantener las variables locales y evitar conflictos con variables globales.
- Recuerda que las variables de solo lectura no pueden ser modificadas, así que úsalas para valores que no deben cambiar.
- Al trabajar con arrays, asegúrate de inicializarlos correctamente para evitar errores en el acceso a los elementos.