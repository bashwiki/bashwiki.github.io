# [Linux] Bash blkid Uso: Retrieve block device attributes

## Overview
The `blkid` command in Linux is used to locate and print block device attributes. It can display information such as the device's UUID, filesystem type, and label, making it a valuable tool for system administrators and users who need to manage disk partitions and filesystems.

## Usage
The basic syntax of the `blkid` command is as follows:

```bash
blkid [options] [arguments]
```

## Common Options
- `-o, --output`: Specify the output format (e.g., `value`, `full`, `udev`).
- `-s, --match-tag`: Filter output to show only specific tags (e.g., `UUID`, `TYPE`).
- `-p, --probe`: Probe the device for filesystem information.
- `-c, --cache`: Use a cache file to speed up the command.
- `-h, --help`: Display help information about the command.

## Common Examples
Here are several practical examples of using the `blkid` command:

### Example 1: Display all block devices
```bash
blkid
```
This command lists all block devices along with their attributes.

### Example 2: Get UUID of a specific device
```bash
blkid /dev/sda1
```
This command retrieves the UUID of the `/dev/sda1` partition.

### Example 3: Show only the UUIDs
```bash
blkid -o value -s UUID
```
This command outputs only the UUIDs of all detected block devices.

### Example 4: Display filesystem type
```bash
blkid -o value -s TYPE /dev/sda1
```
This command shows the filesystem type of the `/dev/sda1` partition.

### Example 5: Use cache for faster results
```bash
blkid -c /etc/blkid.tab
```
This command uses a specified cache file to speed up the retrieval of block device information.

## Tips
- Use `blkid` with `sudo` if you encounter permission issues when accessing certain block devices.
- Regularly check the output of `blkid` to keep track of changes in your disk partitions and filesystems.
- Combine `blkid` with other commands like `grep` to filter specific information more efficiently. For example:
  ```bash
  blkid | grep ext4
  ```
  This command filters the output to show only devices with the ext4 filesystem type.