# [Linux] Bash read Usage: Read user input from standard input

## Overview
The `read` command in Bash is used to read a line of input from standard input (usually the keyboard) and assign it to one or more variables. This command is particularly useful in scripts where user interaction is required.

## Usage
The basic syntax of the `read` command is as follows:

```bash
read [options] [variable...]
```

## Common Options
- `-p PROMPT`: Display a prompt before reading input.
- `-s`: Silent mode; does not echo input (useful for passwords).
- `-t TIMEOUT`: Time out after a specified number of seconds if no input is received.
- `-n N`: Read only N characters of input.

## Common Examples

### Example 1: Basic Input
To read a single line of input into a variable:

```bash
read name
echo "Hello, $name!"
```

### Example 2: Prompting for Input
Using the `-p` option to display a prompt:

```bash
read -p "Enter your favorite color: " color
echo "Your favorite color is $color."
```

### Example 3: Silent Input
Reading a password without displaying it on the screen:

```bash
read -s -p "Enter your password: " password
echo "Password read successfully."
```

### Example 4: Timeout for Input
Setting a timeout for user input:

```bash
if read -t 5 -p "You have 5 seconds to enter your name: " name; then
    echo "Hello, $name!"
else
    echo "No input received."
fi
```

### Example 5: Reading Multiple Variables
Reading multiple values into different variables:

```bash
read -p "Enter your first name and last name: " first last
echo "Hello, $first $last!"
```

## Tips
- Always validate user input to ensure it meets your script's requirements.
- Use the `-s` option when asking for sensitive information like passwords.
- Consider using a timeout with `-t` to prevent your script from hanging indefinitely if the user does not respond.
- When reading multiple variables, ensure the input format is clear to the user to avoid confusion.