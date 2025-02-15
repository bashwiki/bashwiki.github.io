# [리눅스] Bash userdel 사용법

## Overview
The `userdel` command in Bash is used to delete a user account from the system. Its primary purpose is to remove user information from the system's user database, effectively revoking access to the system for that user. When a user account is deleted, the associated home directory and mail spool can also be removed, depending on the options specified.

## Usage
The basic syntax of the `userdel` command is as follows:

```bash
userdel [options] username
```

### Common Options
- `-r` : This option removes the user's home directory and mail spool along with the user account.
- `-f` : Forces the removal of the user account, even if the user is currently logged in.
- `-Z` : This option will remove the SELinux user mapping for the user being deleted.

## Examples

### Example 1: Deleting a User Without Removing Home Directory
To delete a user named `exampleuser` without removing their home directory, you would use:

```bash
sudo userdel exampleuser
```

### Example 2: Deleting a User and Their Home Directory
To delete the same user and also remove their home directory and mail spool, you would use:

```bash
sudo userdel -r exampleuser
```

## Tips
- Always ensure that you have backed up any important data associated with the user account before deletion, especially if using the `-r` option.
- Check if the user is currently logged in before deleting the account to avoid potential issues. You can use the `who` or `w` command to see currently logged-in users.
- Consider using the `-f` option with caution, as it can lead to data loss if the user is actively using the system.
- Regularly review user accounts on your system to maintain security and manage user access effectively.