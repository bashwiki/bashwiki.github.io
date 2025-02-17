# [Linux] Bash timeout Uso: Limit command execution time

## Overview
The `timeout` command in Bash is used to run a command with a time limit. If the command does not complete within the specified duration, `timeout` will terminate it. This is particularly useful for preventing long-running processes from hanging indefinitely.

## Usage
The basic syntax of the `timeout` command is as follows:

```bash
timeout [options] duration command [arguments]
```

- `duration`: The time limit for the command to run, specified in seconds (or with suffixes like `m` for minutes, `h` for hours, etc.).
- `command`: The command you want to run with a time limit.
- `arguments`: Any arguments that the command may require.

## Common Options
- `-k, --kill-after=DURATION`: After the initial timeout, this option allows you to specify a duration to wait before forcibly killing the command.
- `-s, --signal=SIGNAL`: Specify the signal to send to the command when the timeout occurs. The default is `SIGTERM`.
- `--preserve-status`: Exit with the status of the command instead of the timeout status.

## Common Examples

1. **Basic usage with a timeout of 5 seconds:**
   ```bash
   timeout 5s sleep 10
   ```
   This command attempts to run `sleep 10`, but it will be terminated after 5 seconds.

2. **Using a different signal:**
   ```bash
   timeout -s SIGKILL 3s sleep 10
   ```
   Here, `sleep 10` will be killed with `SIGKILL` after 3 seconds if it is still running.

3. **Preserving the exit status of the command:**
   ```bash
   timeout --preserve-status 2s false
   echo $?
   ```
   This will run `false` with a timeout of 2 seconds and print the exit status of `false`, which is `1`.

4. **Killing after a timeout with a grace period:**
   ```bash
   timeout -k 5s 10s sleep 20
   ```
   This command will allow `sleep 20` to run for 10 seconds, then send a `SIGTERM`. If it does not terminate within 5 seconds, it will be forcibly killed.

## Tips
- Always specify a reasonable duration to avoid unintentionally terminating important processes.
- Use `--preserve-status` when you need to check the exit status of the command after it runs.
- Consider using the `-k` option if you want to give the command a chance to clean up before being forcibly terminated.