# [리눅스] Bash mv 사용법

## Overview
The `mv` command in Bash is a fundamental utility used for moving and renaming files and directories within a filesystem. Its primary purpose is to transfer files from one location to another or to change the name of a file or directory. The `mv` command is essential for file management in Unix-like operating systems.

## Usage
The basic syntax of the `mv` command is as follows:

```bash
mv [options] source destination
```

### Common Options:
- `-i`: Prompts before overwriting an existing file.
- `-u`: Moves only when the source file is newer than the destination file or when the destination file is missing.
- `-v`: Verbose mode; displays detailed information about the move operation.
- `-n`: Prevents overwriting of existing files (no clobber).

## Examples

### Example 1: Moving a File
To move a file named `example.txt` from the current directory to a directory called `documents`, you would use:

```bash
mv example.txt documents/
```

### Example 2: Renaming a File
To rename a file from `oldname.txt` to `newname.txt`, you can use:

```bash
mv oldname.txt newname.txt
```

### Example 3: Moving with Prompt
If you want to move a file and be prompted before overwriting any existing file, use the `-i` option:

```bash
mv -i example.txt documents/
```

## Tips
- Always use the `-i` option if you are unsure whether the destination file exists, as it helps prevent accidental data loss.
- Use the `-v` option for a clearer understanding of what the command is doing, especially when moving multiple files.
- When moving directories, ensure you have the necessary permissions to avoid permission denied errors.
- To avoid confusion, always specify the full path for both the source and destination when working with files in different directories.