# [리눅스] Bash route 사용법

## Overview
The `route` command in Bash is used to view and manipulate the IP routing table in Linux and Unix-like operating systems. Its primary purpose is to display the current routing table, add new routes, or delete existing routes. This command is essential for network configuration and troubleshooting, allowing engineers and developers to manage how data packets are directed through a network.

## Usage
The basic syntax of the `route` command is as follows:

```bash
route [OPTION] [COMMAND] [ARGUMENTS]
```

### Common Options
- `-n`: Show numerical addresses instead of resolving hostnames.
- `add`: Add a new route to the routing table.
- `del`: Delete a route from the routing table.
- `-net`: Specify that the route is for a network.
- `-host`: Specify that the route is for a single host.
- `gw`: Specify the gateway for the route.

## Examples

### Example 1: Displaying the Routing Table
To display the current routing table in a numerical format, you can use the following command:

```bash
route -n
```

This command will output the routing table without resolving hostnames, showing the destination, gateway, and interface information.

### Example 2: Adding a New Route
To add a new route to a specific network through a designated gateway, you can use the following command:

```bash
route add -net 192.168.1.0/24 gw 192.168.0.1
```

In this example, a route is added for the network `192.168.1.0` with a subnet mask of `255.255.255.0` (indicated by `/24`), directing traffic through the gateway `192.168.0.1`.

### Example 3: Deleting a Route
To delete a previously added route, you can use the command:

```bash
route del -net 192.168.1.0/24
```

This command will remove the route for the network `192.168.1.0`.

## Tips
- Always use the `-n` option when displaying the routing table if you want faster output without DNS resolution delays.
- Be cautious when adding or deleting routes, as incorrect configurations can lead to network connectivity issues.
- Use the `route` command in conjunction with other networking tools like `ping` and `traceroute` for effective network troubleshooting.
- Consider using `ip route` as a more modern alternative to `route`, as it provides more features and better syntax for managing routes.