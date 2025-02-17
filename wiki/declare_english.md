# [Linux] Bash declare Usage: Declare variables and their attributes

## Overview
The `declare` command in Bash is used to declare variables and assign attributes to them. It allows you to create variables with specific properties, such as making them read-only or arrays. This command is particularly useful for managing variable types and ensuring that your scripts behave as expected.

## Usage
The basic syntax of the `declare` command is as follows:

```bash
declare [options] [name[=value]]
```

## Common Options
Here are some common options you can use with the `declare` command:

- `-a`: Declare an array variable.
- `-i`: Declare an integer variable. Arithmetic operations on this variable are performed automatically.
- `-r`: Declare a read-only variable. Once set, its value cannot be changed.
- `-x`: Export a variable to the environment, making it available to child processes.
- `-p`: Display the attributes and values of variables.

## Common Examples

### Declaring a Simple Variable
```bash
declare myVar="Hello, World!"
echo $myVar
```

### Declaring an Integer Variable
```bash
declare -i myInt=5
myInt+=10
echo $myInt  # Outputs: 15
```

### Declaring a Read-Only Variable
```bash
declare -r myConst="This is constant"
echo $myConst
# myConst="New Value"  # This will result in an error
```

### Declaring an Array
```bash
declare -a myArray=("apple" "banana" "cherry")
echo ${myArray[1]}  # Outputs: banana
```

### Exporting a Variable
```bash
declare -x myExportedVar="I am available to child processes"
```

### Displaying Variable Attributes
```bash
declare -p myVar
```

## Tips
- Use `declare -p` to check the attributes and values of your variables, which can help in debugging.
- When working with arrays, remember to use parentheses `()` to initialize them correctly.
- Consider using read-only variables for constants to avoid accidental changes in your scripts.
- Use the `-x` option for any variables that need to be accessed by subprocesses to ensure they are exported correctly.