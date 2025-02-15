# [리눅스] Bash nohup 사용법

## Overview
The `nohup` command in Bash is used to run a command or script immune to hangups, meaning it will continue to run even after the user has logged out or closed the terminal session. This is particularly useful for long-running processes that you want to ensure continue executing without interruption. The output of the command is typically redirected to a file named `nohup.out` if no other output redirection is specified.

## Usage
The basic syntax of the `nohup` command is as follows:

```bash
nohup COMMAND [ARGUMENTS] &
```

### Common Options
- `COMMAND`: The command you want to run.
- `[ARGUMENTS]`: Any arguments that the command requires.
- `&`: This symbol is used to run the command in the background, allowing you to continue using the terminal.

By default, `nohup` redirects the standard output (stdout) and standard error (stderr) to `nohup.out`, but you can specify different output files if needed.

## Examples

### Example 1: Running a Script in the Background
To run a script called `long_running_script.sh` in the background, you would use:

```bash
nohup ./long_running_script.sh &
```

This command will execute `long_running_script.sh` and allow it to continue running even if you log out of the terminal. The output will be saved to `nohup.out`.

### Example 2: Running a Command with Output Redirection
If you want to run a command and redirect the output to a specific file, you can do so like this:

```bash
nohup ping google.com > ping_output.txt 2>&1 &
```

In this example, the `ping` command will run in the background, and both the standard output and standard error will be redirected to `ping_output.txt`.

## Tips
- Always check the `nohup.out` file or your specified output file to monitor the output of your command after it has been executed.
- Use the `jobs` command to list background jobs and the `fg` command to bring a job back to the foreground if needed.
- Consider using `disown` after starting a job with `nohup` to remove it from the shell's job table, which can help prevent it from being terminated if the shell session ends.
- For more control over background processes, consider using `screen` or `tmux`, which allow you to detach and reattach to terminal sessions.