# [Linux] Bash wait Usage: Wait for process completion

## Overview
The `wait` command in Bash is used to pause the execution of a script until one or more background processes have completed. This is particularly useful when you want to ensure that certain tasks finish before moving on to the next steps in your script.

## Usage
The basic syntax of the `wait` command is as follows:

```bash
wait [options] [arguments]
```

## Common Options
- `-n`: Wait for any job to complete.
- `PID`: Specify the process ID of the background job you want to wait for. If no PID is provided, `wait` will wait for all background jobs.

## Common Examples

### Example 1: Wait for a specific background process
```bash
#!/bin/bash
sleep 5 &  # Start a background process
pid=$!     # Get the process ID of the last background command
echo "Waiting for process $pid to complete..."
wait $pid # Wait for the specific process to finish
echo "Process $pid has completed."
```

### Example 2: Wait for all background processes
```bash
#!/bin/bash
sleep 3 &  # Start first background process
sleep 4 &  # Start second background process
echo "Waiting for all background processes to complete..."
wait      # Wait for all background jobs
echo "All background processes have completed."
```

### Example 3: Using wait with the -n option
```bash
#!/bin/bash
sleep 2 &  # Start first background process
sleep 5 &  # Start second background process
echo "Waiting for any background process to complete..."
wait -n   # Wait for any single background job to finish
echo "One of the background processes has completed."
```

## Tips
- Always check the exit status of the process after using `wait` to handle errors appropriately.
- Use `wait` in scripts that involve multiple background tasks to ensure they complete before proceeding.
- Consider using `wait` in combination with other commands to manage dependencies between tasks effectively.