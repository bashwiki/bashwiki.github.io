# [Linux] Bash pkill Uso: Terminar procesos por nombre

## Overview
The `pkill` command in Bash is used to terminate processes based on their name or other attributes. It allows users to send signals to processes, making it a powerful tool for managing running applications.

## Usage
The basic syntax of the `pkill` command is as follows:

```bash
pkill [options] [arguments]
```

## Common Options
- `-f`: Match against the full command line instead of just the process name.
- `-n`: Kill the newest process matching the criteria.
- `-o`: Kill the oldest process matching the criteria.
- `-signal`: Specify a signal to send (e.g., `-9` for SIGKILL).
- `-u`: Specify the user whose processes to target.

## Common Examples
Here are some practical examples of using the `pkill` command:

1. **Terminate a process by name**:
   ```bash
   pkill firefox
   ```
   This command will terminate all instances of Firefox.

2. **Terminate a process using a specific signal**:
   ```bash
   pkill -9 chrome
   ```
   This sends the SIGKILL signal to all Chrome processes, forcing them to close immediately.

3. **Terminate processes based on a full command line match**:
   ```bash
   pkill -f "python script.py"
   ```
   This will terminate any process running the specified Python script.

4. **Kill the newest instance of a process**:
   ```bash
   pkill -n ssh
   ```
   This command will terminate the most recently started SSH session.

5. **Terminate processes for a specific user**:
   ```bash
   pkill -u username
   ```
   This will kill all processes owned by the specified user.

## Tips
- Always use caution when terminating processes, especially with `-9`, as it does not allow processes to clean up.
- Use `pgrep` to preview which processes will be affected by your `pkill` command before executing it.
- Combine `pkill` with other commands in scripts for automated process management.