# [리눅스] Bash uniq 사용법

## Overview
El comando `uniq` en Bash se utiliza para filtrar líneas duplicadas en un archivo o en la entrada estándar. Su propósito principal es identificar y eliminar las líneas repetidas, mostrando solo una instancia de cada línea única. Este comando es especialmente útil cuando se trabaja con archivos de texto que contienen datos repetidos y se desea simplificar la información.

## Usage
La sintaxis básica del comando `uniq` es la siguiente:

```bash
uniq [opciones] [archivo]
```

### Opciones comunes:
- `-c`: Cuenta y muestra el número de ocurrencias de cada línea.
- `-d`: Muestra solo las líneas que están duplicadas.
- `-u`: Muestra solo las líneas que son únicas (no duplicadas).
- `-i`: Ignora las diferencias entre mayúsculas y minúsculas al comparar líneas.

## Examples
### Ejemplo 1: Filtrar líneas duplicadas
Supongamos que tenemos un archivo llamado `datos.txt` que contiene las siguientes líneas:

```
manzana
naranja
manzana
plátano
naranja
```

Para filtrar las líneas duplicadas y mostrar solo las únicas, se puede usar el siguiente comando:

```bash
uniq datos.txt
```

La salida será:

```
manzana
naranja
plátano
```

### Ejemplo 2: Contar líneas duplicadas
Si queremos contar cuántas veces aparece cada línea en el archivo, podemos usar la opción `-c`:

```bash
uniq -c datos.txt
```

La salida será:

```
      2 manzana
      2 naranja
      1 plátano
```

## Tips
- Asegúrate de que el archivo de entrada esté ordenado antes de usar `uniq`, ya que este comando solo elimina duplicados que están adyacentes. Puedes usar el comando `sort` para ordenar el archivo primero.
- Combina `uniq` con otros comandos de Bash utilizando tuberías (`|`) para procesar datos de manera más eficiente. Por ejemplo, puedes usar `cat` y `sort` junto con `uniq` para obtener un conteo de líneas únicas en un archivo:

```bash
cat datos.txt | sort | uniq -c
```

Siguiendo estos consejos y ejemplos, podrás utilizar el comando `uniq` de manera efectiva en tus proyectos y tareas de desarrollo.