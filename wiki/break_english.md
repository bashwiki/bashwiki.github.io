# [리눅스] Bash break 사용법

## Overview
The `break` command in Bash is used to exit from a loop prematurely. It is primarily utilized within `for`, `while`, and `until` loops to terminate the loop's execution when a specific condition is met. This can be particularly useful when you want to stop processing further iterations based on certain criteria, thereby improving efficiency and control in your scripts.

## Usage
The basic syntax of the `break` command is as follows:

```bash
break [n]
```

- `n`: This optional argument specifies the number of nested loops to break out of. If `n` is not provided, `break` will exit from the innermost loop.

## Examples

### Example 1: Basic Usage in a Loop
Here’s a simple example demonstrating the use of `break` to exit a `while` loop when a condition is met:

```bash
count=1
while [ $count -le 10 ]; do
  echo "Count is: $count"
  if [ $count -eq 5 ]; then
    break
  fi
  ((count++))
done
```
*Output:*
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```
In this example, the loop will print the count until it reaches 5, at which point the `break` command is executed, terminating the loop.

### Example 2: Breaking Out of Nested Loops
You can also use `break` to exit from nested loops. Here’s an example:

```bash
for i in {1..3}; do
  for j in {1..3}; do
    if [ $i -eq 2 ] && [ $j -eq 2 ]; then
      break 2
    fi
    echo "i: $i, j: $j"
  done
done
```
*Output:*
```
i: 1, j: 1
i: 1, j: 2
i: 1, j: 3
i: 2, j: 1
```
In this case, the `break 2` command exits both the inner and outer loops when `i` is 2 and `j` is 2.

## Tips
- Use `break` judiciously to avoid making your loops difficult to understand. Clear conditions for breaking out of loops can enhance the readability of your scripts.
- When using `break` in nested loops, always specify the number of levels to break out of if you want to exit more than one loop. This helps in maintaining clarity in your code.
- Consider using `continue` in conjunction with `break` for more complex loop control, allowing you to skip to the next iteration or exit based on different conditions.

By understanding and effectively using the `break` command, you can gain greater control over loop execution in your Bash scripts, leading to more efficient and manageable code.