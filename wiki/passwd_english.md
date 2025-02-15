# [리눅스] Bash passwd 사용법

## Overview
The `passwd` command in Bash is used to change user passwords on Unix-like operating systems. Its primary purpose is to enhance security by allowing users to update their passwords, ensuring that unauthorized access is minimized. The command can be used by both regular users to change their own passwords and by superusers (root) to modify passwords for other users.

## Usage
The basic syntax of the `passwd` command is as follows:

```bash
passwd [OPTION] [USERNAME]
```

### Common Options:
- `USERNAME`: Specify the username whose password you want to change. If omitted, the command will change the password for the current user.
- `-d`: Delete the password for the specified user, allowing them to log in without a password.
- `-e`: Expire the password immediately, forcing the user to change it upon next login.
- `-l`: Lock the specified user account, preventing login.
- `-u`: Unlock a previously locked user account.

## Examples

### Example 1: Changing Your Own Password
To change your own password, simply run the command without any options:

```bash
passwd
```

You will be prompted to enter your current password, followed by your new password twice for confirmation.

### Example 2: Changing Another User's Password
If you are a superuser and want to change the password for another user, specify the username:

```bash
sudo passwd username
```

Replace `username` with the actual username of the account whose password you wish to change. You will be prompted to enter a new password for that user.

## Tips
- Always choose a strong password that includes a mix of uppercase and lowercase letters, numbers, and special characters to enhance security.
- Regularly update your password to reduce the risk of unauthorized access.
- If you are changing another user's password, ensure you have the necessary permissions and inform the user of the change.
- Use the `-e` option to enforce a password change at the next login, which can be useful for security purposes after an account is created or reset.