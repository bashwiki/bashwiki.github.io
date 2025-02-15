# [리눅스] Bash awk 사용법

## Overview
`awk` es una poderosa herramienta de procesamiento de texto y análisis de datos en la línea de comandos de Bash. Su principal propósito es buscar y manipular patrones en archivos de texto o en la entrada estándar. `awk` permite a los usuarios realizar operaciones como la búsqueda, el filtrado, la transformación y la generación de informes a partir de datos estructurados, como archivos CSV o registros de logs.

## Usage
La sintaxis básica del comando `awk` es la siguiente:

```bash
awk 'pattern { action }' archivo
```

- **pattern**: Especifica la condición que debe cumplirse para que se ejecute la acción. Puede ser una expresión regular o una condición lógica.
- **action**: Especifica lo que se debe hacer cuando se cumple el patrón. Puede incluir comandos como imprimir, modificar o calcular.
- **archivo**: Es el archivo de texto que se va a procesar. Si no se especifica un archivo, `awk` leerá de la entrada estándar.

### Opciones comunes
- `-F`: Define el delimitador de campo. Por defecto, `awk` utiliza espacios en blanco como delimitador.
- `-v`: Permite definir variables de entorno que se pueden utilizar dentro del script `awk`.

## Examples

### Ejemplo 1: Imprimir la segunda columna de un archivo
Supongamos que tenemos un archivo llamado `datos.txt` con el siguiente contenido:

```
nombre edad ciudad
Juan 25 Madrid
Ana 30 Barcelona
Luis 22 Valencia
```

Para imprimir la segunda columna (edad), usaríamos el siguiente comando:

```bash
awk '{ print $2 }' datos.txt
```

### Ejemplo 2: Filtrar líneas basadas en una condición
Si queremos filtrar y mostrar solo las líneas donde la edad es mayor a 25, podemos usar:

```bash
awk '$2 > 25 { print $1, $2 }' datos.txt
```

Este comando imprimirá:

```
Ana 30
```

## Tips
- Utiliza `-F` para cambiar el delimitador si trabajas con archivos que no utilizan espacios en blanco. Por ejemplo, para un archivo CSV, puedes usar `-F,`.
- Es recomendable usar comillas simples alrededor del script `awk` para evitar que el intérprete de Bash intente interpretar las variables dentro del script.
- Puedes combinar `awk` con otros comandos de Unix mediante pipes para crear potentes cadenas de procesamiento de datos.
- Familiarízate con las funciones integradas de `awk`, como `length()`, `substr()`, y `split()`, para realizar manipulaciones más complejas en tus datos.