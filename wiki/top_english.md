# [리눅스] Bash top 사용법

## Overview
The `top` command is a powerful utility in Linux that provides a real-time view of the system's resource usage. It displays a dynamic, real-time summary of system processes, including CPU and memory usage, allowing engineers and developers to monitor system performance and identify resource-intensive processes. This command is particularly useful for diagnosing performance issues and managing system resources effectively.

## Usage
The basic syntax of the `top` command is simply:

```bash
top
```

When executed, `top` will display a continuously updating list of processes. Here are some common options you can use with the `top` command:

- `-d <seconds>`: Set the delay between updates. For example, `top -d 5` will refresh every 5 seconds.
- `-p <pid>`: Monitor a specific process by its PID. For example, `top -p 1234` will only show the process with PID 1234.
- `-u <username>`: Display processes for a specific user. For example, `top -u john` will show processes owned by the user "john".

## Examples

1. **Basic Usage**:
   To start monitoring system processes, simply run:
   ```bash
   top
   ```
   This will open the `top` interface, where you can see a list of processes along with their CPU and memory usage.

2. **Monitor a Specific Process**:
   If you want to monitor a process with PID 1234, you can use:
   ```bash
   top -p 1234
   ```
   This will filter the output to show only the specified process, allowing you to focus on its resource consumption.

## Tips
- **Interactive Commands**: While `top` is running, you can use various interactive commands to sort and manage processes. For example, pressing `M` will sort processes by memory usage, while pressing `P` will sort by CPU usage.
- **Killing Processes**: You can kill a process directly from the `top` interface by pressing `k`, then entering the PID of the process you want to terminate.
- **Customizing Display**: You can customize the display by pressing `f` to add or remove fields from the output, allowing you to tailor the information to your needs.
- **Exiting**: To exit the `top` command, simply press `q`.

Using `top` effectively can greatly enhance your ability to monitor and manage system performance in real-time.