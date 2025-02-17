# [Linux] Bash uniq Usage: Remove duplicate lines from sorted files

## Overview
The `uniq` command in Bash is used to filter out repeated lines in a text file or input stream. It is particularly useful for processing sorted data, as it only removes consecutive duplicate lines.

## Usage
The basic syntax of the `uniq` command is as follows:

```bash
uniq [options] [arguments]
```

## Common Options
- `-c`: Precede each output line with the count of occurrences.
- `-d`: Only print duplicate lines.
- `-u`: Only print unique lines (non-duplicate).
- `-i`: Ignore case when comparing lines.
- `-w N`: Compare only the first N characters of each line.

## Common Examples

1. **Removing duplicates from a file:**
   To remove duplicate lines from a sorted file called `file.txt`:
   ```bash
   uniq file.txt
   ```

2. **Counting occurrences of each line:**
   To count how many times each line appears in `file.txt`:
   ```bash
   uniq -c file.txt
   ```

3. **Displaying only duplicate lines:**
   To show only the lines that are duplicated in `file.txt`:
   ```bash
   uniq -d file.txt
   ```

4. **Ignoring case:**
   To remove duplicates while ignoring case sensitivity:
   ```bash
   uniq -i file.txt
   ```

5. **Comparing a specific number of characters:**
   To compare only the first 5 characters of each line in `file.txt`:
   ```bash
   uniq -w 5 file.txt
   ```

## Tips
- Always sort your input before using `uniq`, as it only removes consecutive duplicates.
- You can combine `uniq` with other commands using pipes. For example, `cat file.txt | sort | uniq` will sort the file and then remove duplicates.
- Use the `-c` option to quickly identify which lines are most common in your data.