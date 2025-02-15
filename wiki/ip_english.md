# [리눅스] Bash ip 사용법

## Overview
The `ip` command is a powerful utility used in Linux for managing network interfaces, routing, and various networking configurations. It is part of the `iproute2` package and serves as a modern replacement for older commands like `ifconfig`, `route`, and `arp`. The primary purpose of the `ip` command is to provide a unified interface for network management tasks, allowing users to view and manipulate network settings efficiently.

## Usage
The basic syntax of the `ip` command is as follows:

```
ip [ OPTIONS ] OBJECT { COMMAND | help }
```

- **OPTIONS**: Various options that modify the behavior of the command.
- **OBJECT**: The type of networking object to manage (e.g., `link`, `addr`, `route`, etc.).
- **COMMAND**: The specific action to perform on the object.

### Common Options
- `-h`, `--help`: Display help information.
- `-V`, `--version`: Show version information.
- `-s`, `--statistics`: Display statistics for the specified object.

### Common Objects
- `link`: Manage network interfaces.
- `addr`: Manage IP addresses.
- `route`: Manage routing tables.

## Examples

### Example 1: Displaying Network Interfaces
To list all network interfaces and their statuses, you can use the following command:

```bash
ip link show
```

This command will output a list of all network interfaces, showing their state (up or down) and other relevant information.

### Example 2: Adding an IP Address
To assign an IP address to a network interface (e.g., `eth0`), you can use the following command:

```bash
sudo ip addr add 192.168.1.10/24 dev eth0
```

This command adds the IP address `192.168.1.10` with a subnet mask of `24` to the `eth0` interface.

## Tips
- Always use `sudo` when performing operations that require administrative privileges, such as adding or removing IP addresses.
- Use `ip addr` to quickly check the current IP addresses assigned to all interfaces.
- Familiarize yourself with the various objects and commands available with `ip` by using `ip help` or `man ip` for more detailed documentation.
- Consider using `ip -s` to get statistics along with the standard output, which can be helpful for troubleshooting network issues.