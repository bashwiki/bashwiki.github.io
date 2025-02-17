# [Linux] Bash head Usage: Display the beginning of files

## Overview
The `head` command in Bash is used to display the first few lines of a file or the output of a command. By default, it shows the first 10 lines, but this can be adjusted with options.

## Usage
The basic syntax of the `head` command is as follows:

```bash
head [options] [arguments]
```

## Common Options
- `-n [number]`: Specify the number of lines to display. For example, `-n 5` will show the first 5 lines.
- `-c [number]`: Display the first specified number of bytes instead of lines.
- `-q`: Suppress the output of the file headers when multiple files are being processed.
- `-v`: Always show the file header, even when only one file is being processed.

## Common Examples
Here are some practical examples of using the `head` command:

1. Display the first 10 lines of a file:
   ```bash
   head filename.txt
   ```

2. Display the first 5 lines of a file:
   ```bash
   head -n 5 filename.txt
   ```

3. Display the first 20 bytes of a file:
   ```bash
   head -c 20 filename.txt
   ```

4. Display the first 10 lines of multiple files:
   ```bash
   head file1.txt file2.txt
   ```

5. Always show the file header when displaying the first 10 lines of a file:
   ```bash
   head -v filename.txt
   ```

## Tips
- Use `head` in combination with other commands using pipes. For example, to see the first 10 lines of a long directory listing:
  ```bash
  ls -l | head
  ```
- When working with large files, `head` can quickly give you a preview without opening the entire file.
- Remember that you can adjust the number of lines displayed with the `-n` option to suit your needs.