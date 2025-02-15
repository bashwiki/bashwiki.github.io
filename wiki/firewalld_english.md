# [리눅스] Bash firewalld 사용법

## Overview
`firewalld` is a dynamic firewall management tool that provides a way to configure the Linux kernel's netfilter framework. Its primary purpose is to manage firewall rules in a more user-friendly manner compared to traditional iptables. `firewalld` supports both IPv4 and IPv6 and allows for the use of zones to define the trust level of network connections or interfaces. This makes it easier for engineers and developers to secure their systems while maintaining flexibility in network configurations.

## Usage
The basic syntax for using `firewalld` is as follows:

```bash
firewalld [OPTIONS]
```

Common options include:

- `--start`: Start the firewalld service.
- `--stop`: Stop the firewalld service.
- `--reload`: Reload the firewalld configuration.
- `--status`: Display the current status of the firewalld service.
- `--zone=<zone>`: Specify the zone to which you want to apply rules.
- `--add-service=<service>`: Add a predefined service to a zone.
- `--remove-service=<service>`: Remove a predefined service from a zone.
- `--add-port=<port>/<protocol>`: Open a specific port for a given protocol (e.g., TCP or UDP).
- `--remove-port=<port>/<protocol>`: Close a specific port.

## Examples

### Example 1: Starting the firewalld Service
To start the `firewalld` service, you can use the following command:

```bash
sudo systemctl start firewalld
```

### Example 2: Adding a Service to a Zone
To allow HTTP traffic through the firewall, you can add the `http` service to the default zone:

```bash
sudo firewall-cmd --zone=public --add-service=http --permanent
```

After adding the service, remember to reload the firewall to apply the changes:

```bash
sudo firewall-cmd --reload
```

## Tips
- Always check the current status of `firewalld` with `firewall-cmd --state` to ensure it is running before making changes.
- Use the `--permanent` option when adding or removing services or ports to ensure that changes persist after a reboot.
- To view the current configuration and rules in a specific zone, use the command `firewall-cmd --zone=<zone> --list-all`.
- Consider using the `--add-rich-rule` option for more complex firewall rules that require specific conditions or actions. 

By following these guidelines, you can effectively manage your firewall settings using `firewalld` in a Linux environment.