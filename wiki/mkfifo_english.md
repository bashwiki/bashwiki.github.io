# [리눅스] Bash mkfifo 사용법

## Overview
The `mkfifo` command in Bash is used to create named pipes, also known as FIFOs (First In, First Out). Named pipes allow for inter-process communication (IPC) by enabling data to be passed between processes in a unidirectional manner. When one process writes to the named pipe, another process can read from it, facilitating a synchronized data flow without the need for temporary files.

## Usage
The basic syntax for the `mkfifo` command is as follows:

```bash
mkfifo [OPTION]... NAME...
```

### Common Options
- `-m, --mode=MODE`: Set the file mode (permissions) of the created FIFO. The mode can be specified in octal format (e.g., `0666`).
- `--help`: Display help information about the command and its options.
- `--version`: Show the version information of the `mkfifo` command.

## Examples

### Example 1: Creating a Simple Named Pipe
To create a named pipe called `myfifo`, you can use the following command:

```bash
mkfifo myfifo
```

After executing this command, you can use `myfifo` in other processes to read from or write to it.

### Example 2: Using a Named Pipe for Communication
Here’s an example of how to use a named pipe for communication between two terminal sessions.

1. In the first terminal, create a named pipe:

   ```bash
   mkfifo myfifo
   ```

2. In the first terminal, use the `cat` command to read from the pipe:

   ```bash
   cat myfifo
   ```

3. In the second terminal, write to the named pipe:

   ```bash
   echo "Hello, World!" > myfifo
   ```

4. The first terminal will display the message "Hello, World!" as it is read from the named pipe.

## Tips
- **Permissions**: When creating a FIFO, consider setting appropriate permissions using the `-m` option to control who can read from or write to the pipe.
- **Cleanup**: Remember to remove the named pipe using the `rm` command when it is no longer needed to avoid clutter in your filesystem.
- **Blocking Behavior**: Be aware that reading from a FIFO will block until there is data to read, and writing to a FIFO will block until there is a reader. This behavior can be useful for synchronizing processes.
- **Debugging**: If you encounter issues with processes not communicating as expected, check if the named pipe exists and if the permissions are set correctly.