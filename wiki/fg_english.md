# [리눅스] Bash fg 사용법

## Overview
The `fg` command in Bash is used to bring a background job to the foreground. When you run a command in the background (using `&`), it allows you to continue using the terminal for other tasks. However, if you need to interact with that background job, you can use `fg` to bring it back to the foreground, enabling you to provide input or view its output directly.

## Usage
The basic syntax of the `fg` command is as follows:

```bash
fg [job_spec]
```

- `job_spec`: This is an optional argument that specifies which job to bring to the foreground. If you have multiple background jobs, you can refer to them by their job number (e.g., `%1`, `%2`, etc.) or by their process ID.

### Common Options
- If no job specification is provided, `fg` will bring the most recently suspended or background job to the foreground.

## Examples

### Example 1: Bringing the Most Recent Background Job to the Foreground
Suppose you have started a long-running process in the background:

```bash
sleep 100 &
```

You can bring this job back to the foreground by simply running:

```bash
fg
```

### Example 2: Bringing a Specific Job to the Foreground
If you have multiple background jobs, you can list them using the `jobs` command:

```bash
jobs
```

This might output something like:

```
[1]+  12345 Stopped                 nano
[2]-  12346 Running                 sleep 100 &
```

To bring the first job (nano) to the foreground, you would use:

```bash
fg %1
```

## Tips
- Use the `jobs` command to check the status of your background jobs before using `fg`. This will help you identify which job you want to bring to the foreground.
- If you need to stop a job that is running in the foreground, you can usually do so by pressing `Ctrl + Z`, which suspends the job and puts it in the background. You can then use `fg` to bring it back if needed.
- Remember that when a job is running in the foreground, it takes control of the terminal, so you won't be able to execute other commands until you either finish or suspend the job.