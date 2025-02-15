# [리눅스] Bash xz 사용법

## Overview
The `xz` command is a data compression tool that uses the LZMA (Lempel-Ziv-Markov chain algorithm) compression algorithm. It is primarily used to compress files and reduce their size for storage or transmission. The `xz` command is known for its high compression ratio, making it a popular choice for compressing large files, such as software packages and archives.

## Usage
The basic syntax of the `xz` command is as follows:

```bash
xz [OPTIONS] [FILE...]
```

### Common Options
- `-d`, `--decompress`: Decompress the specified file(s).
- `-k`, `--keep`: Keep the original file(s) after compression or decompression.
- `-f`, `--force`: Force compression or decompression, even if the output file already exists.
- `-z`, `--compress`: Compress the specified file(s) (this is the default action).
- `-t`, `--test`: Test the integrity of the compressed file(s).
- `-v`, `--verbose`: Provide detailed output during the compression or decompression process.

## Examples

### Example 1: Compressing a File
To compress a file named `example.txt`, you can use the following command:

```bash
xz example.txt
```

This will create a compressed file named `example.txt.xz` and remove the original `example.txt` file.

### Example 2: Decompressing a File
To decompress a previously compressed file, you can use:

```bash
xz -d example.txt.xz
```

This command will restore the original `example.txt` file and remove the compressed `example.txt.xz`.

## Tips
- If you want to keep the original file after compression, use the `-k` option. For example:

  ```bash
  xz -k example.txt
  ```

- To compress multiple files at once, list them all in the command:

  ```bash
  xz file1.txt file2.txt file3.txt
  ```

- Use the `-v` option for verbose output to monitor the progress of your compression or decompression tasks.

- To test the integrity of a compressed file without decompressing it, use the `-t` option:

  ```bash
  xz -t example.txt.xz
  ```

By following these guidelines, you can effectively use the `xz` command for file compression and decompression in your projects.