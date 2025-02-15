# [리눅스] Bash true 사용법

## Overview
The `true` command in Bash is a simple utility that does nothing and returns a successful exit status (0). Its primary purpose is to serve as a placeholder in scripts or command lines where a command is required syntactically but no action is needed. This can be particularly useful in control structures like loops or conditional statements.

## Usage
The basic syntax of the `true` command is straightforward:

```bash
true
```

There are no options or arguments for the `true` command; it simply executes and exits with a status code of 0, indicating success.

## Examples

### Example 1: Using `true` in a Loop
You can use `true` in a loop where you want to create an infinite loop that does nothing:

```bash
while true; do
    echo "This will print indefinitely."
done
```

In this example, the loop will continuously print the message until it is interrupted.

### Example 2: Placeholder in Conditional Statements
`true` can also be used as a placeholder in scripts where a command is required but no action is desired:

```bash
if true; then
    echo "This condition is always true."
fi
```

In this case, the `if` statement will always evaluate to true, and the message will be printed.

## Tips
- **Use in Scripts**: The `true` command is often used in scripts as a placeholder to maintain syntax without performing any operation.
- **Combining with Other Commands**: You can combine `true` with other commands in conditional execution. For example, you can use it to ensure a command always runs regardless of the previous command's success:
  
  ```bash
  command1 || true
  ```

  In this case, if `command1` fails, the script will continue executing without interruption.

- **Debugging**: When debugging scripts, replacing a command with `true` can help isolate issues without affecting the flow of the script.

By understanding the `true` command, you can enhance your scripting capabilities and manage control flows more effectively in your Bash scripts.