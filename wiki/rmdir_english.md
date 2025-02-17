# [Linux] Bash rmdir Uso: Remove empty directories

## Overview
The `rmdir` command is used in Bash to remove empty directories from the filesystem. If the directory contains files or other directories, the command will not execute and will return an error message.

## Usage
The basic syntax of the `rmdir` command is as follows:

```bash
rmdir [options] [arguments]
```

## Common Options
- `-p` : Remove parent directories if they become empty after the removal of the specified directory.
- `--ignore-fail-on-non-empty` : Do not report an error if the directory is not empty.

## Common Examples

1. **Remove a single empty directory:**
   ```bash
   rmdir my_empty_directory
   ```

2. **Remove multiple empty directories:**
   ```bash
   rmdir dir1 dir2 dir3
   ```

3. **Remove a directory and its empty parent directories:**
   ```bash
   rmdir -p parent_dir/child_dir
   ```

4. **Ignore errors for non-empty directories:**
   ```bash
   rmdir --ignore-fail-on-non-empty my_non_empty_directory
   ```

## Tips
- Always ensure that the directory is empty before using `rmdir`, as it will not remove directories that contain files or other directories.
- Use the `-p` option carefully, as it will remove parent directories if they become empty after the specified directory is removed.
- Consider using `rm -r` if you need to remove a directory and all its contents, but be cautious as this command is irreversible.