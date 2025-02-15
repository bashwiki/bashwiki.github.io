# [리눅스] Bash diff 사용법

## Overview
The `diff` command in Bash is a powerful tool used to compare the contents of two files line by line. Its primary purpose is to identify differences between the files, which can be particularly useful for developers and engineers when reviewing changes in source code, configuration files, or any text-based documents. The output of `diff` highlights the lines that differ, making it easier to understand what has changed.

## Usage
The basic syntax of the `diff` command is as follows:

```bash
diff [options] file1 file2
```

### Common Options
- `-u`: Produces a unified diff, which shows a few lines of context around the changes, making it easier to read.
- `-c`: Generates a context diff, providing more context around the differences.
- `-i`: Ignores case differences in the file contents.
- `-w`: Ignores all white space when comparing lines.
- `-r`: Recursively compares any subdirectories found.

## Examples

### Example 1: Basic Comparison
To compare two text files, `file1.txt` and `file2.txt`, you can use the following command:

```bash
diff file1.txt file2.txt
```

This will output the lines that differ between the two files.

### Example 2: Unified Diff
If you want to see a unified diff, which provides context around the changes, you can use the `-u` option:

```bash
diff -u file1.txt file2.txt
```

The output will show the differences with a few lines of context, making it easier to understand the changes.

## Tips
- When working with source code, consider using the `-u` option to generate patches that can be easily applied with the `patch` command.
- Use the `-r` option when comparing directories to identify differences in multiple files at once.
- For large files, consider using `diff` in combination with `less` to paginate the output, like so:

```bash
diff file1.txt file2.txt | less
```

This allows you to scroll through the differences more comfortably.