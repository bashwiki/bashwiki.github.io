# [Linux] Bash expr Usage: Evaluate expressions and perform calculations

## Overview
The `expr` command in Bash is used to evaluate expressions and perform arithmetic calculations. It can handle integer arithmetic, string operations, and logical comparisons, making it a versatile tool for scripting and command-line operations.

## Usage
The basic syntax of the `expr` command is as follows:

```bash
expr [options] [arguments]
```

## Common Options
- `+` : Addition operator.
- `-` : Subtraction operator.
- `*` : Multiplication operator (must be escaped as `\*` or enclosed in quotes).
- `/` : Division operator.
- `%` : Modulus operator.
- `=` : String comparison operator.
- `!=` : String inequality operator.
- `>` : Greater than comparison.
- `<` : Less than comparison.
- `\` : Escape character for special characters.

## Common Examples

### Basic Arithmetic
To perform basic arithmetic operations:

```bash
expr 5 + 3
```
Output: `8`

```bash
expr 10 - 4
```
Output: `6`

### Multiplication
To multiply two numbers, remember to escape the asterisk:

```bash
expr 4 \* 7
```
Output: `28`

### Division
To divide two numbers:

```bash
expr 20 / 4
```
Output: `5`

### Modulus
To find the remainder of a division:

```bash
expr 10 % 3
```
Output: `1`

### String Comparison
To compare two strings:

```bash
expr "hello" = "hello"
```
Output: `1` (true)

```bash
expr "hello" != "world"
```
Output: `1` (true)

### Logical Comparison
To check if one number is greater than another:

```bash
expr 10 \> 5
```
Output: `1` (true)

## Tips
- Always remember to escape the multiplication operator `*` or use quotes to avoid syntax errors.
- Use parentheses to group expressions for clarity, especially in complex calculations.
- For string operations, ensure that the strings are enclosed in quotes to prevent word splitting.
- Consider using `$(( ))` for arithmetic operations in Bash, as it is often more straightforward and supports more complex expressions.