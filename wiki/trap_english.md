# [Linux] Bash trap uso: Manage signals and cleanup tasks

## Overview
The `trap` command in Bash is used to specify commands that will be executed when the shell receives certain signals or when specific events occur. This is particularly useful for handling cleanup tasks or managing the behavior of scripts when they are interrupted.

## Usage
The basic syntax of the `trap` command is as follows:

```bash
trap [commands] [signals]
```

- `commands`: The commands to execute when the specified signals are received.
- `signals`: The signals that will trigger the execution of the commands.

## Common Options
- `SIGINT`: Triggered by pressing Ctrl+C.
- `SIGTERM`: The default signal sent by the `kill` command.
- `EXIT`: Executes commands when the script exits, regardless of the reason.
- `ERR`: Executes commands when a command fails (returns a non-zero status).

## Common Examples

### Example 1: Cleanup on Exit
To remove a temporary file when the script exits:

```bash
trap 'rm -f /tmp/mytempfile' EXIT
```

### Example 2: Handle Interrupt Signal
To display a message and exit gracefully when the script is interrupted:

```bash
trap 'echo "Script interrupted!"; exit' SIGINT
```

### Example 3: Multiple Signals
To handle both SIGINT and SIGTERM with the same command:

```bash
trap 'echo "Terminating..."; exit' SIGINT SIGTERM
```

### Example 4: Error Handling
To print a message when a command fails:

```bash
trap 'echo "An error occurred!"' ERR
```

## Tips
- Always ensure that the commands specified in `trap` are simple and quick to execute, as they will run in response to signals.
- Use `trap` to manage resources effectively, especially in scripts that create temporary files or open network connections.
- Remember to test your scripts to ensure that the `trap` commands behave as expected under different scenarios.