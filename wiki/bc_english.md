# [Linux] Bash bc Usage: Perform arbitrary precision arithmetic

## Overview
The `bc` command in Bash is a powerful calculator that supports arbitrary precision arithmetic. It allows users to perform mathematical operations with a high degree of accuracy, making it ideal for calculations that require more precision than standard floating-point arithmetic.

## Usage
The basic syntax of the `bc` command is as follows:

```bash
bc [options] [arguments]
```

You can use `bc` in both interactive mode and by passing expressions directly through standard input or files.

## Common Options
- `-l`: Load the standard math library, which provides additional mathematical functions.
- `-q`: Suppress the introductory message and prompt, useful for scripting.
- `-e`: Execute the commands provided as arguments instead of entering interactive mode.

## Common Examples

### Basic Arithmetic
To perform simple arithmetic operations, you can use `bc` as follows:

```bash
echo "5 + 3" | bc
```
This will output `8`.

### Floating Point Division
For division that requires precision, use the `scale` variable:

```bash
echo "scale=2; 10 / 3" | bc
```
This will output `3.33`.

### Using the Math Library
To use functions from the math library, include the `-l` option:

```bash
echo "scale=4; sqrt(2)" | bc -l
```
This will output `1.4142`.

### Multiple Operations
You can chain multiple operations together:

```bash
echo "scale=3; (5 + 2) * (10 - 3) / 2" | bc
```
This will output `24.500`.

### Reading from a File
You can also read expressions from a file:

```bash
echo -e "5 + 3\n10 / 2" > calculations.txt
bc calculations.txt
```
This will output:
```
8
5
```

## Tips
- Always set the `scale` variable when performing division to avoid truncation of decimal points.
- Use the `-l` option for advanced mathematical functions like sine, cosine, and logarithm.
- For scripting, consider using the `-q` option to keep output clean and free of unnecessary prompts.