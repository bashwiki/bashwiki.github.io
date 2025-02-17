# [Linux] Bash paste Usage: Combine lines of files

## Overview
The `paste` command in Bash is used to merge lines of files side by side. It takes multiple input files and combines their corresponding lines into a single output, making it useful for creating tabular data or combining text from different sources.

## Usage
The basic syntax of the `paste` command is as follows:

```bash
paste [options] [arguments]
```

## Common Options
- `-d` : Specify a delimiter to use between the pasted lines (default is a tab).
- `-s` : Paste the lines of each file sequentially rather than in parallel.
- `-z` : Treats the input as a set of null-terminated lines instead of newline-terminated lines.

## Common Examples

### Example 1: Basic usage
Combine two files line by line using the default tab delimiter.

```bash
paste file1.txt file2.txt
```

### Example 2: Using a custom delimiter
Combine two files with a comma as the delimiter.

```bash
paste -d ',' file1.txt file2.txt
```

### Example 3: Sequential pasting
Paste the lines of a single file sequentially.

```bash
paste -s file1.txt
```

### Example 4: Pasting multiple files
Combine three files into a single output.

```bash
paste file1.txt file2.txt file3.txt
```

### Example 5: Using null as a delimiter
Use null characters as delimiters for pasting.

```bash
paste -z file1.txt file2.txt
```

## Tips
- Always check the output format when using custom delimiters to ensure it meets your needs.
- Use the `-s` option when you want to create a single line output from multiple lines in a file.
- Combine `paste` with other commands like `sort` or `uniq` for more complex data manipulation tasks.