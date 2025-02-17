# [Linux] Bash passwd uso: Change user passwords

## Overview
The `passwd` command in Linux is used to change user passwords. It allows users to update their own passwords or, if executed by a superuser, to change passwords for other users. This command is essential for maintaining security by ensuring that user accounts have strong, unique passwords.

## Usage
The basic syntax of the `passwd` command is as follows:

```bash
passwd [options] [username]
```

If no username is specified, the command will change the password for the currently logged-in user.

## Common Options
- `-d`: Delete the password for the specified user, allowing login without a password.
- `-e`: Expire the password immediately, forcing the user to change it upon next login.
- `-l`: Lock the specified user's password, preventing them from logging in.
- `-u`: Unlock a previously locked user account.
- `-S`: Display the password status of the specified user.

## Common Examples

1. **Change your own password:**
   ```bash
   passwd
   ```

2. **Change another user's password (requires superuser privileges):**
   ```bash
   sudo passwd username
   ```

3. **Delete a user's password:**
   ```bash
   sudo passwd -d username
   ```

4. **Expire a user's password immediately:**
   ```bash
   sudo passwd -e username
   ```

5. **Lock a user's account:**
   ```bash
   sudo passwd -l username
   ```

6. **Unlock a user's account:**
   ```bash
   sudo passwd -u username
   ```

7. **Check the password status of a user:**
   ```bash
   passwd -S username
   ```

## Tips
- Always use strong passwords that combine letters, numbers, and special characters to enhance security.
- Regularly update passwords to minimize the risk of unauthorized access.
- If you are changing another user's password, ensure you have the necessary permissions to avoid errors.