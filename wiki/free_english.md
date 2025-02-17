# [Linux] Bash free comando: mostrar el uso de memoria del sistema

## Overview
The `free` command is a simple yet powerful tool in Linux that displays the amount of free and used memory in the system. It provides a quick overview of memory usage, including physical memory (RAM) and swap space, helping users monitor system performance.

## Usage
The basic syntax of the `free` command is as follows:

```bash
free [options] [arguments]
```

## Common Options
- `-h` or `--human`: Display the output in a human-readable format (e.g., in MB or GB).
- `-m`: Show memory usage in megabytes.
- `-g`: Show memory usage in gigabytes.
- `-s <seconds>`: Continuously display memory usage at specified intervals (in seconds).
- `-t`: Show a total line that summarizes the memory usage.

## Common Examples
Here are some practical examples of using the `free` command:

1. **Basic Memory Usage**
   ```bash
   free
   ```

2. **Human-Readable Format**
   ```bash
   free -h
   ```

3. **Memory Usage in Megabytes**
   ```bash
   free -m
   ```

4. **Memory Usage in Gigabytes**
   ```bash
   free -g
   ```

5. **Continuous Monitoring Every 5 Seconds**
   ```bash
   free -s 5
   ```

6. **Including Total Memory Usage**
   ```bash
   free -t
   ```

## Tips
- Use the `-h` option for easier reading of memory statistics, especially on systems with large amounts of RAM.
- Combine `free` with other commands like `watch` for real-time monitoring:
  ```bash
  watch free -h
  ```
- Regularly check memory usage to identify potential performance issues or memory leaks in applications.