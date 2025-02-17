# [Linux] Bash getopts Uso: [analizar opciones de línea de comandos]

## Overview
El comando `getopts` en Bash se utiliza para analizar opciones y argumentos de línea de comandos en scripts. Permite a los desarrolladores manejar entradas de usuario de manera estructurada, facilitando la creación de scripts más robustos y flexibles.

## Usage
La sintaxis básica del comando `getopts` es la siguiente:

```bash
getopts [options] [arguments]
```

## Common Options
- `-a`: Permite especificar opciones adicionales.
- `-l`: Permite el uso de opciones largas.
- `-n`: Establece el nombre del script que se mostrará en los mensajes de error.

## Common Examples

### Ejemplo 1: Análisis de opciones simples
Este ejemplo muestra cómo analizar opciones simples con `getopts`.

```bash
#!/bin/bash

while getopts "ab:c" opt; do
  case $opt in
    a)
      echo "Opción A activada"
      ;;
    b)
      echo "Opción B con argumento: $OPTARG"
      ;;
    c)
      echo "Opción C activada"
      ;;
    *)
      echo "Opción no válida"
      ;;
  esac
done
```

### Ejemplo 2: Uso de opciones largas
Aquí se muestra cómo usar `getopts` con opciones largas.

```bash
#!/bin/bash

while getopts ":a:b:c:" opt; do
  case $opt in
    a)
      echo "Opción A activada"
      ;;
    b)
      echo "Opción B con argumento: $OPTARG"
      ;;
    c)
      echo "Opción C activada"
      ;;
    \?)
      echo "Opción no válida: -$OPTARG" >&2
      ;;
    :)
      echo "La opción -$OPTARG requiere un argumento." >&2
      ;;
  esac
done
```

### Ejemplo 3: Manejo de errores
Este ejemplo muestra cómo manejar errores con `getopts`.

```bash
#!/bin/bash

while getopts ":a:b:c" opt; do
  case $opt in
    a)
      echo "Opción A activada"
      ;;
    b)
      echo "Opción B con argumento: $OPTARG"
      ;;
    c)
      echo "Opción C activada"
      ;;
    \?)
      echo "Opción no válida: -$OPTARG" >&2
      ;;
    :)
      echo "La opción -$OPTARG requiere un argumento." >&2
      ;;
  esac
done
```

## Tips
- Siempre inicializa las variables antes de usarlas para evitar errores.
- Usa `OPTIND` para restablecer el índice de opciones si necesitas volver a analizar argumentos.
- Considera el uso de un bucle `while` para manejar múltiples opciones de manera eficiente.