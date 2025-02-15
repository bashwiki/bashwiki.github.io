# [리눅스] Bash renice 사용법

## Overview
The `renice` command in Bash is used to alter the scheduling priority of running processes. It allows users to change the "niceness" value of a process, which affects how much CPU time the process receives relative to others. A lower niceness value means higher priority, while a higher niceness value means lower priority. This command is particularly useful for system administrators and developers who need to manage system resources effectively.

## Usage
The basic syntax for the `renice` command is as follows:

```bash
renice [options] priority [pid...]
```

### Common Options:
- `priority`: This is the new niceness value you want to assign to the specified process. It can range from -20 (highest priority) to 19 (lowest priority).
- `-p`: This option allows you to specify the process ID (PID) of the process you want to renice.
- `-g`: This option allows you to specify a process group ID.
- `-u`: This option allows you to specify a user whose processes you want to renice.

## Examples
### Example 1: Renice a Single Process
To change the niceness value of a process with PID 1234 to 10, you would use the following command:

```bash
renice 10 -p 1234
```

### Example 2: Renice Multiple Processes
If you want to change the niceness value of multiple processes (e.g., PIDs 1234 and 5678) to -5, you can do so with:

```bash
renice -5 -p 1234 5678
```

## Tips
- Use `renice` with caution, especially when lowering the niceness value (increasing priority) of processes, as it can lead to resource contention and affect system performance.
- You may need superuser privileges (root access) to change the niceness value of processes that are not owned by your user. Use `sudo` if necessary.
- To check the current niceness values of processes, you can use the `ps` command with the `-o` option, for example: `ps -o pid,ni,cmd`.
- Consider using `nice` when starting a new process if you want to set its niceness value from the beginning, rather than using `renice` on an already running process.