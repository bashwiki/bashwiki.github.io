# [리눅스] Bash shift 사용법

## Overview
The `shift` command in Bash is used to manipulate the positional parameters of a script or a function. When you invoke `shift`, it shifts the positional parameters to the left by a specified number of positions. This means that `$1` becomes `$2`, `$2` becomes `$3`, and so on. The primary purpose of `shift` is to facilitate the processing of command-line arguments in scripts, allowing you to handle each argument in a loop or sequentially without needing to manage indices manually.

## Usage
The basic syntax of the `shift` command is as follows:

```bash
shift [n]
```

- `n`: An optional argument that specifies the number of positions to shift. If `n` is not provided, the default value is `1`.

### Common Options
- `n`: A non-negative integer that indicates how many positions to shift. For example, `shift 2` will shift the positional parameters two places to the left.

## Examples

### Example 1: Basic Shift
Here’s a simple example demonstrating the use of `shift` in a script that processes command-line arguments:

```bash
#!/bin/bash

echo "Total arguments: $#"
while [ "$#" -gt 0 ]; do
    echo "Processing: $1"
    shift
done
```

In this script, the `shift` command is used to process each argument one by one. The loop continues until there are no more arguments left.

### Example 2: Shift with a Specified Number
In this example, we will shift the positional parameters by two:

```bash
#!/bin/bash

echo "Original arguments: $@"
shift 2
echo "Arguments after shifting: $@"
```

If you run this script with the arguments `arg1 arg2 arg3 arg4`, the output will be:

```
Original arguments: arg1 arg2 arg3 arg4
Arguments after shifting: arg3 arg4
```

## Tips
- Always check the number of positional parameters using `$#` before using `shift` to avoid unexpected behavior or errors when there are no parameters left to shift.
- Use `shift` in conjunction with loops to process all command-line arguments efficiently.
- Be cautious when using a number greater than the number of positional parameters, as it will result in empty positional parameters, which may lead to confusion in your script logic.
- Consider using `shift` in functions to manage local parameters effectively, especially when dealing with multiple arguments.

By understanding and utilizing the `shift` command, you can enhance the flexibility and readability of your Bash scripts when handling command-line arguments.