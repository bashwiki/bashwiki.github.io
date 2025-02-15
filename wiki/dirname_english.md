# [리눅스] Bash dirname 사용법

## Overview
The `dirname` command in Bash is a utility that is used to extract the directory path from a given file path. Its primary purpose is to provide the directory portion of a specified pathname, effectively stripping the filename and returning only the path leading to it. This can be particularly useful in scripts and command-line operations where you need to manipulate or reference the directory structure of files.

## Usage
The basic syntax of the `dirname` command is as follows:

```bash
dirname [OPTION] PATH
```

### Common Options
- `-z`, `--zero`: This option allows the command to handle input paths that are separated by a null character instead of a newline. This is useful when dealing with file names that may contain newlines.

## Examples
Here are a couple of practical examples demonstrating how to use the `dirname` command:

### Example 1: Basic Usage
To extract the directory path from a given file path:

```bash
$ dirname /home/user/documents/report.txt
/home/user/documents
```

In this example, `dirname` takes the full path of the file `report.txt` and returns the directory path `/home/user/documents`.

### Example 2: Using with Variables
You can also use `dirname` with shell variables:

```bash
$ FILE_PATH="/var/log/syslog"
$ DIR_PATH=$(dirname "$FILE_PATH")
$ echo $DIR_PATH
/var/log
```

Here, we store a file path in a variable and then use `dirname` to extract the directory path, which is stored in another variable.

## Tips
- Always quote your file paths when using `dirname` to prevent issues with spaces or special characters in file names.
- Consider using `dirname` in combination with other commands like `basename` to handle file paths more effectively in scripts.
- When working with scripts that process multiple files, consider using a loop to apply `dirname` to each file path in a list.

By understanding and utilizing the `dirname` command, you can efficiently manage file paths and directories in your Bash scripting and command-line tasks.