# [리눅스] Bash fgrep 사용법

## Overview
`fgrep` is a command-line utility in Unix-like operating systems that is used to search for fixed strings in files. Unlike `grep`, which interprets regular expressions, `fgrep` treats the search pattern as a literal string, making it faster for searching fixed strings. This is particularly useful when you want to find exact matches without the overhead of regular expression processing.

## Usage
The basic syntax for the `fgrep` command is as follows:

```bash
fgrep [OPTIONS] PATTERN [FILE...]
```

### Common Options
- `-i`: Ignore case distinctions in both the pattern and the input files.
- `-v`: Invert the match to select non-matching lines.
- `-c`: Count the number of matching lines instead of displaying them.
- `-l`: List the names of files with matching lines, once for each file.
- `-n`: Prefix each line of output with the line number within its input file.

## Examples

### Example 1: Basic Usage
To search for the exact string "error" in a file named `logfile.txt`, you would use the following command:

```bash
fgrep "error" logfile.txt
```

This command will output all lines in `logfile.txt` that contain the exact string "error".

### Example 2: Case Insensitive Search
If you want to perform a case-insensitive search for the string "error", you can use the `-i` option:

```bash
fgrep -i "error" logfile.txt
```

This command will match "error", "Error", "ERROR", and any other case variations.

## Tips
- Use `fgrep` when you need to search for fixed strings, as it is generally faster than `grep` for this purpose.
- Combine options for more complex queries. For example, to count how many times the string "success" appears in a file without showing the matching lines, use:

```bash
fgrep -c "success" logfile.txt
```
- When searching through multiple files, you can specify multiple filenames or use wildcards (e.g., `*.txt`) to search through all text files in a directory.
- If you need to search for a string that contains special characters (like `*`, `?`, etc.), `fgrep` is ideal since it treats them as literal characters rather than regex operators.