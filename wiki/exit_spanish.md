# [리눅스] Bash exit 사용법

## Overview
El comando `exit` en Bash se utiliza para salir de un script o de una sesión de shell. Su propósito principal es cerrar el entorno actual y, opcionalmente, devolver un código de estado al sistema operativo. Este código de estado puede ser utilizado para indicar si el script se ejecutó correctamente o si ocurrió un error.

## Usage
La sintaxis básica del comando `exit` es la siguiente:

```bash
exit [n]
```

Donde `n` es un número entero que representa el código de salida. Si no se proporciona un número, Bash devolverá el código de salida del último comando ejecutado. Por convención, un código de salida de `0` indica éxito, mientras que cualquier otro número indica un error.

## Examples
### Ejemplo 1: Salir de un script con un código de éxito
```bash
#!/bin/bash
echo "Ejecutando el script..."
exit 0
```
En este ejemplo, el script se ejecuta y luego sale con un código de éxito (`0`).

### Ejemplo 2: Salir de un script con un código de error
```bash
#!/bin/bash
echo "Ocurrió un error."
exit 1
```
Aquí, el script informa que ocurrió un error y sale con un código de error (`1`).

## Tips
- Siempre es una buena práctica utilizar códigos de salida específicos para diferentes tipos de errores. Esto facilita la depuración y el manejo de errores en scripts más complejos.
- Puedes verificar el código de salida del último comando ejecutado utilizando la variable especial `$?`. Esto es útil para tomar decisiones en scripts basados en el éxito o fracaso de comandos anteriores.
- Al salir de un shell interactivo, simplemente escribir `exit` sin argumentos cerrará la sesión actual.