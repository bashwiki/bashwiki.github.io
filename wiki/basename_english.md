# [리눅스] Bash basename 사용법

## Overview
The `basename` command in Bash is used to strip the directory and suffix from filenames. Its primary purpose is to extract the actual file name from a full path, making it easier to work with file names in scripts and command-line operations. This is particularly useful when you need to manipulate or display just the name of a file without its preceding path.

## Usage
The basic syntax of the `basename` command is as follows:

```bash
basename [OPTION]... NAME [SUFFIX]
```

### Common Options:
- `NAME`: The full path of the file from which you want to extract the base name.
- `SUFFIX`: An optional argument that allows you to remove a specified suffix from the base name.

## Examples
Here are a couple of practical examples demonstrating how to use the `basename` command:

### Example 1: Basic Usage
To extract the base name from a full file path:

```bash
$ basename /usr/local/bin/script.sh
script.sh
```
In this example, `basename` takes the full path `/usr/local/bin/script.sh` and returns just `script.sh`.

### Example 2: Removing a Suffix
To remove a specified suffix from the base name:

```bash
$ basename /usr/local/bin/script.sh .sh
script
```
Here, `basename` not only extracts the base name but also removes the `.sh` suffix, resulting in just `script`.

## Tips
- When using `basename`, ensure that you provide the correct path to avoid confusion, especially when working with symbolic links or relative paths.
- If you need to handle multiple files, consider using a loop in your script to apply `basename` to each file individually.
- Combine `basename` with other commands like `find` or `ls` to create powerful scripts that manipulate file names effectively.

By understanding and utilizing the `basename` command, you can streamline file name handling in your Bash scripts and command-line operations.