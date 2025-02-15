# [리눅스] Bash arp 사용법

## Overview
The `arp` command is a utility in Unix-like operating systems that is used to manipulate the Address Resolution Protocol (ARP) cache. The primary purpose of this command is to display, add, or delete entries in the ARP table, which maps IP addresses to MAC (Media Access Control) addresses. This mapping is crucial for network communication within a local area network (LAN), as it allows devices to locate each other using their hardware addresses.

## Usage
The basic syntax of the `arp` command is as follows:

```bash
arp [options] [hostname]
```

### Common Options
- `-a`: Displays the current ARP entries in a human-readable format.
- `-d hostname`: Deletes the ARP entry for the specified hostname or IP address.
- `-s hostname ether_addr`: Adds a static ARP entry for the specified hostname, mapping it to the given Ethernet address (MAC address).
- `-n`: Displays the ARP entries without resolving hostnames, showing only IP addresses.

## Examples

### Example 1: Displaying ARP Entries
To view the current ARP table, you can use the following command:

```bash
arp -a
```

This will list all the ARP entries, showing the IP addresses and their corresponding MAC addresses.

### Example 2: Adding a Static ARP Entry
If you want to add a static ARP entry for a device, you can use:

```bash
arp -s 192.168.1.10 00:1A:2B:3C:4D:5E
```

This command associates the IP address `192.168.1.10` with the MAC address `00:1A:2B:3C:4D:5E`, ensuring that the system will always resolve this IP to the specified MAC address.

## Tips
- Use the `-n` option when displaying ARP entries if you want to avoid DNS lookups, which can speed up the output and reduce network traffic.
- Regularly check your ARP table, especially in environments with frequent device changes, to ensure that the mappings are accurate and up-to-date.
- Be cautious when adding static ARP entries, as incorrect entries can lead to network communication issues. Always verify the MAC address before adding it to the ARP table.