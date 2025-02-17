# [Linux] Bash useradd Usage: Create a new user account

## Overview
The `useradd` command is used in Linux systems to create a new user account. It allows system administrators to add users to the system, set their home directories, and configure various user settings.

## Usage
The basic syntax of the `useradd` command is as follows:

```bash
useradd [options] [username]
```

## Common Options
- `-m`: Create the user's home directory if it does not exist.
- `-d`: Specify the home directory for the new user.
- `-s`: Set the login shell for the new user.
- `-G`: Add the user to specified supplementary groups.
- `-c`: Provide a comment or description for the user account.
- `-e`: Set an expiration date for the user account.

## Common Examples

1. **Create a new user with a home directory:**
   ```bash
   useradd -m newuser
   ```

2. **Create a user with a specific home directory:**
   ```bash
   useradd -d /home/customuser -m customuser
   ```

3. **Create a user with a specific shell:**
   ```bash
   useradd -s /bin/bash newuser
   ```

4. **Create a user and add them to supplementary groups:**
   ```bash
   useradd -G sudo,developers newuser
   ```

5. **Create a user with a comment:**
   ```bash
   useradd -c "John Doe, Developer" johndoe
   ```

6. **Create a user with an expiration date:**
   ```bash
   useradd -e 2023-12-31 expireduser
   ```

## Tips
- Always use the `-m` option to ensure that a home directory is created for the new user.
- Use the `-s` option to set a preferred shell, especially if the user will be using the command line frequently.
- Consider adding users to relevant groups using the `-G` option for appropriate permissions.
- After creating a user, remember to set a password using the `passwd` command.