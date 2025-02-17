# [Linux] Bash mapfile Usage: Read lines into an array

## Overview
The `mapfile` command in Bash is used to read lines from a file or standard input into an array. This is particularly useful for processing multiline text data efficiently, allowing you to manipulate each line as an individual element of an array.

## Usage
The basic syntax of the `mapfile` command is as follows:

```bash
mapfile [options] [array_name]
```

If no array name is provided, the default array `MAPFILE` will be used.

## Common Options
- `-n N`: Read up to N lines.
- `-s N`: Skip the first N lines.
- `-t`: Remove the trailing newlines from each line read.
- `-d DELIMITER`: Use DELIMITER instead of a newline to determine line endings.

## Common Examples

### Example 1: Read lines from a file into an array
```bash
mapfile lines < myfile.txt
echo "${lines[@]}"
```
This command reads all lines from `myfile.txt` into the array `lines` and then prints all elements of the array.

### Example 2: Read specific number of lines
```bash
mapfile -n 3 lines < myfile.txt
echo "${lines[@]}"
```
Here, only the first 3 lines from `myfile.txt` are read into the array `lines`.

### Example 3: Skip lines and remove trailing newlines
```bash
mapfile -s 2 -t lines < myfile.txt
echo "${lines[@]}"
```
This example skips the first 2 lines of `myfile.txt`, reads the rest into the array `lines`, and removes any trailing newlines.

### Example 4: Use a custom delimiter
```bash
mapfile -d ',' lines < myfile.csv
echo "${lines[@]}"
```
In this case, the command reads lines from a CSV file `myfile.csv`, using a comma as the delimiter instead of the default newline.

## Tips
- Always check the contents of your array after using `mapfile` to ensure it has been populated as expected.
- Use the `-t` option if you want to avoid dealing with trailing newlines, which can lead to unexpected behavior in further processing.
- Consider using `mapfile` in combination with other commands like `grep` or `awk` for more complex data manipulation tasks.