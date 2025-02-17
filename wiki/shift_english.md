# [Linux] Bash shift用法: Shift positional parameters

## Overview
The `shift` command in Bash is used to manipulate the positional parameters of a script. When you invoke `shift`, it shifts the values of the positional parameters to the left, effectively discarding the first parameter and moving all subsequent parameters one position down. This is particularly useful in scripts that process command-line arguments.

## Usage
The basic syntax of the `shift` command is as follows:

```bash
shift [n]
```

Where `n` is an optional argument that specifies the number of positions to shift. If `n` is not provided, it defaults to 1.

## Common Options
- `n`: Specifies the number of positions to shift. For example, `shift 2` will remove the first two positional parameters.

## Common Examples

### Example 1: Basic Shift
```bash
#!/bin/bash
echo "Before shift: $1 $2 $3"
shift
echo "After shift: $1 $2 $3"
```
Output:
```
Before shift: first second third
After shift: second third 
```

### Example 2: Shifting Multiple Positions
```bash
#!/bin/bash
echo "Before shift: $1 $2 $3 $4"
shift 2
echo "After shift: $1 $2 $3 $4"
```
Output:
```
Before shift: one two three four
After shift: three four 
```

### Example 3: Looping Through Parameters
```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Processing: $1"
    shift
done
```
Output (if called with `./script.sh a b c`):
```
Processing: a
Processing: b
Processing: c
```

## Tips
- Use `shift` when you need to process command-line arguments in a loop, allowing you to handle each argument one at a time.
- Always check the number of positional parameters (`$#`) before using `shift` to avoid errors when there are no parameters left.
- Combine `shift` with other commands like `case` or `if` to create more complex argument parsing in your scripts.