# [Linux] Bash help Uso: Display built-in command information

## Overview
The `help` command in Bash is used to display information about built-in shell commands. It provides users with a quick reference to understand how to use these commands, including their options and syntax.

## Usage
The basic syntax of the `help` command is as follows:

```bash
help [options] [arguments]
```

You can use it to get information on a specific built-in command by providing the command name as an argument.

## Common Options
- `-s`, `--silent`: Suppress output of the command.
- `-m`, `--man`: Display the manual page for the command.
- `-d`, `--description`: Show a brief description of the command.

## Common Examples
Here are some practical examples of using the `help` command:

1. **Get help for a specific built-in command:**

   ```bash
   help cd
   ```

   This command will display information about the `cd` command, including its usage and options.

2. **List all available built-in commands:**

   ```bash
   help
   ```

   Running `help` without arguments will show a list of all built-in commands available in your shell.

3. **Get a brief description of a command:**

   ```bash
   help -d echo
   ```

   This will provide a short description of the `echo` command.

4. **Display help in a silent mode:**

   ```bash
   help -s pwd
   ```

   This command will show no output unless there is an error, useful for scripting.

## Tips
- Use `help` to quickly learn about built-in commands without needing to search online or consult external documentation.
- Combine `help` with other commands in scripts to provide users with context about what each command does.
- Remember that `help` only works for built-in commands; for external commands, consider using `man` or `--help` options.