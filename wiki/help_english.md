# [리눅스] Bash help 사용법

## Overview
The `help` command in Bash is a built-in utility that provides information about Bash built-in commands. Its primary purpose is to assist users in understanding the usage and options of various built-in commands without needing to refer to external documentation. This command is particularly useful for quick reference while working in the terminal.

## Usage
The basic syntax of the `help` command is as follows:

```bash
help [COMMAND]
```

- `COMMAND`: This is an optional argument where you can specify the name of the built-in command you want help with. If no command is provided, `help` will display a list of all available built-in commands.

### Common Options
- `-s`, `--silent`: Suppresses the output of the command and only returns the exit status.
- `-m`, `--man`: Displays the help information in a format similar to the `man` command.

## Examples

1. **Get Help on a Specific Built-in Command**
   To get help on the `cd` command, you can run:

   ```bash
   help cd
   ```

   This will display information about how to use the `cd` command, including its options and usage examples.

2. **List All Available Built-in Commands**
   If you want to see a list of all built-in commands available in your Bash session, simply run:

   ```bash
   help
   ```

   This will output a list of all built-in commands along with a brief description of each.

## Tips
- Use `help` as a quick reference tool when you are unsure about the syntax or options of a built-in command.
- Remember that `help` only provides information on built-in commands. For external commands, you should use the `man` command or `--help` option with the specific command.
- Familiarize yourself with the most commonly used built-in commands to enhance your efficiency in the terminal.