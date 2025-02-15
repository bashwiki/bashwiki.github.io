# [리눅스] Bash cp 사용법

## Overview
The `cp` command in Bash is used to copy files and directories from one location to another. Its primary purpose is to create duplicates of files or directories, allowing users to manage their data more effectively. This command is essential for tasks such as backing up files, organizing data, and transferring files between directories.

## Usage
The basic syntax of the `cp` command is as follows:

```bash
cp [options] source destination
```

### Common Options
- `-r` or `--recursive`: This option is used to copy directories recursively. It allows you to copy an entire directory along with its contents.
- `-i` or `--interactive`: Prompts the user before overwriting files. This is useful for preventing accidental data loss.
- `-u` or `--update`: Copies only when the source file is newer than the destination file or when the destination file is missing.
- `-v` or `--verbose`: Provides detailed output of the copy process, showing the files being copied.
- `-a` or `--archive`: This option preserves the attributes of the files being copied, such as timestamps and permissions, and is equivalent to using `-dR --preserve=all`.

## Examples
### Example 1: Copying a Single File
To copy a file named `file1.txt` to a new file named `file2.txt`, you would use the following command:

```bash
cp file1.txt file2.txt
```

### Example 2: Copying a Directory Recursively
To copy a directory named `myfolder` and all its contents to a new directory named `myfolder_backup`, you would use:

```bash
cp -r myfolder myfolder_backup
```

## Tips
- Always use the `-i` option when copying files if you're unsure whether the destination file exists. This will help prevent accidental overwrites.
- Use the `-v` option to monitor the progress of your copy operations, especially when dealing with large files or directories.
- When copying files between different file systems, consider using the `-a` option to preserve file attributes.
- For large-scale file copying, consider using `rsync` as it provides more features and options for synchronization and transfer.