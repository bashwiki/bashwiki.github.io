# [리눅스] Bash rev 사용법

## Overview
El comando `rev` en Bash se utiliza para invertir el orden de los caracteres en cada línea de un archivo o de la entrada estándar. Su propósito principal es facilitar la manipulación de cadenas de texto al permitir que los desarrolladores y ingenieros puedan ver o procesar datos en un formato invertido, lo que puede ser útil en diversas aplicaciones, como la depuración o el análisis de datos.

## Usage
La sintaxis básica del comando `rev` es la siguiente:

```bash
rev [opciones] [archivo]
```

### Opciones Comunes
- `-` o `--`: Si no se especifica un archivo, `rev` lee desde la entrada estándar.
- `archivo`: Especifica el archivo del cual se desea invertir el contenido línea por línea.

## Examples
### Ejemplo 1: Invertir texto desde un archivo
Supongamos que tenemos un archivo llamado `texto.txt` con el siguiente contenido:

```
Hola
Mundo
```

Para invertir el contenido de este archivo, se puede usar el siguiente comando:

```bash
rev texto.txt
```

La salida será:

```
aloH
odnuM
```

### Ejemplo 2: Invertir texto desde la entrada estándar
También se puede utilizar `rev` para invertir texto ingresado directamente en la terminal. Por ejemplo:

```bash
echo "Ingeniería" | rev
```

La salida será:

```
airénegnI
```

## Tips
- `rev` es especialmente útil en scripts donde se necesita manipular cadenas de texto de manera rápida y sencilla.
- Combina `rev` con otros comandos de Unix, como `sort` o `uniq`, para realizar análisis más complejos. Por ejemplo, puedes invertir líneas y luego ordenarlas.
- Recuerda que `rev` invierte los caracteres en cada línea de forma independiente, por lo que el resultado puede no ser lo que esperas si no se considera la estructura del texto original.