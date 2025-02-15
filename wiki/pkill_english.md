# [리눅스] Bash pkill 사용법

## Overview
`pkill` is a command-line utility in Unix-like operating systems that allows users to terminate processes based on their names or other attributes. Unlike the `kill` command, which requires the process ID (PID) to terminate a process, `pkill` simplifies this by allowing users to specify the name of the process directly. This is particularly useful for managing multiple instances of a process without needing to look up their PIDs.

## Usage
The basic syntax of the `pkill` command is as follows:

```bash
pkill [options] pattern
```

### Common Options
- `-f`: Match against the full command line instead of just the process name.
- `-n`: Only kill the newest process matching the pattern.
- `-o`: Only kill the oldest process matching the pattern.
- `-signal`: Specify a signal to send to the process (default is `TERM`).
- `-u`: Match processes owned by a specific user.

## Examples

### Example 1: Terminating a Process by Name
To terminate all instances of a process named `firefox`, you can use the following command:

```bash
pkill firefox
```

This command sends the default `TERM` signal to all processes with the name `firefox`, effectively closing them.

### Example 2: Using Full Command Line Matching
If you want to terminate a process that may have a similar name or if you want to be more specific, you can use the `-f` option. For example, to kill a process that includes the string `python script.py` in its command line, you can run:

```bash
pkill -f "python script.py"
```

This command will match and terminate any process that has `python script.py` in its command line.

## Tips
- Always double-check the processes you are about to terminate, especially in a production environment, to avoid accidentally closing critical applications.
- Use the `-n` or `-o` options if you only want to terminate the most recent or oldest instance of a process, respectively.
- Consider using `pkill -l` to list the signals available for use with `pkill`, which can help you specify the right signal for your needs.
- For safety, you can use `pgrep` with the same pattern first to see which processes will be affected before executing `pkill`.

By understanding and utilizing `pkill`, you can efficiently manage processes on your system with ease.