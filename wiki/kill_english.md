# [Linux] Bash kill用法: Terminate processes

## Overview
The `kill` command in Bash is used to send signals to processes, primarily to terminate them. It allows users to manage running processes by specifying their process IDs (PIDs) and the type of signal to send.

## Usage
The basic syntax of the `kill` command is as follows:

```bash
kill [options] [arguments]
```

## Common Options
- `-l`: List all signal names.
- `-s SIGNAL`: Specify the signal to send (e.g., `SIGKILL`, `SIGTERM`).
- `-n NUMBER`: Send the signal specified by the signal number.
- `-p`: Print the process ID of the specified process without sending a signal.

## Common Examples
1. **Terminate a process by PID**:
   To terminate a process with PID 1234:
   ```bash
   kill 1234
   ```

2. **Forcefully kill a process**:
   To forcefully kill a process using the `SIGKILL` signal:
   ```bash
   kill -9 1234
   ```

3. **Send a different signal**:
   To send the `SIGTERM` signal (default) to a process:
   ```bash
   kill -s SIGTERM 1234
   ```

4. **List available signals**:
   To list all available signals:
   ```bash
   kill -l
   ```

5. **Kill multiple processes**:
   To kill multiple processes at once:
   ```bash
   kill 1234 5678 91011
   ```

## Tips
- Always try to use `SIGTERM` (signal 15) before `SIGKILL` (signal 9) to allow processes to terminate gracefully.
- Use `ps` or `top` commands to find the PID of the process you want to kill.
- Be cautious when using `kill` with root privileges, as you might terminate critical system processes.