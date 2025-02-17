# [Linux] Bash firewalld uso: Manage firewall settings dynamically

## Overview
The `firewalld` command is a dynamic firewall management tool that provides a way to manage firewall rules without the need to restart the firewall service. It allows users to configure and manage firewall settings in a more flexible manner, supporting both IPv4 and IPv6, as well as Ethernet bridges.

## Usage
The basic syntax of the `firewalld` command is as follows:

```bash
firewalld [options] [arguments]
```

## Common Options
- `--zone=<zone>`: Specify the zone to which the rule applies.
- `--add-service=<service>`: Add a service to the specified zone.
- `--remove-service=<service>`: Remove a service from the specified zone.
- `--add-port=<port>/<protocol>`: Open a specific port for a given protocol (e.g., TCP or UDP).
- `--remove-port=<port>/<protocol>`: Close a specific port for a given protocol.
- `--list-all`: Display all settings for the specified zone.

## Common Examples
Here are some practical examples of using `firewalld`:

1. **Add a service to a zone**:
   To allow HTTP traffic in the public zone:
   ```bash
   firewall-cmd --zone=public --add-service=http
   ```

2. **Remove a service from a zone**:
   To block HTTP traffic in the public zone:
   ```bash
   firewall-cmd --zone=public --remove-service=http
   ```

3. **Open a specific port**:
   To open port 8080 for TCP traffic:
   ```bash
   firewall-cmd --zone=public --add-port=8080/tcp
   ```

4. **Close a specific port**:
   To close port 8080 for TCP traffic:
   ```bash
   firewall-cmd --zone=public --remove-port=8080/tcp
   ```

5. **List all settings for a zone**:
   To view all configurations in the public zone:
   ```bash
   firewall-cmd --zone=public --list-all
   ```

## Tips
- Always check the current firewall settings before making changes using `firewall-cmd --list-all`.
- Use the `--permanent` option to make changes persistent across reboots. For example:
  ```bash
  firewall-cmd --zone=public --add-service=http --permanent
  ```
- After making permanent changes, remember to reload the firewall to apply them:
  ```bash
  firewall-cmd --reload
  ```