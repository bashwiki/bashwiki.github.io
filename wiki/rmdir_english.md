# [리눅스] Bash rmdir 사용법

## Overview
The `rmdir` command in Bash is used to remove empty directories from the filesystem. Its primary purpose is to help users manage their directory structure by deleting directories that are no longer needed, provided that these directories do not contain any files or subdirectories. If a directory is not empty, `rmdir` will not delete it and will return an error message.

## Usage
The basic syntax for the `rmdir` command is as follows:

```bash
rmdir [OPTION]... DIRECTORY...
```

### Common Options
- `-p`, `--parents`: Remove the DIRECTORY and its parent directories if they become empty after the removal.
- `--ignore-fail-on-non-empty`: Do not report an error if the directory is not empty.

## Examples

### Example 1: Removing a Single Empty Directory
To remove a single empty directory named `mydir`, you would use the following command:

```bash
rmdir mydir
```

If `mydir` is empty, it will be removed successfully. If it contains files or subdirectories, you will receive an error message.

### Example 2: Removing a Directory and Its Parents
If you want to remove a directory and its parent directories (if they are also empty), you can use the `-p` option. For example:

```bash
rmdir -p parentdir/childdir
```

This command will remove `childdir` and, if `parentdir` is empty after removing `childdir`, it will also remove `parentdir`.

## Tips
- Always ensure that the directory you want to remove is empty before using `rmdir`, as it will not delete non-empty directories.
- Use the `-p` option with caution, as it can remove multiple directories in one command if they are empty.
- To check if a directory is empty before attempting to remove it, you can use the `ls` command:

```bash
ls -A mydir
```

If this command returns no output, the directory is empty and safe to remove with `rmdir`.