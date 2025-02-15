# [리눅스] Bash yes 사용법

## Overview
The `yes` command in Bash is a simple utility that outputs a string repeatedly until it is terminated. By default, it outputs the string "y" followed by a newline, which is commonly used to automate responses to prompts in scripts or command-line operations. Its primary purpose is to provide a continuous stream of output, which can be piped into other commands that require confirmation or repeated input.

## Usage
The basic syntax of the `yes` command is as follows:

```bash
yes [STRING]
```

- `STRING`: This is the string that you want `yes` to output repeatedly. If no string is provided, `yes` defaults to outputting "y".

### Common Options
- `-n`: Suppresses the newline character after each output. This option is not standard and may not be available in all implementations of `yes`.

## Examples

### Example 1: Basic Usage
To use `yes` with its default behavior, simply run:

```bash
yes
```
This will continuously output "y" until you stop it with `Ctrl+C`.

### Example 2: Custom String Output
You can specify a different string to be outputted. For example, if you want to output "Hello World!" repeatedly, you can use:

```bash
yes "Hello World!"
```
This will print "Hello World!" followed by a newline, continuously, until interrupted.

### Example 3: Piping Yes Output
A common use case for `yes` is to pipe its output into another command that requires confirmation. For example, if you want to forcefully remove a directory and all its contents without prompts, you can use:

```bash
yes | rm -rf /path/to/directory
```
This command will send a continuous stream of "y" to the `rm` command, effectively confirming all prompts.

## Tips
- **Use with Caution**: When using `yes` with commands that modify or delete files, be cautious as it can lead to unintended data loss.
- **Combine with Other Commands**: `yes` can be very useful when combined with commands that require user input, such as installation scripts or commands that prompt for confirmation.
- **Performance Consideration**: While `yes` is lightweight, consider the performance implications when using it in scripts that run in tight loops or with high-frequency calls.

By understanding and utilizing the `yes` command, you can streamline your command-line interactions and automate repetitive tasks effectively.