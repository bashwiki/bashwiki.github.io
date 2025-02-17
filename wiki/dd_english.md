# [Linux] Bash dd Uso equivalente: Copiar y convertir archivos

## Overview
The `dd` command in Bash is a powerful utility for low-level copying and conversion of raw data. It is often used for tasks such as backing up and restoring entire disks, creating disk images, and converting file formats.

## Usage
The basic syntax of the `dd` command is as follows:

```bash
dd [options] [arguments]
```

## Common Options
- `if=`: Specifies the input file. This is the file to read from.
- `of=`: Specifies the output file. This is the file to write to.
- `bs=`: Sets the block size for both read and write operations.
- `count=`: Limits the number of blocks to copy.
- `status=`: Controls the output of the command's progress. Options include `none`, `noxfer`, and `progress`.

## Common Examples

1. **Copying a file:**
   ```bash
   dd if=input.txt of=output.txt
   ```

2. **Creating a disk image:**
   ```bash
   dd if=/dev/sda of=/path/to/disk_image.img bs=4M
   ```

3. **Restoring a disk image:**
   ```bash
   dd if=/path/to/disk_image.img of=/dev/sda bs=4M
   ```

4. **Creating a bootable USB drive:**
   ```bash
   dd if=path/to/iso_file.iso of=/dev/sdb bs=4M status=progress
   ```

5. **Copying only a specific number of bytes:**
   ```bash
   dd if=input.txt of=output.txt bs=1 count=100
   ```

## Tips
- Always double-check the `of=` option to avoid overwriting important data.
- Use `status=progress` to monitor the progress of long-running operations.
- Consider using `sync` option to ensure that all data is written before the command completes.
- When working with devices, ensure you have the necessary permissions (often requires `sudo`).