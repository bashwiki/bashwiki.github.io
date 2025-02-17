# [Linux] Bash factor uso equivalente: Factorizar números

## Overview
The `factor` command in Bash is used to factor integers into their prime factors. It takes one or more integers as input and outputs the prime factorization of each number.

## Usage
The basic syntax of the `factor` command is as follows:

```bash
factor [options] [arguments]
```

## Common Options
- `--help`: Displays help information about the command.
- `--version`: Shows the version of the `factor` command.
- `-n`: Suppresses the output of the number being factored, showing only the factors.

## Common Examples

1. **Factor a single number:**
   To factor the number 12, you can use:
   ```bash
   factor 12
   ```
   Output:
   ```
   12: 2 2 3
   ```

2. **Factor multiple numbers:**
   You can factor several numbers at once:
   ```bash
   factor 15 28 30
   ```
   Output:
   ```
   15: 3 5
   28: 2 2 7
   30: 2 3 5
   ```

3. **Using the `-n` option:**
   To suppress the output of the numbers being factored:
   ```bash
   factor -n 18
   ```
   Output:
   ```
   2 3 3
   ```

4. **Getting help information:**
   To see the help information for the `factor` command:
   ```bash
   factor --help
   ```

## Tips
- Use `factor` in scripts to automate the process of finding prime factors for a list of numbers.
- Combine `factor` with other commands like `xargs` to handle input from files or other command outputs.
- Remember that `factor` only works with positive integers; using negative numbers or non-integer values will result in an error.