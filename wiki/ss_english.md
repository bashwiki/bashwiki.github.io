# [리눅스] Bash ss 사용법

## Overview
The `ss` command is a utility in Linux used to investigate sockets. It provides detailed information about network connections, including TCP, UDP, and UNIX domain sockets. `ss` is often favored over the older `netstat` command due to its speed and ability to provide more detailed output. Its primary purpose is to help users monitor and troubleshoot network connections and socket usage on their systems.

## Usage
The basic syntax of the `ss` command is as follows:

```
ss [OPTIONS]
```

### Common Options:
- `-t`: Display TCP sockets.
- `-u`: Display UDP sockets.
- `-l`: Show listening sockets.
- `-p`: Show the process using the socket.
- `-n`: Show numerical addresses instead of resolving hostnames.
- `-a`: Display all sockets (listening and non-listening).
- `-s`: Display summary statistics.

## Examples
### Example 1: Display all TCP connections
To view all active TCP connections on your system, you can use the following command:

```bash
ss -t -a
```

This command will list all TCP sockets, both listening and established, along with their respective states.

### Example 2: Show listening UDP sockets with process information
To see which processes are using listening UDP sockets, you can run:

```bash
ss -u -l -p
```

This command will display all listening UDP sockets along with the associated process IDs and names, helping you identify which applications are waiting for incoming UDP traffic.

## Tips
- Use the `-n` option to speed up the output by avoiding DNS lookups, especially useful on systems with many connections.
- Combine options for more specific queries, such as `ss -t -p` to see only TCP sockets with process information.
- Regularly monitor socket usage with `ss` to troubleshoot network issues or to ensure that services are running as expected.