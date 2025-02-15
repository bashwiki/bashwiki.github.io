# [리눅스] Bash shutdown 사용법

## Overview
The `shutdown` command in Bash is used to bring the system down in a safe manner. Its primary purpose is to halt, power off, or reboot the machine, ensuring that all processes are terminated properly and that the file system is unmounted safely. This is crucial for maintaining system integrity and preventing data loss.

## Usage
The basic syntax of the `shutdown` command is as follows:

```
shutdown [OPTION] [TIME] [MESSAGE]
```

### Common Options:
- `-h` or `--halt`: Halt the machine after shutting down.
- `-r` or `--reboot`: Reboot the machine after shutting down.
- `-P` or `--poweroff`: Power off the machine after shutting down.
- `TIME`: Specifies when to shut down. This can be specified in various formats, such as `now`, `+5` (for 5 minutes from now), or an exact time (e.g., `23:00`).
- `MESSAGE`: An optional message that will be broadcasted to all logged-in users before the shutdown occurs.

## Examples

1. **Shutting down immediately:**
   To shut down the system immediately, you can use the following command:
   ```bash
   shutdown now
   ```

2. **Rebooting after a delay:**
   To reboot the system after a 10-minute delay, you can use:
   ```bash
   shutdown -r +10 "The system will reboot in 10 minutes."
   ```

## Tips
- Always ensure that you save your work and notify users before executing a shutdown command, especially on multi-user systems.
- Use the `-k` option to send a warning message without actually shutting down the system. This can be useful for notifying users without disrupting their work.
- Consider scheduling shutdowns during off-peak hours to minimize disruption to users.
- To cancel a scheduled shutdown, you can use the command:
  ```bash
  shutdown -c
  ```
  This will abort any pending shutdown operations.