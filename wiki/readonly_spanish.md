# [Linux] Bash readonly Uso equivalente: Establecer variables como solo lectura

## Overview
El comando `readonly` en Bash se utiliza para marcar variables como solo lectura. Esto significa que una vez que una variable ha sido declarada como `readonly`, su valor no puede ser modificado ni eliminada durante la sesión actual del shell.

## Usage
La sintaxis básica del comando `readonly` es la siguiente:

```bash
readonly [nombre_variable]
```

## Common Options
- `-p`: Muestra una lista de todas las variables que han sido marcadas como solo lectura.

## Common Examples

### Ejemplo 1: Crear una variable de solo lectura
```bash
readonly MI_VARIABLE="Hola, mundo"
```
En este ejemplo, `MI_VARIABLE` se establece como una variable de solo lectura.

### Ejemplo 2: Intentar modificar una variable de solo lectura
```bash
readonly MI_VARIABLE="Hola, mundo"
MI_VARIABLE="Nuevo valor"  # Esto generará un error
```
Aquí, se intenta cambiar el valor de `MI_VARIABLE`, lo que resultará en un error porque es de solo lectura.

### Ejemplo 3: Listar variables de solo lectura
```bash
readonly -p
```
Este comando mostrará todas las variables que han sido marcadas como solo lectura en el entorno actual.

## Tips
- Utiliza `readonly` para proteger variables importantes que no deben ser modificadas accidentalmente.
- Recuerda que `readonly` solo afecta a la sesión actual del shell; al cerrar la terminal, las variables no se mantendrán como solo lectura en futuras sesiones.
- Puedes usar `declare -r` como una alternativa para declarar variables de solo lectura, que funciona de manera similar.