# [Linux] Bash df Uso equivalente: Display disk space usage

## Overview
The `df` command in Bash is used to display information about disk space usage on file systems. It provides a summary of available and used disk space, helping users monitor their storage resources.

## Usage
The basic syntax of the `df` command is as follows:

```bash
df [options] [arguments]
```

## Common Options
- `-h`: Human-readable format. Displays sizes in a more understandable format (e.g., KB, MB, GB).
- `-T`: Shows the file system type.
- `-a`: Includes dummy file systems in the output.
- `-i`: Displays inode information instead of block usage.
- `--total`: Displays a grand total of all file systems.

## Common Examples

1. **Basic Disk Usage**
   To display the disk space usage of all mounted file systems:
   ```bash
   df
   ```

2. **Human-Readable Format**
   To display the disk space in a human-readable format:
   ```bash
   df -h
   ```

3. **File System Type**
   To include the file system type in the output:
   ```bash
   df -T
   ```

4. **Including Dummy File Systems**
   To include dummy file systems in the output:
   ```bash
   df -a
   ```

5. **Inode Information**
   To display inode usage instead of block usage:
   ```bash
   df -i
   ```

6. **Total Disk Usage**
   To show a total of all file systems:
   ```bash
   df --total
   ```

## Tips
- Use the `-h` option for easier interpretation of disk space, especially on systems with large storage capacities.
- Regularly check disk usage to avoid running out of space, which can lead to system issues.
- Combine options for more detailed output, such as `df -hT` to see both human-readable sizes and file system types.