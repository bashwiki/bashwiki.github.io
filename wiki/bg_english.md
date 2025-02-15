# [리눅스] Bash bg 사용법

## Overview
The `bg` command in Bash is used to resume a suspended job and run it in the background. When a job is suspended (usually by pressing `Ctrl+Z`), it can be resumed with `bg`, allowing the user to continue using the terminal for other commands while the job runs in the background. This is particularly useful for long-running processes that do not require immediate interaction.

## Usage
The basic syntax of the `bg` command is as follows:

```
bg [job_spec]
```

- `job_spec`: This is an optional argument that specifies which job to resume in the background. If omitted, `bg` will resume the most recently suspended job.

### Common Options
- `job_spec`: You can specify a job by its job number (e.g., `%1`, `%2`) or by its process ID (PID). The job number can be found using the `jobs` command.

## Examples

### Example 1: Resuming the Most Recent Suspended Job
1. Start a long-running command, such as `sleep`:
   ```bash
   sleep 100
   ```
2. Suspend the job by pressing `Ctrl+Z`.
3. Resume the job in the background:
   ```bash
   bg
   ```

### Example 2: Resuming a Specific Job
1. Start two jobs:
   ```bash
   sleep 100 &
   sleep 200 &
   ```
2. Suspend the first job:
   ```bash
   kill -STOP %1
   ```
3. Check the job status:
   ```bash
   jobs
   ```
4. Resume the first job in the background:
   ```bash
   bg %1
   ```

## Tips
- Use the `jobs` command to list all current jobs and their statuses. This will help you identify which jobs can be resumed with `bg`.
- Remember that jobs running in the background can still produce output to the terminal, which may clutter your command line. Consider redirecting output to a file if necessary.
- To bring a job back to the foreground, use the `fg` command followed by the job specification (e.g., `fg %1`).
- If you want to stop a background job completely, you can use the `kill` command followed by the job's PID.

By mastering the `bg` command, you can effectively manage multiple processes in your terminal, enhancing your productivity and workflow.