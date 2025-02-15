# [리눅스] Bash dd 사용법

## Overview
The `dd` command in Bash is a powerful utility primarily used for low-level copying and conversion of raw data. It is commonly employed for tasks such as creating disk images, backing up and restoring entire drives or partitions, and converting file formats. The command operates at a byte level, making it suitable for handling binary files and devices.

## Usage
The basic syntax of the `dd` command is as follows:

```bash
dd if=<input_file> of=<output_file> [options]
```

- `if=<input_file>`: Specifies the input file or device. This can be a regular file, a block device (like a hard drive), or even `/dev/zero` for generating empty files.
- `of=<output_file>`: Specifies the output file or device where the data will be written.
- `[options]`: Additional options to modify the behavior of the command. Some common options include:
  - `bs=<size>`: Sets the block size for both read and write operations. For example, `bs=4M` reads and writes in 4 megabyte chunks.
  - `count=<number>`: Limits the number of blocks to copy. For instance, `count=10` will copy only 10 blocks of the specified size.
  - `status=<level>`: Controls the output of the command's progress. Options include `none`, `noxfer`, and `progress`.

## Examples

### Example 1: Creating a Disk Image
To create a disk image of a USB drive located at `/dev/sdb`, you can use the following command:

```bash
dd if=/dev/sdb of=usb_backup.img bs=4M status=progress
```
This command copies the entire contents of the USB drive into a file named `usb_backup.img`, using a block size of 4 megabytes and displaying progress information.

### Example 2: Restoring from a Disk Image
To restore the disk image back to the USB drive, you would use:

```bash
dd if=usb_backup.img of=/dev/sdb bs=4M status=progress
```
This command writes the contents of `usb_backup.img` back to the USB drive, effectively restoring it to its previous state.

## Tips
- **Be Cautious**: The `dd` command can overwrite data without warning. Always double-check the `if` and `of` parameters to avoid accidental data loss.
- **Use `sync`**: To ensure that all data is written to the output file before the command completes, you can add the `sync` option at the end of the command. This will flush the output buffer.
- **Test with Small Files**: Before using `dd` on large disks or important data, practice with small files to understand how it works.
- **Check Disk Usage**: Use the `df` command to ensure you have enough space on the destination before copying large files or images.

By following these guidelines and examples, you can effectively utilize the `dd` command for various data manipulation tasks in Bash.