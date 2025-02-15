# [리눅스] Bash free 사용법

## Overview
The `free` command is a simple yet powerful tool in Linux that provides information about the system's memory usage. Its primary purpose is to display the total amount of free and used physical and swap memory in the system, along with the buffers and caches used by the kernel. This command is particularly useful for system administrators and developers who need to monitor memory usage and ensure optimal performance of applications.

## Usage
The basic syntax of the `free` command is as follows:

```bash
free [options]
```

### Common Options
- `-h`, `--human`: Display the output in a human-readable format (e.g., using KB, MB, or GB).
- `-m`: Show memory usage in megabytes.
- `-g`: Show memory usage in gigabytes.
- `-s <seconds>`: Continuously display memory usage at specified intervals (in seconds).
- `-t`: Display a total line that summarizes the memory usage.

## Examples
### Example 1: Basic Memory Usage
To view the current memory usage in a human-readable format, you can use the following command:

```bash
free -h
```

This command will output the total, used, free, shared, buff/cache, and available memory in a format that is easy to understand.

### Example 2: Continuous Monitoring
If you want to monitor memory usage continuously every 5 seconds, you can use the `-s` option:

```bash
free -h -s 5
```

This command will refresh the memory usage statistics every 5 seconds, allowing you to observe changes in real-time.

## Tips
- Use the `-h` option for a more intuitive understanding of memory usage, especially when dealing with large amounts of data.
- Combine `free` with other commands like `watch` for real-time monitoring. For example:

  ```bash
  watch free -h
  ```

- Regularly check memory usage to identify potential memory leaks or performance bottlenecks in your applications.
- Remember that the "available" memory is a more accurate representation of how much memory is free for new applications, as it includes memory that can be reclaimed from buffers and caches.