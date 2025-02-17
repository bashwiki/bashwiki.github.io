# [Linux] Bash printf用法: Format and print data

## Overview
The `printf` command in Bash is used to format and print data to the standard output. It allows for greater control over the output format compared to the `echo` command, making it ideal for creating formatted text, tables, and more.

## Usage
The basic syntax of the `printf` command is as follows:

```bash
printf [options] format [arguments]
```

## Common Options
- `-v var`: Assign the output to a variable instead of printing it.
- `--help`: Display a help message with usage information.
- `--version`: Show the version information of the command.

## Common Examples

### Example 1: Basic String Formatting
Print a simple string with a newline.

```bash
printf "Hello, World!\n"
```

### Example 2: Formatting Numbers
Print a number with leading zeros.

```bash
printf "Number: %05d\n" 42
```

### Example 3: Floating Point Numbers
Print a floating-point number with two decimal places.

```bash
printf "Price: %.2f\n" 19.99
```

### Example 4: Multiple Arguments
Print multiple formatted strings in one command.

```bash
printf "Name: %s, Age: %d\n" "Alice" 30
```

### Example 5: Assigning Output to a Variable
Store formatted output in a variable.

```bash
printf -v result "The result is: %.2f" 3.14159
echo "$result"
```

## Tips
- Use `\n` to add new lines in your output.
- Be mindful of format specifiers like `%s` for strings, `%d` for integers, and `%.nf` for floating-point numbers where `n` is the number of decimal places.
- When using `printf` in scripts, always check for proper formatting to avoid unexpected output.