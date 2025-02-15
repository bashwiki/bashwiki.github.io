# [리눅스] Bash vmstat 사용법

## Overview
The `vmstat` command, short for "virtual memory statistics," is a utility in Linux that provides a snapshot of system performance, particularly focusing on memory, processes, paging, block I/O, traps, and CPU activity. Its primary purpose is to help system administrators and developers monitor system performance and diagnose issues related to memory and CPU usage.

## Usage
The basic syntax of the `vmstat` command is as follows:

```bash
vmstat [options] [delay [count]]
```

### Common Options:
- `delay`: The interval in seconds between updates. If specified, `vmstat` will continuously report statistics at this interval.
- `count`: The number of updates to display. If not specified, `vmstat` will run indefinitely until interrupted.
- `-s`: Display memory statistics in a more detailed format.
- `-m`: Show memory statistics related to slabinfo.
- `-d`: Display disk statistics.

## Examples
### Example 1: Basic Usage
To display system performance statistics once, you can simply run:

```bash
vmstat
```

This will output a single line of statistics, including information about processes, memory, paging, block I/O, traps, and CPU usage.

### Example 2: Continuous Monitoring
To monitor the system performance every 2 seconds for a total of 5 updates, use:

```bash
vmstat 2 5
```

This command will provide a continuous output of system statistics every 2 seconds, stopping after 5 iterations.

## Tips
- Use `vmstat` in conjunction with other monitoring tools like `top` or `htop` for a comprehensive view of system performance.
- Pay attention to the CPU idle percentage; low values may indicate that your system is under heavy load.
- The `-s` option can be particularly useful for a quick overview of memory usage, especially when troubleshooting memory-related issues.
- Consider redirecting the output to a file for later analysis, for example: `vmstat 2 5 > vmstat_output.txt`.