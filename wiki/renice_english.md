# [Linux] Bash renice uso equivalente: Adjust process priority

## Overview
The `renice` command in Bash is used to change the priority of running processes. By adjusting a process's priority, you can influence how much CPU time it receives relative to other processes. A lower nice value means higher priority, while a higher nice value means lower priority.

## Usage
The basic syntax of the `renice` command is as follows:

```bash
renice [options] [arguments]
```

## Common Options
- `-n, --priority <number>`: Set the new priority value. The value can range from -20 (highest priority) to 19 (lowest priority).
- `-p, --pid <pid>`: Specify the process ID(s) to renice.
- `-u, --user <user>`: Renice all processes owned by the specified user.
- `-g, --group <group>`: Renice all processes in the specified group.

## Common Examples
Here are some practical examples of using the `renice` command:

1. **Change the priority of a specific process by PID**:
   ```bash
   renice -n 10 -p 1234
   ```
   This command sets the priority of the process with PID 1234 to 10.

2. **Renice all processes owned by a specific user**:
   ```bash
   renice -n 5 -u username
   ```
   This command changes the priority of all processes owned by `username` to 5.

3. **Change the priority of multiple processes**:
   ```bash
   renice -n -5 -p 1234 5678
   ```
   This command sets the priority of processes with PIDs 1234 and 5678 to -5.

4. **Renice all processes in a specific group**:
   ```bash
   renice -n 15 -g groupname
   ```
   This command changes the priority of all processes in the group `groupname` to 15.

## Tips
- Always check the current priority of a process using the `ps` command before renicing it.
- Use `renice` with caution, especially when lowering the priority of critical system processes, as it may affect system performance.
- You may need superuser privileges to change the priority of processes owned by other users. Use `sudo` if necessary.