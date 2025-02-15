# [리눅스] Bash resize2fs 사용법

## Overview
`resize2fs` is a command-line utility in Linux used to resize ext2, ext3, or ext4 file systems. Its primary purpose is to allow users to increase or decrease the size of a file system on a partition. This is particularly useful when managing disk space, as it enables efficient use of available storage by adjusting file system sizes according to the needs of the system or applications.

## Usage
The basic syntax of the `resize2fs` command is as follows:

```bash
resize2fs [options] <filesystem>
```

### Common Options
- `<filesystem>`: This can be a device name (e.g., `/dev/sda1`) or a mount point (e.g., `/mnt/data`) of the file system you wish to resize.
- `-f`: Force the resize operation, even if the file system is not clean.
- `-p`: Print progress information while resizing.
- `-s`: Resize the file system to the size of the underlying block device.

## Examples

### Example 1: Increasing the Size of a File System
To increase the size of an ext4 file system located on `/dev/sda1`, you would first ensure that the underlying partition has been resized (e.g., using `fdisk` or `parted`), and then run:

```bash
resize2fs /dev/sda1
```

This command will adjust the file system to fill the entire partition.

### Example 2: Decreasing the Size of a File System
To decrease the size of a file system, you must first unmount it. After unmounting, you can specify the new size:

```bash
umount /dev/sda1
resize2fs /dev/sda1 20G
```

This command resizes the file system on `/dev/sda1` to 20 gigabytes.

## Tips
- Always back up your data before resizing a file system, as there is a risk of data loss if something goes wrong.
- Ensure that the file system is unmounted before decreasing its size to prevent corruption.
- Use the `-p` option to monitor the progress of the resizing operation, especially for large file systems.
- Check the file system for errors using `e2fsck` before resizing to ensure its integrity.