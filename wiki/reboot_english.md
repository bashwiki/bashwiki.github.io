# [Linux] Bash reboot uso: Restart the system

The `reboot` command is used to restart the system immediately or after a specified delay.

## Overview
The `reboot` command is a straightforward way to reboot your Linux system. It can be used by system administrators to restart the machine, either immediately or with a delay, ensuring that all processes are terminated and the system is rebooted cleanly.

## Usage
The basic syntax of the `reboot` command is as follows:

```bash
reboot [options] [arguments]
```

## Common Options
- `-f` : Force the reboot without flushing the file systems.
- `-i` : Send an interrupt signal to all processes before rebooting.
- `-p` : Power off the machine after rebooting.
- `--help` : Display help information about the command.

## Common Examples
Here are some practical examples of using the `reboot` command:

1. **Immediate Reboot**
   ```bash
   reboot
   ```

2. **Force Reboot**
   ```bash
   reboot -f
   ```

3. **Reboot with Power Off**
   ```bash
   reboot -p
   ```

4. **Reboot with a Delay**
   ```bash
   shutdown -r +5
   ```
   (This command schedules a reboot in 5 minutes. Note that `shutdown` is often used for delayed reboots.)

5. **Reboot with a Message**
   ```bash
   shutdown -r now "System is rebooting for maintenance."
   ```
   (This sends a message to all users before rebooting.)

## Tips
- Always save your work before executing the `reboot` command to avoid data loss.
- Use the `-f` option with caution, as it can lead to data corruption if processes are not terminated properly.
- Consider using `shutdown` for scheduled reboots, as it provides more control over the timing and messaging to users.