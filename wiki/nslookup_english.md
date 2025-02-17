# [Linux] Bash nslookup Uso: Query DNS records

## Overview
The `nslookup` command is a network utility used to query Domain Name System (DNS) records. It allows users to obtain information about domain names, IP addresses, and other DNS-related data, making it a valuable tool for troubleshooting network issues and verifying DNS configurations.

## Usage
The basic syntax of the `nslookup` command is as follows:

```bash
nslookup [options] [arguments]
```

## Common Options
- `-type=TYPE`: Specifies the type of DNS record to query (e.g., A, AAAA, MX, TXT).
- `-debug`: Enables debugging mode to provide more detailed output.
- `-timeout=SECONDS`: Sets the time to wait for a response before timing out.
- `-port=PORT`: Specifies the port number to use for the DNS query (default is 53).

## Common Examples

1. **Querying an A record:**
   To find the IP address associated with a domain name:
   ```bash
   nslookup example.com
   ```

2. **Querying a specific DNS record type:**
   To retrieve the MX (Mail Exchange) records for a domain:
   ```bash
   nslookup -type=MX example.com
   ```

3. **Using a specific DNS server:**
   To query a specific DNS server (e.g., Google's public DNS):
   ```bash
   nslookup example.com 8.8.8.8
   ```

4. **Debugging DNS queries:**
   To enable debugging for more detailed output:
   ```bash
   nslookup -debug example.com
   ```

5. **Querying a reverse DNS lookup:**
   To find the domain name associated with an IP address:
   ```bash
   nslookup 93.184.216.34
   ```

## Tips
- Always specify the type of record you are interested in to get more relevant results.
- Use the `-debug` option when troubleshooting to gain insights into the DNS resolution process.
- If you frequently query a specific DNS server, consider setting it as the default in your `nslookup` session for convenience.