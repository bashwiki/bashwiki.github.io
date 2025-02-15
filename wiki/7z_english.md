# [리눅스] Bash 7z 사용법

## Overview
The `7z` command is a powerful file archiving tool that is part of the 7-Zip software suite. It is widely used for compressing and decompressing files and directories, supporting a variety of archive formats. The primary purpose of `7z` is to create compressed archives to save disk space and facilitate file transfer, while also allowing users to extract files from existing archives.

## Usage
The basic syntax of the `7z` command is as follows:

```
7z [command] [options] [archive] [files...]
```

### Common Options
- `a`: Add files to an archive.
- `x`: Extract files from an archive.
- `t`: Test the integrity of an archive.
- `l`: List the contents of an archive.
- `d`: Delete files from an archive.
- `-p`: Set a password for the archive.
- `-m`: Specify the compression method (e.g., `-mx=9` for maximum compression).

## Examples

### Example 1: Creating a Compressed Archive
To create a compressed archive named `example.7z` containing all `.txt` files in the current directory, you would use the following command:

```bash
7z a example.7z *.txt
```

### Example 2: Extracting Files from an Archive
To extract the contents of an archive named `example.7z` into the current directory, the command would be:

```bash
7z x example.7z
```

## Tips
- When creating archives, consider using the `-mx` option to specify the level of compression according to your needs. Higher compression levels reduce file size but may increase processing time.
- Use the `-p` option to secure your archives with a password, especially when dealing with sensitive data.
- Regularly test your archives using the `t` command to ensure their integrity and prevent data loss.
- Familiarize yourself with the various compression formats supported by `7z`, such as `.zip`, `.tar`, and `.gzip`, to choose the best one for your use case.