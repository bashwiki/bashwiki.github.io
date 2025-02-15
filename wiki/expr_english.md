# [리눅스] Bash expr 사용법

## Overview
The `expr` command in Bash is a utility that evaluates expressions and performs arithmetic operations. It is primarily used for integer arithmetic, string manipulation, and logical operations. `expr` can be particularly useful in shell scripts where you need to perform calculations or evaluate conditions.

## Usage
The basic syntax of the `expr` command is as follows:

```bash
expr expression
```

### Common Options
- **Arithmetic Operations**: You can perform basic arithmetic operations such as addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **String Operations**: `expr` can also be used to evaluate string lengths and extract substrings.
- **Logical Operations**: It supports logical comparisons like equality (`=`), inequality (`!=`), and relational operators (`<`, `>`, `<=`, `>=`).

Note that when using `expr`, you need to be cautious with spaces and special characters, especially for multiplication, which requires escaping (`\*`).

## Examples

### Example 1: Basic Arithmetic
To perform a simple addition of two numbers:

```bash
result=$(expr 5 + 3)
echo "The result of 5 + 3 is: $result"
```

This command will output:

```
The result of 5 + 3 is: 8
```

### Example 2: String Length
To find the length of a string:

```bash
string="Hello, World!"
length=$(expr length "$string")
echo "The length of the string is: $length"
```

This command will output:

```
The length of the string is: 13
```

## Tips
- Always use quotes around strings to prevent word splitting and globbing issues.
- For multiplication, remember to escape the asterisk (`*`) as `\*` to avoid it being interpreted as a wildcard.
- If you are performing multiple operations, consider using parentheses to group expressions, but remember to escape them as well: `expr \( 5 + 3 \) \* 2`.
- While `expr` is useful, consider using `$(( ))` for arithmetic operations in newer scripts, as it is more straightforward and supports floating-point arithmetic.

By following these guidelines and examples, you can effectively utilize the `expr` command in your Bash scripts for various calculations and evaluations.