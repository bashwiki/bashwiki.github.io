# [Linux] Bash mkfifo Usage: Create named pipes for inter-process communication

## Overview
The `mkfifo` command in Bash is used to create named pipes, also known as FIFOs (First In, First Out). These special files allow for inter-process communication, enabling different processes to communicate with each other by reading from and writing to the same pipe.

## Usage
The basic syntax of the `mkfifo` command is as follows:

```bash
mkfifo [options] [arguments]
```

## Common Options
- `-m, --mode=MODE`: Set the file mode (permissions) for the created FIFO.
- `-Z, --context=CONTEXT`: Set the SELinux security context for the created FIFO.

## Common Examples

### Create a Simple Named Pipe
To create a named pipe called `myfifo`, you can use the following command:

```bash
mkfifo myfifo
```

### Create a Named Pipe with Specific Permissions
If you want to create a named pipe with specific permissions, you can use the `-m` option. For example, to create a pipe with read and write permissions for the owner and read permissions for others:

```bash
mkfifo -m 644 myfifo
```

### Using a Named Pipe
You can use named pipes to facilitate communication between processes. For example, in one terminal, you can write to the pipe:

```bash
echo "Hello, World!" > myfifo
```

In another terminal, you can read from the pipe:

```bash
cat myfifo
```

### Create Multiple Named Pipes
You can create multiple named pipes at once by specifying multiple names:

```bash
mkfifo pipe1 pipe2 pipe3
```

## Tips
- Always ensure that the named pipe is created in a directory where you have the necessary permissions.
- Remember that reading from a named pipe will block until there is data to read, and writing to a named pipe will block until there is a reader.
- Clean up your named pipes after use to avoid cluttering your filesystem with unused files. You can remove them using the `rm` command:

```bash
rm myfifo
```