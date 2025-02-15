# [리눅스] Bash wc 사용법

## Overview
The `wc` command, short for "word count," is a utility in Unix and Unix-like operating systems that is used to count lines, words, and characters in text files. It is particularly useful for quickly analyzing the content of files and can be employed in scripts and command-line operations to gather statistics about text data.

## Usage
The basic syntax for the `wc` command is as follows:

```bash
wc [OPTION]... [FILE]...
```

### Common Options:
- `-l`: Count the number of lines in the input.
- `-w`: Count the number of words in the input.
- `-c`: Count the number of bytes in the input.
- `-m`: Count the number of characters in the input (useful for multi-byte character sets).
- `-L`: Print the length of the longest line in the input.

You can combine these options. For example, `wc -lw` will give you both the line and word counts.

## Examples

1. **Count Lines, Words, and Characters in a File**:
   To count the lines, words, and characters in a file named `example.txt`, you can run:

   ```bash
   wc example.txt
   ```

   This will output three numbers followed by the filename: the number of lines, words, and characters.

2. **Count Only Lines**:
   If you only want to count the number of lines in a file, use the `-l` option:

   ```bash
   wc -l example.txt
   ```

   This will return just the number of lines in `example.txt`.

## Tips
- When using `wc` in a pipeline, you can pipe the output of other commands into `wc`. For example, to count the number of lines in the output of `ls`, you can use:

  ```bash
  ls | wc -l
  ```

- To count words in multiple files at once, simply list the files after the command:

  ```bash
  wc -w file1.txt file2.txt
  ```

- If you want to ignore empty lines when counting, you might consider using `grep` in combination with `wc`:

  ```bash
  grep -v '^$' example.txt | wc -l
  ```

This command will count only the non-empty lines in `example.txt`.

Using `wc` effectively can help you quickly analyze text files and integrate these statistics into your scripts and workflows.