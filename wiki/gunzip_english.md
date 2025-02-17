# [Linux] Bash gunzip Uso: Decompress files compressed with gzip

## Overview
The `gunzip` command is used to decompress files that have been compressed using the `gzip` (GNU zip) compression algorithm. It restores the original files from their compressed `.gz` format, making them accessible for use.

## Usage
The basic syntax of the `gunzip` command is as follows:

```bash
gunzip [options] [arguments]
```

## Common Options
- `-c`: Write output to standard output and keep the original files.
- `-f`: Force decompression, even if the target files already exist.
- `-k`: Keep the original compressed files after decompression.
- `-r`: Recursively decompress files in directories.
- `-v`: Verbosely list the files processed.

## Common Examples

1. **Decompress a single file**:
   ```bash
   gunzip file.txt.gz
   ```

2. **Decompress and keep the original file**:
   ```bash
   gunzip -k file.txt.gz
   ```

3. **Decompress multiple files at once**:
   ```bash
   gunzip file1.gz file2.gz file3.gz
   ```

4. **Decompress all `.gz` files in a directory**:
   ```bash
   gunzip *.gz
   ```

5. **Decompress and display output to standard output**:
   ```bash
   gunzip -c file.txt.gz > file.txt
   ```

## Tips
- Always use the `-k` option if you want to keep the original compressed files for future use.
- Use the `-v` option for verbose output to see which files are being processed, especially when dealing with multiple files.
- If you are unsure about the contents of a `.gz` file, you can use `gunzip -c filename.gz | less` to view it without decompressing it to disk.