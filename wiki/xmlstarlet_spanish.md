# [Linux] Bash xmlstarlet uso: Manipulación y transformación de XML

## Overview
El comando `xmlstarlet` es una herramienta de línea de comandos que permite manipular y transformar archivos XML. Proporciona una variedad de funciones para consultar, modificar y validar documentos XML de manera eficiente.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
xmlstarlet [opciones] [argumentos]
```

## Common Options
- `xmlstarlet sel`: Selecciona nodos de un documento XML.
- `xmlstarlet ed`: Edita un documento XML.
- `xmlstarlet val`: Valida un documento XML contra un esquema.
- `xmlstarlet tr`: Transforma un documento XML usando XSLT.
- `xmlstarlet fo`: Formatea un documento XML para mejorar su legibilidad.

## Common Examples

### Seleccionar nodos
Para seleccionar todos los nodos `<nombre>` de un archivo XML:

```bash
xmlstarlet sel -t -m "//nombre" -v "." -n archivo.xml
```

### Editar un documento XML
Para agregar un nuevo nodo `<edad>` con el valor `30` a cada nodo `<persona>`:

```bash
xmlstarlet ed -u "//persona" -v "30" -n "edad" archivo.xml
```

### Validar un documento XML
Para validar un archivo XML contra un esquema XSD:

```bash
xmlstarlet val -e esquema.xsd archivo.xml
```

### Transformar un documento XML
Para transformar un archivo XML usando un archivo XSLT:

```bash
xmlstarlet tr transformacion.xsl archivo.xml
```

### Formatear un documento XML
Para formatear un archivo XML y mejorar su legibilidad:

```bash
xmlstarlet fo archivo.xml
```

## Tips
- Siempre realiza una copia de seguridad de tus archivos XML antes de hacer modificaciones.
- Utiliza `xmlstarlet fo` para verificar la estructura de tu XML antes de realizar cambios.
- Familiarízate con XPath, ya que es fundamental para seleccionar nodos de manera efectiva con `xmlstarlet sel`.