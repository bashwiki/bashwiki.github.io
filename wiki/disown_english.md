# [Linux] Bash disown Uso equivalente: Detach jobs from the shell

## Overview
The `disown` command in Bash is used to remove jobs from the shell's job table, effectively detaching them from the terminal. This allows processes to continue running in the background even after the user has logged out or closed the terminal.

## Usage
The basic syntax of the `disown` command is as follows:

```bash
disown [options] [arguments]
```

## Common Options
- `-h`: This option prevents the specified job from receiving a SIGHUP signal when the shell exits.
- `-a`: Disown all jobs.
- `-r`: Disown only running jobs.

## Common Examples

1. **Disown a specific job**: If you have a job running in the background (e.g., a long-running script), you can disown it by specifying its job number.
   ```bash
   disown %1
   ```

2. **Disown all jobs**: To detach all jobs from the shell, use the `-a` option.
   ```bash
   disown -a
   ```

3. **Disown a running job**: If you want to disown only the jobs that are currently running, you can use the `-r` option.
   ```bash
   disown -r
   ```

4. **Prevent SIGHUP for a specific job**: If you want to disown a job and prevent it from receiving a hangup signal, use the `-h` option.
   ```bash
   disown -h %1
   ```

## Tips
- Always check the job list with the `jobs` command before using `disown` to ensure you are disowning the correct job.
- Use `bg` to send a job to the background before disowning it, if it’s currently running in the foreground.
- Remember that once a job is disowned, you cannot bring it back to the foreground using `fg`.