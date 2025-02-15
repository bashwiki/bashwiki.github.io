# [리눅스] Bash test 사용법

## Overview
The `test` command in Bash is a built-in command used to evaluate conditional expressions. Its primary purpose is to return a status code based on the evaluation of the given expressions, which can be used in control flow statements like `if`, `while`, or `until`. The `test` command allows users to check file types, compare strings, and evaluate numeric expressions.

## Usage
The basic syntax of the `test` command is as follows:

```bash
test EXPRESSION
```

Alternatively, it can be invoked using square brackets, which is a more common and user-friendly syntax:

```bash
[ EXPRESSION ]
```

### Common Options
- **-e FILE**: Returns true if the file exists.
- **-f FILE**: Returns true if the file exists and is a regular file.
- **-d FILE**: Returns true if the file exists and is a directory.
- **-s FILE**: Returns true if the file exists and has a size greater than zero.
- **STRING1 = STRING2**: Returns true if the two strings are equal.
- **STRING1 != STRING2**: Returns true if the two strings are not equal.
- **NUM1 -eq NUM2**: Returns true if the two numbers are equal.
- **NUM1 -ne NUM2**: Returns true if the two numbers are not equal.
- **NUM1 -lt NUM2**: Returns true if NUM1 is less than NUM2.
- **NUM1 -le NUM2**: Returns true if NUM1 is less than or equal to NUM2.
- **NUM1 -gt NUM2**: Returns true if NUM1 is greater than NUM2.
- **NUM1 -ge NUM2**: Returns true if NUM1 is greater than or equal to NUM2.

## Examples

### Example 1: Checking if a file exists
```bash
filename="example.txt"

if test -e "$filename"; then
    echo "$filename exists."
else
    echo "$filename does not exist."
fi
```

### Example 2: Comparing two strings
```bash
string1="hello"
string2="world"

if test "$string1" != "$string2"; then
    echo "The strings are not equal."
else
    echo "The strings are equal."
fi
```

## Tips
- Use the `[` syntax for better readability, especially for those who may not be familiar with the `test` command.
- Always quote variables to prevent issues with spaces or special characters.
- Combine multiple conditions using logical operators like `-a` (and) and `-o` (or) for more complex evaluations.
- Remember that the `test` command returns a status code of `0` for true and `1` for false, which can be useful for debugging and scripting.