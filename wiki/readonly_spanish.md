# [리눅스] Bash readonly 사용법

## Overview
El comando `readonly` en Bash se utiliza para marcar variables como de solo lectura. Una vez que una variable ha sido declarada como `readonly`, su valor no puede ser modificado ni eliminada durante la sesión actual del shell. Esto es útil para proteger variables que no deben cambiar a lo largo de la ejecución de un script o en la línea de comandos, asegurando así la integridad de los datos.

## Usage
La sintaxis básica del comando `readonly` es la siguiente:

```bash
readonly VARIABLE_NAME=valor
```

También puedes usar `readonly` para marcar una variable ya existente como de solo lectura:

```bash
readonly VARIABLE_NAME
```

### Opciones Comunes
- No hay opciones adicionales para el comando `readonly`. Su funcionalidad se centra únicamente en establecer variables como de solo lectura.

## Examples
### Ejemplo 1: Declarar una variable como de solo lectura
```bash
readonly PI=3.14159
echo $PI  # Salida: 3.14159
```
En este ejemplo, la variable `PI` se establece como de solo lectura. Si intentas cambiar su valor, recibirás un error.

### Ejemplo 2: Intentar modificar una variable de solo lectura
```bash
readonly NAME="Juan"
NAME="Pedro"  # Esto generará un error: bash: NAME: readonly variable
```
Aquí, intentamos cambiar el valor de `NAME`, pero dado que es una variable de solo lectura, Bash generará un error.

## Tips
- Utiliza `readonly` para variables que contienen configuraciones o valores críticos que no deben cambiar durante la ejecución del script.
- Puedes listar todas las variables de solo lectura en tu sesión actual utilizando el comando `declare -r` o `readonly` sin argumentos.
- Recuerda que `readonly` solo afecta a la sesión actual del shell. Si cierras la terminal o inicias una nueva sesión, las variables de solo lectura no se mantendrán.

El uso adecuado de `readonly` puede ayudar a prevenir errores en scripts y asegurar que ciertos valores permanezcan constantes a lo largo de la ejecución.