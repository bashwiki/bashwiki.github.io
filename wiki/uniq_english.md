# [리눅스] Bash uniq 사용법

## Overview
The `uniq` command in Bash is a utility that filters out repeated lines in a text file or standard input. Its primary purpose is to help users identify and remove duplicate lines, making it easier to process and analyze data. It is often used in conjunction with the `sort` command, as `uniq` only removes consecutive duplicate lines.

## Usage
The basic syntax of the `uniq` command is as follows:

```bash
uniq [OPTION]... [INPUT [OUTPUT]]
```

### Common Options
- `-c`: Precede each output line with the number of occurrences.
- `-d`: Only print duplicate lines.
- `-u`: Only print unique lines (lines that are not repeated).
- `-i`: Ignore case when comparing lines.
- `-w N`: Compare no more than N characters in lines.

## Examples

### Example 1: Removing Duplicate Lines
To remove duplicate lines from a sorted file called `data.txt`, you can use the following command:

```bash
sort data.txt | uniq
```
This command first sorts the lines in `data.txt`, and then `uniq` filters out any consecutive duplicate lines.

### Example 2: Counting Occurrences of Each Line
If you want to count how many times each line appears in a file, use the `-c` option:

```bash
sort data.txt | uniq -c
```
This will output each unique line preceded by the number of times it appears in the file.

## Tips
- Always sort your input before using `uniq` if you want to remove all duplicates, as `uniq` only removes consecutive duplicates.
- Use the `-i` option if you want to treat lines as identical regardless of case, which is useful for case-insensitive comparisons.
- Combine `uniq` with other commands like `grep` or `awk` for more complex data processing tasks.