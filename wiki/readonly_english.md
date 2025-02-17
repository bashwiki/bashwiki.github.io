# [Linux] Bash readonly用法: Prevent variable modification

## Overview
The `readonly` command in Bash is used to mark variables or functions as read-only. Once a variable or function is declared as readonly, its value cannot be changed or unset, which helps prevent accidental modifications in scripts.

## Usage
The basic syntax of the `readonly` command is as follows:

```bash
readonly [options] [arguments]
```

## Common Options
- `-p`: Display a list of all readonly variables and functions in the current shell session.

## Common Examples

### Example 1: Declaring a Readonly Variable
To declare a variable as readonly, use the following command:

```bash
readonly MY_VAR="Hello, World!"
```

Attempting to change the value of `MY_VAR` will result in an error:

```bash
MY_VAR="New Value"  # This will fail with an error
```

### Example 2: Declaring a Readonly Function
You can also declare a function as readonly:

```bash
readonly my_function() {
    echo "This is a readonly function."
}
```

Trying to redefine `my_function` will produce an error:

```bash
my_function() {
    echo "Attempting to redefine."  # This will fail with an error
}
```

### Example 3: Listing Readonly Variables
To see all readonly variables and functions, use the `-p` option:

```bash
readonly -p
```

This will output a list of all currently defined readonly variables and functions.

## Tips
- Use readonly variables for constants that should not change throughout the script to improve code reliability.
- Be cautious when declaring functions as readonly, as it can limit flexibility in your scripts.
- Always check the list of readonly variables with `readonly -p` if you encounter unexpected behavior related to variable modification.