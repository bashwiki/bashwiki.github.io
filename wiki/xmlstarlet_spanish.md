# [리눅스] Bash xmlstarlet 사용법

## Overview
`xmlstarlet` es una herramienta de línea de comandos para procesar y manipular archivos XML. Su propósito principal es permitir a los desarrolladores y administradores de sistemas realizar operaciones como la transformación, validación, y consulta de datos en archivos XML de manera eficiente. `xmlstarlet` es especialmente útil para automatizar tareas relacionadas con XML en scripts de Bash.

## Usage
La sintaxis básica del comando `xmlstarlet` es la siguiente:

```bash
xmlstarlet [opciones] [comando] [archivo.xml]
```

Algunas de las opciones y comandos más comunes son:

- `xmlstarlet sel`: Selecciona nodos de un archivo XML usando XPath.
- `xmlstarlet ed`: Edita un archivo XML, permitiendo agregar, modificar o eliminar nodos.
- `xmlstarlet val`: Valida un archivo XML contra un esquema DTD o XSD.
- `xmlstarlet tr`: Transforma un archivo XML usando XSLT.

## Examples

### Ejemplo 1: Seleccionar nodos
Supongamos que tenemos un archivo XML llamado `datos.xml` y queremos seleccionar todos los elementos `<nombre>`.

```bash
xmlstarlet sel -t -m "//nombre" -v "." -n datos.xml
```

En este ejemplo, `-t` indica que se va a utilizar una plantilla, `-m` especifica el patrón de búsqueda (XPath), `-v` imprime el valor del nodo seleccionado, y `-n` añade una nueva línea después de cada resultado.

### Ejemplo 2: Editar un archivo XML
Si queremos agregar un nuevo elemento `<edad>` a un nodo existente `<persona>` en `datos.xml`, podemos usar el siguiente comando:

```bash
xmlstarlet ed -s "//persona" -t -n "edad" -v "30" datos.xml
```

Aquí, `-s` se utiliza para agregar un nuevo nodo, `-t` indica que estamos creando un nuevo nodo, `-n` especifica el nombre del nuevo nodo, y `-v` establece su valor.

## Tips
- Siempre es recomendable hacer una copia de seguridad de los archivos XML antes de realizar modificaciones, especialmente cuando se utilizan comandos de edición.
- Familiarízate con XPath, ya que es fundamental para seleccionar nodos de manera efectiva con `xmlstarlet`.
- Utiliza la opción `--help` para obtener más información sobre las opciones y comandos disponibles en `xmlstarlet`:

```bash
xmlstarlet --help
```

Con estos conocimientos, podrás utilizar `xmlstarlet` de manera efectiva para manejar archivos XML en tus proyectos.