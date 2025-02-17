# [Linux] Bash mpstat Uso: Monitor CPU usage statistics

## Overview
The `mpstat` command is a part of the `sysstat` package in Linux that provides detailed CPU usage statistics. It displays the average CPU usage for each available CPU core, which helps in monitoring system performance and diagnosing potential bottlenecks.

## Usage
The basic syntax of the `mpstat` command is as follows:

```bash
mpstat [options] [interval] [count]
```

## Common Options
- `-P ALL`: Display statistics for all CPUs.
- `-u`: Show CPU usage in percentage.
- `-h`: Display output in a human-readable format.
- `-V`: Show version information of `mpstat`.

## Common Examples

1. **Display CPU usage for all CPUs:**
   ```bash
   mpstat -P ALL
   ```

2. **Monitor CPU usage every 2 seconds for 5 times:**
   ```bash
   mpstat 2 5
   ```

3. **Show CPU usage in a human-readable format:**
   ```bash
   mpstat -h
   ```

4. **Display only the user CPU time:**
   ```bash
   mpstat -u
   ```

5. **Check the version of mpstat:**
   ```bash
   mpstat -V
   ```

## Tips
- Use `mpstat` in combination with other monitoring tools like `top` or `htop` for a comprehensive view of system performance.
- Regularly monitor CPU statistics during peak usage times to identify potential performance issues.
- Consider logging the output of `mpstat` to a file for further analysis and historical tracking of CPU performance.