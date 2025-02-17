# [Linux] Bash su equivalente: Switch user in the terminal

## Overview
The `su` command in Bash allows a user to switch to another user account within the terminal. By default, it switches to the root user, enabling administrative privileges for executing commands that require elevated permissions.

## Usage
The basic syntax of the `su` command is as follows:

```bash
su [options] [username]
```

If no username is specified, `su` defaults to the root user.

## Common Options
- `-l` or `--login`: Start the shell as a login shell, which initializes the environment as if the user had logged in directly.
- `-c`: Execute a command as the specified user and then exit.
- `-s`: Specify a different shell to use instead of the default shell.
- `-m` or `-p`: Preserve the environment variables of the current user.

## Common Examples
1. **Switch to the root user:**
   ```bash
   su
   ```
   This command prompts for the root password and switches to the root user.

2. **Switch to a specific user:**
   ```bash
   su john
   ```
   This command switches to the user account named "john".

3. **Execute a command as another user:**
   ```bash
   su -c 'ls /root' john
   ```
   This command runs the `ls /root` command as user "john".

4. **Start a login shell as another user:**
   ```bash
   su -l john
   ```
   This command switches to user "john" and starts a login shell, loading their environment.

5. **Preserve the environment while switching users:**
   ```bash
   su -m john
   ```
   This command switches to user "john" while keeping the current user's environment variables.

## Tips
- Always use `su` with caution, especially when switching to the root user, as it grants full control over the system.
- Consider using `sudo` for executing single commands with elevated privileges instead of switching users entirely.
- Remember that the `su` command requires the password of the target user, so ensure you have the necessary credentials.