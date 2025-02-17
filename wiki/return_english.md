# [Linux] Bash return <Usage equivalent in English>: Exit with a return status

## Overview
The `return` command in Bash is used to exit a function and return a specific exit status to the caller. This is particularly useful for indicating success or failure of a function's execution, allowing for better control flow in scripts.

## Usage
The basic syntax of the `return` command is as follows:

```bash
return [n]
```

Where `n` is an optional exit status code. If no status code is provided, the return status of the last executed command within the function is used.

## Common Options
- `n`: An integer value representing the exit status. By convention, a status of `0` indicates success, while any non-zero value indicates an error or failure.

## Common Examples

### Example 1: Basic Return
In this example, a function returns a success status.

```bash
my_function() {
    echo "Function executed successfully."
    return 0
}

my_function
echo "Return status: $?"
```

### Example 2: Return with Error Code
Here, a function returns a specific error code.

```bash
my_function() {
    echo "An error occurred."
    return 1
}

my_function
echo "Return status: $?"
```

### Example 3: Returning the Status of a Command
You can return the status of the last command executed within a function.

```bash
my_function() {
    ls /nonexistent_directory
    return $?  # Return the exit status of the `ls` command
}

my_function
echo "Return status: $?"
```

## Tips
- Always use `return` in functions to provide meaningful exit statuses, which can help in debugging and controlling script flow.
- Use `return 0` to indicate successful completion and `return 1` or other non-zero values to indicate different types of errors.
- Remember that the `return` command can only be used within functions; using it in the main body of a script will result in an error.