# [Linux] Bash tac Usage: Reverse file contents line by line

## Overview
The `tac` command in Bash is used to concatenate and display files in reverse order, specifically reversing the order of lines. It is essentially the reverse of the `cat` command, which displays file contents in the standard order.

## Usage
The basic syntax of the `tac` command is as follows:

```bash
tac [options] [arguments]
```

## Common Options
- `-b`, `--before`: Place a delimiter before the line instead of after it.
- `-r`, `--regex`: Treat the delimiter as a regular expression.
- `-s`, `--separator`: Specify a custom separator instead of the default newline.

## Common Examples

### Example 1: Reverse a Single File
To reverse the contents of a file named `example.txt`:

```bash
tac example.txt
```

### Example 2: Reverse Multiple Files
To reverse the contents of multiple files, `file1.txt` and `file2.txt`, and display them one after the other:

```bash
tac file1.txt file2.txt
```

### Example 3: Using a Custom Separator
To reverse the contents of a file and use a custom separator, such as a comma:

```bash
tac -s ',' example.txt
```

### Example 4: Reverse Output with a Delimiter
To reverse lines and place a delimiter before each line:

```bash
tac -b example.txt
```

## Tips
- Use `tac` in combination with other commands like `grep` or `sort` to manipulate data more effectively.
- Redirect the output of `tac` to a new file if you want to save the reversed content:

  ```bash
  tac example.txt > reversed_example.txt
  ```
- Remember that `tac` reads the entire file into memory, so it may not be suitable for very large files.