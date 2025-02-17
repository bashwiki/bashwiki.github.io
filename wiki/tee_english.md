# [Linux] Bash tee Uso: Redirect output to files and display it

## Overview
The `tee` command in Bash is used to read from standard input and write to standard output and one or more files simultaneously. This allows you to view the output of a command while also saving it to a file.

## Usage
The basic syntax of the `tee` command is as follows:

```bash
tee [options] [arguments]
```

## Common Options
- `-a`, `--append`: Append the output to the given files instead of overwriting them.
- `-i`, `--ignore-interrupts`: Ignore interrupt signals.
- `--help`: Display help information about the command.
- `--version`: Show the version information of the command.

## Common Examples

1. **Basic Usage**: Redirect output to a file while displaying it.
   ```bash
   echo "Hello, World!" | tee output.txt
   ```

2. **Appending to a File**: Append output to an existing file.
   ```bash
   echo "Another line" | tee -a output.txt
   ```

3. **Multiple Files**: Write output to multiple files.
   ```bash
   echo "Logging data" | tee file1.txt file2.txt
   ```

4. **Using with Other Commands**: Combine `tee` with other commands in a pipeline.
   ```bash
   ls -l | tee directory_listing.txt | grep ".txt"
   ```

5. **Ignoring Interrupts**: Use the ignore interrupts option.
   ```bash
   echo "This will not be interrupted" | tee -i output.txt
   ```

## Tips
- Use the `-a` option when you want to keep adding data to a file without losing the existing content.
- Combine `tee` with other commands in a pipeline to capture intermediate output for debugging or logging purposes.
- Remember that `tee` will overwrite files by default, so use the `-a` option if you want to append instead.