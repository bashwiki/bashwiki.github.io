# [리눅스] Bash tac 사용법

## Overview
The `tac` command in Bash is a utility that reads lines from a file and outputs them in reverse order. The name "tac" is derived from "cat" spelled backwards, reflecting its functionality of reversing the order of lines rather than concatenating them. This command is particularly useful for quickly viewing the last entries in log files or any text files where the most recent information is located at the end.

## Usage
The basic syntax of the `tac` command is as follows:

```bash
tac [OPTION]... [FILE]...
```

### Common Options
- `-r`, `--regex`: Treats each line as a regular expression.
- `-s`, `--separator=STRING`: Specifies a custom separator instead of the default newline character.
- `-b`, `--before`: Places the separator before the line instead of after it.
- `-h`, `--help`: Displays a help message with usage information.
- `-V`, `--version`: Outputs the version information of the `tac` command.

If no file is specified, `tac` reads from standard input.

## Examples

### Example 1: Basic Usage
To reverse the lines of a file named `example.txt`, you would use the following command:

```bash
tac example.txt
```

This command will display the contents of `example.txt` with the last line appearing first and the first line appearing last.

### Example 2: Using a Custom Separator
If you want to reverse lines in a file but separate them with a custom string, such as a comma, you can use the `-s` option:

```bash
tac -s ',' example.txt
```

In this example, `tac` will reverse the lines of `example.txt` and separate them with commas instead of newlines.

## Tips
- When working with large files, consider using `tac` in combination with other commands like `head` or `tail` to quickly access specific sections of the file.
- If you are processing multiple files, `tac` will reverse the lines of each file individually and concatenate the results in the order they are provided.
- Be cautious when using `tac` with files that contain a large number of lines, as reversing the entire file may consume significant memory.