# [리눅스] Bash exit 사용법

## Overview
The `exit` command in Bash is used to terminate a shell session or a script. Its primary purpose is to provide an exit status to the calling process, which can be useful for error handling and debugging. When a script or a shell session ends, the exit status can indicate whether it completed successfully or encountered an error.

## Usage
The basic syntax of the `exit` command is as follows:

```bash
exit [n]
```

Where `n` is an optional integer that represents the exit status. If no status is provided, the exit status of the last executed command is used. By convention, an exit status of `0` indicates success, while any non-zero value indicates an error.

### Common Options
- `n`: An integer value between 0 and 255. This value is returned to the parent process as the exit status.
  
## Examples

### Example 1: Exiting a Script with a Success Status
```bash
#!/bin/bash
echo "This script will exit with a success status."
exit 0
```
In this example, the script prints a message and then exits with a status of `0`, indicating successful completion.

### Example 2: Exiting a Script with an Error Status
```bash
#!/bin/bash
echo "An error occurred."
exit 1
```
Here, the script indicates an error has occurred and exits with a status of `1`. This can be useful for signaling to other scripts or processes that something went wrong.

## Tips
- Always use meaningful exit status codes in your scripts. For example, use `1` for general errors, `2` for misuse of shell builtins, and other codes for specific error conditions.
- You can check the exit status of the last command executed using the special variable `$?`. This can help in debugging and controlling the flow of your scripts.
- When writing scripts that may be sourced (using `source` or `.`), be cautious with the `exit` command, as it will terminate the entire shell session if executed in that context. Use `return` instead if you want to exit from a function or sourced script without terminating the shell.