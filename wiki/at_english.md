# [리눅스] Bash at 사용법

## Overview
The `at` command in Bash is a utility that allows users to schedule commands to be executed at a specified time in the future. It is particularly useful for automating tasks that need to run once at a certain time, rather than on a recurring basis. This command is part of the `at` daemon, which listens for scheduled jobs and executes them at the designated time.

## Usage
The basic syntax of the `at` command is as follows:

```bash
at [OPTION] TIME
```

### Common Options:
- `-f FILE`: Read the commands to be executed from the specified file instead of standard input.
- `-m`: Send mail to the user after the job has completed, regardless of whether it produced any output.
- `-q QUEUE`: Specify the queue to which the job should be added. Different queues can be used to prioritize jobs.
- `-v`: Print the job's ID and the time it is scheduled to run.

### Time Formats:
The `TIME` argument can be specified in several formats, such as:
- `now + 1 hour`
- `2:00 PM`
- `tomorrow`
- `next Friday`

## Examples

### Example 1: Scheduling a Simple Command
To schedule a command to display "Hello, World!" at 3:00 PM today, you can use the following command:

```bash
echo "echo 'Hello, World!'" | at 3:00 PM
```

This command pipes the echo command into `at`, which schedules it to run at the specified time.

### Example 2: Using a File to Schedule Commands
If you have a script saved in a file called `backup.sh` that you want to run at midnight, you can do this:

```bash
at midnight -f backup.sh
```

This command tells `at` to execute the commands in `backup.sh` at midnight.

## Tips
- Always check your scheduled jobs with the `atq` command, which lists all pending jobs for the user.
- Use the `atrm` command to remove a scheduled job if you no longer need it. You can specify the job ID obtained from `atq`.
- Be mindful of the time zone settings on your system, as they can affect when your scheduled jobs execute.
- Consider using the `-m` option if you want to receive notifications about the completion of your scheduled tasks, especially for long-running jobs.