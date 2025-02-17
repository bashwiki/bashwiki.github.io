# [Linux] Bash cp Uso equivalente: Copy files and directories

The `cp` command is used to copy files and directories in Linux and Unix-like operating systems.

## Overview
The `cp` command stands for "copy." It allows users to duplicate files and directories from one location to another. This is a fundamental command for file management in the terminal.

## Usage
The basic syntax of the `cp` command is as follows:

```bash
cp [options] [source] [destination]
```

## Common Options
- `-r`: Recursively copy directories and their contents.
- `-i`: Prompt before overwriting files.
- `-u`: Copy only when the source file is newer than the destination file or when the destination file is missing.
- `-v`: Verbosely show the files being copied.
- `-a`: Archive mode; it preserves the attributes of files while copying.

## Common Examples
Here are some practical examples of how to use the `cp` command:

1. **Copy a single file:**
   ```bash
   cp file.txt /path/to/destination/
   ```

2. **Copy a directory recursively:**
   ```bash
   cp -r /path/to/source_directory/ /path/to/destination_directory/
   ```

3. **Copy a file and prompt before overwriting:**
   ```bash
   cp -i file.txt /path/to/destination/
   ```

4. **Copy only newer files:**
   ```bash
   cp -u file.txt /path/to/destination/
   ```

5. **Copy with verbose output:**
   ```bash
   cp -v file.txt /path/to/destination/
   ```

## Tips
- Always double-check the destination path to avoid accidental overwrites.
- Use the `-i` option when copying files to prevent overwriting important files unintentionally.
- For backing up directories, consider using the `-a` option to preserve file attributes and permissions.