# [리눅스] Bash tee 사용법

## Overview
The `tee` command in Bash is a powerful utility that reads from standard input and writes to standard output and one or more files simultaneously. Its primary purpose is to allow users to view the output of a command while also saving it to a file, making it particularly useful for logging and debugging purposes.

## Usage
The basic syntax of the `tee` command is as follows:

```bash
tee [OPTION]... [FILE]...
```

### Common Options:
- `-a`, `--append`: Append the output to the given files instead of overwriting them.
- `-i`, `--ignore-interrupts`: Ignore interrupt signals.
- `--help`: Display help information about the command.
- `--version`: Show the version information of the `tee` command.

## Examples

### Example 1: Basic Usage
To capture the output of a command and save it to a file while also displaying it in the terminal, you can use:

```bash
echo "Hello, World!" | tee output.txt
```

In this example, the string "Hello, World!" is echoed and simultaneously written to `output.txt` while also being displayed on the terminal.

### Example 2: Appending Output
If you want to append additional output to the same file instead of overwriting it, use the `-a` option:

```bash
echo "Another line" | tee -a output.txt
```

This command will add "Another line" to the end of `output.txt` while still displaying it in the terminal.

## Tips
- Use `tee` in combination with other commands in a pipeline to log their output without losing visibility. For example, you can log the output of a long-running process:
  
  ```bash
  long_running_command | tee log.txt
  ```

- When using `tee` with multiple files, simply list them after the command:

  ```bash
  echo "Data" | tee file1.txt file2.txt
  ```

- Remember that if you do not specify the `-a` option, `tee` will overwrite the specified files, so use it with caution if you want to preserve existing data.

By understanding and utilizing the `tee` command effectively, you can enhance your command-line workflows, allowing for better output management and logging.