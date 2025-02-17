# [Linux] Bash tune2fs Usage: Adjust ext2/ext3/ext4 filesystem parameters

## Overview
The `tune2fs` command is a utility for adjusting tunable filesystem parameters on ext2, ext3, and ext4 filesystems. It allows users to modify various settings that can affect performance and behavior without needing to unmount the filesystem.

## Usage
The basic syntax of the `tune2fs` command is as follows:

```bash
tune2fs [options] [arguments]
```

## Common Options
- `-c <max_mount_count>`: Set the maximum mount count before a filesystem check is forced.
- `-i <interval>`: Set the maximum time interval between filesystem checks.
- `-O <feature>`: Enable specific filesystem features.
- `-o <options>`: Set filesystem options.
- `-l`: Display the current superblock information.
- `-j`: Add a journal to an ext2 filesystem, converting it to ext3.

## Common Examples
Here are some practical examples of using `tune2fs`:

### 1. Check current filesystem parameters
```bash
tune2fs -l /dev/sda1
```

### 2. Set the maximum mount count to 20
```bash
tune2fs -c 20 /dev/sda1
```

### 3. Set the maximum time interval between checks to 30 days
```bash
tune2fs -i 30d /dev/sda1
```

### 4. Enable the "dir_index" feature
```bash
tune2fs -O dir_index /dev/sda1
```

### 5. Add a journal to an ext2 filesystem
```bash
tune2fs -j /dev/sda1
```

## Tips
- Always ensure you have backups before modifying filesystem parameters.
- Use the `-l` option to review current settings before making changes.
- Be cautious when enabling or disabling features, as they can affect filesystem compatibility and performance.
- Regularly check the filesystem health using `fsck` in conjunction with `tune2fs` settings for optimal performance.