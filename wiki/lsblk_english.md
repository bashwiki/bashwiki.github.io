# [Linux] Bash lsblk Uso equivalente: Listar bloques de dispositivos

## Overview
The `lsblk` command is used in Linux to list information about all available or specified block devices. It provides a tree-like structure that shows how devices are related to each other, making it easier to understand the storage layout of your system.

## Usage
The basic syntax of the `lsblk` command is:

```bash
lsblk [options] [arguments]
```

## Common Options
- `-a`, `--all`: Show all devices, including empty ones.
- `-f`, `--fs`: Display filesystem information.
- `-l`, `--list`: Use a list format instead of the tree format.
- `-o`, `--output`: Specify which columns to display.
- `-n`, `--noheadings`: Suppress the header output.
- `-p`, `--paths`: Show device paths instead of names.

## Common Examples
Here are some practical examples of using `lsblk`:

1. **List all block devices:**
   ```bash
   lsblk
   ```

2. **List all devices including empty ones:**
   ```bash
   lsblk -a
   ```

3. **Display filesystem information:**
   ```bash
   lsblk -f
   ```

4. **List devices in a flat format:**
   ```bash
   lsblk -l
   ```

5. **Show specific columns (e.g., NAME, SIZE, TYPE):**
   ```bash
   lsblk -o NAME,SIZE,TYPE
   ```

6. **Suppress headers in the output:**
   ```bash
   lsblk -n
   ```

## Tips
- Use the `-f` option to quickly check the filesystem type and label of your partitions.
- Combine `lsblk` with other commands like `grep` to filter specific devices or types.
- Regularly check your block devices with `lsblk` to monitor changes, especially after adding or removing storage devices.