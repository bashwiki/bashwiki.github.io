# [리눅스] Bash usermod 사용법

## Overview
The `usermod` command in Linux is a powerful utility used to modify user accounts. Its primary purpose is to change user attributes such as username, home directory, group memberships, and user permissions. This command is typically used by system administrators to manage user accounts effectively.

## Usage
The basic syntax for the `usermod` command is as follows:

```bash
usermod [options] username
```

### Common Options
- `-l new_username`: Change the username of the specified user.
- `-d new_home`: Change the user's home directory to `new_home`.
- `-m`: Move the contents of the user's home directory to the new location when changing the home directory.
- `-G group1[,group2,...]`: Add the user to the specified supplementary groups.
- `-a`: Append the user to the supplementary groups specified with the `-G` option (without this, the user will be removed from other groups).
- `-s shell`: Change the user's login shell to `shell`.
- `-e expire_date`: Set the date on which the user account will expire.

## Examples

### Example 1: Changing a Username
To change a user's username from `olduser` to `newuser`, you would use the following command:

```bash
usermod -l newuser olduser
```

### Example 2: Adding a User to a Group
To add the user `john` to the supplementary group `developers`, you can use:

```bash
usermod -aG developers john
```

## Tips
- Always ensure that you have the necessary administrative privileges to execute the `usermod` command, as it typically requires root access.
- Be cautious when changing usernames or home directories, as this can affect user permissions and access to files.
- Use the `-m` option when changing the home directory to ensure that the user's files are moved to the new location, preventing potential data loss.
- After making changes with `usermod`, it is often a good practice to inform the user of the changes, especially if their username or home directory has been altered.