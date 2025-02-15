# [리눅스] Bash unxz 사용법

## Overview
The `unxz` command is a utility in Unix-like operating systems used to decompress files that have been compressed using the XZ compression algorithm. The primary purpose of `unxz` is to restore the original file from its compressed state, making it accessible for further use. It is particularly useful for handling large files efficiently, as XZ compression is known for its high compression ratio.

## Usage
The basic syntax of the `unxz` command is as follows:

```bash
unxz [OPTION]... [FILE]...
```

### Common Options
- `-k`, `--keep`: Keep the input files (do not delete them after decompression).
- `-f`, `--force`: Force overwrite of output files without prompting.
- `-v`, `--verbose`: Provide detailed output during the decompression process.
- `-t`, `--test`: Test the integrity of the compressed file without decompressing it.
- `--help`: Display help information about the command and its options.
- `--version`: Show the version information of the `unxz` command.

## Examples
### Example 1: Basic Decompression
To decompress a file named `example.xz`, you can use the following command:

```bash
unxz example.xz
```

This command will decompress `example.xz` and remove the original compressed file, resulting in a file named `example`.

### Example 2: Keeping the Original File
If you want to keep the original compressed file after decompression, you can use the `-k` option:

```bash
unxz -k example.xz
```

In this case, both `example.xz` and the decompressed file `example` will remain in the directory.

## Tips
- Always check the integrity of the compressed file before decompression using the `-t` option. This can help prevent data loss if the file is corrupted.
- Use the `-v` option for verbose output if you are working with multiple files or large datasets. This can provide useful feedback on the progress of the decompression.
- For batch processing, consider using wildcards (e.g., `*.xz`) to decompress multiple files at once, but be cautious about the `-f` option to avoid unintentional overwrites.