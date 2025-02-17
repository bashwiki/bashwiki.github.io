# [Linux] Bash grep Usage: Search for patterns in text

## Overview
The `grep` command is a powerful text search utility in Unix/Linux systems. It allows users to search for specific patterns within files or input streams, making it an essential tool for developers, system administrators, and anyone working with text data.

## Usage
The basic syntax of the `grep` command is as follows:

```bash
grep [options] [pattern] [file...]
```

## Common Options
- `-i`: Ignore case distinctions in both the pattern and the input files.
- `-v`: Invert the match, showing only lines that do not match the pattern.
- `-r` or `-R`: Recursively search through directories.
- `-n`: Show line numbers along with matching lines.
- `-l`: List only the names of files with matching lines, not the lines themselves.
- `-c`: Count the number of matching lines instead of displaying them.

## Common Examples
Here are some practical examples of using `grep`:

1. **Basic search in a file**:
   ```bash
   grep "error" logfile.txt
   ```
   This command searches for the term "error" in `logfile.txt` and displays all matching lines.

2. **Case-insensitive search**:
   ```bash
   grep -i "warning" logfile.txt
   ```
   This will find "warning", "Warning", "WARNING", etc., in `logfile.txt`.

3. **Search recursively in a directory**:
   ```bash
   grep -r "TODO" /path/to/project/
   ```
   This command searches for the term "TODO" in all files within the specified directory and its subdirectories.

4. **Count matching lines**:
   ```bash
   grep -c "success" logfile.txt
   ```
   This will output the number of lines that contain the word "success" in `logfile.txt`.

5. **Show line numbers with matches**:
   ```bash
   grep -n "main" source.c
   ```
   This command will display the line numbers along with lines containing "main" in `source.c`.

## Tips
- Use `grep` in combination with other commands using pipes to filter output effectively.
- Regular expressions can enhance your search patterns, allowing for more complex queries.
- When searching large files, consider using `less` in combination with `grep` for easier navigation of results: 
  ```bash
  grep "pattern" largefile.txt | less
  ```