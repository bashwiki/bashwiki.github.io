# [리눅스] Bash head 사용법

## Overview
The `head` command in Bash is a utility that allows users to view the beginning of a file or output stream. Its primary purpose is to display the first few lines of a file, which can be particularly useful for quickly inspecting the contents of large files without needing to open them entirely. By default, `head` shows the first 10 lines, but this can be customized with options.

## Usage
The basic syntax of the `head` command is as follows:

```bash
head [OPTION]... [FILE]...
```

### Common Options:
- `-n NUM`, `--lines=NUM`: Output the first NUM lines instead of the default 10.
- `-c NUM`, `--bytes=NUM`: Output the first NUM bytes of each file.
- `-q`, `--quiet`, `--silent`: Suppress printing of headers when multiple files are being processed.
- `-v`, `--verbose`: Always print headers giving file names.

## Examples
### Example 1: Display the first 10 lines of a file
To view the first 10 lines of a file named `example.txt`, you can use:

```bash
head example.txt
```

### Example 2: Display the first 5 lines of a file
If you want to see only the first 5 lines, you can specify the `-n` option:

```bash
head -n 5 example.txt
```

### Example 3: Display the first 20 bytes of a file
To view the first 20 bytes of a file, you can use the `-c` option:

```bash
head -c 20 example.txt
```

## Tips
- Use `head` in combination with other commands in a pipeline to quickly inspect output. For example, you can use `grep` to filter lines and then pipe the result to `head` to see the first few matches.
  
  ```bash
  grep "search_term" largefile.txt | head -n 10
  ```

- When working with multiple files, remember that `head` will print the file name before the output of each file, which can help you identify which output belongs to which file.
  
- If you frequently need to view more than the default 10 lines, consider creating an alias in your `.bashrc` file for convenience. For example:

  ```bash
  alias h='head -n 20'
  ```

This will allow you to use `h filename.txt` to view the first 20 lines directly.