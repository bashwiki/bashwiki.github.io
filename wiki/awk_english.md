# [리눅스] Bash awk 사용법

## Overview
`awk` is a powerful text processing tool in Unix and Linux environments. It is primarily used for pattern scanning and processing, allowing users to manipulate and analyze text files or streams. With its built-in programming language, `awk` excels at tasks such as extracting specific fields from structured data, performing calculations, and generating formatted output.

## Usage
The basic syntax of the `awk` command is as follows:

```bash
awk 'pattern { action }' input_file
```

- **pattern**: This is a condition that `awk` checks for each line of the input. If the pattern matches, the associated action is executed.
- **action**: This is a block of code that defines what to do with the lines that match the pattern. If no action is specified, `awk` will print the matching lines by default.
- **input_file**: This is the file that `awk` will read. If no file is specified, `awk` reads from standard input.

### Common Options
- `-F`: Specifies the input field separator. For example, `-F,` sets the separator to a comma.
- `-v var=value`: Allows you to pass variables into the `awk` program.
- `-f file`: Allows you to specify a file containing `awk` commands instead of writing them directly in the command line.

## Examples

### Example 1: Print Specific Columns
To print the first and third columns from a CSV file, you can use the following command:

```bash
awk -F, '{ print $1, $3 }' data.csv
```

In this example, `-F,` sets the field separator to a comma, and `{ print $1, $3 }` specifies that `awk` should print the first and third columns of each line.

### Example 2: Conditional Processing
To print lines where the value in the second column is greater than 100, you can use:

```bash
awk '$2 > 100 { print $0 }' data.txt
```

Here, `$2 > 100` is the pattern that checks if the second column's value is greater than 100, and `{ print $0 }` prints the entire line if the condition is met.

## Tips
- Use `-F` to specify the correct field separator for your data; this is crucial for accurate processing.
- When working with large files, consider using `awk` in combination with other tools like `grep` or `sort` for more complex data manipulation.
- Take advantage of `awk`'s built-in variables, such as `NR` (number of records) and `NF` (number of fields), to enhance your scripts.
- For more complex scripts, consider writing your `awk` commands in a separate file and using the `-f` option to execute them, improving readability and maintainability.