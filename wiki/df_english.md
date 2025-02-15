# [리눅스] Bash df 사용법

## Overview
The `df` command in Bash is used to report the amount of disk space used and available on file systems. Its primary purpose is to provide users with a quick overview of the disk usage on their system, helping them monitor and manage storage effectively. This command is particularly useful for system administrators and developers who need to ensure that their applications have sufficient disk space to operate.

## Usage
The basic syntax of the `df` command is as follows:

```bash
df [OPTION]... [FILE]...
```

### Common Options:
- `-h`: Human-readable format. This option displays sizes in a more understandable format (e.g., KB, MB, GB).
- `-T`: Displays the type of each file system.
- `-a`: Includes dummy file systems in the output.
- `-i`: Shows information about inodes instead of block usage.
- `-t TYPE`: Limits the output to file systems of the specified type.
- `-x TYPE`: Excludes file systems of the specified type from the output.

## Examples
### Example 1: Basic Disk Usage
To display the disk space usage in a human-readable format, you can use the following command:

```bash
df -h
```
This command will output a list of all mounted file systems along with their total size, used space, available space, and the mount point.

### Example 2: Displaying File System Types
If you want to see the types of file systems along with their usage, you can use:

```bash
df -hT
```
This command will show the same information as the previous example but will also include the type of each file system, which can be helpful for understanding the storage architecture.

## Tips
- Always use the `-h` option for easier readability, especially when dealing with large disk sizes.
- Combine options for more detailed output. For example, `df -hT` gives you both human-readable sizes and file system types.
- Regularly check disk usage to avoid running out of space, which can lead to application failures or data loss.
- Use the `-i` option to monitor inode usage, especially on systems where many small files are stored, as running out of inodes can also prevent file creation.