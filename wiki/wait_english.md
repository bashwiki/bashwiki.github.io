# [리눅스] Bash wait 사용법

## Overview
The `wait` command in Bash is used to pause the execution of a script until one or more background processes complete. Its primary purpose is to synchronize the execution of scripts when dealing with multiple background jobs, allowing you to manage process completion effectively. This is particularly useful in scenarios where subsequent commands depend on the results of background tasks.

## Usage
The basic syntax of the `wait` command is as follows:

```bash
wait [PID...]
```

- `PID`: This is an optional argument. You can specify one or more process IDs (PIDs) of the background jobs you want to wait for. If no PID is provided, `wait` will wait for all background jobs to complete.

### Common Options
- There are no specific options for the `wait` command itself, but it can be used in conjunction with other commands that create background processes.

## Examples

### Example 1: Waiting for a Single Background Job
```bash
#!/bin/bash

# Start a background job
sleep 5 &

# Get the PID of the last background job
JOB_PID=$!

# Wait for the background job to complete
wait $JOB_PID

echo "Background job has completed."
```
In this example, the script starts a background job that sleeps for 5 seconds. The script then waits for that specific job to finish before printing a message.

### Example 2: Waiting for Multiple Background Jobs
```bash
#!/bin/bash

# Start multiple background jobs
sleep 3 &
sleep 5 &
sleep 2 &

# Wait for all background jobs to complete
wait

echo "All background jobs have completed."
```
Here, three background jobs are started, each with different sleep durations. The `wait` command without any arguments ensures that the script waits for all background jobs to finish before proceeding.

## Tips
- **Use `$!` to capture PIDs**: When starting a background job, use `$!` to capture its PID for later use with `wait`.
- **Error Handling**: After `wait`, you can check the exit status of the background jobs using `$?`. This can help in error handling and debugging.
- **Combine with Other Commands**: The `wait` command can be effectively combined with other commands in scripts to ensure that resources are managed properly and that tasks are completed in the desired order.

By using the `wait` command effectively, you can create more robust and efficient Bash scripts that handle multiple processes seamlessly.