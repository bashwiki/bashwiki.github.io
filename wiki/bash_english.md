# [리눅스] Bash bash 사용법

## Overview
The `bash` command is the command-line interpreter for the Bourne Again SHell (Bash), which is a widely used shell in Linux and Unix-like operating systems. It serves as both a command processor and a scripting language interpreter. Its primary purpose is to allow users to execute commands, run scripts, and manage system tasks through a command-line interface. Bash provides features such as command history, job control, and shell functions, making it a powerful tool for engineers and developers.

## Usage
The basic syntax for the `bash` command is as follows:

```bash
bash [options] [file]
```

### Common Options:
- `-c`: This option allows you to pass a command as a string to be executed by the shell.
- `-i`: This option starts an interactive shell session.
- `-l`: This option starts a login shell, which reads the user's profile scripts.
- `-s`: This option reads commands from standard input.

## Examples

### Example 1: Starting an Interactive Shell
To start a new interactive Bash shell session, simply type:

```bash
bash
```

This will open a new shell prompt where you can enter commands as you would in your default shell.

### Example 2: Executing a Command from a String
You can execute a command directly from the command line by using the `-c` option. For example, to list the contents of the current directory, you can run:

```bash
bash -c "ls -l"
```

This command will execute `ls -l` and display the output in the terminal.

## Tips
- When running scripts, ensure that the script file has execute permissions. You can set this using `chmod +x script.sh`.
- Use `bash -i` for debugging scripts interactively, as it allows you to test commands in a live environment.
- To exit a Bash session, simply type `exit` or press `Ctrl+D`.
- Familiarize yourself with Bash scripting to automate repetitive tasks and improve efficiency in your development workflow.