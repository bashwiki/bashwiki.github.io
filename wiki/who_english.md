# [리눅스] Bash who 사용법

## Overview
The `who` command in Bash is used to display information about users who are currently logged into the system. It provides details such as the username, terminal line, login time, and originating IP address or hostname. This command is particularly useful for system administrators and developers who need to monitor user activity on a multi-user system.

## Usage
The basic syntax of the `who` command is as follows:

```bash
who [OPTION...]
```

### Common Options
- `-a`, `--all`: Display all available information about users, including idle time and the process ID of their login session.
- `-b`, `--boot`: Show the last system boot time.
- `-q`, `--count`: Display only the usernames and the number of users currently logged in.
- `-H`, `--heading`: Print the column headings for the output.

## Examples

### Example 1: Basic Usage
To simply list the users currently logged into the system, you can use the command without any options:

```bash
who
```

**Output:**
```
user1    pts/0        2023-10-01 10:00 (192.168.1.10)
user2    pts/1        2023-10-01 10:05 (192.168.1.11)
```

### Example 2: Detailed User Information
To get a more detailed view of the logged-in users, including idle time and process IDs, you can use the `-a` option:

```bash
who -a
```

**Output:**
```
user1    pts/0        2023-10-01 10:00   .         1234 (192.168.1.10)
user2    pts/1        2023-10-01 10:05   .         5678 (192.168.1.11)
```

## Tips
- Use `who -q` to quickly check how many users are logged in without displaying their details.
- Combine `who` with other commands like `grep` to filter results. For example, to find a specific user, you can run:

  ```bash
  who | grep username
  ```

- Regularly check who is logged in, especially on shared systems, to maintain security and monitor user activity.