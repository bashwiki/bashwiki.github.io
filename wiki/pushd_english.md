# [리눅스] Bash pushd 사용법

## Overview
The `pushd` command in Bash is used to change the current directory while simultaneously saving the previous directory on a stack. This allows users to easily switch back to the original directory later using the `popd` command. The primary purpose of `pushd` is to facilitate navigation between directories without losing track of where you came from, which is especially useful in scripting and command-line operations.

## Usage
The basic syntax of the `pushd` command is as follows:

```bash
pushd [directory]
```

### Common Options
- `directory`: This is the target directory you want to navigate to. If no directory is specified, `pushd` will swap the top two directories on the stack.

## Examples

### Example 1: Basic Usage
To navigate to a specific directory and save the current directory on the stack, you can use:

```bash
pushd /path/to/directory
```

After executing this command, your current working directory will change to `/path/to/directory`, and the previous directory will be saved on the stack.

### Example 2: Using pushd without Arguments
If you want to swap between the current directory and the last directory you visited, simply run:

```bash
pushd
```

This will switch your current directory with the last one on the stack.

## Tips
- **Stack Management**: You can view the current directory stack by using the `dirs` command. This will show you the list of directories stored in the stack.
- **Combining with popd**: To return to the previous directory, use the `popd` command. This will remove the top directory from the stack and change your current directory back to it.
- **Scripting**: When writing scripts, consider using `pushd` and `popd` to manage directory changes cleanly, ensuring that your script can return to the original directory without hardcoding paths.
- **Error Handling**: Always check if the directory you are trying to push exists to avoid errors. You can use conditional statements to handle such cases gracefully.

By utilizing `pushd`, you can enhance your command-line navigation efficiency, making it easier to work across multiple directories.