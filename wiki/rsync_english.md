# [리눅스] Bash rsync 사용법

## Overview
`rsync` is a powerful file transfer and synchronization tool commonly used in Unix-like operating systems. Its primary purpose is to efficiently copy and synchronize files and directories between two locations, which can be on the same machine or across a network. `rsync` is particularly known for its ability to transfer only the differences between source and destination files, making it faster and more efficient than traditional copy commands.

## Usage
The basic syntax for the `rsync` command is as follows:

```bash
rsync [OPTION]... SRC [SRC]... DEST
```

### Common Options:
- `-a` or `--archive`: Enables archive mode, which preserves permissions, timestamps, symbolic links, and other file attributes.
- `-v` or `--verbose`: Provides detailed output of the transfer process.
- `-z` or `--compress`: Compresses file data during the transfer for faster transmission over the network.
- `-r` or `--recursive`: Recursively copies directories and their contents.
- `-u` or `--update`: Skips files that are newer on the destination.
- `-e` or `--rsh=COMMAND`: Specifies the remote shell to use, allowing for secure transfers over SSH.
- `--delete`: Deletes files in the destination that are no longer present in the source.

## Examples
### Example 1: Basic File Synchronization
To synchronize a local directory (`/path/to/source/`) with a remote directory (`user@remote:/path/to/destination/`), you can use the following command:

```bash
rsync -avz /path/to/source/ user@remote:/path/to/destination/
```
This command will copy all files and directories from the source to the destination, preserving their attributes and compressing the data during transfer.

### Example 2: Synchronizing with Deletion
If you want to ensure that the destination directory mirrors the source directory exactly, including deleting files that no longer exist in the source, you can use:

```bash
rsync -av --delete /path/to/source/ user@remote:/path/to/destination/
```
This command will synchronize the files and also remove any files in the destination that are not present in the source.

## Tips
- Always use the `-n` or `--dry-run` option when testing your `rsync` commands. This will simulate the transfer without making any changes, allowing you to verify what will happen before executing the command.
  
  ```bash
  rsync -avn /path/to/source/ user@remote:/path/to/destination/
  ```

- When working with large datasets or over slow networks, consider using the `-z` option to compress data, which can significantly reduce transfer times.

- For regular backups, consider using `rsync` in a cron job to automate the synchronization process at scheduled intervals.

- Be cautious with the `--delete` option, as it can lead to data loss if not used carefully. Always ensure you have backups of important data before performing deletions.