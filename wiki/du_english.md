# [Linux] Bash du kullanım: Disk kullanımını analiz etme

## Overview
The `du` (disk usage) command is a standard Unix/Linux command used to estimate and report the amount of disk space used by files and directories. It helps users understand how much space is being consumed on their file systems.

## Usage
The basic syntax of the `du` command is as follows:

```bash
du [options] [arguments]
```

## Common Options
- `-h`: Display sizes in a human-readable format (e.g., KB, MB).
- `-s`: Show only a total for each argument.
- `-a`: Include files in the output, not just directories.
- `-c`: Produce a grand total at the end of the output.
- `--max-depth=N`: Limit the output to directories and files at depth N.

## Common Examples
1. **Check disk usage of the current directory**:
   ```bash
   du
   ```

2. **Display disk usage in a human-readable format**:
   ```bash
   du -h
   ```

3. **Get a summary of disk usage for a specific directory**:
   ```bash
   du -sh /path/to/directory
   ```

4. **List all files and directories with their sizes**:
   ```bash
   du -ah /path/to/directory
   ```

5. **Show disk usage with a maximum depth of 1**:
   ```bash
   du --max-depth=1 -h
   ```

6. **Get a total disk usage for multiple directories**:
   ```bash
   du -ch /path/to/dir1 /path/to/dir2
   ```

## Tips
- Use the `-h` option to easily interpret the sizes without needing to convert from bytes.
- Combine `du` with `sort` to find the largest directories:
  ```bash
  du -h | sort -hr
  ```
- Regularly check disk usage to manage storage effectively and avoid running out of space.