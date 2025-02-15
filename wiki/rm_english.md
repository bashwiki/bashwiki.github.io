# [리눅스] Bash rm 사용법

## Overview
The `rm` command in Bash is used to remove files and directories from the filesystem. Its primary purpose is to delete unwanted files, freeing up space and maintaining an organized directory structure. However, it is important to use this command with caution, as deleted files are not easily recoverable.

## Usage
The basic syntax of the `rm` command is as follows:

```bash
rm [OPTION]... [FILE]...
```

### Common Options:
- `-f`: Forcefully remove files without prompting for confirmation, even if the files are write-protected.
- `-i`: Prompt for confirmation before each file is removed. This is useful for preventing accidental deletions.
- `-r` or `-R`: Recursively remove directories and their contents. This option is necessary when you want to delete a directory that contains files or other directories.
- `-v`: Verbosely display the names of files as they are being removed. This can help in tracking which files are being deleted.

## Examples
### Example 1: Removing a Single File
To remove a file named `example.txt`, you would use the following command:

```bash
rm example.txt
```

### Example 2: Recursively Removing a Directory
To remove a directory named `old_folder` and all of its contents, you would use:

```bash
rm -r old_folder
```

If you want to ensure that you are prompted for confirmation before each file is deleted, you can combine options:

```bash
rm -ri old_folder
```

## Tips
- Always double-check the files you are about to delete, especially when using the `-f` option, to avoid accidental data loss.
- Consider using the `-i` option when running `rm` on important files or directories to add an extra layer of safety.
- For critical files, consider backing them up before deletion, as recovery can be difficult or impossible after using `rm`.
- Use the `-v` option to keep track of the deletion process, especially when removing multiple files or directories.