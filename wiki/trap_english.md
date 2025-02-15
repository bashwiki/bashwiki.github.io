# [리눅스] Bash trap 사용법

## Overview
The `trap` command in Bash is used to specify commands that will be executed when the shell receives certain signals or when specific events occur. This is particularly useful for handling cleanup tasks, such as removing temporary files or restoring terminal settings, before a script exits or is interrupted. By using `trap`, developers can ensure that their scripts behave predictably in the face of interruptions.

## Usage
The basic syntax of the `trap` command is as follows:

```bash
trap COMMANDS SIGNALS
```

- **COMMANDS**: The commands to be executed when the specified signals are received. This can be a single command or a list of commands separated by semicolons.
- **SIGNALS**: The signals that will trigger the execution of the specified commands. Common signals include:
  - `SIGINT` (interrupt signal, usually triggered by Ctrl+C)
  - `SIGTERM` (termination signal)
  - `EXIT` (executes when the script exits, regardless of how it exits)

### Common Options
- `-p`: Print the current trap settings for the specified signals.
- `-l`: List all signal names.

## Examples

### Example 1: Basic Usage with SIGINT
This example demonstrates how to use `trap` to handle an interrupt signal (Ctrl+C) gracefully.

```bash
#!/bin/bash

trap 'echo "Script interrupted! Cleaning up..."; exit' SIGINT

echo "Running script. Press Ctrl+C to interrupt."
while true; do
    sleep 1
done
```

In this script, if the user presses Ctrl+C, the message "Script interrupted! Cleaning up..." will be displayed, and the script will exit cleanly.

### Example 2: Cleanup on Exit
In this example, `trap` is used to perform cleanup actions when the script exits.

```bash
#!/bin/bash

trap 'echo "Cleaning up temporary files..."; rm -f /tmp/mytempfile' EXIT

echo "Creating a temporary file..."
touch /tmp/mytempfile

# Simulate some work
sleep 5

echo "Script completed."
```

Here, when the script exits (whether normally or due to an error), it will remove the temporary file `/tmp/mytempfile`.

## Tips
- Always include cleanup commands in your `trap` to ensure resources are released properly.
- Use `trap` with `EXIT` to handle cleanup tasks that should occur regardless of how the script terminates.
- Be cautious when using `trap` with signals that can be sent by other processes, as this can lead to unexpected behavior if not managed correctly.
- Test your scripts thoroughly to ensure that the `trap` commands behave as expected under various conditions.