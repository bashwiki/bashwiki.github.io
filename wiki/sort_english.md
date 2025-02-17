# [Linux] Bash sort uso: Sorts lines of text files

## Overview
The `sort` command in Bash is used to sort lines of text files. It organizes the input data in a specified order, which can be ascending or descending, and can handle both numerical and alphabetical sorting. This command is particularly useful for organizing data for easier reading or processing.

## Usage
The basic syntax of the `sort` command is as follows:

```bash
sort [options] [arguments]
```

## Common Options
Here are some common options you can use with the `sort` command:

- `-r`: Sort in reverse order (descending).
- `-n`: Sort numerically instead of alphabetically.
- `-k`: Sort based on a specific key (column).
- `-u`: Output only the first of an equal run (unique).
- `-o`: Write the result to a specified output file.

## Common Examples

1. **Sort a text file alphabetically:**
   ```bash
   sort filename.txt
   ```

2. **Sort a text file in reverse order:**
   ```bash
   sort -r filename.txt
   ```

3. **Sort numerically:**
   ```bash
   sort -n numbers.txt
   ```

4. **Sort based on a specific column (e.g., second column):**
   ```bash
   sort -k2 filename.txt
   ```

5. **Sort and save the output to a new file:**
   ```bash
   sort filename.txt -o sorted.txt
   ```

6. **Sort unique lines:**
   ```bash
   sort -u filename.txt
   ```

## Tips
- When sorting large files, consider using the `-S` option to specify the amount of memory to use for sorting.
- Combine `sort` with other commands like `uniq` to filter out duplicate lines after sorting.
- Use `cat` with `sort` for sorting the output of multiple files:
  ```bash
  cat file1.txt file2.txt | sort
  ```
- Always check the output with `head` or `tail` to ensure the sorting is as expected.