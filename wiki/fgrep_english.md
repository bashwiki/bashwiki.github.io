# [Linux] Bash fgrep Usage: Search fixed strings in files

## Overview
The `fgrep` command in Bash is used to search for fixed strings in files. Unlike `grep`, which interprets regular expressions, `fgrep` treats the search pattern as a literal string, making it useful for searching for specific text without any special character interpretation.

## Usage
The basic syntax of the `fgrep` command is as follows:

```bash
fgrep [options] [arguments]
```

## Common Options
- `-i`: Ignore case distinctions in both the pattern and the input files.
- `-v`: Invert the match, showing only lines that do not contain the specified string.
- `-c`: Count the number of lines that match the specified string.
- `-l`: List the names of files with matching lines, once for each file.
- `-n`: Prefix each line of output with the line number within its input file.

## Common Examples

1. **Basic string search in a file:**
   ```bash
   fgrep "hello" myfile.txt
   ```
   This command searches for the string "hello" in `myfile.txt`.

2. **Case-insensitive search:**
   ```bash
   fgrep -i "hello" myfile.txt
   ```
   This command searches for "hello" in a case-insensitive manner.

3. **Count occurrences of a string:**
   ```bash
   fgrep -c "hello" myfile.txt
   ```
   This command counts how many lines in `myfile.txt` contain the string "hello".

4. **List files containing the string:**
   ```bash
   fgrep -l "hello" *.txt
   ```
   This command lists all `.txt` files in the current directory that contain the string "hello".

5. **Invert match to find lines that do not contain the string:**
   ```bash
   fgrep -v "hello" myfile.txt
   ```
   This command shows all lines in `myfile.txt` that do not contain the string "hello".

## Tips
- Use `fgrep` when you need to search for strings that may contain special characters, as it will treat them literally.
- Combine `fgrep` with other commands using pipes for more complex operations, such as filtering output from other commands.
- Remember that `fgrep` is often faster than `grep` when searching for fixed strings, as it does not process regular expressions.