# [리눅스] Bash disown 사용법

## Overview
The `disown` command in Bash is used to remove jobs from the shell's job table. When a job is disowned, it no longer receives signals from the shell, such as SIGHUP (hangup signal) when the shell is closed. This is particularly useful for long-running processes that you want to keep running even after you log out or close the terminal.

## Usage
The basic syntax of the `disown` command is as follows:

```bash
disown [options] [job_spec]
```

### Common Options
- `-h`: This option prevents the specified job from receiving the HUP signal when the shell exits, but it does not remove it from the job table.
- `-a`: This option disowns all jobs in the job table.
- `-r`: This option disowns all running jobs.

If no job specification is provided, `disown` will disown the current job (the job that was last backgrounded).

## Examples

### Example 1: Disowning a Specific Job
1. Start a long-running command in the background:
   ```bash
   sleep 300 &
   ```
   This command will run for 300 seconds in the background.

2. Disown the job:
   ```bash
   disown %1
   ```
   Here, `%1` refers to the job number of the background process. You can check the job number by running the `jobs` command.

### Example 2: Disowning All Jobs
If you have multiple jobs running in the background and want to disown them all, you can use the `-a` option:
```bash
disown -a
```
This command will remove all jobs from the job table, allowing them to continue running independently of the shell.

## Tips
- Always check your current jobs using the `jobs` command before disowning them, to ensure you are disowning the correct job.
- Use `disown -h` if you want to keep a job running but still want to prevent it from being terminated when the shell exits.
- Remember that once a job is disowned, you cannot bring it back to the foreground or background using job control commands like `fg` or `bg`.