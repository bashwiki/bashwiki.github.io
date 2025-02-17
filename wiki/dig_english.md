# [Linux] Bash dig Uso: DNS lookup tool

## Overview
The `dig` command, short for "Domain Information Groper," is a powerful tool used for querying DNS (Domain Name System) records. It allows users to retrieve various types of DNS information, including A records, MX records, and more, making it essential for network troubleshooting and domain management.

## Usage
The basic syntax of the `dig` command is as follows:

```bash
dig [options] [arguments]
```

## Common Options
- `@server`: Specify a DNS server to query (e.g., `@8.8.8.8` for Google DNS).
- `-t type`: Specify the type of DNS record to query (e.g., `A`, `MX`, `TXT`).
- `+short`: Display a simplified output with only the answer.
- `+trace`: Follow the delegation path from the root DNS servers to the queried domain.

## Common Examples
Here are some practical examples of using the `dig` command:

1. **Querying an A Record:**
   ```bash
   dig example.com
   ```

2. **Querying an MX Record:**
   ```bash
   dig -t MX example.com
   ```

3. **Using a Specific DNS Server:**
   ```bash
   dig @8.8.8.8 example.com
   ```

4. **Getting a Short Answer:**
   ```bash
   dig +short example.com
   ```

5. **Tracing the DNS Resolution Path:**
   ```bash
   dig +trace example.com
   ```

## Tips
- Use the `+short` option for quick lookups when you only need the answer without additional details.
- When troubleshooting DNS issues, the `+trace` option can help identify where the resolution is failing.
- Always specify a DNS server if you suspect issues with your local resolver to get a different perspective on the DNS records.