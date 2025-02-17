# [Linux] Bash at: Schedule commands for later execution

## Overview
The `at` command in Bash is used to schedule commands to be executed at a specified time in the future. This allows users to automate tasks without needing to keep a terminal open or run scripts manually.

## Usage
The basic syntax of the `at` command is as follows:

```bash
at [options] [time]
```

Here, `time` specifies when the command should be executed.

## Common Options
- `-f FILE`: Read commands from the specified file instead of standard input.
- `-l`: List all scheduled jobs.
- `-d JOB_ID`: Delete the specified job.
- `-q QUEUE`: Specify the queue to use for the job.

## Common Examples
Here are some practical examples of how to use the `at` command:

1. **Schedule a command to run at a specific time:**
   ```bash
   echo "echo 'Hello, World!'" | at 14:00
   ```
   This schedules the command to print "Hello, World!" at 2 PM.

2. **Schedule a command for a specific date and time:**
   ```bash
   echo "backup.sh" | at 2023-10-30 10:00
   ```
   This schedules the `backup.sh` script to run on October 30, 2023, at 10 AM.

3. **List all scheduled jobs:**
   ```bash
   at -l
   ```
   This command lists all jobs that have been scheduled with `at`.

4. **Delete a scheduled job:**
   ```bash
   at -d 2
   ```
   This deletes the job with ID 2 from the scheduled jobs list.

5. **Schedule a command to run 5 minutes from now:**
   ```bash
   echo "echo 'This runs in 5 minutes!'" | at now + 5 minutes
   ```
   This schedules a command to run 5 minutes from the current time.

## Tips
- Always check your scheduled jobs with `at -l` to ensure you know what is set to run.
- Use the `-f` option to read commands from a file for more complex tasks.
- Remember that the `at` command uses the system's timezone, so be mindful of that when scheduling tasks.