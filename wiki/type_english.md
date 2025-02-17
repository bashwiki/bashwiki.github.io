# [Linux] Bash type comando: [determinar tipo de comando]

## Overview
The `type` command in Bash is used to determine the type of a command, whether it is a built-in shell command, an alias, a function, or an external executable. This can be particularly useful for understanding how a command will behave when executed.

## Usage
The basic syntax of the `type` command is as follows:

```bash
type [options] [arguments]
```

## Common Options
- `-t`: Outputs a single word describing the type of the command (e.g., alias, function, builtin, file).
- `-a`: Displays all locations of the command, including aliases and functions, not just the first one found.
- `-p`: Shows the path of the command if it is an external executable.

## Common Examples

### Example 1: Determine the type of a command
```bash
type ls
```
This will output something like `ls is /bin/ls`, indicating that `ls` is an external command located in `/bin`.

### Example 2: Check if a command is built-in
```bash
type echo
```
The output will be `echo is a shell builtin`, showing that `echo` is a built-in command.

### Example 3: List all locations of a command
```bash
type -a ls
```
This will return all instances of `ls`, including any aliases or functions that may exist.

### Example 4: Get the type of an alias
```bash
alias ll='ls -l'
type ll
```
The output will be `ll is aliased to 'ls -l'`, indicating that `ll` is an alias for `ls -l`.

## Tips
- Use `type` to troubleshoot command issues by verifying if a command is being overridden by an alias or function.
- Combine `type` with other commands in scripts to ensure the correct command type is being used.
- Remember that `type` does not execute the command; it only provides information about it.