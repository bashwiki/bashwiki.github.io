# [리눅스] Bash users 사용법

## Overview
The `users` command in Bash is a simple utility that displays the usernames of users who are currently logged into the system. Its primary purpose is to provide a quick way to see which users are active at a given moment, making it useful for system administrators and developers who need to monitor user activity.

## Usage
The basic syntax of the `users` command is as follows:

```bash
users [OPTION]
```

### Common Options
The `users` command does not have many options, but here are some common usages:

- **No options**: When run without any options, `users` will simply output the usernames of all users currently logged in, separated by spaces.

## Examples
Here are a couple of practical examples demonstrating how to use the `users` command:

1. **Basic Usage**:
   To see the list of currently logged-in users, simply run:

   ```bash
   users
   ```

   **Output**:
   ```
   user1 user2 user3
   ```

   This output indicates that `user1`, `user2`, and `user3` are currently logged into the system.

2. **Using in a Script**:
   You can incorporate the `users` command into a shell script to log active users. For example:

   ```bash
   #!/bin/bash
   echo "Currently logged in users: $(users)" >> user_log.txt
   ```

   This script appends the list of currently logged-in users to a file named `user_log.txt`.

## Tips
- **Combine with other commands**: You can use the output of the `users` command in combination with other commands, such as `wc -w`, to count the number of logged-in users:

   ```bash
   users | wc -w
   ```

   This command will return the total number of users currently logged in.

- **Use in monitoring**: Incorporate the `users` command in monitoring scripts to keep track of user activity over time, especially on multi-user systems.

By understanding and utilizing the `users` command, you can efficiently monitor user activity on your system.