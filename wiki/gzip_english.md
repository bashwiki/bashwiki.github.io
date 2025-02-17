# [Linux] Bash gzip Usage: Compress and decompress files

## Overview
The `gzip` command is a widely used utility in Unix-like operating systems for compressing files. It reduces the size of files to save disk space and speed up file transfers. The compressed files typically have a `.gz` extension.

## Usage
The basic syntax of the `gzip` command is as follows:

```bash
gzip [options] [arguments]
```

## Common Options
- `-d`, `--decompress`: Decompress the specified file.
- `-k`, `--keep`: Keep the original file after compression.
- `-r`, `--recursive`: Compress files in the specified directory and its subdirectories.
- `-v`, `--verbose`: Display the compression ratio and other details during the process.
- `-f`, `--force`: Force compression or decompression, even if the file already exists.

## Common Examples
1. **Compress a single file:**
   ```bash
   gzip filename.txt
   ```
   This command compresses `filename.txt` and creates `filename.txt.gz`.

2. **Decompress a file:**
   ```bash
   gzip -d filename.txt.gz
   ```
   This command decompresses `filename.txt.gz` back to `filename.txt`.

3. **Compress multiple files:**
   ```bash
   gzip file1.txt file2.txt file3.txt
   ```
   This command compresses `file1.txt`, `file2.txt`, and `file3.txt` into their respective `.gz` files.

4. **Keep the original file after compression:**
   ```bash
   gzip -k filename.txt
   ```
   This command compresses `filename.txt` but retains the original file.

5. **Compress files in a directory recursively:**
   ```bash
   gzip -r /path/to/directory
   ```
   This command compresses all files in the specified directory and its subdirectories.

## Tips
- Use the `-v` option to monitor the compression process and see how much space you are saving.
- When decompressing, you can use the `-f` option to overwrite existing files without prompt.
- Consider using `tar` in conjunction with `gzip` for archiving and compressing multiple files into a single `.tar.gz` file.