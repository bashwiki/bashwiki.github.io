# [리눅스] Bash printf 사용법

## Overview
El comando `printf` en Bash se utiliza para formatear y mostrar texto en la salida estándar. Su propósito principal es ofrecer un control más preciso sobre la presentación de los datos en comparación con el comando `echo`. `printf` permite especificar el formato de salida, lo que es especialmente útil para la creación de informes, la depuración y la visualización de datos de manera estructurada.

## Usage
La sintaxis básica del comando `printf` es la siguiente:

```bash
printf "formato" [argumentos...]
```

### Opciones comunes:
- **%s**: Formato para cadenas de texto.
- **%d**: Formato para enteros.
- **%f**: Formato para números de punto flotante.
- **%x**: Formato para números en hexadecimal.
- **\n**: Nueva línea.
- **\t**: Tabulación.

## Examples
### Ejemplo 1: Formatear una cadena
```bash
printf "Hola, %s!\n" "Mundo"
```
Este comando imprimirá: `Hola, Mundo!`

### Ejemplo 2: Formatear múltiples valores
```bash
printf "Nombre: %s, Edad: %d, Altura: %.2f m\n" "Juan" 30 1.75
```
Este comando imprimirá: `Nombre: Juan, Edad: 30, Altura: 1.75 m`

## Tips
- Utiliza `printf` en lugar de `echo` cuando necesites un formato específico o cuando estés trabajando con caracteres especiales que pueden ser interpretados de manera diferente por `echo`.
- Recuerda que `printf` no agrega automáticamente una nueva línea al final de la salida, a menos que lo especifiques con `\n`.
- Puedes utilizar el modificador de ancho y precisión para controlar la longitud de la salida. Por ejemplo, `%.2f` limitará un número de punto flotante a dos decimales.
- Al usar `printf` en scripts, asegúrate de que el formato y los argumentos coincidan para evitar errores de salida inesperados.