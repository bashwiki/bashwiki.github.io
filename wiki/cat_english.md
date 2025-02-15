# [리눅스] Bash cat 사용법

## Overview
The `cat` command in Bash is a standard utility used to concatenate and display the contents of files. Its primary purpose is to read files sequentially, writing them to standard output. This makes it a versatile tool for viewing file contents, combining multiple files, and creating new files from existing ones.

## Usage
The basic syntax of the `cat` command is as follows:

```bash
cat [OPTION]... [FILE]...
```

### Common Options:
- `-A`, `--show-all`: Show all non-printing characters (equivalent to `-vET`).
- `-b`, `--number-nonblank`: Number non-empty output lines, starting at 1.
- `-e`: Equivalent to `-vE`, it shows non-printing characters and adds a `$` at the end of each line.
- `-n`, `--number`: Number all output lines, starting at 1.
- `-s`, `--squeeze-blank`: Suppress repeated empty output lines.
- `-T`, `--show-tabs`: Show tab characters as `^I`.
- `-v`, `--show-nonprinting`: Use `^` and `M-` notation to display non-printing characters.

## Examples

### Example 1: Displaying a File
To display the contents of a file named `example.txt`, you can use:

```bash
cat example.txt
```

This command will output the entire content of `example.txt` to the terminal.

### Example 2: Combining Multiple Files
To concatenate the contents of `file1.txt` and `file2.txt` and display them together, you can use:

```bash
cat file1.txt file2.txt
```

If you want to save the combined output into a new file named `combined.txt`, you can redirect the output:

```bash
cat file1.txt file2.txt > combined.txt
```

## Tips
- Use `cat` with the `-n` option to number all lines in the output, which can be helpful for reference or debugging:
  
  ```bash
  cat -n example.txt
  ```

- When dealing with large files, consider using `less` or `more` instead of `cat`, as they allow for easier navigation through the content.
- To quickly check the contents of a file without opening an editor, `cat` is a fast and effective choice.
- Be cautious when using redirection with `cat`, as it can overwrite files if not used properly. Always double-check your command before executing it.