# [Linux] Bash continue Usage equivalent in English: Resume the next iteration of a loop

## Overview
The `continue` command in Bash is used within loops to skip the remaining commands in the current iteration and proceed to the next iteration of the loop. This is particularly useful when you want to bypass certain conditions without exiting the loop entirely.

## Usage
The basic syntax of the `continue` command is as follows:

```bash
continue [n]
```

Here, `n` is an optional argument that specifies how many levels of nested loops to skip. If `n` is omitted, it defaults to 1, meaning it will skip to the next iteration of the innermost loop.

## Common Options
- `n`: An optional integer that specifies the number of nested loops to continue. For example, `continue 2` would skip to the next iteration of the second outer loop.

## Common Examples

### Example 1: Basic usage in a `for` loop
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "Number: $i"
done
```
*Output:*
```
Number: 1
Number: 2
Number: 4
Number: 5
```
In this example, when `i` equals 3, the `continue` command skips the `echo` statement, resulting in 3 not being printed.

### Example 2: Using `continue` in a `while` loop
```bash
count=0
while [ $count -lt 5 ]; do
    count=$((count + 1))
    if [ $count -eq 2 ]; then
        continue
    fi
    echo "Count: $count"
done
```
*Output:*
```
Count: 1
Count: 3
Count: 4
Count: 5
```
Here, the loop skips the output when `count` is 2.

### Example 3: Skipping multiple levels of nested loops
```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            continue 2
        fi
        echo "i: $i, j: $j"
    done
done
```
*Output:*
```
i: 1, j: 1
i: 1, j: 3
i: 2, j: 1
i: 2, j: 3
i: 3, j: 1
i: 3, j: 3
```
In this case, when `j` equals 2, the command skips to the next iteration of the outer loop as well.

## Tips
- Use `continue` to improve the readability of your loops by avoiding deeply nested `if` statements.
- Be cautious when using `continue` in nested loops; ensure you specify the correct level to avoid skipping unintended iterations.
- Always test your loops to confirm that the `continue` command behaves as expected, especially in complex scripts.