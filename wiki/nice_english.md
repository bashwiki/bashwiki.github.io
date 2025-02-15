# [리눅스] Bash nice 사용법

## Overview
The `nice` command in Bash is used to run a program with a modified scheduling priority. By default, processes in Linux are assigned a priority level, which determines how much CPU time they receive relative to other processes. The `nice` command allows users to start a process with a "nice" value, which can be adjusted to be more or less favorable to the CPU scheduler. A higher nice value means lower priority, while a lower nice value (including negative values) means higher priority. This is particularly useful for managing system resources and ensuring that critical processes receive the CPU time they need.

## Usage
The basic syntax of the `nice` command is as follows:

```bash
nice [OPTION] [COMMAND [ARGUMENTS...]]
```

### Common Options:
- `-n, --adjustment=N`: This option allows you to specify the nice value adjustment. The value can range from -20 (highest priority) to 19 (lowest priority). If not specified, the default adjustment is 10.
- `-h, --help`: Displays help information about the command.
- `--version`: Shows the version of the `nice` command.

## Examples
### Example 1: Running a command with a higher priority
To run a command with a higher priority (lower nice value), you can use a negative adjustment. For example, to run a script called `my_script.sh` with a nice value of -5:

```bash
nice -n -5 ./my_script.sh
```

### Example 2: Running a command with a lower priority
If you want to run a command with a lower priority (higher nice value), you can specify a positive adjustment. For example, to run a command called `backup.sh` with a nice value of 15:

```bash
nice -n 15 ./backup.sh
```

## Tips
- Use the `top` or `htop` command to monitor running processes and their nice values. This can help you understand how your adjustments are affecting system performance.
- Be cautious when using negative nice values, as they can starve other processes of CPU time, potentially leading to system slowdowns.
- If you need to change the nice value of an already running process, consider using the `renice` command instead.
- For scripts that are not time-sensitive, consider using a higher nice value to allow more critical processes to run smoothly.