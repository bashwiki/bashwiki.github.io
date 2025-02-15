# [리눅스] Bash gzip 사용법

## Overview
The `gzip` command is a widely used utility in Unix-like operating systems for file compression. Its primary purpose is to reduce the size of files, making them easier to store and transfer. `gzip` uses the DEFLATE algorithm, which is a combination of LZ77 and Huffman coding, to achieve efficient compression. It is particularly useful for compressing text files, such as logs or source code, and is often employed in conjunction with other commands in shell scripts.

## Usage
The basic syntax of the `gzip` command is as follows:

```bash
gzip [OPTION]... [FILE]...
```

### Common Options
- `-d`, `--decompress`: Decompress the specified files.
- `-k`, `--keep`: Keep the original files after compression.
- `-r`, `--recursive`: Compress files in the specified directory and its subdirectories.
- `-v`, `--verbose`: Display the name of each file processed.
- `-f`, `--force`: Force compression or decompression, even if the file already exists.

## Examples

### Example 1: Compressing a File
To compress a file named `example.txt`, you can use the following command:

```bash
gzip example.txt
```
This will create a compressed file named `example.txt.gz` and remove the original `example.txt`.

### Example 2: Decompressing a File
To decompress the previously compressed file, you can use:

```bash
gzip -d example.txt.gz
```
This command will restore the original `example.txt` from the compressed file and remove `example.txt.gz`.

## Tips
- When compressing multiple files, you can specify them all in one command, like so:

  ```bash
  gzip file1.txt file2.txt file3.txt
  ```

- If you want to keep the original files while compressing, use the `-k` option:

  ```bash
  gzip -k example.txt
  ```

- For better compression ratios, you can use the `-9` option to specify the highest level of compression:

  ```bash
  gzip -9 example.txt
  ```

- When working with directories, the `-r` option can be very useful to compress all files within a directory:

  ```bash
  gzip -r my_directory/
  ```

By understanding and utilizing the `gzip` command effectively, you can manage file sizes and optimize storage and transfer processes in your development workflows.