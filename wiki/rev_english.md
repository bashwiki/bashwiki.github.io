# [Linux] Bash rev: Reverse lines of text

## Overview
The `rev` command is a simple utility in Bash that reverses the characters of each line in a given input. It is particularly useful for manipulating text data where you need to see the content in reverse order.

## Usage
The basic syntax of the `rev` command is as follows:

```bash
rev [options] [arguments]
```

## Common Options
- `-h`, `--help`: Displays a help message with usage information.
- `-V`, `--version`: Shows the version information of the `rev` command.

## Common Examples

### Example 1: Reverse a file's content
To reverse the characters of each line in a file named `example.txt`, you can use:

```bash
rev example.txt
```

### Example 2: Reverse input from standard input
You can also use `rev` to reverse text input directly from the command line. For example:

```bash
echo "Hello World" | rev
```

This will output:

```
dlroW olleH
```

### Example 3: Reverse multiple lines from a file
If you have a file with multiple lines, such as `data.txt`, you can reverse each line like this:

```bash
rev data.txt
```

### Example 4: Reverse a string in a variable
You can reverse a string stored in a variable as follows:

```bash
my_string="Bash Scripting"
echo "$my_string" | rev
```

This will output:

```
gnitpirS shaB
```

## Tips
- Use `rev` in combination with other commands, such as `cat` or `echo`, to process text dynamically.
- Remember that `rev` operates on a line-by-line basis; it will not reverse the order of lines, only the characters within each line.
- For larger files, consider redirecting the output to a new file using `>` to save the reversed content:

```bash
rev example.txt > reversed_example.txt
```