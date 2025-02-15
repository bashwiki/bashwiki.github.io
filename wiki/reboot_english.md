# [리눅스] Bash reboot 사용법

## Overview
The `reboot` command in Bash is used to restart the system. It is a powerful command that instructs the operating system to terminate all running processes and then restart the machine. This command is typically used by system administrators and developers when they need to apply system updates, recover from an unresponsive state, or simply refresh the system environment.

## Usage
The basic syntax for the `reboot` command is as follows:

```bash
reboot [OPTION]
```

### Common Options
- `-f`, `--force`: Forces an immediate reboot without performing a clean shutdown of the system. This option should be used with caution, as it may lead to data loss or corruption.
- `-p`, `--poweroff`: This option is used to power off the machine instead of rebooting it. While this is not the primary function of `reboot`, it can be useful in certain scenarios.
- `--halt`: Halts the system without rebooting. This option is similar to powering off but may leave the system in a state where it can be restarted without a full power cycle.

## Examples
### Example 1: Basic Reboot
To perform a standard reboot of the system, simply run:

```bash
sudo reboot
```

This command will initiate a clean shutdown of all processes and then restart the system.

### Example 2: Force Reboot
If the system is unresponsive and you need to force a reboot, you can use the `-f` option:

```bash
sudo reboot -f
```

This will immediately restart the system without shutting down processes gracefully.

## Tips
- Always try to use the standard `reboot` command without options first to ensure that all processes are terminated cleanly.
- Use the `-f` option only as a last resort, as it can lead to data loss or corruption.
- If you are working on a remote server, ensure that you have saved all work and notified other users before executing the reboot command.
- Consider using `shutdown` with a specified time if you want to give users a warning before the system goes down, e.g., `sudo shutdown -r now` for an immediate reboot with a warning.