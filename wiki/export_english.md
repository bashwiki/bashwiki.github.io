# [리눅스] Bash export 사용법

## Overview
The `export` command in Bash is used to set environment variables or mark variables for automatic export to the environment of subsequently executed commands. This is particularly useful when you want to make certain variables available to child processes, allowing them to inherit the values set in the parent shell.

## Usage
The basic syntax for the `export` command is as follows:

```bash
export [OPTION] [VARIABLE[=VALUE]]
```

### Common Options
- `-p`: Displays all exported variables in the current shell session.
- `-n`: Unsets the export attribute for the specified variable, making it no longer available to child processes.

## Examples

### Example 1: Setting an Environment Variable
To set an environment variable called `MY_VAR` and make it available to child processes, you can use:

```bash
export MY_VAR="Hello, World!"
```

You can verify that the variable is set by using the `echo` command:

```bash
echo $MY_VAR
```

### Example 2: Exporting Multiple Variables
You can export multiple variables in a single command. For example:

```bash
export VAR1="Value1" VAR2="Value2"
```

To check if both variables are exported, you can use:

```bash
echo $VAR1
echo $VAR2
```

## Tips
- Always use `export` when you need environment variables to be accessible in scripts or programs that are executed from the shell.
- To view all currently exported variables, simply run `export -p`.
- Remember that changes made to environment variables using `export` will only persist for the duration of the shell session unless you add them to your shell's configuration files (like `.bashrc` or `.bash_profile`).
- Be cautious when naming environment variables to avoid conflicts with existing system variables.