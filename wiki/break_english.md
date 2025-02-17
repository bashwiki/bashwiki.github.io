# [Linux] Bash break用法: Exit a loop early

## Overview
The `break` command in Bash is used to exit from a loop prematurely. When executed within a loop, it immediately terminates that loop and continues with the next command following the loop. This is particularly useful when a certain condition is met, and you want to stop the iteration without waiting for the loop to finish.

## Usage
The basic syntax of the `break` command is as follows:

```bash
break [n]
```

Here, `n` is an optional argument that specifies how many levels of loops to break out of. If `n` is not provided, it defaults to breaking out of the innermost loop.

## Common Options
- `n`: An optional integer that specifies the number of nested loops to exit. If omitted, it breaks from the innermost loop.

## Common Examples

### Example 1: Basic break in a loop
```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    break
  fi
  echo $i
done
```
**Output:**
```
1
2
```
In this example, the loop will terminate when `i` equals 3, so it only prints 1 and 2.

### Example 2: Breaking out of nested loops
```bash
for i in {1..3}; do
  for j in {1..3}; do
    if [ $j -eq 2 ]; then
      break 2
    fi
    echo "i: $i, j: $j"
  done
done
```
**Output:**
```
i: 1, j: 1
```
Here, the `break 2` command exits both the inner and outer loops when `j` equals 2.

### Example 3: Using break with while loop
```bash
count=1
while [ $count -le 5 ]; do
  if [ $count -eq 4 ]; then
    break
  fi
  echo $count
  ((count++))
done
```
**Output:**
```
1
2
3
```
In this while loop, it stops printing when `count` reaches 4.

## Tips
- Use `break` judiciously to avoid confusion in complex nested loops.
- Consider using `continue` if you want to skip the current iteration instead of breaking out of the loop.
- Always ensure that your break conditions are clear to maintain readability and prevent infinite loops.