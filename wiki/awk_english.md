# [Linux] Bash awk uso equivalente: Process text files and extract data

## Overview
The `awk` command is a powerful text processing tool in Unix-like operating systems. It is primarily used for pattern scanning and processing, allowing users to extract and manipulate data from files or input streams based on specified patterns.

## Usage
The basic syntax of the `awk` command is as follows:

```bash
awk [options] 'pattern { action }' file
```

## Common Options
- `-F`: Specifies the field separator (default is whitespace).
- `-v`: Allows you to assign a value to a variable before executing the program.
- `-f`: Allows you to specify a file containing `awk` commands.
- `-e`: Allows you to specify the `awk` program as a command line argument.

## Common Examples

### Example 1: Print specific columns
To print the first and third columns from a file named `data.txt`, you can use:

```bash
awk '{print $1, $3}' data.txt
```

### Example 2: Using a custom field separator
If your data is comma-separated, you can specify the field separator with the `-F` option:

```bash
awk -F, '{print $1, $2}' data.csv
```

### Example 3: Pattern matching
To print lines that contain the word "error" from a log file:

```bash
awk '/error/' log.txt
```

### Example 4: Calculating sums
To calculate the sum of values in the second column of a file:

```bash
awk '{sum += $2} END {print sum}' data.txt
```

### Example 5: Using variables
You can use the `-v` option to set a variable and use it in your `awk` command:

```bash
awk -v threshold=100 '$2 > threshold {print $1}' data.txt
```

## Tips
- Always quote your `awk` commands to avoid shell interpretation issues.
- Use the `BEGIN` and `END` blocks to perform actions before processing the input or after finishing it, respectively.
- Test your `awk` commands with sample data to ensure they work as expected before applying them to larger datasets.