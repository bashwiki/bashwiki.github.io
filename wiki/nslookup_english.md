# [리눅스] Bash nslookup 사용법

## Overview
The `nslookup` command is a network utility used to query the Domain Name System (DNS) to obtain domain name or IP address mapping information. Its primary purpose is to help users troubleshoot DNS-related issues by allowing them to look up DNS records for a specified domain or IP address. This command can be particularly useful for network engineers and developers when diagnosing connectivity problems or verifying DNS configurations.

## Usage
The basic syntax of the `nslookup` command is as follows:

```bash
nslookup [options] [hostname | IP address]
```

### Common Options
- `-type=TYPE`: Specifies the type of DNS record to query (e.g., A, AAAA, MX, CNAME, etc.). If not specified, the default type is A (IPv4 address).
- `-debug`: Provides detailed information about the query process, which can be helpful for troubleshooting.
- `-timeout=seconds`: Sets the time to wait for a response from the DNS server.
- `-port=port`: Specifies the port number to use for the DNS query (default is 53).
- `server`: Allows you to specify a different DNS server to query instead of the default one.

## Examples
### Example 1: Basic Domain Lookup
To look up the IP address of a domain, you can use the following command:

```bash
nslookup example.com
```

This command will return the IP address associated with `example.com`, along with other relevant DNS information.

### Example 2: Querying a Specific DNS Record Type
If you want to find the mail exchange (MX) records for a domain, you can specify the record type like this:

```bash
nslookup -type=MX example.com
```

This command will return the MX records for `example.com`, showing the mail servers responsible for handling email for that domain.

## Tips
- Use the `-debug` option to gain insights into the DNS resolution process, especially when troubleshooting issues.
- If you frequently query a specific DNS server, consider specifying it directly in your command to avoid relying on the default server.
- Remember that DNS changes can take time to propagate; if you don't see expected results, it may be worth waiting or checking the TTL (Time to Live) settings for the records.
- For more comprehensive DNS diagnostics, consider using `dig`, which provides more detailed output and additional functionality compared to `nslookup`.