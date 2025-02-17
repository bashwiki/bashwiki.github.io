# [Linux] Bash builtin `builtin`: Access shell builtins directly

## Overview
The `builtin` command in Bash allows users to execute shell built-in commands directly, bypassing any external commands that may have the same name. This is particularly useful when you want to ensure that you are using the built-in version of a command rather than an external one.

## Usage
The basic syntax for the `builtin` command is as follows:

```bash
builtin [options] [arguments]
```

## Common Options
- `-p`: This option allows you to use the `builtin` command to print the location of the built-in command without executing it.
- `-f`: This option forces the execution of the built-in command, even if an external command with the same name exists.

## Common Examples

### Example 1: Using `builtin` to call a built-in command
To explicitly call the built-in `echo` command, you would use:

```bash
builtin echo "This is a built-in echo command."
```

### Example 2: Accessing the built-in `cd` command
If you want to ensure you are using the built-in `cd` command, you can do so like this:

```bash
builtin cd /path/to/directory
```

### Example 3: Finding the location of a built-in command
To find out where the built-in `type` command is located, you can use:

```bash
builtin -p type
```

### Example 4: Forcing the execution of a built-in command
If you have an external command named `test` and you want to ensure the built-in `test` is executed, you can use:

```bash
builtin test -z ""
```

## Tips
- Use `builtin` when you have a naming conflict between a built-in command and an external command to ensure the correct version is executed.
- Familiarize yourself with the built-in commands available in your shell to make better use of the `builtin` command.
- Remember that using `builtin` can help improve script performance by avoiding the overhead of starting an external command.