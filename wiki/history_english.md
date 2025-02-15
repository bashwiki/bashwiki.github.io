# [리눅스] Bash history 사용법

## Overview
The `history` command in Bash is used to display the command history for the current shell session. Its primary purpose is to allow users to view, manage, and reuse previously executed commands, which can significantly enhance productivity and efficiency when working in the terminal. By keeping a record of commands, users can easily recall and execute them without needing to retype them, thereby saving time and reducing errors.

## Usage
The basic syntax of the `history` command is as follows:

```bash
history [n]
```

Where `n` is an optional argument that specifies the number of recent commands to display. If no argument is provided, the command will display the entire history list.

### Common Options
- `-c`: Clears the entire command history.
- `-d offset`: Deletes the history entry at the specified offset.
- `-a`: Appends the current session's history to the history file.
- `-r`: Reads the history from the history file and adds it to the current session.
- `-n`: Reads new history lines from the history file, ignoring lines already in the current session.

## Examples

### Example 1: Displaying Recent Commands
To display the last 10 commands executed in the current session, you can use:

```bash
history 10
```

This command will output the last 10 commands along with their corresponding history numbers.

### Example 2: Re-executing a Command
If you want to re-execute a specific command from your history, you can use the `!` followed by the history number. For instance, if the command you want to re-execute is number 25 in your history, you would type:

```bash
!25
```

This will execute the command associated with that history number.

## Tips
- Use the `Ctrl + R` shortcut to initiate a reverse search through your command history. This allows you to quickly find and execute previous commands without scrolling through the entire history list.
- Regularly clear your history with `history -c` if you are concerned about privacy or security, especially on shared systems.
- Consider using `history -a` at the end of your session to ensure that all commands are saved to your history file, making them available in future sessions.
- You can customize the size of your history by modifying the `HISTSIZE` and `HISTFILESIZE` variables in your `.bashrc` file. This allows you to keep a larger or smaller history as per your preference.