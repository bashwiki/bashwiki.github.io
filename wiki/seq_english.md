# [리눅스] Bash seq 사용법

## Overview
The `seq` command in Bash is a utility that generates a sequence of numbers. It is primarily used for creating lists of numbers in a specified range, which can be particularly useful in scripting and automation tasks. The command allows for flexible formatting and incrementing options, making it a versatile tool for developers and engineers.

## Usage
The basic syntax of the `seq` command is as follows:

```
seq [OPTION]... LAST
seq [OPTION]... FIRST LAST
seq [OPTION]... FIRST INCREMENT LAST
```

### Common Options:
- `-f, --format=FORMAT`: Specify a format for the output numbers. This allows for controlling the number of decimal places and overall formatting.
- `-s, --separator=STRING`: Define a custom string to separate the output numbers instead of the default newline.
- `-w, --equal-width`: Pad the output numbers with leading zeros to ensure they all have the same width.

## Examples

### Example 1: Basic Number Sequence
To generate a simple sequence of numbers from 1 to 5, you can use:

```bash
seq 1 5
```
**Output:**
```
1
2
3
4
5
```

### Example 2: Custom Increment
To generate a sequence of numbers from 1 to 10 with an increment of 2, use:

```bash
seq 1 2 10
```
**Output:**
```
1
3
5
7
9
```

### Example 3: Formatted Output
If you want to generate a sequence of numbers from 1 to 5 with two decimal places, you can format the output as follows:

```bash
seq -f "%.2f" 1 5
```
**Output:**
```
1.00
2.00
3.00
4.00
5.00
```

## Tips
- Use the `-s` option to create a comma-separated list of numbers. For example, `seq -s "," 1 5` will output `1,2,3,4,5`.
- When using `-w`, be mindful of the total range of numbers, as it will pad all numbers to the width of the largest number in the sequence.
- Combine `seq` with other commands in a pipeline for more complex operations, such as using it with `xargs` to execute commands for each number in the sequence.

By understanding and utilizing the `seq` command effectively, you can streamline many tasks that involve numerical sequences in your scripts and command-line operations.