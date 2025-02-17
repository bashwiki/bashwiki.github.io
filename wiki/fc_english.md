# [Linux] Bash fc Usage: Edit and re-execute commands

## Overview
The `fc` command in Bash is used to list, edit, and re-execute commands from the shell's history. It allows users to modify previous commands before running them again, making it a powerful tool for improving efficiency in the command line.

## Usage
The basic syntax of the `fc` command is as follows:

```bash
fc [options] [arguments]
```

## Common Options
- `-l`: List the commands in the history.
- `-r`: Reverses the order of the commands when listing.
- `-s`: Re-execute the command without opening an editor.
- `-n`: Suppress the command numbers when listing.

## Common Examples

### Listing Recent Commands
To list the last 10 commands from your history:

```bash
fc -l -n -10
```

### Editing a Specific Command
To edit the command with history number 42:

```bash
fc 42
```

This will open the command in your default text editor for modification.

### Re-executing the Last Command
To re-execute the last command without editing:

```bash
fc -s
```

### Listing Commands in Reverse Order
To list the last 5 commands in reverse order:

```bash
fc -r -l -5
```

## Tips
- Use `fc -s` to quickly rerun the last command without needing to edit it, which can save time.
- Familiarize yourself with your default text editor, as `fc` will open commands in that editor for editing.
- Combine `fc` with other commands like `grep` to filter through your command history for specific tasks. For example, `fc -l | grep 'git'` will show all previous Git commands.