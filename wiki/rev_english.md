# [리눅스] Bash rev 사용법

## Overview
The `rev` command in Bash is a simple utility that reverses the order of characters in each line of a given input. Its primary purpose is to facilitate the manipulation of text data by allowing users to quickly see the reverse representation of strings, which can be useful in various programming and data processing tasks.

## Usage
The basic syntax of the `rev` command is as follows:

```bash
rev [OPTION]... [FILE]
```

### Common Options
- `-h`, `--help`: Display a help message and exit.
- `-V`, `--version`: Output version information and exit.
- If no file is specified, `rev` reads from standard input.

## Examples

### Example 1: Reversing a String from a File
Suppose you have a file named `example.txt` containing the following lines:

```
hello
world
```

You can reverse the characters in each line by using the `rev` command as follows:

```bash
rev example.txt
```

**Output:**
```
olleh
dlrow
```

### Example 2: Reversing Input from Standard Input
You can also use `rev` to reverse a string directly from the command line. For example:

```bash
echo "Bash is powerful" | rev
```

**Output:**
```
lufrewop si hsab
```

## Tips
- When using `rev` in scripts, consider redirecting input from files or using pipes to handle larger datasets efficiently.
- Combine `rev` with other text processing commands like `sort` or `uniq` for more complex data manipulation tasks.
- Be cautious when reversing lines that contain special characters or escape sequences, as their representation may change when reversed.