# [Linux] Bash ss Usage Equivalent: Display socket statistics

## Overview
The `ss` command is a powerful utility in Linux that provides detailed information about network sockets. It is used to investigate and analyze network connections, showing both listening and established sockets. `ss` is often preferred over older tools like `netstat` due to its speed and ability to provide more detailed information.

## Usage
The basic syntax of the `ss` command is as follows:

```bash
ss [options] [arguments]
```

## Common Options
- `-t`: Display TCP sockets.
- `-u`: Display UDP sockets.
- `-l`: Show listening sockets.
- `-p`: Show the process using the socket.
- `-n`: Show numerical addresses instead of resolving hostnames.
- `-a`: Display all sockets (both listening and non-listening).
- `-s`: Display summary statistics.

## Common Examples

### Display all TCP sockets
To view all TCP sockets, use the following command:

```bash
ss -t
```

### Show listening UDP sockets
To list all listening UDP sockets, you can run:

```bash
ss -u -l
```

### Display all sockets with process information
To see all sockets along with the associated processes, use:

```bash
ss -a -p
```

### Show numerical addresses
If you want to see the numerical addresses instead of resolving hostnames, you can execute:

```bash
ss -n
```

### Summary of socket statistics
To get a quick summary of socket usage, use:

```bash
ss -s
```

## Tips
- Combine options for more specific queries, such as `ss -t -l` to show only listening TCP sockets.
- Use `ss` in scripts for monitoring network connections, as it provides a quick and efficient way to gather socket information.
- Familiarize yourself with the output format of `ss` to better understand the state of your network connections.