# [Linux] Bash dirs Uso equivalente: Manage directory stack

## Overview
The `dirs` command in Bash is used to display the list of currently stored directories in the directory stack. It helps users keep track of their navigation history within the terminal, allowing for easy access to previously visited directories.

## Usage
The basic syntax of the `dirs` command is as follows:

```bash
dirs [options] [arguments]
```

## Common Options
- `-l`: Displays the directory stack in a long format, showing the full path for each directory.
- `-p`: Prints the directory stack without modifying it.
- `-c`: Clears the directory stack.

## Common Examples

1. **Display the current directory stack:**
   ```bash
   dirs
   ```

2. **Display the directory stack in long format:**
   ```bash
   dirs -l
   ```

3. **Clear the directory stack:**
   ```bash
   dirs -c
   ```

4. **Display the directory stack without modifying it:**
   ```bash
   dirs -p
   ```

5. **Using `pushd` and `popd` with `dirs`:**
   After using `pushd` to navigate to a new directory, you can check the stack:
   ```bash
   pushd /path/to/directory
   dirs
   popd
   ```

## Tips
- Use `pushd` and `popd` in conjunction with `dirs` to effectively manage your directory stack.
- Regularly check your directory stack with `dirs` to avoid confusion about your current location in the file system.
- Remember that the directory stack is a feature of the shell, so it will reset if you start a new terminal session.