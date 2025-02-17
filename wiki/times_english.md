# [Linux] Bash times: Display process timing information

## Overview
The `times` command in Bash is used to display the accumulated user and system time for the current shell and its child processes. This command is particularly useful for monitoring the performance of scripts and commands, allowing users to understand how much CPU time has been consumed.

## Usage
The basic syntax of the `times` command is as follows:

```bash
times [options] [arguments]
```

However, `times` does not take any arguments or options in most cases; it simply returns the timing information when executed.

## Common Options
The `times` command does not have any specific options or arguments. It is a straightforward command that outputs the timing data without additional configuration.

## Common Examples

### Example 1: Basic Usage
To display the accumulated time for the current shell and its child processes, simply run:

```bash
times
```

### Example 2: After Running a Command
You can run a command and then check the timing information. For example:

```bash
sleep 2
times
```
This will show the time spent in user and system mode after the `sleep` command has completed.

### Example 3: In a Script
You can include `times` in a script to monitor the execution time of various commands:

```bash
#!/bin/bash
echo "Starting script..."
sleep 3
echo "Running some commands..."
ls -l
times
```

## Tips
- Use `times` at the end of your scripts to get a summary of how much CPU time was used.
- Combine `times` with other commands in a script to analyze performance across multiple operations.
- Remember that `times` only shows the time for the current shell and its child processes, so it won't provide information about other running processes.