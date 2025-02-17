# [Linux] Bash command cp: Copy files and directories

## Overview
The `cp` command in Bash is used to copy files and directories from one location to another. It allows users to duplicate files, preserving their contents and attributes, and can also be used to create backups.

## Usage
The basic syntax of the `cp` command is as follows:

```bash
cp [options] [source] [destination]
```

## Common Options
- `-r` or `--recursive`: Copy directories recursively.
- `-i` or `--interactive`: Prompt before overwriting files.
- `-u` or `--update`: Copy only when the source file is newer than the destination file or when the destination file is missing.
- `-v` or `--verbose`: Show the files being copied.
- `-a` or `--archive`: Preserve the original file attributes (like timestamps and permissions) while copying.

## Common Examples
1. **Copy a single file:**
   ```bash
   cp file.txt /path/to/destination/
   ```

2. **Copy a directory recursively:**
   ```bash
   cp -r /path/to/source_directory /path/to/destination_directory/
   ```

3. **Copy a file with confirmation before overwriting:**
   ```bash
   cp -i file.txt /path/to/destination/
   ```

4. **Copy only newer files:**
   ```bash
   cp -u file.txt /path/to/destination/
   ```

5. **Copy a file and show the progress:**
   ```bash
   cp -v file.txt /path/to/destination/
   ```

## Tips
- Always use the `-i` option if you're unsure whether the destination file exists to avoid accidental overwrites.
- When copying large directories, consider using the `-v` option to monitor the progress of the operation.
- Use the `-a` option when you want to maintain the original file attributes, especially when backing up files.