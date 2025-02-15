# [리눅스] Bash mpstat 사용법

## Overview
`mpstat` is a command-line utility in Linux that provides detailed statistics about CPU usage on a multi-core system. It is part of the `sysstat` package and is primarily used to monitor CPU performance, allowing engineers and developers to analyze how effectively the CPU resources are being utilized. By displaying CPU usage for each available processor, `mpstat` helps identify performance bottlenecks and optimize system performance.

## Usage
The basic syntax of the `mpstat` command is as follows:

```bash
mpstat [options] [interval] [count]
```

### Common Options:
- `-P [processor]`: Specify which processor(s) to report. Use `ALL` to display statistics for all processors.
- `-u`: Display CPU usage (this is the default behavior).
- `-h`: Display output in a human-readable format.
- `-V`: Display version information.

### Parameters:
- `interval`: The time in seconds between each report. If not specified, `mpstat` will only provide a single report.
- `count`: The number of reports to generate. If not specified, it will continue until interrupted.

## Examples

### Example 1: Basic CPU Usage Report
To display CPU usage statistics for all processors every 2 seconds, run the following command:

```bash
mpstat 2
```

This command will output CPU usage statistics every 2 seconds until you stop it (usually with `Ctrl+C`).

### Example 2: CPU Usage for a Specific Processor
To view the CPU usage for a specific processor (e.g., CPU 0) every 5 seconds, use:

```bash
mpstat -P 0 5
```

This will provide a report for CPU 0 every 5 seconds.

## Tips
- Use the `-h` option to make the output more readable, especially when dealing with large numbers.
- Combine `mpstat` with other performance monitoring tools like `top` or `htop` for a more comprehensive view of system performance.
- Regularly monitor CPU usage during peak and off-peak hours to identify trends and potential issues.
- Consider scripting `mpstat` commands to log CPU usage over time for analysis and reporting.

By utilizing `mpstat`, engineers and developers can gain valuable insights into CPU performance, helping to ensure systems run efficiently and effectively.