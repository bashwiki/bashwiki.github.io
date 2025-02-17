# [Linux] Bash cat uso: Displaying file contents

## Overview
The `cat` command in Bash is used to concatenate and display the contents of files. It is a simple yet powerful tool that allows users to read file contents directly in the terminal or combine multiple files into one.

## Usage
The basic syntax of the `cat` command is as follows:

```bash
cat [options] [arguments]
```

## Common Options
- `-n`: Number all output lines.
- `-b`: Number non-empty output lines.
- `-E`: Display a dollar sign (`$`) at the end of each line.
- `-s`: Suppress repeated empty output lines.
- `-A`: Show all characters, including non-printing characters.

## Common Examples

1. **Display a single file:**
   ```bash
   cat filename.txt
   ```

2. **Display multiple files:**
   ```bash
   cat file1.txt file2.txt
   ```

3. **Create a new file by concatenating existing files:**
   ```bash
   cat file1.txt file2.txt > newfile.txt
   ```

4. **Append contents of one file to another:**
   ```bash
   cat file1.txt >> file2.txt
   ```

5. **Display line numbers:**
   ```bash
   cat -n filename.txt
   ```

6. **Suppress repeated empty lines:**
   ```bash
   cat -s filename.txt
   ```

## Tips
- Use `cat` in combination with other commands through piping to process file contents further.
- For large files, consider using `less` or `more` instead of `cat` to avoid overwhelming the terminal.
- Be cautious when using redirection (`>`) to avoid overwriting existing files unintentionally. Always double-check your command before executing it.