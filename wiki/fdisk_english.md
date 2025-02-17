# [Linux] Bash fdisk Usage: Manage disk partitions

## Overview
The `fdisk` command is a powerful utility in Linux used for managing disk partitions. It allows users to create, delete, resize, and manipulate disk partitions on hard drives and other storage devices. With `fdisk`, you can also view partition tables and change partition types.

## Usage
The basic syntax of the `fdisk` command is as follows:

```bash
fdisk [options] [device]
```

Where `[device]` is the disk you want to manage (e.g., `/dev/sda`).

## Common Options
- `-l`: List the partition tables of all devices.
- `-u`: Use sectors instead of cylinders for displaying sizes.
- `-v`: Display version information.
- `-n`: Create a new partition.
- `-d`: Delete a partition.
- `-t`: Change a partition's system ID.

## Common Examples

### Listing Partitions
To list all partitions on all disks, use:
```bash
fdisk -l
```

### Creating a New Partition
To create a new partition on `/dev/sda`, start `fdisk` interactively:
```bash
fdisk /dev/sda
```
Then, follow the prompts to create a new partition.

### Deleting a Partition
To delete a partition, start `fdisk` interactively:
```bash
fdisk /dev/sda
```
Select the partition you want to delete and follow the prompts.

### Changing a Partition Type
To change the type of a partition, start `fdisk` and use the `t` option:
```bash
fdisk /dev/sda
```
Then, specify the partition number and the new type.

## Tips
- Always back up important data before modifying partitions.
- Use `parted` for more advanced partitioning tasks, especially with larger disks.
- Be cautious when deleting partitions, as this action is irreversible and can lead to data loss.