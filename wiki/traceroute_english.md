# [Linux] Bash traceroute Uso: Trace the path of network packets

## Overview
The `traceroute` command is a network diagnostic tool used to track the path that packets take from your computer to a specified destination on the internet. It provides information about each hop along the route, including the time taken for each segment, which can help identify network issues.

## Usage
The basic syntax of the `traceroute` command is as follows:

```bash
traceroute [options] [destination]
```

## Common Options
- `-m <max_ttl>`: Set the maximum time-to-live (TTL) for packets. This limits the number of hops.
- `-q <nqueries>`: Specify the number of probe packets sent per hop (default is 3).
- `-w <waittime>`: Set the time to wait for a response from each probe (in seconds).
- `-I`: Use ICMP ECHO instead of UDP datagrams.
- `-T`: Use TCP SYN packets instead of UDP.

## Common Examples
Here are some practical examples of using the `traceroute` command:

1. **Basic Traceroute**
   To trace the route to a website, such as example.com:
   ```bash
   traceroute example.com
   ```

2. **Set Maximum TTL**
   To limit the traceroute to a maximum of 10 hops:
   ```bash
   traceroute -m 10 example.com
   ```

3. **Using ICMP ECHO**
   To perform a traceroute using ICMP ECHO requests:
   ```bash
   traceroute -I example.com
   ```

4. **Specify Number of Probes**
   To send 5 probes per hop:
   ```bash
   traceroute -q 5 example.com
   ```

5. **Set Wait Time**
   To set a wait time of 2 seconds for each probe:
   ```bash
   traceroute -w 2 example.com
   ```

## Tips
- Use `sudo` if you encounter permission issues, as some options may require elevated privileges.
- Combine options to customize your traceroute command for specific needs, such as adjusting the TTL and number of probes.
- Analyze the output carefully; high response times or timeouts may indicate network congestion or issues at specific hops.