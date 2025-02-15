# [리눅스] Bash getopts 사용법

## Overview
The `getopts` command in Bash is a built-in utility used for parsing command-line options and arguments. Its primary purpose is to handle short options (single-character flags) in a structured way, allowing scripts to easily manage user input. This is particularly useful in scripts that require options to modify their behavior or specify input files.

## Usage
The basic syntax of `getopts` is as follows:

```bash
getopts optstring variable
```

- `optstring`: A string that defines the valid options. Each character in the string represents a valid option. If an option requires an argument, it is followed by a colon (`:`).
- `variable`: The name of the variable that will hold the current option being processed.

### Common Options
- `:` (colon) at the beginning of `optstring`: If specified, `getopts` will handle errors differently, setting the variable to `?` when an invalid option is encountered.
- `-` (dash): Not used in `optstring`, but is often included in the command line when invoking the script.

## Examples

### Example 1: Basic Option Parsing
Here’s a simple script that uses `getopts` to handle options `-a` and `-b`:

```bash
#!/bin/bash

while getopts "ab" option; do
  case $option in
    a) echo "Option A selected." ;;
    b) echo "Option B selected." ;;
    *) echo "Invalid option." ;;
  esac
done
```

**Usage:**
```bash
./script.sh -a
# Output: Option A selected.

./script.sh -b
# Output: Option B selected.

./script.sh -c
# Output: Invalid option.
```

### Example 2: Options with Arguments
This example demonstrates how to handle options that require arguments:

```bash
#!/bin/bash

while getopts "a:b:" option; do
  case $option in
    a) echo "Option A with argument: $OPTARG" ;;
    b) echo "Option B with argument: $OPTARG" ;;
    *) echo "Invalid option." ;;
  esac
done
```

**Usage:**
```bash
./script.sh -a value1
# Output: Option A with argument: value1

./script.sh -b value2
# Output: Option B with argument: value2
```

## Tips
- Always initialize your option variable before using `getopts` to avoid unexpected behavior.
- Use `OPTIND` to reset the index of the next option to be processed if you need to call `getopts` multiple times in the same script.
- To handle long options (more than one character), consider using `getopt` or a combination of `getopts` and additional logic.
- Provide clear help messages for users by checking for `-h` or `--help` options and displaying usage instructions.

By following these guidelines and examples, you can effectively utilize `getopts` in your Bash scripts to create robust command-line interfaces.