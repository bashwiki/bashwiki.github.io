# [리눅스] Bash stat 사용법

## Overview
The `stat` command in Bash is used to display detailed information about files and file systems. Its primary purpose is to provide metadata such as file size, permissions, ownership, and timestamps (creation, modification, and access times). This command is particularly useful for developers and system administrators who need to analyze file properties for debugging, monitoring, or auditing purposes.

## Usage
The basic syntax of the `stat` command is as follows:

```bash
stat [OPTION]... [FILE]...
```

### Common Options
- `-c`, `--format=FORMAT`: Use the specified format for output. You can define your own format string.
- `-f`, `--file-system`: Display file system status instead of file status.
- `-L`, `--dereference`: Follow symbolic links and display information about the target file.
- `-t`, `--terse`: Output in a terse format, which is more suitable for scripts.
- `--help`: Display help information about the command.
- `--version`: Show the version of the `stat` command.

## Examples
### Example 1: Basic File Information
To display detailed information about a specific file, you can use:

```bash
stat example.txt
```

This command will output information such as the file size, permissions, and timestamps for `example.txt`.

### Example 2: Custom Format Output
To customize the output format, you can use the `-c` option. For example, to display just the file size and last modification time, you can run:

```bash
stat -c "Size: %s bytes, Last Modified: %y" example.txt
```

This will output the size in bytes and the last modified date in a user-friendly format.

## Tips
- When using `stat` in scripts, consider using the `-t` option for a more concise output that is easier to parse.
- If you frequently need specific information, create a custom format string to streamline your workflow.
- Use the `--dereference` option if you want to get information about the target of a symbolic link rather than the link itself.
- Combine `stat` with other commands like `grep` or `awk` for advanced processing of file information in scripts.

By understanding and utilizing the `stat` command effectively, you can gain valuable insights into file properties and improve your file management tasks in a Linux environment.