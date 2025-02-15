# [리눅스] Bash popd 사용법

## Overview
The `popd` command is a built-in command in Bash that is used to remove the top directory from the directory stack and change the current working directory to that directory. It is primarily used in conjunction with the `pushd` command, which adds directories to the stack. This allows users to easily navigate between multiple directories without needing to type out full paths.

## Usage
The basic syntax of the `popd` command is as follows:

```bash
popd [options]
```

### Common Options
- `+N`: Removes the N-th directory from the stack, counting from the left (0-based index), and changes to that directory.
- `-N`: Removes the N-th directory from the stack, counting from the right (0-based index), and changes to that directory.

If no options are provided, `popd` will remove the top directory from the stack.

## Examples

### Example 1: Basic Usage
1. First, use `pushd` to add directories to the stack:
   ```bash
   pushd /path/to/first-directory
   pushd /path/to/second-directory
   ```
2. Now, use `popd` to return to the first directory:
   ```bash
   popd
   ```
   After executing this command, your current working directory will be `/path/to/first-directory`.

### Example 2: Using Index with popd
1. Push multiple directories onto the stack:
   ```bash
   pushd /path/to/first-directory
   pushd /path/to/second-directory
   pushd /path/to/third-directory
   ```
2. Use `popd` with an index to go back to the first directory:
   ```bash
   popd +1
   ```
   This command will remove the second directory from the stack and change the current working directory to `/path/to/second-directory`.

## Tips
- Use `dirs` command to view the current directory stack before using `popd`. This can help you understand the order of directories and make informed decisions about which directory to pop.
- Combine `pushd` and `popd` in scripts to create temporary working environments without cluttering your command history with full path changes.
- Remember that the directory stack is session-specific; once you close your terminal, the stack will be lost.