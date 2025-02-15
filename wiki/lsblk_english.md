# [리눅스] Bash lsblk 사용법

## Overview
The `lsblk` command in Linux is used to list information about all available block devices. Block devices are storage devices that read and write data in blocks, such as hard drives, SSDs, USB drives, and partitions. The primary purpose of `lsblk` is to provide a clear and organized view of the storage devices connected to the system, including their hierarchy, size, and mount points.

## Usage
The basic syntax of the `lsblk` command is as follows:

```bash
lsblk [OPTION...]
```

### Common Options
- `-a`, `--all`: Show all devices, including empty ones.
- `-f`, `--fs`: Display filesystem information, including type, label, and UUID.
- `-l`, `--list`: Use a list format instead of the tree format.
- `-o`, `--output`: Specify which columns to display (e.g., NAME, SIZE, TYPE).
- `-p`, `--paths`: Print device paths instead of device names.
- `-n`, `--noheadings`: Suppress the header output.

## Examples

### Example 1: Basic Usage
To list all block devices in a tree format, simply run:

```bash
lsblk
```

This will display a hierarchical view of all block devices, their sizes, types, and mount points.

### Example 2: Display Filesystem Information
To include filesystem details in the output, use the `-f` option:

```bash
lsblk -f
```

This command will show the filesystem type, label, and UUID for each block device, providing more context about the storage devices.

## Tips
- Use the `-o` option to customize the output columns to display only the information you need, which can make it easier to read and analyze.
- Combine `lsblk` with other commands like `grep` to filter results. For example, to find a specific device, you can use:

  ```bash
  lsblk | grep sda
  ```

- Regularly check your block devices with `lsblk` to monitor disk usage and ensure that your system's storage is organized and functioning correctly.