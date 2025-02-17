# [Linux] Bash nohup用法: Prevent command termination on logout

## Overview
The `nohup` command in Bash is used to run another command immune to hangups, meaning it will continue to run even after you log out or close the terminal. This is particularly useful for long-running processes that you want to keep active without needing a terminal session.

## Usage
The basic syntax of the `nohup` command is as follows:

```bash
nohup [options] [arguments]
```

## Common Options
- `&`: Run the command in the background.
- `-h`: Display help information about the command.
- `-v`: Enable verbose mode, providing more detailed output.

## Common Examples

1. **Running a script in the background:**
   ```bash
   nohup ./my_script.sh &
   ```
   This command runs `my_script.sh` in the background, allowing you to log out without stopping the script.

2. **Redirecting output to a file:**
   ```bash
   nohup python my_long_running_script.py > output.log &
   ```
   Here, the output of the Python script is redirected to `output.log`, making it easier to review later.

3. **Running a command with no output:**
   ```bash
   nohup sleep 300 &
   ```
   This command runs a sleep command for 300 seconds in the background without producing any output.

4. **Using nohup with a command that requires input:**
   ```bash
   nohup bash -c 'read -p "Press enter to continue..."' &
   ```
   This example runs a command that waits for user input but will not terminate if you log out.

## Tips
- Always redirect output to a file when using `nohup` to avoid cluttering your terminal or losing important logs.
- Use the `jobs` command to check the status of background processes started with `nohup`.
- Combine `nohup` with `disown` to remove the job from the shell’s job table, allowing it to continue running independently.