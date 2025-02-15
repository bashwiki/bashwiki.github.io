# [리눅스] Bash dirs 사용법

## Overview
The `dirs` command in Bash is used to display the list of currently remembered directories in the directory stack. The directory stack is a feature that allows users to navigate through multiple directories easily. The primary purpose of the `dirs` command is to show the current state of this stack, which can be particularly useful when working with multiple directories in a terminal session.

## Usage
The basic syntax of the `dirs` command is as follows:

```bash
dirs [options]
```

### Common Options
- `-l`: Displays the directory stack in a long format, showing the full path of each directory.
- `-p`: Prints the directory stack without any formatting, which can be useful for scripting purposes.

## Examples
### Example 1: Displaying the Directory Stack
To simply display the current directory stack, you can use the command without any options:

```bash
dirs
```
Output might look like this:
```
~/projects ~/documents ~/downloads
```

### Example 2: Long Format Display
To view the directory stack in a long format, use the `-l` option:

```bash
dirs -l
```
Output might look like this:
```
/home/user/projects /home/user/documents /home/user/downloads
```

## Tips
- Use the `pushd` and `popd` commands to manipulate the directory stack. `pushd` adds a directory to the stack, while `popd` removes the top directory from the stack.
- Combine `dirs` with `pushd` and `popd` to keep track of your navigation history effectively, especially when working on complex projects that require switching between multiple directories frequently.
- If you find yourself needing to check the directory stack often, consider creating an alias in your `.bashrc` file for quicker access, such as `alias ds='dirs -l'`.