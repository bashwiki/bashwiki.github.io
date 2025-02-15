# [리눅스] Bash iostat 사용법

## Overview
The `iostat` command is a part of the sysstat package in Linux and is primarily used for monitoring system input/output device loading by observing the time the devices are active in relation to their average transfer rates. It provides valuable insights into the performance of the system's disks and can help identify potential bottlenecks in disk I/O operations. By analyzing the output of `iostat`, engineers and developers can make informed decisions about system performance tuning and resource allocation.

## Usage
The basic syntax of the `iostat` command is as follows:

```bash
iostat [options] [interval] [count]
```

### Common Options:
- `-c`: Display CPU statistics.
- `-d`: Display device utilization statistics.
- `-x`: Display extended statistics, including more detailed information about device performance.
- `-m`: Display statistics in megabytes per second instead of blocks.
- `-h`: Display output in a human-readable format.
- `interval`: The number of seconds between each report (default is 1 second).
- `count`: The number of reports to generate.

## Examples

### Example 1: Basic Disk I/O Statistics
To display the basic disk I/O statistics every 2 seconds for a total of 5 reports, you can use the following command:

```bash
iostat 2 5
```

This command will output the CPU and device utilization statistics, allowing you to monitor the performance of your disks over time.

### Example 2: Extended Statistics with Human-Readable Format
To get extended statistics in a human-readable format, you can use the `-x` and `-h` options:

```bash
iostat -x -h 3 4
```

This command will provide detailed statistics about each device every 3 seconds for a total of 4 reports, making it easier to interpret the data.

## Tips
- Use the `-c` option to monitor CPU usage alongside disk I/O statistics to get a complete picture of system performance.
- Combine the `-m` option with `-d` to view disk I/O in megabytes per second, which can be more intuitive than raw block counts.
- Regularly monitor your system with `iostat` during peak usage times to identify trends and potential performance issues.
- Consider redirecting the output to a file for further analysis or for keeping historical records of system performance:

```bash
iostat -x -h 5 > iostat_output.txt
```

By utilizing the `iostat` command effectively, you can gain valuable insights into your system's performance and make informed decisions to optimize resource usage.