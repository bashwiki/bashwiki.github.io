# [Linux] Bash ip uso equivalente: Manage network interfaces and routing

## Overview
The `ip` command is a powerful utility in Linux used for managing network interfaces, routing, and network configurations. It allows users to view and manipulate various aspects of the network stack, including IP addresses, routes, and link settings.

## Usage
The basic syntax of the `ip` command is as follows:

```bash
ip [options] [arguments]
```

## Common Options
- `link`: Manage network interfaces (e.g., enable, disable).
- `addr`: Display or manipulate IP addresses.
- `route`: Manage the routing table.
- `neigh`: Manage the ARP table.
- `maddr`: Manage multicast addresses.

## Common Examples

### Show all network interfaces
To display all network interfaces and their statuses, use:
```bash
ip link show
```

### Add an IP address to an interface
To assign an IP address to a specific interface, use:
```bash
ip addr add 192.168.1.10/24 dev eth0
```

### Delete an IP address from an interface
To remove an IP address from an interface, use:
```bash
ip addr del 192.168.1.10/24 dev eth0
```

### Show the routing table
To view the current routing table, use:
```bash
ip route show
```

### Add a new route
To add a new route to a specific network, use:
```bash
ip route add 10.0.0.0/24 via 192.168.1.1
```

### Delete a route
To remove a route from the routing table, use:
```bash
ip route del 10.0.0.0/24
```

## Tips
- Use `ip -h` to display help and see all available options and commands.
- Always ensure you have the necessary permissions (often root) to modify network settings.
- When troubleshooting network issues, use `ip addr` and `ip route` to quickly gather information about interfaces and routing.