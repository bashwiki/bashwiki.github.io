# [리눅스] Bash readarray 사용법

## Overview
The `readarray` command in Bash is a built-in utility that reads lines from standard input into an indexed array variable. This command is particularly useful for processing multiline input, such as files or command output, and storing each line as an element in an array. This allows for easy manipulation and access to individual lines later in the script.

## Usage
The basic syntax of the `readarray` command is as follows:

```bash
readarray [options] array_name
```

### Common Options
- `-n N`: Read only the first N lines of input.
- `-s N`: Skip the first N lines of input before reading.
- `-t`: Remove the trailing newlines from each line read.
- `-d DELIMITER`: Use DELIMITER instead of a newline to terminate each line.

## Examples

### Example 1: Reading from a File
Suppose you have a text file named `example.txt` with the following content:

```
Line 1
Line 2
Line 3
```

You can read this file into an array as follows:

```bash
readarray lines < example.txt
echo "${lines[0]}"  # Output: Line 1
echo "${lines[1]}"  # Output: Line 2
echo "${lines[2]}"  # Output: Line 3
```

### Example 2: Reading Command Output
You can also use `readarray` to read the output of a command into an array. For example, to read the list of files in the current directory:

```bash
readarray files < <(ls)
echo "${files[0]}"  # Output: First file in the directory
echo "${files[1]}"  # Output: Second file in the directory
```

## Tips
- When using `readarray`, remember to use the `-t` option if you want to remove trailing newlines, which can be helpful when processing input.
- If you only need a specific number of lines, consider using the `-n` option to limit the input, which can improve performance for large files.
- To handle input from a command that produces output with a different delimiter, use the `-d` option to specify the desired delimiter.
- Always check if the array is populated after using `readarray` to avoid errors when accessing its elements. You can do this by checking the length of the array with `${#array_name[@]}`.