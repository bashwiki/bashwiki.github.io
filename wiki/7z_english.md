# [English] Bash 7z Usage: File compression and extraction tool

## Overview
The `7z` command is a powerful file archiving tool that allows users to compress and extract files in various formats. It is part of the 7-Zip software suite and is known for its high compression ratios and support for a wide range of archive formats.

## Usage
The basic syntax of the `7z` command is as follows:

```bash
7z [options] [arguments]
```

## Common Options
- `a`: Add files to an archive.
- `x`: Extract files from an archive.
- `t`: Test the integrity of an archive.
- `l`: List the contents of an archive.
- `d`: Delete files from an archive.
- `u`: Update files in an archive.

## Common Examples

### Compressing Files
To create a new archive named `archive.7z` containing all files in the current directory:

```bash
7z a archive.7z *
```

### Extracting Files
To extract the contents of `archive.7z` into the current directory:

```bash
7z x archive.7z
```

### Listing Archive Contents
To list the files contained in `archive.7z` without extracting them:

```bash
7z l archive.7z
```

### Testing an Archive
To check the integrity of `archive.7z`:

```bash
7z t archive.7z
```

### Deleting Files from an Archive
To remove a specific file named `file.txt` from `archive.7z`:

```bash
7z d archive.7z file.txt
```

## Tips
- Always check the integrity of your archives with the `t` option after creating them to ensure they are not corrupted.
- Use the `-p` option followed by a password to create encrypted archives for sensitive data.
- For large files, consider using the `-mx` option to set the compression level, where `-mx=9` provides the highest compression ratio.