# [리눅스] Bash readonly 사용법

## Overview
The `readonly` command in Bash is used to mark variables or functions as read-only. Once a variable or function is declared as readonly, it cannot be modified or unset during the current shell session. This is particularly useful for protecting important values from accidental changes and ensuring that certain configurations remain constant throughout the execution of a script or command.

## Usage
The basic syntax of the `readonly` command is as follows:

```bash
readonly [name[=value] ...]
```

### Options
- `name`: The name of the variable or function you want to mark as readonly. You can also assign a value to the variable at the same time by using the `name=value` format.
- If no arguments are provided, `readonly` will display a list of all readonly variables in the current shell session.

## Examples

### Example 1: Marking a Variable as Readonly
```bash
# Declare a variable and assign a value
readonly MY_VAR="Hello, World!"

# Attempting to modify the variable will result in an error
MY_VAR="New Value"  # This will produce an error: "bash: MY_VAR: readonly variable"
```

### Example 2: Listing Readonly Variables
```bash
# Declare some readonly variables
readonly VAR1="Value 1"
readonly VAR2="Value 2"

# List all readonly variables
readonly
```
This command will output:
```
declare -r VAR1="Value 1"
declare -r VAR2="Value 2"
```

## Tips
- Use `readonly` for variables that should not change throughout the execution of your script to avoid unintended side effects.
- Remember that once a variable is marked as readonly, it cannot be unset or modified in the current session. If you need to change its value later, you will need to start a new shell session.
- To remove the readonly attribute from a variable, you must first unset it (if it is not readonly) or start a new session if it is already marked as readonly.