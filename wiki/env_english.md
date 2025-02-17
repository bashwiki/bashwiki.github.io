# [Linux] Bash env uso equivalente: Manage environment variables

## Overview
The `env` command in Bash is used to run a command in a modified environment. It allows you to set or unset environment variables for the command you want to execute, making it a useful tool for testing and running applications with specific configurations.

## Usage
The basic syntax of the `env` command is as follows:

```bash
env [options] [arguments]
```

## Common Options
- `-i`: Start with an empty environment, ignoring the current environment variables.
- `-u NAME`: Remove the variable NAME from the environment.
- `-0`: Use a null character as the delimiter instead of a newline (useful for handling filenames with spaces).

## Common Examples

1. **Running a command with a modified environment variable:**
   ```bash
   env VAR=value command
   ```
   This sets `VAR` to `value` only for the execution of `command`.

2. **Clearing all environment variables:**
   ```bash
   env -i bash
   ```
   This starts a new Bash shell with no inherited environment variables.

3. **Removing a specific environment variable:**
   ```bash
   env -u VAR command
   ```
   This runs `command` without the environment variable `VAR`.

4. **Listing all current environment variables:**
   ```bash
   env
   ```
   This displays all the environment variables currently set in the shell.

5. **Running a script with a specific environment:**
   ```bash
   env PATH=/custom/path ./script.sh
   ```
   This executes `script.sh` with a modified `PATH`.

## Tips
- Use `env` to test scripts in a clean environment to avoid unexpected behavior due to inherited variables.
- When scripting, consider using `env` to ensure that your scripts run with the correct interpreter by specifying it at the top of the script (e.g., `#!/usr/bin/env python`).
- Be cautious when using `-i`, as it will remove all environment variables, which might affect the execution of commands that rely on them.