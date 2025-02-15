# [리눅스] Bash continue 사용법

## Overview
The `continue` command in Bash is used within loops to skip the current iteration and proceed to the next one. It is primarily employed in `for`, `while`, and `until` loops. When `continue` is executed, the remaining commands in the loop body for the current iteration are ignored, and control is transferred to the loop's next iteration.

## Usage
The basic syntax of the `continue` command is as follows:

```bash
continue [n]
```

- `n`: This optional argument specifies how many levels of enclosing loops to skip. If not provided, it defaults to `1`, meaning it will skip to the next iteration of the innermost loop.

## Examples

### Example 1: Basic Usage in a For Loop
In this example, we will iterate through a list of numbers and skip even numbers.

```bash
for i in {1..10}; do
    if (( i % 2 == 0 )); then
        continue
    fi
    echo "Odd number: $i"
done
```

**Output:**
```
Odd number: 1
Odd number: 3
Odd number: 5
Odd number: 7
Odd number: 9
```

### Example 2: Using `continue` in a While Loop
Here’s an example using `continue` in a while loop to skip processing when a specific condition is met.

```bash
count=1
while [ $count -le 10 ]; do
    if [ $count -eq 5 ]; then
        count=$((count + 1))
        continue
    fi
    echo "Count: $count"
    count=$((count + 1))
done
```

**Output:**
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 6
Count: 7
Count: 8
Count: 9
Count: 10
```

## Tips
- Use `continue` to improve the readability of your loop logic by avoiding deeply nested conditional statements.
- Be cautious when using `continue` in nested loops. If you specify a number with `continue`, ensure it matches the intended loop level to avoid skipping iterations unintentionally.
- Consider adding comments in your code to clarify the purpose of using `continue`, especially in complex loops, to aid future maintenance and understanding.