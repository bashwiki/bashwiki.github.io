# [Linux] Bash killall Uso: Termina procesos por nombre

## Overview
The `killall` command in Bash is used to terminate processes by their name. Unlike the `kill` command, which requires a process ID (PID), `killall` allows you to specify the name of the process you want to stop, making it easier to manage multiple instances of the same application.

## Usage
The basic syntax of the `killall` command is as follows:

```bash
killall [options] [arguments]
```

## Common Options
- `-u <user>`: Only kill processes owned by the specified user.
- `-i`: Prompt for confirmation before killing each process.
- `-q`: Suppress error messages for processes that do not exist.
- `-r`: Use regular expressions to match process names.
- `-s <signal>`: Specify a signal to send to the processes (default is `TERM`).

## Common Examples
Here are some practical examples of using the `killall` command:

1. **Terminate all instances of a process by name:**
   ```bash
   killall firefox
   ```

2. **Kill all processes owned by a specific user:**
   ```bash
   killall -u username
   ```

3. **Prompt for confirmation before killing each process:**
   ```bash
   killall -i chrome
   ```

4. **Use a regular expression to match process names:**
   ```bash
   killall -r 'python.*'
   ```

5. **Send a specific signal to a process (e.g., SIGKILL):**
   ```bash
   killall -s KILL apache2
   ```

## Tips
- Always double-check the process name before using `killall`, as it will terminate all matching processes without confirmation (unless the `-i` option is used).
- Use the `-q` option to avoid cluttering your terminal with error messages if some processes are not found.
- Consider using `pgrep` in combination with `killall` for more complex process management tasks, such as filtering processes based on additional criteria.