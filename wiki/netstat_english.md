# [Linux] Bash netstat Uso: Monitor network connections and statistics

## Overview
The `netstat` command is a powerful tool used in Linux and other Unix-like operating systems to display network connections, routing tables, interface statistics, masquerade connections, and multicast memberships. It helps users understand the current state of the network and troubleshoot connectivity issues.

## Usage
The basic syntax of the `netstat` command is as follows:

```bash
netstat [options] [arguments]
```

## Common Options
Here are some commonly used options with the `netstat` command:

- `-a`: Show all connections and listening ports.
- `-t`: Display TCP connections.
- `-u`: Display UDP connections.
- `-n`: Show numerical addresses instead of resolving hostnames.
- `-l`: Show only listening sockets.
- `-p`: Show the process ID and name of the program to which each socket belongs.
- `-r`: Display the routing table.

## Common Examples

1. **Display all active connections:**
   ```bash
   netstat -a
   ```

2. **Show only TCP connections:**
   ```bash
   netstat -t
   ```

3. **Show only listening ports:**
   ```bash
   netstat -l
   ```

4. **Display connections with numerical addresses:**
   ```bash
   netstat -n
   ```

5. **Show the process using each connection:**
   ```bash
   netstat -p
   ```

6. **Display the routing table:**
   ```bash
   netstat -r
   ```

## Tips
- Combine options for more detailed output. For example, `netstat -tuln` will show all listening TCP and UDP ports with numerical addresses.
- Use `grep` to filter results. For example, `netstat -a | grep LISTEN` will show only listening connections.
- Regularly monitor your network connections to identify any unauthorized access or unusual activity.