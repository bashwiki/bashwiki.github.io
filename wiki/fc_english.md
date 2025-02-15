# [리눅스] Bash fc 사용법

## Overview
The `fc` command in Bash is a built-in utility that allows users to list, edit, and re-execute commands from the shell's history. Its primary purpose is to facilitate the correction and re-execution of previous commands, making it a valuable tool for developers and engineers who frequently work in the command line environment. By using `fc`, users can easily access and modify commands without needing to retype them entirely.

## Usage
The basic syntax for the `fc` command is as follows:

```bash
fc [options] [first] [last]
```

### Common Options:
- `-l`: List the commands in the history. You can specify a range of commands by providing two numbers (e.g., `fc -l 10 20` lists commands 10 to 20).
- `-r`: Reverses the order of the commands when listing them.
- `-s`: Re-executes the last command without opening an editor.
- `-n`: Suppresses the command numbers when listing.

If no arguments are provided, `fc` will edit the last command in the history by default.

## Examples

### Example 1: Listing Commands
To list the last 5 commands from your history, you can use:

```bash
fc -l -5
```

This command will display the last 5 commands you executed, allowing you to see what you might want to re-run or modify.

### Example 2: Editing and Re-executing a Command
Suppose you want to edit the last command you executed. You can simply run:

```bash
fc
```

This will open the last command in your default text editor (usually `vi` or `nano`). After making your changes, save and exit the editor, and the modified command will be executed automatically.

## Tips
- Use `fc -l` to quickly review your command history and find commands that you may want to reuse or modify.
- Combine `fc` with other command-line tools like `grep` to filter through your history for specific commands. For example:

  ```bash
  history | grep "git"
  ```

- Familiarize yourself with your default text editor, as `fc` will open commands in that editor for modification. If you prefer a different editor, you can change the `EDITOR` environment variable.
- Remember that `fc` operates on the command history, so ensure your history settings are configured to retain the commands you want to access later.