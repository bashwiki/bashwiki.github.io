# [Linux] Bash w: Display who is logged on and what they are doing

## Overview
The `w` command in Bash is used to display information about users currently logged into the system and their activities. It provides details such as the username, the terminal they are using, their login time, idle time, and the command they are currently executing.

## Usage
The basic syntax of the `w` command is as follows:

```bash
w [options] [user]
```

## Common Options
- `-h`: Suppresses the header line.
- `-s`: Displays the output in a shorter format.
- `-f`: Shows the full login name of the users.
- `-u`: Displays the user’s idle time in a more human-readable format.

## Common Examples

1. **Basic Usage**
   To display a list of currently logged-in users and their activities:
   ```bash
   w
   ```

2. **Suppressing the Header**
   To view the information without the header line:
   ```bash
   w -h
   ```

3. **Short Format**
   To show the output in a shorter format:
   ```bash
   w -s
   ```

4. **Full User Names**
   To display the full login names of the users:
   ```bash
   w -f
   ```

5. **Checking a Specific User**
   To check the activity of a specific user (e.g., `john`):
   ```bash
   w john
   ```

## Tips
- Use `w` regularly to monitor system usage and identify active users.
- Combine `w` with other commands like `grep` to filter results for specific users or activities.
- Remember that the output can change rapidly, so consider running the command multiple times for a better overview of user activity.