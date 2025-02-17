# [Linux] Bash mv uso equivalente: Move or rename files and directories

## Overview
The `mv` command in Bash is used to move or rename files and directories. It allows users to change the location of a file or folder, or to give it a new name within the same directory.

## Usage
The basic syntax of the `mv` command is as follows:

```bash
mv [options] [source] [destination]
```

- **source**: The file or directory you want to move or rename.
- **destination**: The new location or name for the file or directory.

## Common Options
- `-i`: Prompts before overwriting an existing file.
- `-u`: Moves only when the source file is newer than the destination file or when the destination file does not exist.
- `-v`: Verbose mode; shows what is being done.
- `-n`: No overwrite; does not overwrite an existing file.

## Common Examples
1. **Moving a file to a different directory:**
   ```bash
   mv myfile.txt /home/user/documents/
   ```

2. **Renaming a file:**
   ```bash
   mv oldname.txt newname.txt
   ```

3. **Moving and renaming a file:**
   ```bash
   mv myfile.txt /home/user/documents/newfile.txt
   ```

4. **Moving multiple files to a directory:**
   ```bash
   mv file1.txt file2.txt /home/user/documents/
   ```

5. **Using the interactive option to avoid overwriting:**
   ```bash
   mv -i myfile.txt /home/user/documents/
   ```

## Tips
- Always use the `-i` option if you are unsure about overwriting files, as it helps prevent accidental data loss.
- Use `-v` to see a detailed output of the operation, which can be helpful for tracking what files are being moved or renamed.
- When moving files across different file systems, be aware that `mv` may copy and then delete the original file, which can take longer than moving files within the same file system.