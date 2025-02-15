# [리눅스] Bash env 사용법

## Overview
The `env` command in Bash is used to run a command in a modified environment. It allows users to set environment variables for the command being executed, or to print a list of the current environment variables. This command is particularly useful for scripting and for ensuring that a command runs with the correct environment settings.

## Usage
The basic syntax of the `env` command is as follows:

```bash
env [OPTION]... [NAME=VALUE]... [COMMAND [ARGUMENTS]...]
```

### Common Options
- `-i`, `--ignore-environment`: Start with an empty environment, ignoring the current environment variables.
- `-u`, `--unset=NAME`: Remove the variable NAME from the environment.
- `--help`: Display help information about the command.
- `--version`: Show the version of the `env` command.

## Examples

### Example 1: Running a Command with Modified Environment Variables
You can use `env` to run a command with specific environment variables. For instance, if you want to run a Python script with a specific `PYTHONPATH`, you can do so as follows:

```bash
env PYTHONPATH=/my/custom/path python my_script.py
```

In this example, `PYTHONPATH` is set to `/my/custom/path` only for the duration of `my_script.py`.

### Example 2: Listing Current Environment Variables
To simply list all the current environment variables, you can use the `env` command without any arguments:

```bash
env
```

This will display a list of all environment variables along with their values.

## Tips
- Use `env` in scripts to ensure that the script runs with the expected environment variables, especially when deploying applications in different environments.
- When using `-i` to ignore the current environment, be cautious as it may lead to unexpected behavior if the command relies on certain environment variables.
- Combine `env` with other commands in a pipeline to manipulate the environment dynamically, enhancing the flexibility of your scripts.