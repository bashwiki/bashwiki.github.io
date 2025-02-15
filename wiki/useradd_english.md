# [리눅스] Bash useradd 사용법

## Overview
The `useradd` command is a fundamental utility in Linux systems used for creating new user accounts. Its primary purpose is to add a new user to the system, allowing for user-specific configurations and permissions. This command is typically executed by a system administrator and is essential for managing user access and security on multi-user systems.

## Usage
The basic syntax for the `useradd` command is as follows:

```bash
useradd [options] username
```

### Common Options:
- `-c, --comment`: Allows you to add a comment or description for the user.
- `-d, --home HOME_DIR`: Specifies the home directory for the new user. If not provided, a default home directory is created.
- `-m, --create-home`: Creates the user's home directory if it does not exist.
- `-s, --shell SHELL`: Specifies the login shell for the new user. The default is usually `/bin/bash`.
- `-G, --groups GROUP1[,GROUP2,...]`: Adds the user to specified supplementary groups.
- `-p, --password PASSWORD`: Sets the user's password (hashed).
- `-e, --expiredate EXPIRE_DATE`: Sets the date on which the user account will be disabled.

## Examples
### Example 1: Creating a Basic User
To create a new user named `john` with a home directory and default shell, you can use the following command:

```bash
sudo useradd -m john
```

### Example 2: Creating a User with Additional Options
To create a user named `alice`, set a comment, specify a home directory, and assign a shell, you can use:

```bash
sudo useradd -m -c "Alice Doe" -d /home/alice -s /bin/zsh alice
```

## Tips
- Always use the `-m` option to ensure that the user's home directory is created, as it is essential for user-specific files.
- Consider using the `-G` option to add users to additional groups for better permission management.
- After creating a user with `useradd`, remember to set a password using the `passwd` command:

```bash
sudo passwd john
```

- Be cautious with the `-p` option, as it requires a hashed password. It is generally safer to set the password separately after account creation.
- Regularly review user accounts and remove any that are no longer needed to maintain system security.