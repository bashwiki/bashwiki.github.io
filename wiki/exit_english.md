# [Linux] Bash exit command: Terminate a shell session

## Overview
The `exit` command in Bash is used to terminate a shell session. It can be used to exit from a script or to close the terminal window. When you exit, you can also return an exit status code, which can be useful for indicating success or failure of a script.

## Usage
The basic syntax of the `exit` command is as follows:

```bash
exit [n]
```

Where `n` is an optional exit status code. If no status code is provided, the exit status of the last executed command is used.

## Common Options
- `n`: An optional numeric argument that specifies the exit status. By convention, a status of `0` indicates success, while any non-zero value indicates an error.

## Common Examples

### Example 1: Exit a shell session
To simply exit a shell session, you can use:

```bash
exit
```

### Example 2: Exit a shell session with a specific status code
To exit with a status code of `1`, indicating an error, you can use:

```bash
exit 1
```

### Example 3: Using exit in a script
In a Bash script, you can use `exit` to indicate the success or failure of the script:

```bash
#!/bin/bash
# A simple script example
echo "Running script..."
# Simulate an error
if [ ! -f "important_file.txt" ]; then
    echo "Error: important_file.txt not found!"
    exit 1
fi
echo "Script completed successfully."
exit 0
```

### Example 4: Exiting from a subshell
If you are in a subshell and want to exit back to the parent shell, you can use:

```bash
(subshell_command)
exit
```

## Tips
- Always use `exit 0` at the end of your scripts to indicate successful completion.
- Use meaningful exit codes (e.g., `1` for general errors, `2` for command not found) to make debugging easier.
- Remember that exiting a subshell will not affect the parent shell; it only terminates the current subshell session.