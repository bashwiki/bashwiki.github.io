# [리눅스] Bash pwd 사용법

## Overview
The `pwd` command, which stands for "print working directory," is a fundamental command in Unix-like operating systems, including Linux. Its primary purpose is to display the current working directory of the shell session. This is particularly useful for users who need to confirm their location in the filesystem hierarchy before executing further commands.

## Usage
The basic syntax of the `pwd` command is as follows:

```bash
pwd [OPTION]
```

### Common Options
- `-L`: This option displays the logical current working directory. It shows the path as it is defined in the shell, which may include symbolic links.
- `-P`: This option displays the physical current working directory. It resolves all symbolic links and shows the actual path on the filesystem.

By default, `pwd` operates in the logical mode if no options are specified.

## Examples

### Example 1: Basic Usage
To simply display the current working directory, you can run:

```bash
pwd
```

**Output:**
```
/home/user/projects
```

This output indicates that the user is currently in the `projects` directory within their home directory.

### Example 2: Using the -P Option
To see the physical path of the current working directory, use the `-P` option:

```bash
pwd -P
```

**Output:**
```
/home/user/projects
```

If the current directory is a symbolic link, this command will resolve it and show the actual path.

## Tips
- Use `pwd` frequently to keep track of your current location in the filesystem, especially when navigating through multiple directories.
- Combine `pwd` with other commands in scripts to dynamically reference the current directory. For example, you can use it to create backup scripts that save files in the current directory.
- Remember that using the `-L` option can be helpful when working with symbolic links, as it allows you to see the path as it appears in the shell, which may differ from the physical path.