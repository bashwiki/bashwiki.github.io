# [Linux] Bash tcpdump Uso: Capture network packets

## Overview
The `tcpdump` command is a powerful network packet analyzer that allows users to capture and display the packets being transmitted or received over a network. It is widely used for network troubleshooting, analysis, and security monitoring.

## Usage
The basic syntax of the `tcpdump` command is as follows:

```bash
tcpdump [options] [arguments]
```

## Common Options
- `-i <interface>`: Specify the network interface to listen on (e.g., `eth0`, `wlan0`).
- `-n`: Disable DNS resolution to show IP addresses instead of hostnames.
- `-c <count>`: Capture only a specified number of packets.
- `-w <file>`: Write the captured packets to a file for later analysis.
- `-r <file>`: Read packets from a previously saved file.
- `-v`, `-vv`, `-vvv`: Increase the verbosity of the output for more detailed information.

## Common Examples
1. **Capture packets on a specific interface:**
   ```bash
   tcpdump -i eth0
   ```

2. **Capture a limited number of packets:**
   ```bash
   tcpdump -i eth0 -c 10
   ```

3. **Capture packets and write them to a file:**
   ```bash
   tcpdump -i eth0 -w capture.pcap
   ```

4. **Read packets from a file:**
   ```bash
   tcpdump -r capture.pcap
   ```

5. **Capture packets without resolving hostnames:**
   ```bash
   tcpdump -i eth0 -n
   ```

6. **Capture only TCP packets:**
   ```bash
   tcpdump -i eth0 tcp
   ```

## Tips
- Always run `tcpdump` with appropriate permissions (often requires root access).
- Use the `-v` option for more detailed output, especially when troubleshooting.
- Filter packets by port or protocol to reduce noise in the output (e.g., `tcpdump -i eth0 port 80`).
- Save captured packets to a file for later analysis with tools like Wireshark.