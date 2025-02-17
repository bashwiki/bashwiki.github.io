# [Linux] Bash export Uso equivalente: Set environment variables

The `export` command is used to set environment variables in a Bash shell, making them available to child processes.

## Overview
The `export` command allows you to create environment variables or mark existing shell variables for export to child processes. This is essential for passing configuration settings or other data to scripts and programs that are executed from the shell.

## Usage
The basic syntax of the `export` command is as follows:

```bash
export [options] [arguments]
```

## Common Options
- `-n`: Unsets the export property for the specified variable, making it a regular shell variable.
- `-p`: Displays all exported variables and their values.

## Common Examples

### Example 1: Exporting a new variable
To create and export a new environment variable named `MY_VAR` with the value `Hello, World!`, use:

```bash
export MY_VAR="Hello, World!"
```

### Example 2: Exporting an existing variable
If you already have a variable and want to export it, you can do so like this:

```bash
MY_VAR="Hello, World!"
export MY_VAR
```

### Example 3: Unsetting an exported variable
To unset the export property of a variable, use the `-n` option:

```bash
export -n MY_VAR
```

### Example 4: Displaying all exported variables
To see all currently exported variables, you can use:

```bash
export -p
```

## Tips
- Always use quotes around variable values that contain spaces to avoid syntax errors.
- Remember that exported variables are available to any child processes, so be cautious with sensitive information.
- Use `unset` to remove a variable entirely if it is no longer needed.