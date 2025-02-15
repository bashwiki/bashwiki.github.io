# [리눅스] Bash iptables 사용법

## Overview
`iptables` is a powerful command-line utility used in Linux for configuring the IP packet filter rules of the Linux kernel. Its primary purpose is to control the incoming and outgoing network traffic on a system by defining rules that dictate how packets should be handled. This includes allowing or blocking traffic based on various criteria such as IP address, port number, and protocol type. `iptables` is essential for setting up firewalls and enhancing the security of a Linux server.

## Usage
The basic syntax for the `iptables` command is as follows:

```bash
iptables [options] [chain] [rule-specification] [target]
```

### Common Options:
- `-A` or `--append`: Adds a rule to the end of a specified chain.
- `-D` or `--delete`: Deletes a rule from a specified chain.
- `-I` or `--insert`: Inserts a rule at a specified position in a chain.
- `-L` or `--list`: Lists all rules in a specified chain.
- `-F` or `--flush`: Deletes all rules in a specified chain.
- `-P` or `--policy`: Sets the default policy for a specified chain (e.g., ACCEPT or DROP).
- `-s` or `--source`: Specifies the source IP address or network.
- `-d` or `--destination`: Specifies the destination IP address or network.
- `-p` or `--protocol`: Specifies the protocol (e.g., tcp, udp, icmp).

## Examples

### Example 1: Allowing SSH Traffic
To allow incoming SSH traffic on port 22, you can use the following command:

```bash
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```
This command appends a rule to the INPUT chain that accepts TCP packets destined for port 22.

### Example 2: Blocking a Specific IP Address
To block all incoming traffic from a specific IP address (e.g., 192.168.1.100), you can use:

```bash
iptables -A INPUT -s 192.168.1.100 -j DROP
```
This command appends a rule to the INPUT chain that drops all packets from the specified source IP.

## Tips
- Always back up your current `iptables` rules before making changes. You can save the current rules to a file using:
  ```bash
  iptables-save > /path/to/backup_file
  ```
- Use `iptables -L -v -n` to view the current rules with verbose output, which includes packet and byte counters.
- Consider using `iptables` in conjunction with `ipset` for managing large sets of IP addresses efficiently.
- Test your rules carefully to avoid accidentally locking yourself out of a remote server, especially when working with SSH.
- Remember that the order of rules matters; `iptables` processes rules in the order they are listed, so place more specific rules before more general ones.