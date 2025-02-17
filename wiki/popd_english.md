# [Linux] Bash popd Uso equivalente: Remove directories from the stack

The `popd` command is used to remove directories from the directory stack in Bash, allowing users to navigate back to previous directories easily.

## Overview
The `popd` command is part of the directory stack management in Bash. It allows users to remove the top directory from the stack and change the current working directory to that directory. This is particularly useful for managing multiple directories without needing to type out full paths.

## Usage
The basic syntax of the `popd` command is as follows:

```bash
popd [options] [arguments]
```

## Common Options
- `+N`: Removes the N-th directory from the stack and changes to it. The counting starts from 0.
- `-N`: Removes the N-th directory from the stack but does not change to it.

## Common Examples
Here are some practical examples of using the `popd` command:

1. **Basic Usage**: Remove the top directory from the stack and change to it.
   ```bash
   popd
   ```

2. **Using with a specific directory**: Remove the second directory from the stack and change to it.
   ```bash
   popd +1
   ```

3. **Removing without changing**: Remove the top directory from the stack without changing to it.
   ```bash
   popd -0
   ```

4. **Combining with pushd**: Push a directory onto the stack and then pop it off.
   ```bash
   pushd /path/to/directory
   popd
   ```

## Tips
- Use `dirs` to view the current directory stack before using `popd` to understand which directory will be removed.
- Combine `pushd` and `popd` for efficient navigation when working with multiple directories.
- Remember that the directory stack is session-specific; if you close your terminal, the stack will be lost.