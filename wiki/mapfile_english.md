# [리눅스] Bash mapfile 사용법

## Overview
The `mapfile` command in Bash is used to read lines from a file or standard input into an indexed array. This command is particularly useful for processing multiline input or files, as it allows developers to easily manipulate and access each line as an element of an array. The primary purpose of `mapfile` is to facilitate the handling of input data in a structured manner.

## Usage
The basic syntax of the `mapfile` command is as follows:

```bash
mapfile [options] array_name
```

### Common Options
- `-n N`: Read only the first N lines from the input.
- `-s N`: Skip the first N lines before reading.
- `-t`: Remove the trailing newlines from each line read.
- `-O N`: Specify the index at which to start storing the lines in the array.

## Examples

### Example 1: Basic Usage
To read lines from a file into an array, you can use the following command:

```bash
mapfile lines < myfile.txt
```

In this example, each line from `myfile.txt` is stored as an element in the `lines` array. You can access the lines using `${lines[index]}`.

### Example 2: Using Options
Here’s an example that demonstrates the use of options:

```bash
mapfile -t first_five < myfile.txt
```

This command reads the first five lines from `myfile.txt` into the `first_five` array, removing any trailing newlines. You can then iterate over the array like this:

```bash
for line in "${first_five[@]}"; do
    echo "$line"
done
```

## Tips
- When using `mapfile`, remember that it reads until the end of the input, so if you're working with large files, consider using the `-n` option to limit the number of lines read.
- Use the `-t` option to avoid issues with trailing newlines, especially if you plan to process the lines further.
- If you need to skip a certain number of lines, the `-s` option can be very helpful, especially when dealing with header lines in CSV files or similar formats.

By utilizing `mapfile`, you can efficiently manage multiline input in your Bash scripts, making your code cleaner and easier to maintain.