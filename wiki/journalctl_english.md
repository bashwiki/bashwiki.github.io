# [Linux] Bash journalctl uso: View and query system logs

## Overview
The `journalctl` command is a utility for querying and displaying messages from the journal, which is a component of the systemd system and service manager. It allows users to access logs from various sources, including system services, kernel messages, and user applications.

## Usage
The basic syntax of the `journalctl` command is as follows:

```bash
journalctl [options] [arguments]
```

## Common Options
- `-b`: Show logs from the current boot only.
- `-f`: Follow the log output in real-time, similar to `tail -f`.
- `--since`: Show logs since a specific date/time.
- `--until`: Show logs until a specific date/time.
- `-u <unit>`: Show logs for a specific systemd unit (service).
- `-p <priority>`: Filter logs by priority level (e.g., `info`, `warning`, `error`).

## Common Examples
Here are some practical examples of using `journalctl`:

1. **View all logs:**
   ```bash
   journalctl
   ```

2. **View logs from the current boot:**
   ```bash
   journalctl -b
   ```

3. **Follow log output in real-time:**
   ```bash
   journalctl -f
   ```

4. **View logs for a specific service:**
   ```bash
   journalctl -u ssh.service
   ```

5. **View logs since a specific date:**
   ```bash
   journalctl --since "2023-10-01 10:00:00"
   ```

6. **View logs until a specific date:**
   ```bash
   journalctl --until "2023-10-01 12:00:00"
   ```

7. **Filter logs by priority level:**
   ```bash
   journalctl -p warning
   ```

## Tips
- Use `journalctl -b -1` to view logs from the previous boot, which can be helpful for troubleshooting.
- Combine options for more refined queries, such as `journalctl -u nginx.service -b`.
- Consider using `grep` in conjunction with `journalctl` to search for specific keywords in the logs, like so:
  ```bash
  journalctl | grep "error"
  ```