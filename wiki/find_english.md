# [Linux] Bash find uso: find file names

## Overview
The `find` command is a powerful utility in Unix-like operating systems that allows users to search for files and directories within a specified location based on various criteria such as name, type, size, and modification date.

## Usage
The basic syntax of the `find` command is as follows:

```bash
find [options] [path] [expression]
```

- **options**: Modifiers that change the behavior of the command.
- **path**: The directory path where the search will begin.
- **expression**: Criteria to filter the search results.

## Common Options
- `-name`: Search for files by name (case-sensitive).
- `-iname`: Search for files by name (case-insensitive).
- `-type`: Specify the type of file to search for (e.g., `f` for regular files, `d` for directories).
- `-size`: Search for files of a specific size (e.g., `+100M` for files larger than 100 MB).
- `-mtime`: Search for files modified within a certain number of days (e.g., `-mtime -7` for files modified in the last 7 days).
- `-exec`: Execute a command on the found files.

## Common Examples
Here are some practical examples of using the `find` command:

### 1. Find files by name
```bash
find /path/to/directory -name "filename.txt"
```

### 2. Find files by name (case-insensitive)
```bash
find /path/to/directory -iname "filename.txt"
```

### 3. Find all directories
```bash
find /path/to/directory -type d
```

### 4. Find files larger than 100MB
```bash
find /path/to/directory -type f -size +100M
```

### 5. Find files modified in the last 7 days
```bash
find /path/to/directory -type f -mtime -7
```

### 6. Execute a command on found files
```bash
find /path/to/directory -type f -name "*.log" -exec rm {} \;
```

## Tips
- Use `-print` at the end of your command to explicitly display the results if needed.
- Combine multiple criteria using logical operators like `-and` and `-or` for more complex searches.
- Always test your `find` command without `-exec` first to ensure you're selecting the correct files before executing any commands on them.