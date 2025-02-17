# [Linux] Bash tr <Uso equivalente en español>: Convertir y traducir caracteres

## Overview
El comando `tr` en Bash se utiliza para traducir o eliminar caracteres de la entrada estándar. Es especialmente útil para manipular texto en scripts y en la línea de comandos.

## Usage
La sintaxis básica del comando `tr` es la siguiente:

```bash
tr [opciones] [argumentos]
```

## Common Options
- `-d`: Elimina los caracteres especificados.
- `-s`: Suprime las secuencias repetidas de caracteres.
- `-c`: Complementa el conjunto de caracteres especificado.

## Common Examples

1. **Convertir minúsculas a mayúsculas:**

```bash
echo "hola mundo" | tr 'a-z' 'A-Z'
```

Este comando convierte todas las letras minúsculas en mayúsculas.

2. **Eliminar caracteres específicos:**

```bash
echo "hola mundo" | tr -d 'o'
```

Este comando elimina todas las letras 'o' de la cadena.

3. **Suprimir espacios en blanco repetidos:**

```bash
echo "hola    mundo" | tr -s ' '
```

Este comando convierte múltiples espacios en un solo espacio.

4. **Complementar caracteres:**

```bash
echo "hola mundo" | tr -c 'a-zA-Z' ' '
```

Este comando reemplaza todos los caracteres que no son letras por espacios.

## Tips
- Siempre prueba tus comandos con una entrada de ejemplo para asegurarte de que el resultado sea el esperado.
- Combina `tr` con otros comandos como `grep` o `awk` para realizar manipulaciones más complejas de texto.
- Recuerda que `tr` solo trabaja con caracteres y no con cadenas completas.