# [Linux] Bash userdel Usage: Remove user accounts

## Overview
The `userdel` command is used in Linux to delete a user account from the system. When a user is deleted, their home directory and mail spool can also be removed, depending on the options used.

## Usage
The basic syntax of the `userdel` command is as follows:

```bash
userdel [options] [username]
```

## Common Options
- `-r`: Remove the user's home directory and mail spool along with the user account.
- `-f`: Force the removal of the user account, even if the user is currently logged in.
- `-Z`: Remove any SELinux user mapping for the user account.

## Common Examples

1. **Delete a user without removing their home directory:**
   ```bash
   userdel john
   ```

2. **Delete a user and remove their home directory:**
   ```bash
   userdel -r john
   ```

3. **Forcefully delete a user who is currently logged in:**
   ```bash
   userdel -f john
   ```

4. **Delete a user and remove SELinux user mapping:**
   ```bash
   userdel -Z john
   ```

## Tips
- Always ensure that you have backed up any important data before deleting a user account.
- Use the `-r` option with caution, as it will permanently delete the user's home directory and all its contents.
- Check if the user is logged in before deletion to avoid disrupting active sessions, unless you are using the `-f` option intentionally.