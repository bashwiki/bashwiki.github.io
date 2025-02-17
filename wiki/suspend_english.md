# [Linux] Bash suspend usage: Pause a running process

## Overview
The `suspend` command in Bash is used to pause the execution of a currently running foreground job. This allows users to temporarily stop a process and later resume it, making it a useful tool for managing tasks without terminating them.

## Usage
The basic syntax of the `suspend` command is as follows:

```bash
suspend
```

Note that `suspend` is typically used within a job control context, meaning it is invoked from a shell session where a job is currently running in the foreground.

## Common Options
The `suspend` command does not have any options. It is a straightforward command that simply pauses the current foreground job.

## Common Examples

### Example 1: Suspending a foreground job
If you have a long-running process, such as a text editor, you can suspend it by pressing `Ctrl + Z`. This will stop the process and return you to the shell prompt.

```bash
# Running a text editor
nano myfile.txt
# Press Ctrl + Z to suspend
```

### Example 2: Listing suspended jobs
After suspending a job, you can list all jobs, including suspended ones, using the `jobs` command.

```bash
jobs
```

### Example 3: Resuming a suspended job
To resume a suspended job in the foreground, use the `fg` command followed by the job number.

```bash
fg %1  # Resumes job number 1
```

To resume it in the background, use the `bg` command:

```bash
bg %1  # Resumes job number 1 in the background
```

## Tips
- Always remember that `suspend` is typically invoked using `Ctrl + Z` rather than as a command in the terminal.
- Use the `jobs` command to keep track of suspended and background jobs.
- If you need to terminate a suspended job, you can use the `kill` command followed by the job's process ID (PID).