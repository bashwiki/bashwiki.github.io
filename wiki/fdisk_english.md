# [리눅스] Bash fdisk 사용법

## Overview
The `fdisk` command is a powerful utility in Linux used for managing disk partitions. It allows users to create, delete, resize, and manipulate disk partitions on hard drives and other storage devices. `fdisk` operates primarily on MBR (Master Boot Record) partition tables, making it a crucial tool for system administrators and developers who need to manage storage configurations and ensure optimal disk usage.

## Usage
The basic syntax of the `fdisk` command is as follows:

```bash
fdisk [options] <device>
```

### Common Options:
- `-l`: Lists the partition tables for the specified devices. If no device is specified, it lists all available devices.
- `-u`: Displays sizes in sectors rather than cylinders, which can be more precise.
- `-s`: Displays the size of the specified partition in sectors.
- `-v`: Displays the version of `fdisk`.

## Examples

### Example 1: Listing Partitions
To list all the partitions on your system, you can use the following command:

```bash
fdisk -l
```

This command will display a list of all disk devices and their respective partitions, along with details such as size, type, and filesystem.

### Example 2: Creating a New Partition
To create a new partition on a specific device (e.g., `/dev/sda`), you would typically enter the interactive mode:

```bash
fdisk /dev/sda
```

Once in the interactive mode, you can use the following commands:
- `n`: Create a new partition.
- `p`: Print the partition table.
- `w`: Write the changes to the disk and exit.

After entering `n`, you will be prompted to specify the partition type (primary or extended), partition number, and size.

## Tips
- **Backup Data**: Always ensure that you have a backup of important data before modifying partitions, as mistakes can lead to data loss.
- **Unmount Partitions**: If you are modifying a mounted partition, make sure to unmount it first to prevent data corruption.
- **Use with Caution**: `fdisk` can significantly alter your disk structure; use it with caution and double-check commands before executing them.
- **Consult Documentation**: For more advanced options and usage, refer to the `man fdisk` command to access the manual pages, which provide detailed information about all available options and functionalities.