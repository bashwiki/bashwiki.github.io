# [리눅스] Bash su 사용법

## Overview
The `su` command, short for "substitute user," is a standard Unix/Linux command that allows a user to switch to another user account within a terminal session. Its primary purpose is to enable users to execute commands with the privileges of another user, typically the superuser (root), which is essential for performing administrative tasks that require elevated permissions.

## Usage
The basic syntax of the `su` command is as follows:

```bash
su [OPTION] [USER]
```

### Common Options:
- `-`: This option initiates a login shell for the target user, simulating a full login. It sets the environment variables as if the user had logged in directly.
- `-c`: This option allows you to pass a command to be executed as the target user. For example, `su -c 'command' USER`.
- `-s`: This option specifies a different shell to use instead of the default shell for the target user.
- `-l` or `--login`: Similar to `-`, this option starts a login shell for the target user.

If no user is specified, `su` defaults to the root user.

## Examples

1. **Switching to the root user:**
   To switch to the root user, simply run:
   ```bash
   su -
   ```
   After executing this command, you will be prompted to enter the root user's password. Once authenticated, you will have root privileges.

2. **Executing a command as another user:**
   If you want to run a specific command as another user without switching to their shell, you can use:
   ```bash
   su -c 'ls /root' username
   ```
   This command will list the contents of the `/root` directory as the specified `username`.

## Tips
- Always be cautious when using `su`, especially when switching to the root user, as it grants full control over the system.
- If you frequently need to execute commands as another user, consider using `sudo`, which can provide more granular control over permissions and is often preferred for security reasons.
- When using `su -`, remember that it will change your environment variables, so any environment-specific configurations will be reset to those of the target user.
- To avoid typing the password repeatedly, you can use `su` in combination with `ssh` to connect to remote systems where you have the necessary permissions.