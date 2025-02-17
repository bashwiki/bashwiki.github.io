# [Linux] Bash true用法: Always returns a successful exit status

## Overview
The `true` command in Bash is a simple utility that always returns a successful exit status (0). It is often used in scripts and command lines where a successful exit is required, but no actual operation needs to be performed.

## Usage
The basic syntax of the `true` command is straightforward:

```bash
true [options]
```

Since `true` does not take any arguments or options, you can simply call it without any additional input.

## Common Options
The `true` command does not have any options or arguments. It is designed to perform its function without any additional parameters.

## Common Examples

1. **Basic Usage**: Simply run `true` to see that it returns a success status.
   ```bash
   true
   echo $?  # This will output 0, indicating success.
   ```

2. **Using in Conditional Statements**: You can use `true` in a conditional statement to always execute a block of code.
   ```bash
   if true; then
       echo "This will always run."
   fi
   ```

3. **As a Placeholder**: `true` can be used as a placeholder in scripts where a command is required but no action is needed.
   ```bash
   for i in {1..5}; do
       true  # Placeholder for future commands
   done
   ```

4. **In Loops**: You can create an infinite loop using `true`.
   ```bash
   while true; do
       echo "This will run indefinitely. Press Ctrl+C to stop."
   done
   ```

## Tips
- **Use in Scripts**: `true` is particularly useful in scripts where you need a command that does nothing but still returns a success status.
- **Combining with Other Commands**: You can use `true` in conjunction with other commands to ensure that a script continues running even if a previous command fails.
- **Debugging**: When debugging scripts, replacing a command with `true` can help you isolate issues without affecting the flow of the script.