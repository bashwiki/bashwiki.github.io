# [Linux] Bash stat Usage: Display file or file system status

## Overview
The `stat` command in Bash is used to display detailed information about files or file systems. It provides various attributes such as file size, permissions, last access time, and modification time, which can be useful for monitoring and managing files.

## Usage
The basic syntax of the `stat` command is as follows:

```bash
stat [options] [arguments]
```

## Common Options
- `-c, --format=FORMAT`: Specify the output format using a format string.
- `-f, --file-system`: Display information about the file system instead of the file.
- `-t, --terse`: Display the output in a terse format.
- `--help`: Display help information about the command.
- `--version`: Show the version of the stat command.

## Common Examples

1. **Basic File Information**
   To display detailed information about a specific file:
   ```bash
   stat filename.txt
   ```

2. **Custom Format Output**
   To display specific attributes using a custom format:
   ```bash
   stat -c '%s %y' filename.txt
   ```
   This will show the file size and last modification time.

3. **File System Information**
   To get information about the file system where a file is located:
   ```bash
   stat -f filename.txt
   ```

4. **Terse Output**
   For a more concise output:
   ```bash
   stat -t filename.txt
   ```

5. **Multiple Files**
   To check the status of multiple files at once:
   ```bash
   stat file1.txt file2.txt file3.txt
   ```

## Tips
- Use the `--format` option to customize the output to display only the information you need.
- Combine `stat` with other commands like `grep` or `awk` for advanced processing of file information.
- Regularly check file permissions and modification times to maintain security and data integrity.