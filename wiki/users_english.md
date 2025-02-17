# [Linux] Bash users equivalente: List user information

## Overview
The `users` command in Bash is used to display the usernames of users currently logged into the system. It provides a quick way to see who is actively using the machine at any given time.

## Usage
The basic syntax of the `users` command is as follows:

```bash
users [options] [arguments]
```

## Common Options
- `-n`: Suppresses duplicate usernames, showing each user only once.
- `-r`: Displays only the usernames of users who are logged in as regular users, excluding system users.

## Common Examples

1. **Display currently logged-in users:**
   ```bash
   users
   ```

2. **Display unique usernames of logged-in users:**
   ```bash
   users -n
   ```

3. **Display usernames of regular users only:**
   ```bash
   users -r
   ```

## Tips
- Use the `-n` option when you want a cleaner output, especially in systems with multiple sessions from the same user.
- Combine the `users` command with other commands, like `wc -l`, to count the number of users currently logged in:
  ```bash
  users | wc -w
  ```
- Remember that the `users` command only shows users logged in at the time of execution; it does not provide historical login data.