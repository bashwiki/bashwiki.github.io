# [리눅스] Bash watch 사용법

## Overview
The `watch` command in Bash is a utility that allows users to execute a specified command at regular intervals, displaying the output in the terminal. Its primary purpose is to monitor the output of commands that change over time, making it particularly useful for observing system performance, file changes, or any other dynamic data.

## Usage
The basic syntax of the `watch` command is as follows:

```bash
watch [options] command
```

### Common Options
- `-n, --interval`: Specify the interval (in seconds) between command executions. The default is 2 seconds.
- `-d, --differences`: Highlight the differences between successive updates. This option makes it easier to spot changes in the output.
- `-t, --no-title`: Suppress the header showing the command being executed and the interval.
- `-x, --exec`: Execute the command with arguments, allowing for more complex command structures.

## Examples

### Example 1: Monitoring Disk Usage
To monitor the disk usage of the `/home` directory every 5 seconds, you can use the following command:

```bash
watch -n 5 du -sh /home
```

This command will execute `du -sh /home` every 5 seconds, providing a real-time view of the disk usage.

### Example 2: Checking System Load
To observe the system load average every 2 seconds and highlight any changes, use:

```bash
watch -d uptime
```

This command will run `uptime` every 2 seconds and highlight any differences in the load averages, making it easy to see how the load changes over time.

## Tips
- Use the `-d` option to quickly identify changes in the output, especially when monitoring outputs that can vary frequently.
- Adjust the interval with `-n` to suit your needs; shorter intervals provide more real-time data but can be overwhelming, while longer intervals may miss quick changes.
- Combine `watch` with commands that generate concise outputs to keep the terminal output manageable and readable.
- If you want to stop the `watch` command, simply press `Ctrl + C` to terminate it.