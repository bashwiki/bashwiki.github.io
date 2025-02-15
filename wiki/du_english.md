# [리눅스] Bash du 사용법

## Overview
The `du` command, short for "disk usage," is a standard Unix/Linux command used to estimate and report the file space usage of directories and files. Its primary purpose is to help users understand how much disk space is being consumed by specific files and directories, which can be particularly useful for system administrators and developers managing storage resources.

## Usage
The basic syntax of the `du` command is as follows:

```bash
du [OPTION]... [FILE]...
```

### Common Options:
- `-h`: Human-readable format. This option displays sizes in a more understandable format (e.g., KB, MB, GB).
- `-s`: Summarize. This option provides a total size for each argument instead of listing the size of each individual file and subdirectory.
- `-a`: All files. This option includes files as well as directories in the output.
- `-c`: Produce a grand total. This option adds a final line showing the total size of all specified files and directories.
- `-d N`: Limit the depth of directory traversal to N levels.

## Examples
### Example 1: Basic Disk Usage of a Directory
To check the disk usage of the current directory and its subdirectories in a human-readable format, you can use:

```bash
du -h
```

### Example 2: Summarize Disk Usage of a Specific Directory
To get a summarized total size of a specific directory (e.g., `/var/log`), you can run:

```bash
du -sh /var/log
```

This command will output the total size of the `/var/log` directory without listing the sizes of individual files and subdirectories.

## Tips
- Use the `-c` option in combination with `-h` and `-s` to get a total size of multiple directories in a human-readable format. For example:

  ```bash
  du -shc /var/log /home/user
  ```

- When dealing with large directories, consider using the `-d` option to limit the depth of the output, making it easier to analyze:

  ```bash
  du -h -d 1 /path/to/directory
  ```

- If you want to exclude certain files or directories from the output, you can use the `--exclude` option. For example:

  ```bash
  du -h --exclude='*.tmp' /path/to/directory
  ```

By leveraging the `du` command effectively, you can manage disk space more efficiently and keep your system organized.