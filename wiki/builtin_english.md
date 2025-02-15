# [리눅스] Bash builtin 사용법

## Overview
The `builtin` command in Bash is used to execute shell built-in commands directly, bypassing any external commands that may have the same name. This is particularly useful when you want to ensure that you are using the built-in version of a command, especially in cases where an external command might shadow the built-in one. The primary purpose of the `builtin` command is to provide a way to access these built-in commands without ambiguity.

## Usage
The basic syntax of the `builtin` command is as follows:

```bash
builtin [command [arguments...]]
```

### Common Options
- `command`: This is the name of the built-in command you want to execute.
- `arguments`: These are the optional arguments that you can pass to the built-in command.

## Examples

### Example 1: Using `builtin` with the `echo` command
To ensure that you are using the built-in `echo` command, you can use:

```bash
builtin echo "This is a built-in echo command."
```

This command will execute the built-in version of `echo`, regardless of any external `echo` command that might be present in your PATH.

### Example 2: Using `builtin` with the `cd` command
If you want to change the directory using the built-in `cd` command, you can do so as follows:

```bash
builtin cd /path/to/directory
```

This ensures that you are using the built-in `cd` command, which is necessary for changing the shell's current working directory.

## Tips
- Use `builtin` when you need to avoid conflicts with external commands that have the same name as built-ins. This is particularly important in scripts where command names may overlap.
- Remember that not all commands have built-in versions. You can check if a command is a built-in by using the `type` command, like so: `type command_name`.
- While using `builtin` can help avoid ambiguity, it is generally not necessary for most common commands unless you are specifically dealing with name conflicts.