# [리눅스] Bash umount 사용법

## Overview
The `umount` command in Bash is used to unmount file systems that have been mounted to the Linux operating system. Its primary purpose is to safely detach a file system from the file hierarchy, ensuring that all data is written to the disk and that the file system is no longer in use. This is crucial for maintaining data integrity and preventing data loss, especially when removing external storage devices or network file systems.

## Usage
The basic syntax of the `umount` command is as follows:

```bash
umount [options] <target>
```

### Common Options
- `<target>`: This can be the mount point (directory) or the device name (e.g., `/dev/sdb1`) of the file system you wish to unmount.
- `-a`: Unmount all mounted file systems listed in `/etc/mtab`.
- `-l`: Lazy unmount. Detaches the file system immediately but delays the actual unmounting until it is no longer busy.
- `-f`: Force unmount. This option is used to unmount a file system that is busy or has errors.
- `-r`: Remount the file system read-only if it is busy.

## Examples
### Example 1: Unmounting a Mounted File System
To unmount a file system mounted at `/mnt/usb`, you would use the following command:

```bash
umount /mnt/usb
```

### Example 2: Force Unmounting a Busy File System
If you need to forcefully unmount a file system that is busy, you can use the `-f` option:

```bash
umount -f /mnt/usb
```

## Tips
- Always ensure that no processes are using the file system you intend to unmount. You can use the `lsof` command to check for open files on the mount point.
- Consider using the `-l` option for a lazy unmount if you encounter a busy file system, as it allows for a safer detachment without immediate disruption.
- Be cautious when using the `-f` option, as it can lead to data loss if there are unsaved changes or ongoing processes.
- Regularly check your `/etc/mtab` or use the `mount` command to see a list of currently mounted file systems before unmounting.