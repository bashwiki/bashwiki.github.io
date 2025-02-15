# [리눅스] Bash tune2fs 사용법

## Overview
`tune2fs` is a command-line utility in Linux that allows users to adjust tunable filesystem parameters on ext2, ext3, and ext4 filesystems. Its primary purpose is to modify filesystem settings that can affect performance, reliability, and behavior without the need to unmount the filesystem. This tool is particularly useful for system administrators and developers who need to optimize filesystem performance or recover from issues.

## Usage
The basic syntax of the `tune2fs` command is as follows:

```bash
tune2fs [options] <device>
```

### Common Options
- `-c <mount-count>`: Set the maximum number of mounts before a filesystem check is forced.
- `-i <interval>`: Set the maximum time interval between filesystem checks.
- `-m <reserved-blocks>`: Set the percentage of the filesystem blocks reserved for the super-user.
- `-O <feature>`: Enable or disable specific filesystem features.
- `-L <label>`: Change the label of the filesystem.
- `-e <error-action>`: Set the action to take when an error is detected.

## Examples

### Example 1: Set Maximum Mount Count
To set the maximum number of mounts before a filesystem check is forced to 20, you can use the following command:

```bash
sudo tune2fs -c 20 /dev/sda1
```

### Example 2: Change Filesystem Label
To change the label of the filesystem on `/dev/sda1` to "MyData", you can execute:

```bash
sudo tune2fs -L MyData /dev/sda1
```

## Tips
- Always ensure that you have proper backups before making changes to filesystem parameters, as incorrect settings can lead to data loss or corruption.
- Use the `-l` option to list current filesystem parameters before making changes. This can help you understand the current configuration and decide what adjustments are necessary.
- Be cautious when modifying reserved blocks (`-m` option) as reducing this percentage too much can lead to performance issues for system processes that require reserved space.
- Consider scheduling regular filesystem checks using the `-i` option to maintain filesystem integrity over time.