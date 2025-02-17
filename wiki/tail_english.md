# [English] Bash tail Usage: Display the end of a file

## Overview
The `tail` command in Bash is used to display the last part of a file. It is particularly useful for viewing the most recent entries in log files or any other text files where the latest information is appended at the end.

## Usage
The basic syntax of the `tail` command is as follows:

```bash
tail [options] [arguments]
```

## Common Options
- `-n [number]`: Displays the last `[number]` lines of the file. For example, `-n 10` shows the last 10 lines.
- `-f`: Follows the file as it grows, displaying new lines in real-time. This is especially useful for monitoring log files.
- `-c [number]`: Displays the last `[number]` bytes of the file.
- `-q`: Suppresses the output of headers when multiple files are being processed.
- `-v`: Always outputs headers when multiple files are being processed, even if there is only one file.

## Common Examples
Here are some practical examples of how to use the `tail` command:

1. **Display the last 10 lines of a file:**
   ```bash
   tail filename.txt
   ```

2. **Display the last 20 lines of a file:**
   ```bash
   tail -n 20 filename.txt
   ```

3. **Follow a log file in real-time:**
   ```bash
   tail -f /var/log/syslog
   ```

4. **Display the last 50 bytes of a file:**
   ```bash
   tail -c 50 filename.txt
   ```

5. **Display the last 5 lines of multiple files:**
   ```bash
   tail -n 5 file1.txt file2.txt
   ```

## Tips
- Use `tail -f` to monitor log files for real-time updates, which is invaluable for troubleshooting.
- Combine `tail` with other commands using pipes for more powerful data manipulation. For example, `tail -n 100 filename.txt | grep "error"` to find errors in the last 100 lines.
- If you want to view the last few lines of a file and then stop following it, you can use `Ctrl + C` to exit the `tail -f` command.