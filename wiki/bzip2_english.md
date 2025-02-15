# [리눅스] Bash bzip2 사용법

## Overview
The `bzip2` command is a widely used data compression utility in Unix-like operating systems. Its primary purpose is to compress files to save disk space and reduce the time required for file transfers. `bzip2` uses the Burrows-Wheeler block sorting text compression algorithm, which generally provides better compression ratios compared to other compression tools like `gzip`. The output of `bzip2` is a file with a `.bz2` extension.

## Usage
The basic syntax for the `bzip2` command is as follows:

```bash
bzip2 [OPTION]... [FILE]...
```

### Common Options
- `-d`, `--decompress`: Decompress the specified `.bz2` file.
- `-k`, `--keep`: Keep the original file after compression or decompression.
- `-f`, `--force`: Force compression or decompression, even if the output file already exists.
- `-v`, `--verbose`: Print the name of each file processed.
- `-1` to `-9`: Set the compression level, where `-1` is the fastest with less compression and `-9` is the slowest with maximum compression.

## Examples

### Example 1: Compressing a File
To compress a file named `example.txt`, you would use the following command:

```bash
bzip2 example.txt
```

This command will create a compressed file named `example.txt.bz2` and remove the original `example.txt` file.

### Example 2: Decompressing a File
To decompress a previously compressed file named `example.txt.bz2`, use the following command:

```bash
bzip2 -d example.txt.bz2
```

This will restore the original file `example.txt` and remove the compressed file `example.txt.bz2`.

## Tips
- When working with large files, consider using the `-k` option to keep the original file until you verify the compression was successful.
- For batch processing, you can compress multiple files at once by listing them:

```bash
bzip2 file1.txt file2.txt file3.txt
```

- To check the compression ratio of a file, you can use the `-v` option during compression, which will provide detailed information about the process.
- If you need to decompress files in a directory, you can use a wildcard:

```bash
bzip2 -d *.bz2
```

By following these guidelines, you can effectively use the `bzip2` command to manage file compression and decompression in your projects.