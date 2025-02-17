# [Linux] Bash id usage: Display user and group information

## Overview
The `id` command in Bash is used to display the user and group information for the current user or a specified user. It provides details such as the user ID (UID), group ID (GID), and the groups to which the user belongs.

## Usage
The basic syntax of the `id` command is as follows:

```bash
id [options] [username]
```

## Common Options
- `-u`: Display only the effective user ID.
- `-g`: Display only the effective group ID.
- `-G`: Display all group IDs the user belongs to.
- `-n`: Display names instead of numeric IDs.
- `-r`: Display the real ID instead of the effective ID.

## Common Examples
Here are some practical examples of using the `id` command:

1. **Display information for the current user:**
   ```bash
   id
   ```

2. **Display information for a specific user (e.g., username):**
   ```bash
   id username
   ```

3. **Display only the effective user ID:**
   ```bash
   id -u
   ```

4. **Display only the effective group ID:**
   ```bash
   id -g
   ```

5. **Display all group IDs for the current user:**
   ```bash
   id -G
   ```

6. **Display user information with names instead of numeric IDs:**
   ```bash
   id -n
   ```

## Tips
- Use `id` without any options to quickly check your own user and group information.
- Combine options for more specific queries, such as `id -Gn` to get the group names of the current user.
- If you encounter permission issues, ensure you have the necessary rights to view information for other users.