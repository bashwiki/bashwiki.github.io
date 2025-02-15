# [리눅스] Bash traceroute 사용법

## Overview
The `traceroute` command is a network diagnostic tool used to trace the path that packets take from one host to another across an IP network. It provides insight into the route taken by the packets, including the intermediate hops and the time taken for each hop. This information is invaluable for troubleshooting network issues, understanding network topology, and optimizing routing.

## Usage
The basic syntax for the `traceroute` command is as follows:

```bash
traceroute [options] <destination>
```

### Common Options:
- `-m <max_ttl>`: Sets the maximum time-to-live (TTL) for the packets. The default is 30 hops.
- `-p <port>`: Specifies the destination port to use for the probe packets. The default is 33434.
- `-w <timeout>`: Sets the time to wait for a response, in seconds. The default is 5 seconds.
- `-q <nqueries>`: Specifies the number of probe packets to send per hop. The default is 3.
- `-I`: Uses ICMP ECHO for probes instead of UDP datagrams (useful for some firewalls).
- `-T`: Uses TCP SYN packets instead of UDP (helpful for bypassing certain network restrictions).

## Examples
### Example 1: Basic Traceroute
To perform a basic traceroute to `example.com`, you would use the following command:

```bash
traceroute example.com
```

This command will display the route taken by packets to reach `example.com`, showing each hop along the way.

### Example 2: Traceroute with Custom TTL
If you want to set a maximum TTL of 15, you can use the `-m` option:

```bash
traceroute -m 15 example.com
```

This command will limit the number of hops displayed to 15, which can be useful for quickly identifying the route without overwhelming output.

## Tips
- **Use with `sudo`**: Depending on your system configuration, you might need to run `traceroute` with elevated privileges to access certain network functionalities. Use `sudo traceroute <destination>` if you encounter permission issues.
- **Analyze Latency**: Pay attention to the time taken for each hop. Significant delays at a particular hop can indicate network congestion or issues with that specific router.
- **Combine with Other Tools**: Consider using `ping` in conjunction with `traceroute` to diagnose network issues more effectively. While `traceroute` shows the path, `ping` can help determine the reachability and response time of each hop.
- **Firewall Considerations**: Be aware that some networks may block `traceroute` packets, especially if using UDP. In such cases, try using the `-I` or `-T` options to switch to ICMP or TCP, respectively.

By understanding and effectively utilizing the `traceroute` command, engineers and developers can gain valuable insights into network performance and troubleshoot connectivity issues more efficiently.