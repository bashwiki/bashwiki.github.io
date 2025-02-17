# [Linux] Bash egrep Uso equivalente: Search for patterns in files

## Overview
The `egrep` command is an extended version of `grep` that allows for more complex pattern matching using regular expressions. It is commonly used to search through text files for lines that match a specified pattern, making it a powerful tool for text processing.

## Usage
The basic syntax of the `egrep` command is as follows:

```
egrep [options] [arguments]
```

## Common Options
- `-i`: Ignore case distinctions in patterns and input data.
- `-v`: Invert the match, showing lines that do not match the pattern.
- `-c`: Count the number of lines that match the pattern.
- `-n`: Show line numbers along with matching lines.
- `-r` or `-R`: Recursively search through directories.

## Common Examples
Here are some practical examples of using `egrep`:

1. **Basic pattern search in a file:**
   ```bash
   egrep "error" logfile.txt
   ```
   This command searches for the word "error" in `logfile.txt`.

2. **Case-insensitive search:**
   ```bash
   egrep -i "warning" logfile.txt
   ```
   This command searches for "warning" in `logfile.txt`, ignoring case.

3. **Count matching lines:**
   ```bash
   egrep -c "success" logfile.txt
   ```
   This command counts how many lines contain the word "success".

4. **Show line numbers with matches:**
   ```bash
   egrep -n "failed" logfile.txt
   ```
   This command displays lines containing "failed" along with their line numbers.

5. **Recursive search in a directory:**
   ```bash
   egrep -r "TODO" /path/to/directory/
   ```
   This command searches for "TODO" in all files within the specified directory and its subdirectories.

## Tips
- Use quotes around your search pattern to avoid shell interpretation of special characters.
- Combine `egrep` with other commands using pipes for more complex data processing.
- Regular expressions can be very powerful; take time to learn their syntax for more advanced searches.