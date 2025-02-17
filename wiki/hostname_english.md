# [Linux] Bash hostname Uso equivalente: Display or set the system's hostname

## Overview
The `hostname` command in Bash is used to display or set the system's hostname, which is the name that identifies the machine on a network. It plays a crucial role in network communication and can be used to configure how the system is recognized by other devices.

## Usage
The basic syntax of the `hostname` command is as follows:

```bash
hostname [options] [arguments]
```

## Common Options
- `-a`, `--alias`: Display the alias name of the host.
- `-d`, `--domain`: Show the domain name of the host.
- `-f`, `--fqdn`: Display the fully qualified domain name (FQDN).
- `-i`, `--ip-address`: Show the IP address associated with the hostname.
- `-s`, `--short`: Display the short hostname (without domain).
- `-V`, `--version`: Show the version of the hostname command.

## Common Examples
Here are some practical examples of using the `hostname` command:

1. **Display the current hostname:**
   ```bash
   hostname
   ```

2. **Display the fully qualified domain name:**
   ```bash
   hostname -f
   ```

3. **Show the short hostname:**
   ```bash
   hostname -s
   ```

4. **Display the IP address of the hostname:**
   ```bash
   hostname -i
   ```

5. **Set a new hostname (requires superuser privileges):**
   ```bash
   sudo hostname new-hostname
   ```

## Tips
- Always ensure you have the necessary permissions when changing the hostname, as it typically requires superuser access.
- After changing the hostname, consider updating the `/etc/hosts` file to reflect the new hostname for local resolution.
- Use the `hostnamectl` command on systems with `systemd` for more advanced hostname management, including setting static, transient, and pretty hostnames.