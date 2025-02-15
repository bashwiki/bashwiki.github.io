# [리눅스] Bash inotifywait 사용법

## Overview
`inotifywait` is a command-line utility that is part of the inotify tools package in Linux. It is used to monitor filesystem events, such as file modifications, deletions, and creations, in real-time. This command is particularly useful for developers and engineers who need to trigger actions based on changes in files or directories, making it an essential tool for tasks like automated testing, backup scripts, and live reloading in development environments.

## Usage
The basic syntax of the `inotifywait` command is as follows:

```bash
inotifywait [options] <path>
```

### Common Options
- `-m`, `--monitor`: Keep running and monitor for events continuously until interrupted.
- `-e`, `--event`: Specify the events to watch for (e.g., `modify`, `create`, `delete`, `move`).
- `-r`, `--recursive`: Watch directories recursively.
- `-q`, `--quiet`: Suppress output of the event name, only show the path.
- `-t`, `--timeout`: Set a timeout for the monitoring session in seconds.

## Examples

### Example 1: Monitor a Single File
To monitor a specific file for modifications, you can use the following command:

```bash
inotifywait -m -e modify /path/to/file.txt
```

This command will output a message every time `file.txt` is modified.

### Example 2: Monitor a Directory Recursively
If you want to monitor an entire directory for any file creation or deletion events, use:

```bash
inotifywait -m -r -e create,delete /path/to/directory
```

This command will continuously monitor the specified directory and all its subdirectories for any files being created or deleted.

## Tips
- **Combine with Scripts**: You can combine `inotifywait` with shell scripts to automate tasks. For example, you can trigger a build process whenever a source file changes.
- **Use with Logging**: Redirect the output of `inotifywait` to a log file to keep track of changes over time for auditing or debugging purposes.
- **Limit Events**: Only monitor the events you need to reduce the amount of output and improve performance. For instance, if you only care about file deletions, specify `-e delete`.
- **Handle Interruptions**: Since `inotifywait` runs indefinitely with the `-m` option, consider using a signal handler in your scripts to gracefully shut down the monitoring process when needed.

By utilizing `inotifywait`, you can effectively monitor filesystem changes and automate responses to those changes, enhancing your development and operational workflows.