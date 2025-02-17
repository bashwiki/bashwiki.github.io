# [Linux] Bash getopts用法等价物: 解析命令行选项

## Overview
The `getopts` command in Bash is used for parsing command-line options and arguments in shell scripts. It simplifies the process of handling options, allowing scripts to accept flags and parameters in a standardized way.

## Usage
The basic syntax of the `getopts` command is as follows:

```bash
getopts optstring variable
```

- `optstring`: A string that defines the valid options.
- `variable`: The name of the variable that will hold the option character.

## Common Options
- `-a`: Indicates that the option requires an argument.
- `-b`: Used to specify a boolean flag.
- `-c`: Can be used to count occurrences of an option.

## Common Examples

### Example 1: Basic Option Parsing
This example shows how to parse a single option `-a`:

```bash
#!/bin/bash

while getopts "a" opt; do
  case $opt in
    a)
      echo "Option -a was triggered."
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done
```

### Example 2: Options with Arguments
In this example, we parse an option `-f` that requires an argument:

```bash
#!/bin/bash

while getopts "f:" opt; do
  case $opt in
    f)
      echo "File name provided: $OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done
```

### Example 3: Multiple Options
This example demonstrates how to handle multiple options:

```bash
#!/bin/bash

while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "Option -a was triggered."
      ;;
    b)
      echo "Option -b with argument: $OPTARG"
      ;;
    c)
      echo "Option -c with argument: $OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done
```

## Tips
- Always include a case for `\?` to handle invalid options gracefully.
- Use a colon (`:`) after an option in `optstring` to indicate that it requires an argument.
- Consider using `shift` after processing options to handle positional parameters if needed.