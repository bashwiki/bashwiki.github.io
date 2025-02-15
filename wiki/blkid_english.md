# [리눅스] Bash blkid 사용법

## Overview
The `blkid` command is a utility in Linux that is used to locate and print block device attributes. Its primary purpose is to identify and display information about block devices, such as their filesystem type, UUID (Universally Unique Identifier), and label. This command is particularly useful for system administrators and developers who need to manage disk partitions and filesystems.

## Usage
The basic syntax of the `blkid` command is as follows:

```bash
blkid [OPTION]... [DEVICE]...
```

### Common Options
- `-o, --output`: Specify the output format. Options include `value`, `full`, `udev`, and `list`.
- `-s, --match-tag`: Specify which tags to display (e.g., `UUID`, `LABEL`).
- `-p, --probe`: Probe the device for information (default behavior).
- `-c, --cache`: Use the cache file to speed up the process.
- `-h, --help`: Display help information about the command.

## Examples
### Example 1: Basic Usage
To list all block devices along with their attributes, simply run:

```bash
blkid
```

This command will output information for all detected block devices, including their UUIDs and filesystem types.

### Example 2: Display Specific Attributes
If you want to display only the UUIDs of the block devices, you can use the `-s` option:

```bash
blkid -s UUID
```

This command will filter the output to show only the UUIDs of the connected block devices.

## Tips
- Use the `-o value` option to get a cleaner output. For example, if you want just the UUIDs without additional information, you can run:

  ```bash
  blkid -o value -s UUID
  ```

- When scripting, consider using the `-c` option to utilize the cache, which can significantly speed up the command execution if you are querying the same devices multiple times.
- Always check the man page (`man blkid`) for the most up-to-date information and additional options that may be available in your specific Linux distribution.