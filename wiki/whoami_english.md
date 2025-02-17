# [Linux] Bash whoami Uso equivalente: Display current user name

## Overview
The `whoami` command is a simple yet effective tool in Bash that displays the username of the current user who is logged into the terminal session. It is particularly useful for confirming your identity in multi-user environments or when working with scripts that require user-specific actions.

## Usage
The basic syntax of the `whoami` command is as follows:

```bash
whoami [options] [arguments]
```

## Common Options
The `whoami` command does not have many options, but here are the commonly used ones:

- `--help`: Displays help information about the command and its usage.
- `--version`: Shows the version of the `whoami` command.

## Common Examples

1. **Display Current User**
   To simply display the username of the current user, you can run:
   ```bash
   whoami
   ```

2. **Using with Other Commands**
   You can use `whoami` in combination with other commands. For example, to create a directory named after the current user:
   ```bash
   mkdir /home/$(whoami)/new_directory
   ```

3. **Check User in a Script**
   In a Bash script, you can check if the current user is 'admin':
   ```bash
   if [ "$(whoami)" = "admin" ]; then
       echo "You are logged in as admin."
   else
       echo "You are not logged in as admin."
   fi
   ```

4. **Display Help Information**
   To view help information for the `whoami` command, use:
   ```bash
   whoami --help
   ```

## Tips
- Use `whoami` to quickly verify your user identity, especially when executing commands that require elevated privileges.
- Combine `whoami` with other commands in scripts to tailor actions based on the logged-in user.
- Remember that `whoami` will only show the username of the user associated with the current terminal session, which can differ from the root user or other users in a multi-user system.