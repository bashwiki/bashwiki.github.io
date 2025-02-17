# [Linux] Bash let: Perform arithmetic operations

## Overview
The `let` command in Bash is used to perform arithmetic operations on integers. It allows you to evaluate expressions and assign the results to variables without needing to use the `expr` command or external tools.

## Usage
The basic syntax of the `let` command is as follows:

```bash
let [options] [arguments]
```

## Common Options
- `-`: Subtraction
- `+`: Addition
- `*`: Multiplication
- `/`: Division
- `%`: Modulus
- `=`: Assignment

## Common Examples

### Example 1: Basic Addition
```bash
let result=5+3
echo $result  # Output: 8
```

### Example 2: Subtraction
```bash
let result=10-4
echo $result  # Output: 6
```

### Example 3: Multiplication
```bash
let result=7*6
echo $result  # Output: 42
```

### Example 4: Division
```bash
let result=20/4
echo $result  # Output: 5
```

### Example 5: Using Variables
```bash
a=10
b=5
let result=a+b
echo $result  # Output: 15
```

### Example 6: Incrementing a Variable
```bash
count=0
let count=count+1
echo $count  # Output: 1
```

## Tips
- Use `let` for simple arithmetic to keep your scripts clean and efficient.
- Remember that `let` only works with integers; using it with floating-point numbers will not yield the expected results.
- You can also use `(( ))` for arithmetic operations, which is often more readable and flexible. For example: `((result = a + b))`.