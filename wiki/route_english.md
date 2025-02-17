# [Linux] Bash route usage: Manage network routing tables

## Overview
The `route` command is used to view and manipulate the IP routing table in Linux-based systems. It allows users to display the current routing table, add new routes, or delete existing ones, which is essential for network configuration and management.

## Usage
The basic syntax of the `route` command is as follows:

```bash
route [options] [arguments]
```

## Common Options
- `-n`: Show numerical addresses instead of resolving hostnames.
- `add`: Add a new route to the routing table.
- `del`: Remove a route from the routing table.
- `-net`: Specify that the route is for a network.
- `-host`: Specify that the route is for a single host.
- `gw`: Specify a gateway for the route.

## Common Examples

1. **Display the current routing table:**
   ```bash
   route -n
   ```

2. **Add a new route to a specific network:**
   ```bash
   route add -net 192.168.1.0/24 gw 192.168.1.1
   ```

3. **Add a route to a specific host:**
   ```bash
   route add -host 10.0.0.5 gw 10.0.0.1
   ```

4. **Delete an existing route:**
   ```bash
   route del -net 192.168.1.0/24
   ```

5. **Add a default gateway:**
   ```bash
   route add default gw 192.168.1.1
   ```

## Tips
- Always use the `-n` option when displaying the routing table to speed up the output by avoiding DNS lookups.
- Be cautious when adding or deleting routes, as incorrect configurations can lead to network connectivity issues.
- Use `ip route` as a more modern alternative to `route`, as it provides more features and flexibility for managing routing tables.