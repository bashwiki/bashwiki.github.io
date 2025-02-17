# [Linux] Bash vmstat Uso equivalente: Monitor system performance

## Overview
The `vmstat` command in Linux provides a snapshot of system performance, including information about processes, memory, paging, block I/O, traps, and CPU activity. It helps system administrators and users understand how the system is performing and diagnose potential issues.

## Usage
The basic syntax of the `vmstat` command is as follows:

```bash
vmstat [options] [delay] [count]
```

- `delay`: The number of seconds between updates.
- `count`: The number of updates to display.

## Common Options
- `-a`: Show active and inactive memory.
- `-m`: Display memory statistics.
- `-s`: Print a table of various event counters and memory statistics.
- `-d`: Show disk statistics.
- `-h`: Display help information.

## Common Examples

1. **Basic Usage**: Display system performance statistics every 2 seconds.
   ```bash
   vmstat 2
   ```

2. **Show Active and Inactive Memory**: Use the `-a` option to include memory details.
   ```bash
   vmstat -a 2
   ```

3. **Display Disk Statistics**: Use the `-d` option to view disk I/O statistics.
   ```bash
   vmstat -d 2
   ```

4. **Memory Statistics**: Use the `-m` option to get detailed memory statistics.
   ```bash
   vmstat -m
   ```

5. **Event Counters**: Print a summary of various event counters.
   ```bash
   vmstat -s
   ```

## Tips
- Use `vmstat` in combination with other monitoring tools like `top` or `htop` for a more comprehensive view of system performance.
- Monitor the system during peak usage times to identify bottlenecks.
- Regularly check the output to understand normal performance baselines, which can help in troubleshooting when issues arise.