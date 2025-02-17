# [Linux] Bash unxz Usage: Decompress .xz files

## Overview
The `unxz` command is a utility used in Unix-like operating systems to decompress files that have been compressed using the XZ compression algorithm. This command is particularly useful for handling files with the `.xz` extension, allowing users to easily extract the original data from compressed archives.

## Usage
The basic syntax of the `unxz` command is as follows:

```bash
unxz [options] [arguments]
```

## Common Options
- `-k`, `--keep`: Keep the original `.xz` file after decompression.
- `-f`, `--force`: Force overwrite of existing files without prompting.
- `-v`, `--verbose`: Provide detailed output during the decompression process.
- `-h`, `--help`: Display help information about the command and its options.

## Common Examples
Here are some practical examples of using the `unxz` command:

1. **Decompress a single file**:
   ```bash
   unxz file.xz
   ```
   This command decompresses `file.xz`, resulting in `file`.

2. **Decompress multiple files**:
   ```bash
   unxz file1.xz file2.xz
   ```
   This command decompresses both `file1.xz` and `file2.xz`.

3. **Keep the original file**:
   ```bash
   unxz -k file.xz
   ```
   This command decompresses `file.xz` while keeping the original compressed file intact.

4. **Force decompression**:
   ```bash
   unxz -f file.xz
   ```
   This command decompresses `file.xz`, overwriting any existing file with the same name without prompting.

5. **Verbose output**:
   ```bash
   unxz -v file.xz
   ```
   This command provides detailed information about the decompression process.

## Tips
- Always check the contents of a `.xz` file before decompression to avoid overwriting important files.
- Use the `-k` option if you want to retain the original compressed file for backup purposes.
- For batch processing, consider using wildcards (e.g., `*.xz`) to decompress multiple files at once.