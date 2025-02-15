# [리눅스] Bash sudo 사용법

## Overview
The `sudo` command, short for "superuser do," is a powerful utility in Unix-like operating systems that allows a permitted user to execute a command as the superuser (root) or another user, as specified by the security policy. Its primary purpose is to grant users the ability to perform administrative tasks without needing to log in as the root user, thus enhancing security by limiting root access.

## Usage
The basic syntax of the `sudo` command is as follows:

```bash
sudo [OPTION] COMMAND [ARGUMENTS...]
```

### Common Options
- `-u USER`: Specify the user to run the command as. If not specified, the command runs as the root user.
- `-k`: Invalidate the user's cached credentials, requiring them to enter their password the next time they use `sudo`.
- `-l`: List the user's privileges or the commands they are allowed to run.
- `-v`: Extend the user's cached credentials for a specified period.

## Examples
### Example 1: Running a Command as Root
To update the package list on a Debian-based system, you can use:

```bash
sudo apt update
```

This command runs `apt update` with superuser privileges, allowing it to access system files necessary for updating the package list.

### Example 2: Running a Command as a Different User
To run a command as a specific user (e.g., `username`), you can use:

```bash
sudo -u username whoami
```

This command will execute `whoami` as `username`, returning the username of the specified user instead of the current user.

## Tips
- Always use `sudo` with caution. Executing commands as the root user can lead to unintended changes or damage to the system.
- Familiarize yourself with the commands you are running with `sudo` to avoid accidental system modifications.
- Consider using `sudo -l` to check your privileges and understand which commands you are allowed to run.
- If you find yourself needing to run multiple commands as root, consider using `sudo su` to switch to the root user temporarily, but remember to exit when done to maintain security.