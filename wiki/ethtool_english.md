# [Linux] Bash ethtool Uso: Manage network device parameters

## Overview
The `ethtool` command is a powerful utility in Linux used to query and control network device driver and hardware settings. It allows users to retrieve information about network interfaces, configure settings, and diagnose network issues.

## Usage
The basic syntax of the `ethtool` command is as follows:

```bash
ethtool [options] [arguments]
```

## Common Options
- `-s, --set-priv-flags`: Set private flags for the device.
- `-i, --driver`: Display driver information for the specified device.
- `-p, --identify`: Blink the LED on the specified device for identification.
- `-t, --test`: Run self-tests on the specified device.
- `-a, --show-pause`: Show pause frame settings.
- `-S, --statistics`: Display statistics for the specified device.

## Common Examples
Here are some practical examples of using the `ethtool` command:

1. **Display information about a network interface:**
   ```bash
   ethtool eth0
   ```

2. **Show driver information for a specific device:**
   ```bash
   ethtool -i eth0
   ```

3. **Blink the LED on a network interface for identification:**
   ```bash
   ethtool -p eth0
   ```

4. **Display statistics for a network interface:**
   ```bash
   ethtool -S eth0
   ```

5. **Run self-tests on a network interface:**
   ```bash
   ethtool -t eth0
   ```

## Tips
- Always run `ethtool` with root privileges for full access to all features.
- Use `man ethtool` to access the manual and explore more options and detailed usage.
- Combine `ethtool` with other network diagnostic tools like `ping` or `traceroute` for comprehensive network troubleshooting.