# [Linux] Bash diff uso equivalente: Compare files line by line

## Overview
The `diff` command is a powerful utility in Bash that allows users to compare the contents of two files line by line. It outputs the differences between the files, making it easier to identify changes, additions, or deletions.

## Usage
The basic syntax of the `diff` command is as follows:

```bash
diff [options] [file1] [file2]
```

## Common Options
- `-u`: Outputs the differences in a unified format, which is easier to read.
- `-c`: Produces a context diff, showing a few lines of context around the changes.
- `-i`: Ignores case differences in the files.
- `-w`: Ignores all whitespace differences.
- `-r`: Compares directories recursively.

## Common Examples

1. **Basic Comparison**
   Compare two text files and display the differences.
   ```bash
   diff file1.txt file2.txt
   ```

2. **Unified Format**
   View the differences in a unified format for better readability.
   ```bash
   diff -u file1.txt file2.txt
   ```

3. **Context Diff**
   Show differences with context lines for clarity.
   ```bash
   diff -c file1.txt file2.txt
   ```

4. **Ignoring Case**
   Compare two files while ignoring case differences.
   ```bash
   diff -i file1.txt file2.txt
   ```

5. **Comparing Directories**
   Compare all files in two directories recursively.
   ```bash
   diff -r dir1/ dir2/
   ```

## Tips
- Always use the `-u` option when sharing diffs with others, as it provides a clearer view of changes.
- For large files, consider using `less` to paginate the output: 
  ```bash
  diff file1.txt file2.txt | less
  ```
- When working with version control systems, `diff` can be used to review changes before committing.