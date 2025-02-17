# [Linux] Bash source equivalent: Execute commands from a file in the current shell

## Overview
The `source` command in Bash is used to execute commands from a specified file in the current shell session. This allows you to run scripts or load environment variables without creating a new subshell, making it a handy tool for managing your shell environment.

## Usage
The basic syntax of the `source` command is as follows:

```bash
source [options] [filename]
```

You can also use the shorthand `.` (dot) to achieve the same effect:

```bash
. [filename]
```

## Common Options
The `source` command does not have many options, but here are some relevant ones:

- `-h`, `--help`: Display help information about the command.
- `-V`, `--version`: Show the version of the shell.

## Common Examples

### Example 1: Sourcing a script
To execute a script named `myscript.sh` in the current shell, you can use:

```bash
source myscript.sh
```

### Example 2: Using the dot shorthand
You can achieve the same result using the dot shorthand:

```bash
. myscript.sh
```

### Example 3: Loading environment variables
If you have a file named `env_vars.sh` that sets environment variables, you can load them into your current session:

```bash
source env_vars.sh
```

### Example 4: Sourcing a file with arguments
While `source` itself does not take arguments, you can pass arguments to the commands within the sourced file. For example, if `script.sh` uses positional parameters, you can call it like this:

```bash
source script.sh arg1 arg2
```

## Tips
- Always ensure that the script you are sourcing is safe and does not contain harmful commands, as it will run in your current shell environment.
- Use `source` to load configuration files for your shell or applications to avoid restarting the shell.
- If you frequently use a specific script, consider adding it to your `.bashrc` or `.bash_profile` to load it automatically when starting a new shell session.