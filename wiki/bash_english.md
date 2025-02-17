# [Linux] Bash bash usage: Command-line shell for executing scripts and commands

## Overview
Bash, short for "Bourne Again SHell," is a command-line shell used in many Unix-like operating systems. It allows users to execute commands, run scripts, and manage system tasks efficiently. Bash is widely used for both interactive command-line sessions and scripting.

## Usage
The basic syntax for using bash is as follows:

```bash
bash [options] [arguments]
```

## Common Options
- `-c`: Read commands from the string provided as an argument.
- `-i`: Run an interactive shell session.
- `-l`: Start a login shell.
- `-s`: Read commands from standard input.
- `-v`: Print shell input lines as they are read.

## Common Examples

### Running a Bash Script
To execute a script named `script.sh`, use the following command:

```bash
bash script.sh
```

### Running Commands from a String
You can execute commands directly from the command line using the `-c` option:

```bash
bash -c 'echo "Hello, World!"'
```

### Starting an Interactive Shell
To start an interactive bash session, simply type:

```bash
bash -i
```

### Reading Commands from Standard Input
You can also run bash and read commands from standard input:

```bash
bash -s
```
Then type your commands and press `Ctrl+D` to execute them.

## Tips
- Always check the permissions of your script files to ensure they are executable (`chmod +x script.sh`).
- Use `bash -v` to debug your scripts by printing each command before execution.
- Familiarize yourself with bash scripting basics to automate repetitive tasks effectively.