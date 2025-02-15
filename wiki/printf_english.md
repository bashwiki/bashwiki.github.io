# [리눅스] Bash printf 사용법

## Overview
The `printf` command in Bash is a powerful utility used for formatted output. It allows users to print text and variables to the terminal with precise control over formatting, including alignment, padding, and number formatting. Unlike the `echo` command, `printf` does not automatically add a newline at the end of the output, making it more versatile for complex formatting tasks.

## Usage
The basic syntax of the `printf` command is as follows:

```bash
printf FORMAT [ARGUMENTS...]
```

- **FORMAT**: A string that specifies how to format the output. It can include format specifiers (like `%s` for strings, `%d` for integers, etc.) that will be replaced by the corresponding arguments.
- **ARGUMENTS**: The values that will be formatted according to the specified format.

### Common Options
- `-v var`: Assign the output to a variable instead of printing it to the terminal.
- `--help`: Display help information about the command.

## Examples

### Example 1: Basic String Formatting
```bash
printf "Hello, %s!\n" "World"
```
**Output:**
```
Hello, World!
```
In this example, `%s` is a format specifier that gets replaced by the string "World". The `\n` at the end adds a newline.

### Example 2: Formatting Numbers
```bash
printf "The value of pi is approximately %.2f\n" 3.14159
```
**Output:**
```
The value of pi is approximately 3.14
```
Here, `%.2f` formats the number to two decimal places.

## Tips
- Use `printf` for consistent formatting, especially when dealing with multiple variables or complex output.
- Remember that `printf` does not automatically append a newline, so include `\n` where necessary to control line breaks.
- For better readability, consider using named variables to hold values that will be formatted, especially in scripts.
- Explore different format specifiers to fully utilize `printf`'s capabilities, such as `%d` for integers, `%f` for floating-point numbers, and `%x` for hexadecimal values.