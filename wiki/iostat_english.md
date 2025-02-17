# [Linux] Bash iostat Uso: Monitor system input/output device loading

## Overview
The `iostat` command is a useful tool for monitoring system input/output device loading in Linux. It provides statistics on CPU utilization and input/output operations for devices and partitions, helping users identify performance bottlenecks.

## Usage
The basic syntax of the `iostat` command is as follows:

```bash
iostat [options] [arguments]
```

## Common Options
- `-c`: Display CPU usage statistics.
- `-d`: Show device utilization statistics.
- `-x`: Provide extended statistics, including more detailed metrics for each device.
- `-m`: Display statistics in megabytes per second.
- `-t`: Include a timestamp in the output.

## Common Examples

1. **Basic CPU and Device Statistics**
   ```bash
   iostat
   ```

2. **Display CPU Usage Only**
   ```bash
   iostat -c
   ```

3. **Show Device Statistics with Extended Information**
   ```bash
   iostat -dx
   ```

4. **Monitor I/O Statistics in Megabytes**
   ```bash
   iostat -m
   ```

5. **Include Timestamps in the Output**
   ```bash
   iostat -t
   ```

6. **Continuous Monitoring Every 5 Seconds**
   ```bash
   iostat 5
   ```

## Tips
- Use the `-x` option for detailed device statistics to better understand performance issues.
- Combine `iostat` with other monitoring tools like `vmstat` or `top` for a comprehensive view of system performance.
- Regularly monitor I/O statistics during peak usage times to identify potential bottlenecks and optimize performance.