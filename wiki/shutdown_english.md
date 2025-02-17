# [Linux] Bash shutdown uso: Shut down or restart the system

## Overview
The `shutdown` command is used to safely turn off or restart a Linux system. It allows users to schedule shutdowns, notify logged-in users, and specify the reason for the shutdown.

## Usage
The basic syntax of the `shutdown` command is as follows:

```bash
shutdown [options] [time] [message]
```

## Common Options
- `-h` or `--halt`: Halts the system after shutdown.
- `-r` or `--reboot`: Reboots the system after shutdown.
- `-P` or `--poweroff`: Powers off the machine after shutdown.
- `-c`: Cancels a scheduled shutdown.
- `time`: Specifies when to shut down (e.g., `now`, `+5` for five minutes later, or a specific time like `23:00`).
- `message`: An optional message to display to users before shutdown.

## Common Examples
1. **Shut down immediately:**
   ```bash
   shutdown now
   ```

2. **Shut down after 10 minutes:**
   ```bash
   shutdown +10
   ```

3. **Reboot the system immediately:**
   ```bash
   shutdown -r now
   ```

4. **Power off the system at a specific time (e.g., 11:30 PM):**
   ```bash
   shutdown 23:30
   ```

5. **Cancel a scheduled shutdown:**
   ```bash
   shutdown -c
   ```

6. **Shut down with a custom message:**
   ```bash
   shutdown +5 "System will shut down in 5 minutes for maintenance."
   ```

## Tips
- Always notify users before shutting down the system, especially on multi-user systems, to prevent data loss.
- Use the `-c` option to cancel a shutdown if you change your mind.
- Schedule shutdowns during off-peak hours to minimize disruption.
- Consider using `shutdown -h` for a complete halt or `shutdown -r` for a reboot, depending on your needs.