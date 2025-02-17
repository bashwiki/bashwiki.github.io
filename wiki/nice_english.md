# [Linux] Bash nice Usage: Adjust process priority

## Overview
The `nice` command in Bash is used to run a program with a modified scheduling priority. By default, processes run with a priority of 0, but you can increase or decrease this value to influence how much CPU time a process receives compared to others. Lowering the priority (using a higher nice value) allows other processes to have more CPU time, while increasing the priority (using a lower nice value) gives the process more CPU time.

## Usage
The basic syntax of the `nice` command is as follows:

```bash
nice [options] [command [arguments]]
```

## Common Options
- `-n, --adjustment=N`: Specify the nice value adjustment. The value can be from -20 (highest priority) to 19 (lowest priority).
- `-h, --help`: Display help information about the command.
- `--version`: Show the version information of the `nice` command.

## Common Examples
1. **Run a command with default nice value (0)**:
   ```bash
   nice sleep 10
   ```
   This command runs `sleep` for 10 seconds with the default priority.

2. **Run a command with a higher priority**:
   ```bash
   nice -n -5 myscript.sh
   ```
   This command runs `myscript.sh` with a nice value of -5, giving it higher priority.

3. **Run a command with a lower priority**:
   ```bash
   nice -n 10 myscript.sh
   ```
   This command runs `myscript.sh` with a nice value of 10, lowering its priority.

4. **Check the nice value of a running process**:
   ```bash
   ps -o pid,nice,cmd -p <PID>
   ```
   Replace `<PID>` with the process ID to see its current nice value.

## Tips
- Use `nice` when running resource-intensive tasks to ensure they do not starve other important processes of CPU time.
- Combine `nice` with `nohup` to run long-running processes in the background without being affected by terminal hangups.
- Regularly check the nice values of running processes using the `ps` command to manage system resources effectively.