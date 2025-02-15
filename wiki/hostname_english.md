# [리눅스] Bash hostname 사용법

## Overview
The `hostname` command in Bash is used to display or set the system's hostname. The hostname is a label that identifies a device on a network, allowing it to communicate with other devices. This command is essential for network configuration and management, particularly in multi-device environments.

## Usage
The basic syntax of the `hostname` command is as follows:

```bash
hostname [OPTION] [NEW_HOSTNAME]
```

### Common Options:
- `-a`, `--alias`: Display the alias name of the host.
- `-d`, `--domain`: Display the domain name of the host.
- `-f`, `--fqdn`, `--long`: Display the fully qualified domain name (FQDN).
- `-i`, `--ip-address`: Display the IP address associated with the hostname.
- `-s`, `--short`: Display the short hostname (the hostname without the domain).
- `--help`: Display help information about the command.
- `--version`: Show the version of the command.

If the `NEW_HOSTNAME` argument is provided, the command will set the hostname to the specified value.

## Examples

### Example 1: Displaying the Current Hostname
To simply display the current hostname of the system, you can run:

```bash
hostname
```

This command will output the current hostname, which is useful for quickly identifying the device.

### Example 2: Setting a New Hostname
To set a new hostname, you can use the following command (note that you may need superuser privileges):

```bash
sudo hostname new-hostname
```

After executing this command, the hostname will be changed to `new-hostname`. To verify the change, you can run `hostname` again.

## Tips
- Always ensure you have the necessary permissions (usually root) when changing the hostname.
- After changing the hostname, consider updating the `/etc/hosts` file to reflect the new hostname for proper name resolution.
- Use the `hostname -f` command to verify the fully qualified domain name after making changes.
- Remember that changes made with the `hostname` command are temporary and may revert after a reboot unless configured in the system's network settings. For permanent changes, consider editing the `/etc/hostname` file.