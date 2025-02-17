# [Linux] Bash mount uso: Mount file systems

## Overview
The `mount` command in Bash is used to attach file systems to a specified directory in the Linux file system hierarchy. This allows users to access files and directories stored on different devices or partitions as if they were part of the main file system.

## Usage
The basic syntax of the `mount` command is as follows:

```bash
mount [options] [device] [mount_point]
```

- `[device]`: The device or file system to be mounted (e.g., `/dev/sda1`).
- `[mount_point]`: The directory where the file system will be attached.

## Common Options
- `-t fstype`: Specify the type of file system (e.g., `ext4`, `ntfs`).
- `-o options`: Specify mount options (e.g., `ro` for read-only).
- `-a`: Mount all file systems mentioned in `/etc/fstab`.
- `-r`: Mount the file system as read-only.
- `-v`: Verbose output, showing more details during the mount process.

## Common Examples

### Mounting a USB Drive
To mount a USB drive located at `/dev/sdb1` to the directory `/mnt/usb`, use the following command:

```bash
sudo mount /dev/sdb1 /mnt/usb
```

### Mounting with Specific File System Type
If you know the file system type is `ntfs`, you can specify it like this:

```bash
sudo mount -t ntfs /dev/sdb1 /mnt/usb
```

### Mounting with Options
To mount a file system as read-only, you can use the `-o` option:

```bash
sudo mount -o ro /dev/sda1 /mnt/data
```

### Mounting All File Systems
To mount all file systems defined in `/etc/fstab`, simply use:

```bash
sudo mount -a
```

## Tips
- Always ensure the mount point directory exists before attempting to mount a file system.
- Use `df -h` to check mounted file systems and their usage.
- To unmount a file system, use the `umount` command followed by the mount point or device.
- Be cautious when mounting file systems as read-write, especially if they contain important data.