# [리눅스] Bash jobs 사용법

## Overview
The `jobs` command in Bash is used to display the status of jobs that are running in the current shell session. A job is a process that has been started by the shell, and it can be in various states such as running, stopped, or terminated. The primary purpose of the `jobs` command is to provide users with a way to monitor and manage these background and foreground processes.

## Usage
The basic syntax of the `jobs` command is as follows:

```bash
jobs [options]
```

### Common Options
- `-l`: Displays the process ID (PID) of each job along with its status.
- `-n`: Shows only jobs that have changed status since the last time the command was run.
- `-p`: Displays only the PIDs of the jobs, without any additional information.

## Examples

### Example 1: Displaying Current Jobs
To see the current jobs running in the background or stopped, simply run:

```bash
jobs
```

This will output a list of jobs with their job numbers and statuses, such as:

```
[1]+  12345 Stopped                 nano myfile.txt
[2]-  67890 Running                 sleep 100 &
```

### Example 2: Displaying Jobs with PIDs
If you want to see the jobs along with their process IDs, you can use the `-l` option:

```bash
jobs -l
```

The output will include the PIDs:

```
[1]+  12345 Stopped                 nano myfile.txt
[2]-  67890 Running                 sleep 100 &
```

## Tips
- Use the `jobs` command frequently to keep track of your background processes, especially when working with multiple tasks.
- If you need to bring a stopped job back to the foreground, you can use the `fg` command followed by the job number (e.g., `fg %1`).
- To send a job to the background, you can use the `bg` command along with the job number (e.g., `bg %1`).
- Remember that jobs are specific to the shell session. If you open a new terminal session, you will not see jobs from the previous session.

By utilizing the `jobs` command effectively, you can enhance your workflow in the Bash shell, allowing for better management of running processes.