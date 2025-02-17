# [Linux] Bash systemctl uso: Manage system services and units

## Overview
The `systemctl` command is a powerful tool used in Linux systems to manage system services and units. It is part of the systemd system and service manager, allowing users to start, stop, enable, disable, and check the status of services and other system resources.

## Usage
The basic syntax of the `systemctl` command is as follows:

```bash
systemctl [options] [arguments]
```

## Common Options
- `start`: Starts a specified service.
- `stop`: Stops a running service.
- `restart`: Restarts a specified service.
- `status`: Displays the current status of a service.
- `enable`: Enables a service to start automatically at boot.
- `disable`: Prevents a service from starting automatically at boot.
- `list-units`: Lists all active units (services, sockets, etc.).
- `is-active`: Checks if a specified service is currently active.

## Common Examples
Here are some practical examples of using the `systemctl` command:

1. **Starting a service**:
   ```bash
   systemctl start apache2
   ```

2. **Stopping a service**:
   ```bash
   systemctl stop apache2
   ```

3. **Restarting a service**:
   ```bash
   systemctl restart apache2
   ```

4. **Checking the status of a service**:
   ```bash
   systemctl status apache2
   ```

5. **Enabling a service to start at boot**:
   ```bash
   systemctl enable apache2
   ```

6. **Disabling a service from starting at boot**:
   ```bash
   systemctl disable apache2
   ```

7. **Listing all active units**:
   ```bash
   systemctl list-units
   ```

8. **Checking if a service is active**:
   ```bash
   systemctl is-active apache2
   ```

## Tips
- Always check the status of a service after starting or stopping it to ensure the desired action was successful.
- Use `systemctl list-units --type=service` to filter the list to only show services.
- Be cautious when enabling services to start at boot, as this can affect system performance and boot time.