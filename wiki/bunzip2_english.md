# [리눅스] Bash bunzip2 사용법

## Overview
`bunzip2` is a command-line utility in Unix-like operating systems used for decompressing files that have been compressed using the `bzip2` compression algorithm. Its primary purpose is to restore files that were previously compressed, allowing users to access the original data. The `bunzip2` command is often used in scenarios where large files need to be reduced in size for storage or transfer, and later need to be decompressed for use.

## Usage
The basic syntax for the `bunzip2` command is as follows:

```bash
bunzip2 [options] [file...]
```

### Common Options:
- `-k`, `--keep`: Keep the original compressed file after decompression.
- `-f`, `--force`: Force decompression, even if the output file already exists.
- `-v`, `--verbose`: Provide detailed information about the decompression process.
- `-h`, `--help`: Display help information about the command and its options.

## Examples

### Example 1: Basic Decompression
To decompress a single file named `example.bz2`, you can use the following command:

```bash
bunzip2 example.bz2
```
This command will decompress `example.bz2` and remove the compressed file, leaving you with `example`.

### Example 2: Keeping the Original File
If you want to decompress a file but keep the original compressed version, you can use the `-k` option:

```bash
bunzip2 -k example.bz2
```
This command will create `example` from `example.bz2` while retaining the original `example.bz2` file.

## Tips
- Always check the available disk space before decompressing large files, as the decompressed files may require significantly more space than their compressed counterparts.
- Use the `-v` option to monitor the progress and get insights into the decompression process, especially when working with large files.
- If you encounter issues with existing files, consider using the `-f` option to overwrite them if necessary.
- For batch decompression, you can specify multiple files at once, like so:

```bash
bunzip2 file1.bz2 file2.bz2 file3.bz2
```

This will decompress all specified files in one command.