# [리눅스] Bash sed 사용법

## Overview
`sed`, short for Stream Editor, is a powerful command-line utility in Unix and Linux systems used for parsing and transforming text. Its primary purpose is to perform basic text transformations on an input stream (a file or input from a pipeline). `sed` is particularly useful for tasks such as text substitution, deletion, and insertion, making it an essential tool for developers and engineers working with text processing.

## Usage
The basic syntax of the `sed` command is as follows:

```bash
sed [OPTIONS] 'SCRIPT' [INPUTFILE...]
```

### Common Options
- `-e`: Allows you to add multiple editing commands.
- `-i`: Edits files in place (modifies the original file).
- `-n`: Suppresses automatic printing of pattern space (useful when combined with the `p` command).
- `-f`: Allows you to specify a file containing `sed` commands.

## Examples

### Example 1: Simple Text Substitution
To replace the first occurrence of "apple" with "orange" in a file named `fruits.txt`, you can use the following command:

```bash
sed 's/apple/orange/' fruits.txt
```

This command will output the modified text to the terminal without changing the original file.

### Example 2: In-Place Editing
If you want to replace all occurrences of "cat" with "dog" directly in the file `pets.txt`, you can use the `-i` option:

```bash
sed -i 's/cat/dog/g' pets.txt
```

The `g` at the end of the command indicates that all occurrences in each line should be replaced, rather than just the first one.

## Tips
- Always make a backup of your original files before using the `-i` option, as it modifies files in place.
- Use the `-n` option with the `p` command to print only the lines that match a specific pattern, which can help in filtering output.
- You can chain multiple `sed` commands using the `-e` option for more complex transformations.
- Regular expressions can be used in `sed` for more advanced pattern matching and text manipulation.

By mastering `sed`, you can significantly enhance your text processing capabilities in Bash, making it a valuable tool in your development toolkit.