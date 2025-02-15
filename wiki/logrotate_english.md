# [리눅스] Bash logrotate 사용법

## Overview
`logrotate` is a system utility in Linux that manages the rotation and compression of log files. Its primary purpose is to help automate the process of archiving old log files, ensuring that they do not consume excessive disk space over time. By rotating logs, `logrotate` allows for the systematic management of log files, making it easier for system administrators to maintain logs without manual intervention.

## Usage
The basic syntax for the `logrotate` command is as follows:

```bash
logrotate [options] [config_file]
```

### Common Options
- `-f`, `--force`: Forces rotation, even if the log files do not meet the criteria for rotation.
- `-s`, `--state`: Specifies the state file to use, which keeps track of the last rotation times.
- `-v`, `--verbose`: Provides detailed output of the rotation process.
- `-d`, `--debug`: Runs in debug mode, showing what would happen without actually performing the rotation.
- `-n`, `--noexec`: Shows what would be done without making any changes.

## Examples

### Example 1: Basic Log Rotation
To perform log rotation using the default configuration file, typically located at `/etc/logrotate.conf`, you can run:

```bash
logrotate /etc/logrotate.conf
```

This command will process the log files as defined in the configuration file, rotating them according to the specified rules.

### Example 2: Forcing Log Rotation
If you want to force the rotation of logs regardless of their current state, you can use the `-f` option:

```bash
logrotate -f /etc/logrotate.conf
```

This command will rotate the logs even if they have not reached the defined size or age for rotation.

## Tips
- **Configuration Files**: Customize your log rotation by creating specific configuration files for different applications in `/etc/logrotate.d/`. This allows for granular control over how each application's logs are managed.
- **Testing Configurations**: Always use the `-d` (debug) option when testing new configurations to ensure that your settings will work as expected without making any changes.
- **Regular Scheduling**: Ensure that `logrotate` is scheduled to run regularly, typically via a cron job, to maintain log files automatically.
- **Monitoring Disk Space**: Keep an eye on disk space usage, especially if logs are not being rotated as expected. This can help prevent issues related to disk space exhaustion.

By following these guidelines and utilizing the `logrotate` command effectively, you can maintain a clean and efficient logging system on your Linux servers.