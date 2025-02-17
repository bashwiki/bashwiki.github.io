# [Linux] Bash top Usage: Monitor system processes in real-time

## Overview
The `top` command is a powerful utility in Linux that provides a dynamic, real-time view of the system's running processes. It displays information about CPU usage, memory consumption, and the processes that are currently active, allowing users to monitor system performance and resource utilization effectively.

## Usage
The basic syntax of the `top` command is as follows:

```bash
top [options] [arguments]
```

## Common Options
Here are some common options you can use with the `top` command:

- `-d <seconds>`: Set the delay between updates (default is 3 seconds).
- `-n <number>`: Specify the number of iterations to display before exiting.
- `-p <pid>`: Monitor a specific process by its process ID (PID).
- `-u <user>`: Show processes for a specific user.

## Common Examples

1. **Start the top command:**
   ```bash
   top
   ```

2. **Set a custom update interval of 5 seconds:**
   ```bash
   top -d 5
   ```

3. **Display processes for a specific user:**
   ```bash
   top -u username
   ```

4. **Monitor a specific process by PID (e.g., PID 1234):**
   ```bash
   top -p 1234
   ```

5. **Limit the output to 10 iterations:**
   ```bash
   top -n 10
   ```

## Tips
- To sort processes by CPU usage while `top` is running, press `Shift + P`.
- To sort by memory usage, press `Shift + M`.
- You can kill a process directly from the `top` interface by pressing `k` and entering the PID of the process you want to terminate.
- Use the `h` key while in `top` to access help and see more options and commands available within the interface.