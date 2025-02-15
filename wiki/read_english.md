# [리눅스] Bash read 사용법

## Overview
The `read` command in Bash is used to read a line of input from standard input (stdin) and assign it to one or more variables. This command is particularly useful in scripts where user interaction is required, allowing developers to capture user input dynamically during script execution.

## Usage
The basic syntax of the `read` command is as follows:

```bash
read [options] variable_name
```

### Common Options:
- `-p prompt`: Displays a prompt before reading input.
- `-s`: Silent mode; does not echo input back to the terminal (useful for passwords).
- `-a array`: Reads the input into an array variable.
- `-d delimiter`: Sets a custom delimiter to end the input (default is newline).
- `-n num`: Reads only a specified number of characters.
- `-t timeout`: Sets a timeout for reading input.

## Examples

### Example 1: Basic Input
```bash
#!/bin/bash
echo "Please enter your name:"
read name
echo "Hello, $name!"
```
In this example, the script prompts the user to enter their name and then greets them using the input received.

### Example 2: Silent Input for Password
```bash
#!/bin/bash
read -sp "Enter your password: " password
echo
echo "Password entered."
```
Here, the script reads a password without displaying it on the screen, ensuring privacy.

## Tips
- Always validate user input after using `read` to ensure it meets your requirements.
- Use the `-p` option to provide clear prompts, making the script more user-friendly.
- When using `-a` to read into an array, remember that the input will be split by whitespace.
- Consider using the `-t` option to prevent your script from hanging indefinitely if no input is provided.
- For sensitive information, always use the `-s` option to keep input secure.

By following these guidelines and examples, you can effectively utilize the `read` command in your Bash scripts to enhance user interaction and input handling.