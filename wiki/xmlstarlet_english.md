# [Linux] Bash xmlstarlet uso: A command-line XML toolkit

## Overview
The `xmlstarlet` command is a versatile command-line utility for parsing, transforming, and querying XML documents. It allows users to manipulate XML data easily, making it a valuable tool for developers and system administrators working with XML files.

## Usage
The basic syntax of the `xmlstarlet` command is as follows:

```bash
xmlstarlet [options] [arguments]
```

## Common Options
- `xmlstarlet sel`: Selects nodes from an XML document.
- `xmlstarlet ed`: Edits an XML document.
- `xmlstarlet tr`: Transforms an XML document using XSLT.
- `xmlstarlet val`: Validates an XML document against a schema.
- `xmlstarlet fo`: Formats an XML document for readability.

## Common Examples

### Selecting Nodes
To select specific nodes from an XML file, you can use the `sel` option. For example, to select all `book` elements from a `books.xml` file:

```bash
xmlstarlet sel -t -m "//book" -v "title" -n books.xml
```

### Editing XML
To add a new element to an existing XML document, use the `ed` option. For instance, to add a new `author` to a `book`:

```bash
xmlstarlet ed -s "//book" -t elem -n "author" -v "New Author" books.xml
```

### Transforming XML
To transform an XML document using an XSLT stylesheet, use the `tr` option. Here’s an example:

```bash
xmlstarlet tr stylesheet.xsl input.xml > output.xml
```

### Validating XML
To validate an XML file against a schema, use the `val` option. For example:

```bash
xmlstarlet val -e schema.xsd input.xml
```

### Formatting XML
To format an XML file for better readability, use the `fo` option:

```bash
xmlstarlet fo input.xml
```

## Tips
- Always back up your XML files before performing edits, as changes can be irreversible.
- Use the `-n` option with `sel` to suppress the output of the selected nodes if you only need to check the existence of nodes.
- Combine multiple options in a single command for more complex operations, such as selecting and transforming XML data in one go.