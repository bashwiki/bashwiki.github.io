# [리눅스] Bash mount 사용법

## Overview
The `mount` command in Bash is used to attach filesystems to the directory tree of the operating system. Its primary purpose is to make files and directories on a device accessible at a specified mount point in the filesystem hierarchy. This command is essential for managing storage devices, such as hard drives, USB drives, and network shares, allowing users to read from and write to these devices.

## Usage
The basic syntax of the `mount` command is as follows:

```bash
mount [options] <device> <mount_point>
```

### Common Options
- `-t <type>`: Specify the filesystem type (e.g., `ext4`, `ntfs`, `vfat`). If omitted, the system attempts to auto-detect the filesystem type.
- `-o <options>`: Pass additional options to the mount command, such as `ro` (read-only), `rw` (read-write), `noexec` (do not allow execution of binaries), and `user` (allow a non-root user to mount).
- `-a`: Mount all filesystems mentioned in `/etc/fstab`.
- `-r`: Mount the filesystem as read-only.

## Examples

### Example 1: Mounting a USB Drive
To mount a USB drive located at `/dev/sdb1` to the directory `/mnt/usb`, you would use the following command:

```bash
sudo mount /dev/sdb1 /mnt/usb
```

### Example 2: Mounting with Specific Filesystem Type
If you know the filesystem type of the device, you can specify it. For example, to mount an NTFS filesystem:

```bash
sudo mount -t ntfs /dev/sdc1 /mnt/ntfs_drive
```

## Tips
- Always ensure that the mount point directory exists before attempting to mount a device. You can create it using `mkdir <mount_point>`.
- Use the `df -h` command to check mounted filesystems and their usage.
- To unmount a filesystem, use the `umount` command followed by the mount point or device name.
- Be cautious when mounting filesystems as root, as it can lead to unintended changes or data loss if not handled properly.
- Consider adding entries to `/etc/fstab` for persistent mounts across reboots, which can simplify the mounting process.