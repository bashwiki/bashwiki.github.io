# [리눅스] Bash realpath 사용법

## Overview
The `realpath` command in Bash is used to resolve and print the absolute path of a given file or directory. Its primary purpose is to convert relative paths into absolute paths, eliminating any symbolic links, `..`, or `.` components in the path. This is particularly useful for ensuring that scripts and applications reference files and directories in a consistent manner, regardless of the current working directory.

## Usage
The basic syntax of the `realpath` command is as follows:

```bash
realpath [OPTION]... FILE...
```

### Common Options:
- `-m`, `--canonicalize-missing`: This option allows `realpath` to return the canonicalized absolute pathname even if the file does not exist.
- `-q`, `--quiet`: Suppresses error messages about nonexistent files.
- `-s`, `--strip`: This option strips the trailing slashes from the output.

## Examples
### Example 1: Basic Usage
To convert a relative path to an absolute path, you can use the following command:

```bash
realpath ./myfolder/myfile.txt
```
This command will output the absolute path of `myfile.txt` located in `myfolder`, resolving any relative components.

### Example 2: Handling Nonexistent Files
If you want to get the absolute path of a file that may not exist, you can use the `-m` option:

```bash
realpath -m ./nonexistentfile.txt
```
This will return the absolute path for `nonexistentfile.txt` even though it does not exist, allowing you to handle paths dynamically in your scripts.

## Tips
- Always use `realpath` when dealing with file paths in scripts to avoid issues with relative paths, especially when the script may be executed from different directories.
- Combine `realpath` with other commands like `cd` or `ln` to ensure that you are always working with the correct file paths.
- Use the `-q` option if you want to suppress error messages in scripts that may encounter missing files, helping to keep your script output clean.