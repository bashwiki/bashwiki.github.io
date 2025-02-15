# [리눅스] Bash killall 사용법

## Overview
The `killall` command in Bash is used to terminate processes by name. Unlike the `kill` command, which requires a process ID (PID), `killall` allows users to specify the name of the process they want to terminate. This is particularly useful for managing multiple instances of the same application or service, providing a straightforward way to stop them all at once.

## Usage
The basic syntax for the `killall` command is as follows:

```bash
killall [options] process_name
```

### Common Options
- `-u, --user <username>`: Kill processes owned by the specified user.
- `-q, --quiet`: Suppress output messages.
- `-I, --ignore-case`: Ignore case when matching process names.
- `-s, --signal <signal>`: Specify a signal to send to the processes. The default is `TERM` (terminate).
- `-v, --verbose`: Provide detailed output of the actions taken.

## Examples

### Example 1: Terminating a Process by Name
To terminate all instances of a process named `firefox`, you can use the following command:

```bash
killall firefox
```

This command will send the default `TERM` signal to all running instances of Firefox, effectively closing them.

### Example 2: Using a Specific Signal
If you want to forcefully kill all instances of a process named `myapp`, you can specify the `KILL` signal as follows:

```bash
killall -s KILL myapp
```

This command will immediately terminate all instances of `myapp`, bypassing any cleanup processes.

## Tips
- Use `killall -q` to suppress output if you are running scripts and do not want unnecessary messages cluttering your terminal.
- Always double-check the process name you are targeting, especially when using `killall` in scripts, to avoid unintentionally terminating critical system processes.
- Combine `killall` with other commands like `ps` or `pgrep` to dynamically find and kill processes based on specific criteria. For example, you can use `killall -u $(whoami)` to terminate all processes owned by the current user.
- Be cautious with the `KILL` signal, as it does not allow processes to clean up before termination, which may lead to data loss or corruption.