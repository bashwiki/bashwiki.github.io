# [리눅스] Bash return 사용법

## Overview
The `return` command in Bash is used to exit a function and optionally return a status code to the caller. This command is primarily utilized within shell functions to indicate the success or failure of the function's execution. The status code returned can be used to control the flow of the script or to provide feedback on the function's outcome.

## Usage
The basic syntax of the `return` command is as follows:

```bash
return [n]
```

Where `n` is an optional integer that represents the exit status. If no value is provided, the return status of the last executed command within the function is used. By convention, a return status of `0` indicates success, while any non-zero value indicates an error or failure.

### Common Options
- `n`: An integer value (0-255) that specifies the exit status to return. 

## Examples

### Example 1: Basic Function with Return
Here is a simple function that checks if a number is even or odd and returns an appropriate status code.

```bash
is_even() {
    if (( $1 % 2 == 0 )); then
        return 0  # Success: the number is even
    else
        return 1  # Failure: the number is odd
    fi
}

is_even 4
echo $?  # Outputs: 0

is_even 3
echo $?  # Outputs: 1
```

In this example, the function `is_even` takes a number as an argument and returns `0` if the number is even and `1` if it is odd. The `echo $?` command is used to print the return status of the last executed command.

### Example 2: Using Return in Conditional Statements
You can also use the `return` command in conjunction with conditional statements to control the flow of your script.

```bash
check_file() {
    if [ -f "$1" ]; then
        echo "File exists."
        return 0
    else
        echo "File does not exist."
        return 1
    fi
}

check_file "example.txt"
if [ $? -eq 0 ]; then
    echo "Proceeding with file operations."
else
    echo "Exiting due to missing file."
fi
```

In this example, the `check_file` function checks for the existence of a file. Depending on whether the file exists, it returns a corresponding status code, which is then used in a conditional statement to determine the next steps.

## Tips
- Always use the `return` command within functions to provide clear feedback on the function's execution status.
- Use meaningful return codes to represent different error states, which can help in debugging and maintaining scripts.
- Remember that the `return` command can only be used within functions; using it outside of a function will result in an error.
- To check the return status of the last command executed, use the special variable `$?`, which can be particularly useful for debugging.

By understanding and effectively utilizing the `return` command, you can enhance the control flow and error handling in your Bash scripts.