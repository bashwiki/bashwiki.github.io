# [Linux] Bash test usage: Evaluate expressions

## Overview
The `test` command in Bash is used to evaluate conditional expressions. It checks file types and compares values, returning a status code that indicates whether the expression is true or false. This command is often used in scripts to control the flow of execution based on certain conditions.

## Usage
The basic syntax of the `test` command is as follows:

```bash
test [options] [arguments]
```

Alternatively, you can use the `[` command, which is a synonym for `test`:

```bash
[ expression ]
```

## Common Options
- `-e FILE`: Returns true if the file exists.
- `-f FILE`: Returns true if the file exists and is a regular file.
- `-d FILE`: Returns true if the file exists and is a directory.
- `-r FILE`: Returns true if the file exists and is readable.
- `-w FILE`: Returns true if the file exists and is writable.
- `-x FILE`: Returns true if the file exists and is executable.
- `STRING1 = STRING2`: Returns true if the two strings are equal.
- `STRING1 != STRING2`: Returns true if the two strings are not equal.
- `NUM1 -eq NUM2`: Returns true if the two numbers are equal.
- `NUM1 -ne NUM2`: Returns true if the two numbers are not equal.

## Common Examples
Here are some practical examples of using the `test` command:

### Check if a file exists
```bash
test -e myfile.txt && echo "File exists."
```

### Check if a directory exists
```bash
test -d /path/to/directory && echo "Directory exists."
```

### Compare two strings
```bash
test "hello" = "hello" && echo "Strings are equal."
```

### Check if a number is greater than another
```bash
NUM1=10
NUM2=5
test $NUM1 -gt $NUM2 && echo "$NUM1 is greater than $NUM2."
```

### Check if a file is readable
```bash
test -r myfile.txt && echo "File is readable."
```

## Tips
- Use `[` as a shorthand for `test` to make your scripts more readable.
- Always quote your string variables to prevent issues with spaces or special characters.
- Combine multiple tests using `&&` (logical AND) or `||` (logical OR) for more complex conditions.
- Remember that `test` returns a status code: 0 for true and 1 for false, which can be useful in scripting for flow control.