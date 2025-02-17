# [Linux] Bash column uso: Format text into columns

## Overview
The `column` command in Bash is used to format text input into neatly aligned columns. It is particularly useful for organizing data output from other commands or files, making it easier to read and interpret.

## Usage
The basic syntax of the `column` command is as follows:

```bash
column [options] [arguments]
```

## Common Options
- `-t`: Create a table by determining the number of columns based on whitespace.
- `-s <char>`: Specify a delimiter character to separate columns (default is whitespace).
- `-n`: Suppress the output of the column header.
- `-x`: Fill columns before filling rows, which can be useful for certain layouts.

## Common Examples

### Example 1: Basic Column Formatting
To format a simple list of items into columns:

```bash
echo -e "Name\nAlice\nBob\nCharlie" | column
```

### Example 2: Using a Custom Delimiter
If you have a CSV file and want to format it using a comma as a delimiter:

```bash
cat data.csv | column -s, -t
```

### Example 3: Creating a Table
You can create a table from space-separated values:

```bash
echo -e "ID Name\n1 Alice\n2 Bob\n3 Charlie" | column -t
```

### Example 4: Filling Columns First
To fill columns before rows, you can use the `-x` option:

```bash
echo -e "A\nB\nC\nD\nE\nF" | column -x
```

## Tips
- Always use the `-t` option for better readability when dealing with space-separated data.
- When working with files, consider using `cat` or redirection to pipe the contents into `column`.
- Experiment with different delimiters using the `-s` option to see what works best for your data format.