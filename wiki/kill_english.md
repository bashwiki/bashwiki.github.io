# [리눅스] Bash kill 사용법

## Overview
The `kill` command in Bash is used to send signals to processes. Its primary purpose is to terminate processes, but it can also be used to send other types of signals, such as those that pause or continue a process. The command is essential for managing processes in a Unix-like operating system, allowing users to control and manipulate running applications.

## Usage
The basic syntax of the `kill` command is as follows:

```bash
kill [options] <pid>
```

- `<pid>`: This is the Process ID of the process you want to send a signal to. You can find a process's PID using commands like `ps` or `top`.
- **Common Options**:
  - `-l`: Lists all available signal names.
  - `-s <signal>`: Specifies the signal to send. If not specified, the default signal is `TERM` (terminate).
  - `-9`: This option sends the `SIGKILL` signal, which forcefully terminates a process without allowing it to clean up.

## Examples
### Example 1: Terminating a Process
To terminate a process with PID 1234, you would use the following command:

```bash
kill 1234
```

This sends the default `TERM` signal to the process, requesting it to terminate gracefully.

### Example 2: Forcefully Killing a Process
If the process does not terminate with the default signal, you can use the `-9` option to forcefully kill it:

```bash
kill -9 1234
```

This sends the `SIGKILL` signal, which immediately stops the process.

## Tips
- Always try to terminate a process with the default `TERM` signal before resorting to `SIGKILL`, as the latter does not allow the process to perform any cleanup operations.
- Use the `kill -l` command to view all available signals and their corresponding numbers. This can help you choose the appropriate signal for your needs.
- Be cautious when killing processes, especially system processes, as this can lead to system instability or data loss.
- Consider using `pkill` or `killall` for terminating processes by name rather than by PID, which can be more convenient in some scenarios.