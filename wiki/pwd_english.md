# [Linux] Bash pwd用法: 显示当前工作目录

## Overview
The `pwd` command stands for "print working directory." It is used in Bash and other Unix-like operating systems to display the current directory you are in within the terminal. This command is particularly useful for confirming your location in the filesystem.

## Usage
The basic syntax of the `pwd` command is as follows:

```
pwd [options] [arguments]
```

## Common Options
- `-L`: Use the logical current working directory. This option shows the path as it is set by the shell, which may include symbolic links.
- `-P`: Use the physical current working directory. This option resolves all symbolic links and shows the actual path.

## Common Examples
Here are some practical examples of using the `pwd` command:

1. **Basic Usage**: Simply type `pwd` to display the current directory.
   ```bash
   pwd
   ```

2. **Using the Logical Option**: Display the logical path of the current directory.
   ```bash
   pwd -L
   ```

3. **Using the Physical Option**: Display the physical path of the current directory.
   ```bash
   pwd -P
   ```

4. **In a Script**: You can use `pwd` in a script to store the current directory in a variable.
   ```bash
   current_dir=$(pwd)
   echo "You are currently in: $current_dir"
   ```

## Tips
- Use `pwd` frequently to keep track of your current location in the filesystem, especially when navigating through multiple directories.
- Combine `pwd` with other commands in scripts to create dynamic paths based on the current working directory.
- Remember that the output of `pwd` can be affected by the options you choose, so select `-L` or `-P` based on your needs.