# [Linux] Bash usermod Usage: Modify user account information

## Overview
The `usermod` command in Bash is used to modify existing user accounts on a Linux system. It allows administrators to change various attributes of user accounts, such as group memberships, home directories, and user names.

## Usage
The basic syntax of the `usermod` command is as follows:

```bash
usermod [options] [username]
```

## Common Options
- `-aG`: Append the user to the supplementary groups.
- `-d`: Change the user's home directory.
- `-l`: Change the user's login name.
- `-g`: Change the user's primary group.
- `-s`: Change the user's login shell.
- `-u`: Change the user's UID.

## Common Examples

### 1. Add a user to a supplementary group
To add a user named `john` to the `developers` group:

```bash
usermod -aG developers john
```

### 2. Change a user's home directory
To change the home directory of user `alice` to `/home/alice_new`:

```bash
usermod -d /home/alice_new alice
```

### 3. Change a user's login name
To change the login name of user `bob` to `robert`:

```bash
usermod -l robert bob
```

### 4. Change a user's primary group
To change the primary group of user `charlie` to `staff`:

```bash
usermod -g staff charlie
```

### 5. Change a user's login shell
To change the login shell of user `dave` to `/bin/zsh`:

```bash
usermod -s /bin/zsh dave
```

## Tips
- Always ensure you have the necessary permissions (usually root) to modify user accounts.
- Use the `-aG` option carefully to avoid removing the user from other groups.
- After changing a user's home directory, consider moving their existing files to the new location.
- Check the current user attributes using the `id` command before making changes.