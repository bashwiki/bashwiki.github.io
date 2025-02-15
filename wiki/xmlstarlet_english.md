# [리눅스] Bash xmlstarlet 사용법

## Overview
`xmlstarlet` is a command-line utility designed for parsing, transforming, and querying XML documents. It provides a suite of tools for working with XML data, allowing users to perform various operations such as validation, transformation, and extraction of information. Its primary purpose is to facilitate the manipulation of XML files in a straightforward and scriptable manner, making it an essential tool for developers and engineers who work with XML data.

## Usage
The basic syntax for using `xmlstarlet` is as follows:

```bash
xmlstarlet [command] [options] [file]
```

### Common Commands and Options:
- `xmlstarlet val`: Validate an XML document against a DTD or XML Schema.
- `xmlstarlet sel`: Select and extract data from an XML document using XPath expressions.
- `xmlstarlet ed`: Edit an XML document, allowing for the addition, modification, or deletion of nodes.
- `xmlstarlet tr`: Transform an XML document using XSLT.
- `xmlstarlet fo`: Format an XML document for better readability.

### Common Options:
- `-u`: Update the XML document in place.
- `-o`: Output the result to standard output.
- `-n`: Suppress the output of the XML declaration.

## Examples

### Example 1: Validating an XML Document
To validate an XML file against a DTD, you can use the following command:

```bash
xmlstarlet val -d myfile.dtd myfile.xml
```

This command checks `myfile.xml` against the DTD defined in `myfile.dtd` and returns any validation errors.

### Example 2: Extracting Data with XPath
To select specific nodes from an XML file, you can use the `sel` command. For example, to extract all the titles from a book list XML:

```bash
xmlstarlet sel -t -m "//book" -v "title" -n books.xml
```

This command will output the titles of all books found in `books.xml`, each on a new line.

## Tips
- When working with large XML files, consider using `xmlstarlet` in combination with other command-line tools like `grep` or `awk` for more complex data processing.
- Always validate your XML documents after editing to ensure they conform to the expected structure.
- Familiarize yourself with XPath syntax, as it is crucial for effectively using the `sel` command to extract data from XML files.
- Use the `-o` option to redirect output to a new file if you want to save the results of your operations without modifying the original XML file.