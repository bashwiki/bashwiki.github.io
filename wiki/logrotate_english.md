# [Linux] Bash logrotate用法: 管理日志文件轮换

## Overview
The `logrotate` command is a utility in Linux that manages the rotation, compression, and removal of log files. It helps to prevent log files from consuming too much disk space by periodically archiving and compressing them.

## Usage
The basic syntax of the `logrotate` command is as follows:

```bash
logrotate [options] [arguments]
```

## Common Options
- `-f`, `--force`: Forces log rotation, even if it is not necessary.
- `-s`, `--state`: Specifies the state file to keep track of the log rotation status.
- `-v`, `--verbose`: Enables verbose output, providing detailed information about the actions taken.
- `-d`, `--debug`: Runs in debug mode, showing what would be done without actually performing the rotation.
- `-n`, `--no-rotate`: Prevents any rotation from occurring, useful for testing configurations.

## Common Examples

### Basic Log Rotation
To perform log rotation using the default configuration file, typically located at `/etc/logrotate.conf`, simply run:

```bash
logrotate /etc/logrotate.conf
```

### Force Log Rotation
To force the rotation of logs regardless of the last rotation date, use:

```bash
logrotate -f /etc/logrotate.conf
```

### Verbose Output
To see detailed output of the log rotation process, you can enable verbose mode:

```bash
logrotate -v /etc/logrotate.conf
```

### Using a Custom State File
If you want to specify a custom state file to track log rotation, you can do so with the `-s` option:

```bash
logrotate -s /path/to/custom.state /etc/logrotate.conf
```

### Debugging Configuration
To check what actions would be taken without actually rotating the logs, use the debug option:

```bash
logrotate -d /etc/logrotate.conf
```

## Tips
- Always test your `logrotate` configuration with the `-d` option before applying changes to ensure it behaves as expected.
- Regularly check your log files and their sizes to adjust the rotation frequency and retention policy as necessary.
- Consider setting up email notifications for critical logs to stay informed about issues without manually checking log files.