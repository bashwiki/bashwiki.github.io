# [Linux] Bash watch uso: Execute a command periodically

## Overview
The `watch` command in Bash is a useful utility that allows you to execute a specified command at regular intervals. This is particularly helpful for monitoring changes in the output of commands, such as system resource usage or file changes.

## Usage
The basic syntax of the `watch` command is as follows:

```bash
watch [options] [arguments]
```

## Common Options
- `-n, --interval <seconds>`: Specify the interval in seconds between command executions. The default is 2 seconds.
- `-d, --differences`: Highlight the differences between successive outputs.
- `-t, --no-title`: Disable the display of the header showing the command being executed and the interval.
- `-x, --exec`: Execute the command with the specified arguments.

## Common Examples

### Example 1: Monitor Disk Usage
To monitor the disk usage of the root directory every 5 seconds, you can use:

```bash
watch -n 5 df -h /
```

### Example 2: Check Running Processes
To see the list of running processes and update it every 2 seconds:

```bash
watch ps aux
```

### Example 3: Monitor a Log File
To monitor the last 10 lines of a log file and see updates:

```bash
watch tail -n 10 /var/log/syslog
```

### Example 4: Highlight Changes
To highlight changes in the output of a command, such as checking the contents of a directory:

```bash
watch -d ls -l /path/to/directory
```

## Tips
- Use the `-n` option to adjust the refresh rate according to your needs; a shorter interval can provide real-time monitoring.
- Combine `watch` with commands that generate dynamic output to effectively track changes.
- Use the `-t` option if you want a cleaner output without the header, which can be useful for scripts or logging.