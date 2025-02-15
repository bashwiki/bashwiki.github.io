# [리눅스] Bash paste 사용법

## Overview
The `paste` command in Bash is used to merge lines of files horizontally. It takes multiple input files and combines their corresponding lines into a single line, separating them with a specified delimiter (default is a tab). This command is particularly useful for combining data from different sources into a single output format, making it easier to analyze or manipulate.

## Usage
The basic syntax of the `paste` command is as follows:

```bash
paste [OPTION]... [FILE]...
```

### Common Options:
- `-d, --delimiters=LIST`: Specify a single-character delimiter to separate the merged lines. You can use multiple delimiters by providing a list.
- `-s, --serial`: Paste the lines of each file serially, rather than in parallel. This means it will combine all lines from the first file, then all lines from the second file, and so on.
- `-z, --zero-terminated`: Treat input lines as zero-terminated instead of newline-terminated.

## Examples

### Example 1: Basic Usage
Suppose you have two files, `file1.txt` and `file2.txt`, with the following contents:

**file1.txt**
```
A
B
C
```

**file2.txt**
```
1
2
3
```

You can use the `paste` command to combine these files:

```bash
paste file1.txt file2.txt
```

**Output:**
```
A       1
B       2
C       3
```

### Example 2: Using a Custom Delimiter
If you want to use a comma as a delimiter instead of a tab, you can do so with the `-d` option:

```bash
paste -d, file1.txt file2.txt
```

**Output:**
```
A,1
B,2
C,3
```

## Tips
- When working with large files, consider using the `-s` option to process files serially if you want to avoid memory issues.
- You can combine `paste` with other commands using pipes for more complex data manipulation. For example, you can use `cat` to concatenate files and then pipe the output to `paste`.
- If you need to merge more than two files, simply list them all in the command. The `paste` command will handle any number of files.
- Always check the contents of your files to ensure they have the same number of lines if you want a clean output; otherwise, `paste` will fill in missing lines with empty fields.