# [리눅스] Bash netstat 사용법

## Overview
The `netstat` command is a powerful networking utility in Linux that provides information about network connections, routing tables, interface statistics, masquerade connections, and multicast memberships. Its primary purpose is to help users monitor and troubleshoot network issues by displaying active connections and listening ports, which can be crucial for diagnosing network problems or understanding network traffic.

## Usage
The basic syntax of the `netstat` command is as follows:

```
netstat [options]
```

### Common Options
- `-a`: Displays all active connections and listening ports.
- `-t`: Shows TCP connections only.
- `-u`: Shows UDP connections only.
- `-n`: Displays addresses and port numbers in numerical form instead of resolving hostnames.
- `-l`: Displays only listening sockets.
- `-p`: Shows the process ID and name of the program to which each socket belongs.
- `-r`: Displays the kernel routing table.
- `-i`: Shows a list of network interfaces and their statistics.

## Examples
### Example 1: Displaying All Active Connections
To view all active network connections along with the listening ports, you can use the following command:

```bash
netstat -a
```

This command will list all connections, including both established connections and ports that are currently listening for incoming connections.

### Example 2: Displaying TCP Connections with Process Information
To see only TCP connections and include the associated process information, you can run:

```bash
netstat -t -p
```

This command will provide a list of all TCP connections along with the process ID and name of the application that is using each connection.

## Tips
- Use the `-n` option to speed up the output by avoiding DNS lookups, especially on systems with many connections.
- Combine options for more specific queries, such as `netstat -tunlp`, which shows TCP and UDP connections with process information.
- Regularly monitor your network connections with `netstat` to identify any unauthorized or suspicious activity.
- Consider using `ss` as a modern alternative to `netstat`, as it provides more detailed information and is faster in many cases.