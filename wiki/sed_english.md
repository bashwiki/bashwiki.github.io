# [English] Bash sed Usage: Stream editor for filtering and transforming text

## Overview
The `sed` command, short for "stream editor," is a powerful tool in Bash used for parsing and transforming text in a pipeline. It allows users to perform basic text transformations on an input stream (a file or input from a pipeline) using a simple and compact syntax.

## Usage
The basic syntax of the `sed` command is as follows:

```bash
sed [options] [script] [file...]
```

- `options`: Flags that modify the behavior of `sed`.
- `script`: The editing commands to be applied to the input text.
- `file`: The file(s) to be processed. If no file is specified, `sed` reads from standard input.

## Common Options
- `-n`: Suppresses automatic printing of pattern space. Only lines explicitly specified for output will be printed.
- `-e`: Allows multiple editing commands to be specified in a single `sed` command.
- `-f`: Allows the user to specify a file containing `sed` commands.
- `-i`: Edits files in place, modifying the original file directly.

## Common Examples

### 1. Substitute text
Replace all occurrences of "apple" with "orange" in a file:

```bash
sed 's/apple/orange/g' fruits.txt
```

### 2. Delete lines
Remove all lines that contain the word "banana":

```bash
sed '/banana/d' fruits.txt
```

### 3. Print specific lines
Print only the first 5 lines of a file:

```bash
sed -n '1,5p' fruits.txt
```

### 4. Edit in place
Replace "grape" with "kiwi" directly in the file:

```bash
sed -i 's/grape/kiwi/g' fruits.txt
```

### 5. Use a script file
Apply commands from a separate file called `commands.sed`:

```bash
sed -f commands.sed fruits.txt
```

## Tips
- Always create a backup of your files before using the `-i` option to avoid accidental data loss.
- Use the `-n` option when you want to control what gets printed, especially when working with large files.
- Test your `sed` commands on a small sample of data before applying them to larger datasets to ensure they work as expected.