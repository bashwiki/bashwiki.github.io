# [리눅스] Bash tcpdump 사용법

## Overview
`tcpdump` is a powerful command-line packet analyzer tool used to capture and display network packets transmitted over a network. It allows engineers and developers to monitor network traffic in real-time, troubleshoot network issues, and analyze the data packets for various protocols. By capturing packets, users can gain insights into network performance, security vulnerabilities, and communication patterns between devices.

## Usage
The basic syntax for the `tcpdump` command is as follows:

```bash
tcpdump [options] [expression]
```

### Common Options:
- `-i <interface>`: Specify the network interface to listen on (e.g., `eth0`, `wlan0`).
- `-n`: Do not resolve hostnames; display IP addresses instead.
- `-v`, `-vv`, `-vvv`: Increase the verbosity of the output for more detailed information.
- `-c <count>`: Capture only a specified number of packets and then stop.
- `-w <file>`: Write the captured packets to a file for later analysis.
- `-r <file>`: Read packets from a previously saved file instead of capturing live traffic.
- `-s <snaplen>`: Set the snapshot length, which determines the amount of data captured for each packet.

## Examples

### Example 1: Capture Live Traffic
To capture live traffic on the `eth0` interface and display it in the terminal, use the following command:

```bash
tcpdump -i eth0
```

This command will show all packets transmitted over the `eth0` interface in real-time.

### Example 2: Capture and Save to a File
To capture packets and save them to a file named `capture.pcap`, use the following command:

```bash
tcpdump -i eth0 -w capture.pcap
```

This command captures all packets on the `eth0` interface and writes them to the `capture.pcap` file for later analysis.

## Tips
- Use the `-n` option to avoid DNS resolution, which can slow down the packet capture process and clutter the output with hostnames.
- Combine the `-c` option with the `-i` option to limit the number of packets captured, which is useful for quick tests or when troubleshooting specific issues.
- When analyzing captured packets, use the `-r` option to read from a saved file, allowing you to review the data without needing to capture live traffic again.
- For more detailed output, consider using the `-vvv` option to increase verbosity, which can help in understanding the packet structure and contents.
- Always ensure you have the necessary permissions to capture packets on the specified interface, as `tcpdump` may require root privileges.