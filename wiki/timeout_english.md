# [리눅스] Bash timeout 사용법

## Overview
The `timeout` command in Bash is used to run a command with a time limit. If the command does not complete within the specified duration, `timeout` will terminate it. This is particularly useful for preventing processes from running indefinitely and for managing system resources effectively.

## Usage
The basic syntax of the `timeout` command is as follows:

```bash
timeout [OPTION] DURATION COMMAND [ARGUMENTS...]
```

### Common Options:
- `DURATION`: Specifies the time limit for the command to run. It can be specified in seconds (s), minutes (m), hours (h), or days (d). For example, `5s` for 5 seconds, `2m` for 2 minutes.
- `-k, --kill-after=DURATION`: This option allows you to specify a grace period after which the command will be forcibly killed. For example, if you set `-k 5s`, the command will be sent a termination signal after the initial timeout, and if it does not exit within 5 seconds, it will be killed.
- `-s, --signal=SIGNAL`: This option allows you to specify the signal to send to the command when the timeout expires. By default, it sends `SIGTERM`, but you can change it to any valid signal (e.g., `SIGKILL`).

## Examples

### Example 1: Basic Usage
To run a command with a timeout of 10 seconds, you can use:

```bash
timeout 10s sleep 20
```
In this example, the `sleep 20` command is intended to sleep for 20 seconds, but `timeout` will terminate it after 10 seconds.

### Example 2: Using a Kill After Option
To run a command with a timeout and a kill after grace period, you can use:

```bash
timeout -k 5s 10s sleep 20
```
Here, the `sleep 20` command will be terminated after 10 seconds, and if it does not exit within an additional 5 seconds, it will be forcibly killed.

## Tips
- Always test your timeout settings in a safe environment to ensure that the command behaves as expected.
- Use the `-s` option to customize the termination signal based on the behavior of the command you are running. For instance, some commands may handle `SIGTERM` gracefully, while others may require `SIGKILL`.
- Consider using `timeout` in scripts to prevent long-running processes from hanging indefinitely, especially in automated tasks or cron jobs.