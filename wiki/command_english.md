# [리눅스] Bash command 사용법

## Overview
The `command` command in Bash is a built-in utility that is primarily used to invoke commands while bypassing any shell functions or built-in commands that may have the same name. It is useful for ensuring that the user is executing the actual command from the system rather than a potentially overridden version.

## Usage
The basic syntax for the `command` command is as follows:

```bash
command [options] command_name [arguments]
```

### Common Options
- `-v`: This option displays the command name and its location in the filesystem.
- `-p`: This option uses the default path for searching commands, ignoring any user-defined paths.

## Examples

### Example 1: Using `command` to bypass a shell function
Suppose you have a shell function named `ls` that modifies the output of the standard `ls` command. You can use `command` to call the original `ls` command:

```bash
function ls() {
    echo "This is a custom ls function."
}

# Call the custom function
ls

# Call the original ls command
command ls
```

### Example 2: Displaying the location of a command
You can use the `-v` option to find out where a command is located:

```bash
command -v ls
```

This will output the path to the `ls` command, such as `/bin/ls`, ensuring you know exactly which version is being executed.

## Tips
- Use `command` when you need to ensure that you are executing the actual command and not a shell function or alias that may have been defined in your environment.
- Combine `command` with options like `-v` and `-p` to gain more control and information about command execution.
- Be cautious when using `command` in scripts, as it may lead to unexpected behavior if the intention is to use a shell function or alias instead of the original command.