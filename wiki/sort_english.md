# [리눅스] Bash sort 사용법

## Overview
The `sort` command in Bash is a powerful utility used to sort lines of text files or standard input. Its primary purpose is to arrange the lines in a specified order, which can be either ascending or descending. The sorting can be based on various criteria, such as numerical values, alphabetical order, or specific fields within a line. This command is essential for data processing, making it easier to analyze and manage text data.

## Usage
The basic syntax of the `sort` command is as follows:

```bash
sort [OPTION]... [FILE]...
```

### Common Options:
- `-n`: Sorts the input numerically.
- `-r`: Reverses the sorting order (sorts in descending order).
- `-k`: Specifies a key (or field) to sort by. For example, `-k2` sorts by the second field.
- `-t`: Defines a custom delimiter for fields. For example, `-t,` uses a comma as the delimiter.
- `-u`: Outputs only unique lines, removing duplicates.
- `-o FILE`: Writes the output to a specified file instead of standard output.

## Examples
### Example 1: Basic Alphabetical Sort
To sort a file named `names.txt` in alphabetical order:

```bash
sort names.txt
```

### Example 2: Numerical Sort with Reverse Order
To sort a file named `numbers.txt` numerically in descending order:

```bash
sort -nr numbers.txt
```

### Example 3: Sorting by a Specific Field
If you have a CSV file named `data.csv` and want to sort it by the second column:

```bash
sort -t, -k2 data.csv
```

## Tips
- Always consider using the `-o` option to save sorted output directly to a file, which can help avoid overwriting the original data unintentionally.
- When sorting large files, consider using the `-S` option to specify the amount of memory to use for sorting, which can improve performance.
- Use the `-u` option in conjunction with sorting to eliminate duplicate entries, especially useful in data cleanup tasks.
- Familiarize yourself with the `man sort` command to explore more advanced options and features of the `sort` command.