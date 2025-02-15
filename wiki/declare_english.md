# [리눅스] Bash declare 사용법

## Overview
The `declare` command in Bash is used to declare variables and their attributes. It allows developers to create variables with specific properties, such as making them read-only, arrays, or integers. This command enhances the way variables are handled in scripts, providing more control over their behavior and scope.

## Usage
The basic syntax of the `declare` command is as follows:

```bash
declare [options] variable_name=value
```

### Common Options
- `-a`: Declare an array variable.
- `-i`: Declare an integer variable. Arithmetic operations will be performed on this variable.
- `-r`: Declare a read-only variable. Once set, its value cannot be changed.
- `-x`: Export the variable to the environment of subsequently executed commands.
- `-p`: Display the attributes and value of each variable.

## Examples

### Example 1: Declaring an Integer Variable
```bash
declare -i num=10
num+=5
echo $num  # Output: 15
```
In this example, `num` is declared as an integer. When we add 5 to `num`, it performs arithmetic addition instead of string concatenation.

### Example 2: Declaring an Array
```bash
declare -a fruits=("apple" "banana" "cherry")
echo ${fruits[1]}  # Output: banana
```
Here, an array named `fruits` is declared. We can access the second element of the array using its index.

## Tips
- Use `declare -r` for constants to prevent accidental modification of critical variables.
- When working with arrays, remember to use parentheses `()` for initialization and curly braces `{}` for accessing elements.
- Utilize `declare -p` to inspect the attributes and values of your variables, which can be helpful for debugging.
- Keep in mind that `declare` is a Bash built-in command, so it may not be available in other shells like sh or dash. Always ensure your scripts are executed in a Bash environment.