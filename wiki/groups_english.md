# [Linux] Bash groups equivalente de uso: Listar grupos de usuarios

## Overview
The `groups` command in Bash is used to display the groups that a specified user belongs to. If no user is specified, it shows the groups for the current user. This command is particularly useful for managing user permissions and understanding user roles within a system.

## Usage
The basic syntax of the `groups` command is as follows:

```bash
groups [options] [username]
```

## Common Options
- `-h`, `--help`: Display help information about the command.
- `-v`, `--version`: Show the version of the `groups` command.

## Common Examples
Here are some practical examples of using the `groups` command:

1. **Display groups for the current user:**
   ```bash
   groups
   ```

2. **Display groups for a specific user:**
   ```bash
   groups username
   ```

3. **Display groups for multiple users:**
   ```bash
   groups user1 user2
   ```

4. **Display help information:**
   ```bash
   groups --help
   ```

## Tips
- Use the `groups` command to quickly verify user permissions before performing administrative tasks.
- Combine the `groups` command with other commands like `id` to get more detailed information about users and their group memberships.
- Remember that group memberships can affect access to files and directories, so it's important to check them regularly, especially in multi-user environments.