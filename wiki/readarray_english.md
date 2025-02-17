# [Linux] Bash readarray Usage: Read lines into an array

## Overview
The `readarray` command in Bash is used to read lines from standard input into an indexed array. This is particularly useful when you want to store multiple lines of text or data into a single variable for further processing.

## Usage
The basic syntax of the `readarray` command is as follows:

```bash
readarray [options] [array_name]
```

## Common Options
- `-n N`: Read only the first N lines.
- `-s N`: Skip the first N lines before reading.
- `-t`: Remove the trailing newlines from each line read.
- `-O N`: Specify the index to start storing the lines in the array.

## Common Examples

### Example 1: Basic Usage
To read lines from a file into an array:

```bash
readarray my_array < my_file.txt
```

### Example 2: Reading from a Command Output
You can also read lines from the output of a command:

```bash
readarray my_array < <(ls -1)
```

### Example 3: Skipping Lines
To skip the first line of a file and read the rest into an array:

```bash
readarray -s 1 my_array < my_file.txt
```

### Example 4: Removing Trailing Newlines
To read lines from a file and remove trailing newlines:

```bash
readarray -t my_array < my_file.txt
```

### Example 5: Specifying Starting Index
To start storing lines in an array from a specific index:

```bash
readarray -O 5 my_array < my_file.txt
```

## Tips
- Use the `-t` option to avoid issues with trailing newlines when processing the array.
- Always check the contents of your array after reading to ensure it has been populated as expected, using `echo "${my_array[@]}"`.
- Combine `readarray` with other commands like `grep` or `awk` for more powerful data manipulation.