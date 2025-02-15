# [리눅스] Bash ps 사용법

## Overview
The `ps` command in Bash is a powerful utility that provides information about the currently running processes on a Unix-like operating system. Its primary purpose is to display a snapshot of the current processes, including details such as process IDs (PIDs), user ownership, CPU and memory usage, and the command that started each process. This information is crucial for system monitoring, debugging, and performance tuning.

## Usage
The basic syntax for the `ps` command is:

```bash
ps [options]
```

Common options include:

- `-e` or `-A`: Show all processes running on the system.
- `-f`: Display full-format listing, which includes additional details such as the parent process ID (PPID) and the command line that started the process.
- `-u [user]`: Show processes for a specific user.
- `-aux`: A commonly used combination that displays all processes with detailed information, including those not associated with a terminal.

## Examples
Here are a couple of practical examples demonstrating how to use the `ps` command:

1. **Display all processes with detailed information**:
   ```bash
   ps aux
   ```
   This command will list all running processes along with detailed information such as the user, PID, CPU and memory usage, and the command that initiated the process.

2. **Show processes for a specific user**:
   ```bash
   ps -u username
   ```
   Replace `username` with the actual username. This command will display all processes that are owned by the specified user.

## Tips
- Use `ps -ef` for a full-format listing that includes the parent process ID, which can be useful for understanding process hierarchies.
- Combine `ps` with other commands like `grep` to filter results. For example, `ps aux | grep httpd` will show all processes related to the Apache HTTP server.
- Remember that `ps` provides a snapshot of processes at the time the command is run. For real-time monitoring, consider using commands like `top` or `htop`.
- Familiarize yourself with the various options available by consulting the manual page using `man ps` for a comprehensive understanding of its capabilities.