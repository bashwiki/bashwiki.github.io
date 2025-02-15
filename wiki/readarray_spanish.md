# [리눅스] Bash readarray 사용법

## Overview
El comando `readarray` en Bash se utiliza para leer líneas de un archivo o de la entrada estándar y almacenarlas en un array. Este comando es especialmente útil cuando se trabaja con datos en formato de texto, ya que permite manipular fácilmente cada línea como un elemento del array. `readarray` es una forma eficiente de manejar múltiples líneas de texto sin necesidad de bucles adicionales.

## Usage
La sintaxis básica del comando `readarray` es la siguiente:

```bash
readarray [opciones] array_name
```

### Opciones Comunes:
- `-t`: Esta opción elimina el carácter de nueva línea al final de cada línea leída, lo que es útil para evitar que los elementos del array contengan saltos de línea.
- `-n`: Permite especificar el número de líneas a leer. Por ejemplo, `-n 5` leerá solo las primeras 5 líneas.
- `-s`: Esta opción permite omitir un número específico de líneas al inicio del archivo o de la entrada.

## Examples
### Ejemplo 1: Leer un archivo en un array
Supongamos que tenemos un archivo llamado `datos.txt` que contiene varias líneas de texto. Podemos leer este archivo en un array de la siguiente manera:

```bash
readarray -t lineas < datos.txt
```

En este ejemplo, cada línea del archivo `datos.txt` se almacenará como un elemento en el array `lineas`, sin los caracteres de nueva línea.

### Ejemplo 2: Leer solo algunas líneas
Si solo queremos leer las primeras 3 líneas de un archivo, podemos usar la opción `-n`:

```bash
readarray -t lineas < <(head -n 3 datos.txt)
```

Aquí, estamos utilizando `head` para limitar la entrada a las primeras 3 líneas antes de pasarlas a `readarray`.

## Tips
- Siempre que sea posible, utiliza la opción `-t` para evitar problemas con los caracteres de nueva línea en los elementos del array.
- Si estás leyendo grandes archivos, considera utilizar `-n` y `-s` para optimizar el rendimiento y evitar cargar más datos de los necesarios.
- Puedes acceder a los elementos del array utilizando la sintaxis `${array_name[index]}`. Por ejemplo, `${lineas[0]}` te dará la primera línea leída.

Con estos consejos y ejemplos, deberías estar bien preparado para utilizar el comando `readarray` en tus scripts de Bash.